from django.apps import AppConfig


class AuditConfig(AppConfig):
    name = 'project_name.apps.audit'

    def ready(self):
        pass
