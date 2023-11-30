import ast
import re

import xmltodict

from sde_collections.models.collection_choice_fields import DocumentTypes


class RuleExtractor:
    """Extracts the rules from an XML config file."""

    def __init__(self, config_xml_string: str) -> None:
        self.config_xml_string = config_xml_string

    @staticmethod
    def extract_string_in_quotes(match_pattern):
        # Extract the URL from within the double quotes
        match = re.findall(r"\"(.*?)\"", match_pattern)
        if match:
            # Add the found URL
            return match[0]
        else:
            # If no double quotes are found, try extracting the URL-like part
            url_like_match = re.search(r"(https?://[^\s]+|\*[^\s]+)", match_pattern)
            if url_like_match:
                return url_like_match.group()

    def _extract_title_rules(self):
        config = xmltodict.parse(self.config_xml_string)

        mappings = [
            mapping
            for mapping in config["Sinequa"]["Mapping"]
            if mapping["Name"] == "title" and mapping["Selection"] is not None
        ]

        rules = [
            {
                "match_pattern": mapping["Selection"],
                "title_pattern": mapping["Value"],
                "pattern_source": 2,
            }
            for mapping in mappings
        ]

        return rules

    def _extract_exclude_rules(self):
        config = xmltodict.parse(self.config_xml_string)

        exclude_tags = ["UrlIndexExcluded", "UrlLinkExcluded"]

        all_rules = []

        for tag in exclude_tags:
            if type(config["Sinequa"][tag]) == str:
                config["Sinequa"][tag] = [config["Sinequa"][tag]]

            rules = [
                {
                    "match_pattern": excluded_url,
                    "pattern_source": 2,
                }
                for excluded_url in config["Sinequa"][tag]
            ]
            all_rules.extend(rules)

        return all_rules

    def _extract_include_rules(self):
        config = xmltodict.parse(self.config_xml_string)

        include_tags = ["UrlIndexIncluded", "UrlLinkIncluded"]

        all_rules = []

        for tag in include_tags:
            if type(config["Sinequa"][tag]) == str:
                config["Sinequa"][tag] = [config["Sinequa"][tag]]

            rules = [
                {
                    "match_pattern": included_url,
                    "pattern_source": 2,
                }
                for included_url in config["Sinequa"][tag]
            ]
            all_rules.extend(rules)

        return all_rules

    def _extract_document_type_rules(self):
        config = xmltodict.parse(self.config_xml_string)

        mappings = [
            mapping
            for mapping in config["Sinequa"]["Mapping"]
            if mapping["Name"] == "sourcestr56" and mapping["Selection"] is not None
        ]

        rules = [
            {
                "match_pattern": mapping["Selection"],
                "document_type": DocumentTypes.lookup_by_text(
                    ast.literal_eval(mapping["Value"])
                ),  # this removes the quotes around the document_type
                "pattern_source": 2,
            }
            for mapping in mappings
        ]

        return rules

    def extract_rules(self):
        exclude_rules = self._extract_exclude_rules()
        title_rules = self._extract_title_rules()
        document_type_rules = self._extract_document_type_rules()

        return exclude_rules, title_rules, document_type_rules
