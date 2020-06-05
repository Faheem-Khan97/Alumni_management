from django.apps import AppConfig


class UsermoduleConfig(AppConfig):
    name = 'UserModule'



    def ready(self):
         import UserModule.signals