import {LoggerLevel} from "./Logger";

export class LogContext {
    get level(): LoggerLevel {
        return this._level;
    }

    set level(value: LoggerLevel) {
        this._level = value;
    }
    get name(): string {
        return this._name;
    }

    set name(value: string) {
        this._name = value;
    }

    private _name: string;
    private _level: LoggerLevel;

}
