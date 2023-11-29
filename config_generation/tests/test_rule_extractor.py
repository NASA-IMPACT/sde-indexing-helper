# from unittest.mock import patch

from ..extract_rules_from_config import RuleExtractor

# def test_extract_string_in_quotes():
#     # Arrange
#     input_string = 'doc.url1 match '"https://lambda.gsfc.nasa.gov/product/cobe/*"''
#     expected_output = "https://lambda.gsfc.nasa.gov/product/cobe/*"
#     extractor = RuleExtractor("")

#     # Act
#     result = extractor.extract_string_in_quotes(input_string)

#     # Assert
#     assert result == expected_output


def test_extract_title_rules():
    # Arrange
    with open("config_generation/tests/config_file_with_rules.xml") as file:
        xml_string = file.read()
    expected_output = [
        {
            "match_pattern": 'doc.url1 match "https://lambda.gsfc.nasa.gov/product/cobe/*"',
            "title_pattern": 'Concat("LAMBDA - ", xpath://*[@id="pageContent"]/h1/text(), " ", xpath://*[@id="pageContent"]/h1[1]/text(), " ", xpath://*[@id="pageContent"]/h1[2]/text(), " ", xpath://*[@id="pageContent"]/table/tbody/tr[1]/td/div/text())',  # noqa
            "pattern_source": 2,
        },
        {
            "match_pattern": 'doc.url1 match "https://lambda.gsfc.nasa.gov/product/bicepkeck/*"',
            "title_pattern": 'Concat("LAMBDA - ", xpath://*[@id="pageContent"]/h1/text(), " ", xpath://*[@id="pageContent"]/table/tbody/tr[1]/td/div/text())',  # noqa
            "pattern_source": 2,
        },
        {
            "match_pattern": 'doc.url1 match "https://lambda.gsfc.nasa.gov/product/wmap/*"',
            "title_pattern": 'Concat("LAMBDA - ", xpath://*[@id="pageContent"]/h1/text())',
            "pattern_source": 2,
        },
        {
            "match_pattern": 'doc.url1 match "https://lambda.gsfc.nasa.gov/product/suborbit/MAXIMA/cosmology.berkeley.edu/group/cmb*"',  # noqa
            "title_pattern": 'Concat("MAXIMA ", Replace(ParseFromLastSep(doc.url1, "/"), ".html", ""))',
            "pattern_source": 2,
        },
        {
            "match_pattern": "doc.url1 match '*lambda.gsfc.nasa.gov/product/wmap/current/effective_feq_tool_doc.html'",  # noqa
            "title_pattern": '"LAMBDA - WMAP Effective Frequency Calculator Tool Documentation"',
            "pattern_source": 2,
        },
    ]  # replace with your expected output
    extractor = RuleExtractor(xml_string)

    # Act
    result = extractor._extract_title_rules()

    # Assert
    assert result == expected_output


# def test_extract_exclude_rules():
#     # Arrange
#     with open("config_generation/tests/config_file_with_rules.xml", "r") as file:
#         xml_string = file.read()
#     expected_output = ["rule1", "rule2", "rule3"]  # replace with your expected output
#     extractor = RuleExtractor(xml_string)

#     # Act
#     result = extractor._extract_exclude_rules()

#     # Assert
#     assert result == expected_output


def test_extract_document_type_rules():
    # Arrange
    with open("config_generation/tests/config_file_with_rules.xml") as file:
        xml_string = file.read()

    expected_output = [
        {
            "match_pattern": "doc.url1 match '*www.earthdata.nasa.gov/apt/'",
            "document_type": 4,
            "pattern_source": 2,
        },
        {
            "match_pattern": "doc.url1 match '*www.earthdata.nasa.gov/apt/'",
            "document_type": 4,
            "pattern_source": 2,
        },
    ]

    extractor = RuleExtractor(xml_string)

    # Act
    result = extractor._extract_document_type_rules()

    # Assert
    assert result == expected_output


# def test_extract_rules():
#     # Arrange
#     with open("config_generation/tests/config_file_with_rules.xml", "r") as file:
#         xml_string = file.read()
#     expected_output = (
#         ["rule1", "rule2", "rule3"],
#         ["rule1", "rule2", "rule3"],
#         ["rule1", "rule2", "rule3"],
#     )  # replace with your expected output
#     extractor = RuleExtractor(xml_string)

#     # Act
#     result = extractor.extract_rules()

#     # Assert
#     assert result == expected_output
