import re

from django.db import models

from .collection_choice_fields import DocumentTypes


class BaseMatchPattern(models.Model):
    class MatchPatternTypeChoices(models.IntegerChoices):
        INDIVIDUAL_URL = 1, "Individual URL Pattern"
        MULTI_URL_PATTERN = 2, "Multi-URL Pattern"

    collection = models.ForeignKey(
        "Collection",
        on_delete=models.CASCADE,
        related_name="%(class)s",
        related_query_name="%(class)ss",
    )
    match_pattern = models.CharField(
        "Pattern",
        help_text="This pattern is compared against the URL of all the documents in the collection "
        "and matching documents will be returned",
    )
    match_pattern_type = models.IntegerField(
        choices=MatchPatternTypeChoices.choices, default=1
    )
    candidate_urls = models.ManyToManyField(
        "CandidateURL",
        related_name="%(class)s_urls",
    )

    def matched_urls(self):
        """Find all the urls matching the pattern."""
        escaped_match_pattern = re.escape(self.match_pattern)
        if self.match_pattern_type == self.MatchPatternTypeChoices.INDIVIDUAL_URL:
            return self.collection.candidate_urls.filter(
                url__regex=f"{escaped_match_pattern}$"
            )
        elif self.match_pattern_type == self.MatchPatternTypeChoices.MULTI_URL_PATTERN:
            return self.collection.candidate_urls.filter(
                url__regex=escaped_match_pattern.replace(
                    r"\*", ".*"
                )  # allow * wildcards
            )
        elif self.match_pattern_type == self.MatchPatternTypeChoices.XPATH_PATTERN:
            raise NotImplementedError

    def apply(self):
        raise NotImplementedError

    def unapply(self):
        raise NotImplementedError

    def save(self, *args, **kwargs):
        """Save the pattern and apply it."""
        super().save(*args, **kwargs)
        self.apply()

    def delete(self, *args, **kwargs):
        """Delete the pattern and unapply it."""
        self.unapply()
        super().delete(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ["match_pattern"]
        unique_together = ("collection", "match_pattern")

    def __str__(self):
        return self.match_pattern


class ExcludePattern(BaseMatchPattern):
    reason = models.TextField("Reason for excluding", default="", blank=True)

    def apply(self):
        matched_urls = self.matched_urls()
        candidate_url_ids = list(matched_urls.values_list("id", flat=True))
        self.candidate_urls.through.objects.bulk_create(
            objs=[
                ExcludePattern.candidate_urls.through(
                    candidateurl_id=candidate_url_id, excludepattern_id=self.id
                )
                for candidate_url_id in candidate_url_ids
            ]
        )

    def unapply(self):
        "Unapplies automatically by deleting excludpattern through objects in a cascade"
        return

    class Meta:
        """Meta definition for ExcludePattern."""

        verbose_name = "Exclude Pattern"
        verbose_name_plural = "Exclude Patterns"
        unique_together = ("collection", "match_pattern")


class TitlePattern(BaseMatchPattern):
    title_pattern = models.CharField(
        "Title Pattern",
        help_text="This is the pattern for the new title. You can write your own text, as well as "
        "add references to a specific xpath or the orignal title. For example 'James Webb {scraped_title}: {xpath}'",
    )

    def apply(self):
        matched_urls = self.matched_urls()
        matched_urls.update(generated_title=self.title_pattern)
        candidate_url_ids = list(matched_urls.values_list("id", flat=True))
        self.candidate_urls.through.objects.bulk_create(
            objs=[
                TitlePattern.candidate_urls.through(
                    candidateurl_id=candidate_url_id, titlepattern_id=self.id
                )
                for candidate_url_id in candidate_url_ids
            ]
        )

    def unapply(self):
        self.candidate_urls.update(generated_title="")

    class Meta:
        """Meta definition for TitlePattern."""

        verbose_name = "Title Pattern"
        verbose_name_plural = "Title Patterns"
        unique_together = ("collection", "match_pattern")


class DocumentTypePattern(BaseMatchPattern):
    document_type = models.IntegerField(choices=DocumentTypes.choices)

    def apply(self):
        matched_urls = self.matched_urls()
        matched_urls.update(document_type=self.document_type)
        candidate_url_ids = list(matched_urls.values_list("id", flat=True))
        self.candidate_urls.through.objects.bulk_create(
            objs=[
                DocumentTypePattern.candidate_urls.through(
                    candidateurl_id=candidate_url_id, documenttypepattern_id=self.id
                )
                for candidate_url_id in candidate_url_ids
            ]
        )

    def unapply(self):
        self.candidate_urls.update(document_type=None)

    class Meta:
        """Meta definition for DocumentTypePattern."""

        verbose_name = "Document Type Pattern"
        verbose_name_plural = "Document Type Patterns"
        unique_together = ("collection", "match_pattern")