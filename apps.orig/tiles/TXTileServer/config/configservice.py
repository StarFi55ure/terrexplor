
class ConfigService():
    '''
    Interface to configuration data

    '''

    def __init__(self):
        self._config = {
            'webclient.api.url': 'http://localhost:7000'
        }

    def get_string(self, object_path):
        '''
        Walk the config tree and return the appropriate config string

        :param object_path:
        :return:
        '''
        return self._config.get(object_path, None)
