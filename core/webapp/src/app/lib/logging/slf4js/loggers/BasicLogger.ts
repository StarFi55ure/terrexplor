import {Appender} from "../appenders/Appender";
import {Logger, LoggerLevel} from "../Logger";
import {LogContext} from "../LogContext";
import {LogEvent} from "../LogEvent";

export class BasicLogger implements Logger {

    private appenders: Array<Appender>;
    private logLevel: LoggerLevel;
    private ancestor: Logger;
    private context: LogContext;

    constructor() {
        this.appenders = new Array<Appender>();
        this.logLevel = LoggerLevel.NONE;
    }

    debug(message: string): void {
        if (this.logLevel > LoggerLevel.DEBUG) {
            return;
        }
        let l = new LogEvent();
        l.message = message;
        l.context = this.context;
        this.log(l);
    }

    error(message: string): void {
        if (this.logLevel > LoggerLevel.ERROR) {
            return;
        }
        let l = new LogEvent();
        l.message = message;
        l.context = this.context;
        this.log(l);
    }

    info(message: string): void {
        if (this.logLevel > LoggerLevel.INFO) {
            return;
        }
        let l = new LogEvent();
        l.message = message;
        l.context = this.context;
        this.log(l);
    }

    trace(message: string): void {
        if (this.logLevel > LoggerLevel.TRACE) {
            return;
        }
        let l = new LogEvent();
        l.message = message;
        l.context = this.context;
        this.log(l);
    }

    warn(message: string): void {
        if (this.logLevel > LoggerLevel.WARN) {
            return;
        }
        let l = new LogEvent();
        l.message = message;
        l.context = this.context;
        this.log(l);
    }

    addAppender(appender: Appender): void {
        this.appenders.push(appender);
    }

    clearAppenders(): void {
        this.appenders = new Array<Appender>();
    }

    log(logEvent: LogEvent): void {
        for (let i=0; i<this.appenders.length; i++) {
            this.appenders[i].doAppend(logEvent);
        }

        if (this.ancestor) {
            this.ancestor.log(logEvent);
        }
    }

    setAncestor(ancestor: Logger): void {
        this.ancestor = ancestor;
    }

    setContext(context: LogContext): void {
        this.context = context;
        this.logLevel = context.level;
    }

    getContext(): LogContext {
        return this.context;
    }

}
