from django.apps import AppConfig
from django.apps import apps
from django.conf.urls import url


class SampleConfig(AppConfig):
    name = 'sample'

    def ready(self):
        self.blog_app = apps.get_app_config('blog')
        self.schedule_app = apps.get_app_config('schedule')
        self.event_app = apps.get_app_config('event')

    def get_urls(self):
        urls = [
            url(r'^blog/', self.blog_app.urls),
            url(r'^schedule/', self.schedule_app.urls),
            url(r'^event/', self.event_app.urls)
        ]
        return urls
