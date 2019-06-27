import {LogContext} from "./LogContext";

export class LogEvent {

    private _timestamp: Date;
    private _context: LogContext;
    private _message: string;
    private _logdata: any;

    constructor() {
        this._timestamp = new Date();
    }

    get timestamp(): Date {
        return this._timestamp;
    }

    set timestamp(value: Date) {
        this._timestamp = value;
    }

    get message(): string {
        return this._message;
    }

    set message(value: string) {
        this._message = value;
    }
    get context(): LogContext {
        return this._context;
    }

    set context(value: LogContext) {
        this._context = value;
    }
    get logdata(): any {
        return this._logdata;
    }

    set logdata(value: any) {
        this._logdata = value;
    }

}
