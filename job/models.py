from django.db import models

# Create your models here.

LEVEL_CHOICES = (
    ("0", "Junior"),
    ("1", "Middle"),
    ("2", "Senior")
)

class Job(models.Model):
    title = models.CharField(
        max_length=255)
    salary = models.IntegerField()
    level = models.CharField(
        max_length=255,
        choices=LEVEL_CHOICES)
    description = models.TextField(
        null=True, blank=True)
    recruiter_name = models.CharField(
        max_length=255,
        blank=True, null=True)
    recruiter_contacts = models.TextField(
        blank=True, null=True)
    img = models.ImageField(
        upload_to='jobs/',
        blank=True, null=True)
    location = models.CharField(
        max_length=255,
        blank=True, null=True)
    engagement_percent = models.IntegerField(
        blank=True, null=True)
    contract_period = models.CharField(
        max_length=255,
        null=True, blank=True)
    published_state = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-level', '-img')
