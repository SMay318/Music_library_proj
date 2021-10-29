SECRET_KEY = 'django-insecure-g91d$)i=2rx+xj10c$7#ul6x7&k*_rint#vje*jwla5mo%yier'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_database',
        'USER': 'root',
        'PASSWORD': 'patriots1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}

