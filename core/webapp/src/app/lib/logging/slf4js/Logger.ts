import {Appender} from "./appenders/Appender";
import {LogContext} from "./LogContext";
import {LogEvent} from "./LogEvent";

export enum LoggerLevel {
    NONE,
    ERROR,
    WARN,
    INFO,
    DEBUG,
    TRACE
};

export interface Logger {

    trace(message: string): void;
    debug(message: string): void;
    info(message: string): void;
    warn(message: string): void;
    error(message: string): void;
    log(logEvent: LogEvent): void;

    addAppender(appender: Appender): void;
    clearAppenders(): void;

    getContext(): LogContext;
    setContext(context: LogContext): void;
    setAncestor(ancestor: Logger): void;
}

