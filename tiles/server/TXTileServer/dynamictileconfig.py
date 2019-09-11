import os

from UPTileServer.config.configservice import ConfigService


class DynamicLayerConfig(dict):
    """
    Get list of data collections as layers before static layers
    """

    def __init__(self, *args, **kwargs):
        super(DynamicLayerConfig, self).__init__(*args, **kwargs)
        self._configservice = ConfigService()

    def keys(self):
        allkeys = super(DynamicLayerConfig, self).keys()
        api_url = self._configservice.get_string('webclient.api.url')
        api_url = os.path.join(api_url, '/api/services/datacollection/get_layer_collection_map')

        return allkeys

    def items(self):
        allitems = super(DynamicLayerConfig, self).items()
        return allitems

    def __contains__(self, item):
        return super(DynamicLayerConfig, self).__contains__(item)

    def __getitem__(self, item):
        api_url = self._configservice.get_string('webclient.api.url')
        api_url = os.path.join(api_url, '/api/services/datacollection/get_layer_collection_map')

        return super(DynamicLayerConfig, self).__getitem__(item)


class DynamicTileConfig():
    """
    Monitor calls for layer configs
    """

    def __init__(self, built_configuration):
        self._staticconfig = built_configuration
        self._dynlayers = DynamicLayerConfig(built_configuration.layers)

    @property
    def cache(self):
        return self._staticconfig.cache

    @property
    def layers(self):
        return self._dynlayers

    @property
    def dirpath(self):
        return self._staticconfig.dirpath

    @property
    def index(self):
        return self._staticconfig.index



