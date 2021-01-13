LOG_LEVEL = 30 # To be deprecated when all microservices use ADSFlask
LOGGING_LEVEL = "INFO"
LOG_STDOUT = True
DEFAULT_REQUEST_TIMEOUT = 60 # seconds
SECURITY_REGISTER_BLUEPRINT = False
EXTENSIONS = ['adsws.ext.menu',
              'adsws.ext.sqlalchemy',
              'adsws.ext.security',
              'adsws.ext.ratelimiter',
]

PACKAGES = ['adsws.modules.oauth2server', ]

CORS_HEADERS = [
    'Content-Type',
    'X-BB-Api-Client-Version',
    'Authorization',
    'Accept',
]
CORS_DOMAINS = [
    'http://localhost:8000',
    'http://localhost:5000',
    'http://adslabs.org',
]
CORS_METHODS = ['GET', 'OPTIONS', 'POST']

RATELIMIT_STORAGE_URL = "redis://localhost:6379"
RATELIMIT_HEADERS_ENABLED = True
RATELIMIT_SWALLOW_ERRORS = True
RATELIMIT_KEY_PREFIX = "limiter"

WEBSERVICES_PUBLISH_ENDPOINT = 'resources'
WEBSERVICES = {
    # uri : deploy_path
    'adsws.solr.app': '/solr',
}
# when defined, the remote resources will be cached (to be reused)
# in case when the service is temporarily down during a worker startup
# WEBSERVICES_DISCOVERY_CACHE_DIR='/tmp'

API_PROXYVIEW_HEADERS = {'Cache-Control': 'public, max-age=600'}
REMOTE_PROXY_ALLOWED_HEADERS = ['Content-Type', 'Content-Disposition', 'Set-Cookie'] # Set-Cookie required for affinity

AFFINITY_ENHANCED_ENDPOINTS = {"/search": "sroute",} # keys: deploy paths, value: cookie
