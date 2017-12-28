from api.constants import *

# String used to be the base of ACIDs
# Param substitution will be used to provide a service-specific prefix to the id
ACID_SEPARATOR_CHAR = ':'

# Some of these concept definitions should be linked with the ontology (or be loaded from it)
AUDIOCOMMONS_ONTOLOGY_PREFIX = 'ac:'

# Component names
SEARCH_TEXT_COMPONENT = 'text_search'
LICENSING_COMPONENT = 'licensing'
DOWNLOAD_COMPONENT = 'download'

# Service description keywords
ACID_DOMAINS_DESCRIPTION_KEYWORD = 'acid_domains'
SUPPORTED_FIELDS_DESCRIPTION_KEYWORD = 'supported_fields'
SUPPORTED_FILTERS_DESCRIPTION_KEYWORD = 'supported_filters'
SUPPORTED_SORT_OPTIONS_DESCRIPTION_KEYWORD = 'supported_sort_options'

# Authentication
APIKEY_AUTH_METHOD = 'apikey_auth'
ENDUSER_AUTH_METHOD = 'enduser_auth'

# Resource fields (just using fake names here)
FIELD_ID = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'id'
FIELD_URL = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'url'
FIELD_NAME = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'name'
FIELD_AUTHOR_NAME = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'author'
FIELD_AUTHOR_URL = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'author_url'
FIELD_COLLECTION_NAME = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'collection'
FIELD_COLLECTION_URL = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'collection_url'
FIELD_TAGS = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'tags'
FIELD_DESCRIPTION = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'description'
FIELD_TIMESTAMP = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'timestamp'
FIELD_LICENSE = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'license'
FIELD_LICENSE_DEED_URL = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'license_deed_url'

FIELD_DURATION = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'duration'
FIELD_FORMAT = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'format'
FIELD_FILESIZE = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'filesize'
FIELD_CHANNELS = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'channels'
FIELD_BITRATE = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'bitrate'
FIELD_BITDEPTH = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'bitdepth'
FIELD_SAMPLERATE = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'samplerate'

FIELD_PREVIEW = AUDIOCOMMONS_ONTOLOGY_PREFIX + 'preview_url'

MINIMUM_RESOURCE_DESCRIPTION_FIELDS = [
    FIELD_ID,
    FIELD_URL,
    FIELD_NAME,
    FIELD_AUTHOR_NAME,
    FIELD_LICENSE,
    FIELD_PREVIEW,
]
ALL_RESOURCE_DESCRIPTION_FIELDS = [globals()[item] for item in dir() if item.startswith('FIELD_')]

# Search results parameters
NEXT_PAGE_PROP = 'next'
PREV_PAGE_PROP = 'prev'
NUM_RESULTS_PROP = 'num_results'
RESULTS_LIST = 'results'

# Sort options
SORT_OPTION_RELEVANCE = 'relevance'
SORT_OPTION_POPULARITY = 'popularity'
SORT_OPTION_DURATION = 'duration'
SORT_OPTION_DOWNLOADS = 'downloads'
SORT_OPTION_CREATED = 'created'

SORT_OPTIONS = [
    SORT_OPTION_RELEVANCE,
    SORT_OPTION_POPULARITY,
    SORT_OPTION_DURATION,
    SORT_OPTION_DOWNLOADS,
    SORT_OPTION_CREATED,
]

# Licenses
LICENSE_UNKNOWN = 'Unknown'
LICENSE_CC0 = 'CC0'
LICENSE_CC_BY = 'BY'
LICENSE_CC_BY_SA = 'BY-SA'
LICENSE_CC_BY_NC = 'BY-NC'
LICENSE_CC_BY_ND = 'BY-ND'
LICENSE_CC_BY_NC_SA = 'BY-NC-SA'
LICENSE_CC_BY_NC_ND = 'BY-NC-ND'
LICENSE_CC_SAMPLING_PLUS = 'SamplingPlus'
