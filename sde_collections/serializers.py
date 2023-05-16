from rest_framework import serializers

from .models import CandidateURL, DocumentTypePattern, ExcludePattern, TitlePattern


class CandidateURLSerializer(serializers.ModelSerializer):
    excluded = serializers.BooleanField(required=False)
    document_type_display = serializers.CharField(
        source="get_document_type_display", read_only=True
    )
    url = serializers.CharField(required=False)

    class Meta:
        model = CandidateURL
        fields = (
            "id",
            "excluded",
            "url",
            "scraped_title",
            "generated_title",
            "document_type",
            "document_type_display",
            "visited",
        )


class BasePatternSerializer(serializers.ModelSerializer):
    match_pattern_type_display = serializers.CharField(
        source="get_match_pattern_type_display", read_only=True
    )
    candidate_urls_count = serializers.SerializerMethodField(read_only=True)

    def get_candidate_urls_count(self, instance):
        return instance.candidate_urls.count()

    class Meta:
        fields = (
            "id",
            "collection",
            "match_pattern",
            "match_pattern_type",
            "match_pattern_type_display",
            "candidate_urls_count",
        )
        abstract = True


class ExcludePatternSerializer(BasePatternSerializer, serializers.ModelSerializer):
    class Meta:
        model = ExcludePattern
        fields = BasePatternSerializer.Meta.fields + ("reason",)


class TitlePatternSerializer(BasePatternSerializer, serializers.ModelSerializer):
    class Meta:
        model = TitlePattern
        fields = BasePatternSerializer.Meta.fields + ("title_pattern",)


class DocumentTypePatternSerializer(BasePatternSerializer, serializers.ModelSerializer):
    document_type_display = serializers.CharField(
        source="get_document_type_display", read_only=True
    )

    class Meta:
        model = DocumentTypePattern
        fields = BasePatternSerializer.Meta.fields + (
            "document_type",
            "document_type_display",
        )
