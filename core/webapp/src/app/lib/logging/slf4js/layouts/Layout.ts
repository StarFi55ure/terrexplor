import {LogEvent} from "../LogEvent";
import {LogContext} from "../LogContext";
import {LoggerLevel} from "../Logger";


export const LayoutLevelMap = new Map<LoggerLevel, string>();
LayoutLevelMap.set(LoggerLevel.TRACE, 'TRACE');
LayoutLevelMap.set(LoggerLevel.DEBUG, 'DEBUG');
LayoutLevelMap.set(LoggerLevel.INFO, 'INFO');
LayoutLevelMap.set(LoggerLevel.WARN, 'WARN');
LayoutLevelMap.set(LoggerLevel.ERROR, 'ERROR');
LayoutLevelMap.set(LoggerLevel.NONE, 'NONE');

export interface Layout {
    doLayout(logEvent: LogEvent, logContext: LogContext): string;
}
