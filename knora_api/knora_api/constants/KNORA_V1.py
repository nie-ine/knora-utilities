# Some constants, used by the Session class

V1_PROJECTS = '/v1/projects'
V1_PROPERTIES = '/v1/properties'
V1_PROPERTYLISTS = '/v1/propertylists'
V1_RESOURCES = '/v1/resources'
V1_RESOURCES_LABEL = '/v1/resources_label'
V1_RESOURCETYPES = '/v1/resourcetypes'
V1_SEARCH = '/v1/search'
V1_VALUE = '/v1/value'
V1_VOCABULARIES = '/v1/vocabularies'

VALUE_NAMES = set('BooleanValue', 'ColorValue', 'DateValue', 'DecimalValue',
                  'ExternalResValue', 'FileValue', 'GeomValue', 'GeonameValue',
                  'IntervalValue', 'IntValue', 'LinkValue', 'ListValue',
                  'TextValue', 'UriValue')

VALUE_TYPES = set('boolean_value', 'color_value', 'date_value',
                  'decimal_value', 'geom_value', 'geoname_value',
                  'hlist_value', 'int_value', 'interval_value',
                  'link_value', 'richtext_value', 'uri_value')
