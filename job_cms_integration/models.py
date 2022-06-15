from cms.models import CMSPlugin
from django.db import models

# Create your models here.
from job.models import Job


class JobPluginModel(CMSPlugin):
    title = models.TextField(default='Highlight')
    jobs = models.ManyToManyField(Job)
