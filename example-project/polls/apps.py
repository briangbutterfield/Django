from django.apps import AppConfig

# Version History:
#   2020.12.30.100 
#   Finished part three of tutorial.  https://docs.djangoproject.com/en/3.1/intro/tutorial03
#   
#   2020.01.07.BeforeGenericViews 
#   Added vote and results views.  From here migrating to generic views.  https://docs.djangoproject.com/en/3.1/intro/tutorial04/#use-generic-views-less-code-is-better
#   
#   2020.01.07.AfterGenericViews 
#   Removed specific view definitions and replaced with generic views provided by Django.
#
#   2021.01.25.100
#   Finished part five of tutorial.  https://docs.djangoproject.com/en/3.1/intro/tutorial05/
#
#   2021.01.27.100
#   Finished part sixe and seven of tutortial.  https://docs.djangoproject.com/en/3.1/intro/tutorial07/
#

class PollsConfig(AppConfig):
    name = 'polls'
