let _service_registry_instance = null;

class ServiceRegistry {

    constructor() {
        this._services = new Map();
    }

    static getInstance() {
        if (_service_registry_instance == null) {
            _service_registry_instance = new ServiceRegistry();
        }
        return _service_registry_instance;
    }

    registerService(name, obj) {
        if (!this._services.has(name)) {
            this._services.set(name, obj);
        } else {
            throw "Cant register service multiple times";
        }
    }

    getService(name) {
        var service = this._services.get(name);
        if (service === undefined) {
            throw "Service not Found";
        }
        return service;
    }
}
