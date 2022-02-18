from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
  '',
    host(r'', 'w3elements.urls', name=''),
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'contributor', 'contributor.urls', name='contributor'),
)