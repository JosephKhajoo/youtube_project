from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'


# class UserProfileConfig(AppConfig):
#     name = 'UserProfile'

    def ready(self):
    	import users.signals