
def setup_django():
    import django
    import os
    import sys

    sys.path.append("../MyVideoGamesProj")
    os.environ["DJANGO_SETTINGS_MODULE"] = "MyVideoGamesProj.settings"
    django.setup()
