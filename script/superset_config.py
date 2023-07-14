import os

ROW_LIMIT = 5000
WEBSERVER_THREADS = 8
SUPERSET_WEBSERVER_PORT = 8088
SUPERSET_WEBSERVER_TIMEOUT = 300
SECRET_KEY=os.environ.get('SECRET_KEY')
WTF_CSRF_ENABLED = True
WTF_CSRF_EXEMPT_LIST = []
MAPBOX_API_KEY = ''
SESSION_COOKIE_SAMESITE = None
ENABLE_PROXY_FIX = True
PUBLIC_ROLE_LIKE_GAMMA = True
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True
}
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/superset'

CORS_OPTIONS = {
  'supports_credentials': True,
  'allow_headers': ['*'],
  'resources':['*'],
  'origins': ['http://localhost:8088', 'http://localhost:8888']
}