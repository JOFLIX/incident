from django.apps import AppConfig


class TatuadminConfig(AppConfig):
    name = 'tatuadmin'

    def ready(self):

        print('signal ready amigo')
        import tatuadmin.signals
