import json

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _

from job_cms_integration.models import JobPluginModel
from job_cms_integration.serializers import JobIntegrationSerializer


@plugin_pool.register_plugin
class JobPluginPublisher(CMSPluginBase):
    model = JobPluginModel
    module = _("Job")
    name = _("Job Plugin")
    render_template = "job_cms_integration/job_plugin.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance

        serializer = JobIntegrationSerializer(instance)
        data = json.dumps(serializer.data)
        context["items_json"] = data

        return context
