class ConfigService {

    constructor() {
        this._config = {
            api: {
                url: 'http://hyperion.dyndns.org'
            },
            tileserver: {
                url: 'http://tiles-{a-c}.hyperion.dyndns.org/tiles',
                theme: 'infrastructure-hillshade',
                defaultLonLat: [18.417, -33.928],
                defaultZoom: 11,
                defaultMaxZoom: 16
            }
        }

        // debug configuration

        if (true) {
            _.merge(this._config, {
                api: {
                    url: 'http://localhost:8080'
                },
                tileserver: {
                    url: 'http://tiles.urbanplanet.local/tiles'
                }
            });
        }

    }

    getOption(option_dot_path) {
        return _.get(this._config, option_dot_path, null);
    }
}

ServiceRegistry.getInstance().registerService('config', new Proxy(new ConfigService(), {
    get: function (target, obj) {
        if (obj in target) {
            return target[obj];
        }

        return target.getOption(obj);
    }
}));
