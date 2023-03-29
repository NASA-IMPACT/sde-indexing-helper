from django.db import models
from treebeard.mp_tree import MP_Node


class Collection(models.Model):
    """Model definition for Collection."""

    class Divisions(models.IntegerChoices):
        ASTROPHYSICS = 1, "Astrophysics"
        BIOLOGY = 2, "Biological and Physical Sciences"
        EARTH_SCIENCE = 3, "Earth Science"
        HELIOPHYSICS = 4, "Heliophysics"
        PLANETARY = 5, "Planetary Science"

    class UpdateFrequencies(models.IntegerChoices):
        DAILY = 1, "Daily"
        WEEKLY = 2, "Weekly"
        BIWEEKLY = 3, "Biweekly"
        MONTHLY = 4, "Monthly"

    class DocumentTypes(models.IntegerChoices):
        IMAGES = 1, "Images"
        DATA = 2, "Data"
        DOCUMENTATION = 3, "Documentation"
        SOFTWARETOOLS = 4, "Software and Tools"
        MISSIONSINSTRUMENTS = 5, "Missions and Instruments"

    class SourceChoices(models.IntegerChoices):
        ONLY_IN_ORIGINAL = 1, "Only in original"
        BOTH = 2, "Both"
        ONLY_IN_SINEQUA_CONFIGS = 3, "Only in Sinequa configs"

    name = models.CharField("Name", max_length=1024)
    config_folder = models.CharField("Config Folder", max_length=2048)
    url = models.URLField("URL", max_length=2048)
    division = models.IntegerField(choices=Divisions.choices)
    turned_on = models.BooleanField("Turned On", default=True)

    source = models.IntegerField(choices=SourceChoices.choices)
    update_frequency = models.IntegerField(
        choices=UpdateFrequencies.choices, default=UpdateFrequencies.WEEKLY
    )
    document_type = models.IntegerField(
        choices=DocumentTypes.choices, null=True, blank=True
    )
    tree_root = models.CharField("Tree Root", max_length=1024, default="", blank=True)

    delete = models.BooleanField(default=False)

    # audit columns for production
    audit_hierarchy = models.CharField(
        "Audit Hierarchy", max_length=2048, default="", blank=True
    )
    audit_url = models.CharField("Audit URL", max_length=2048, default="", blank=True)
    audit_mapping = models.CharField(
        "Audit Mapping", max_length=2048, default="", blank=True
    )
    audit_label = models.CharField(
        "Audit Label", max_length=2048, default="", blank=True
    )
    audit_query = models.CharField(
        "Audit Query", max_length=2048, default="", blank=True
    )
    audit_duplicate_results = models.CharField(
        "Audit Duplicate Results", max_length=2048, default="", blank=True
    )
    audit_metrics = models.CharField(
        "Audit Metrics", max_length=2048, default="", blank=True
    )

    cleaning_assigned_to = models.CharField(
        "Cleaning Assigned To", max_length=128, default="", blank=True
    )

    notes = models.TextField("Notes", blank=True, default="")

    class Meta:
        """Meta definition for Collection."""

        verbose_name = "Collection"
        verbose_name_plural = "Collections"

    def __str__(self):
        """Unicode representation of Collection."""
        return self.name

    @property
    def indexed(self):
        return self.config_folder != ""

    def candidate_url_tree(self):
        tree = {}
        top_level_items = self.candidateurl_set.filter(parent__isnull=True)
        for item in top_level_items:
            tree[item.url] = item.get_tree()
        return tree


class CandidateURL(MP_Node):
    """A candidate URL scraped for a given collection."""

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    url = models.CharField("URL", max_length=2048)
    excluded = models.BooleanField(default=False)
    title = models.CharField("Title", max_length=2048)

    node_order_by = ["url"]

    class Meta:
        """Meta definition for Candidate URL."""

        verbose_name = "Candidate URL"
        verbose_name_plural = "Candidate URLs"

    def __str__(self):
        return self.url
