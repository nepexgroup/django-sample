r"""

     _    _                         _
    /_\  | | __ __ _  _   _  _ __  | |_
   //_\\ | |/ // _` || | | || '_ \ | __|
  /  _  \|   <| (_| || |_| || | | || |_
  \_/ \_/|_|\_\\__,_| \__,_||_| |_| \__|

"""
ASCII_ART = "orge font"

# Use 'alpha', 'beta', 'rc' or 'final' as the 4th element to indicate release type.
VERSION = (2, 0, 1, 'final')


def get_short_version():
    return '%s.%s' % (VERSION[0], VERSION[1])


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    # Append 3rd digit if > 0
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    elif VERSION[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        version = '%s%s' % (version, mapping[VERSION[3]])
        if len(VERSION) == 5:
            version = '%s%s' % (version, VERSION[4])
    return version


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'blog',
    # 'sample',
    # 'sample.apps.blog',
    # 'sample.apps.event',
    # 'sample.apps.schedule',

    'rest_framework',

]
default_app_config = 'sample.config.SampleConfig'
