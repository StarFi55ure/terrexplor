import {Layout, LayoutLevelMap} from "./Layout";
import {LogEvent} from "../LogEvent";
import {LogContext} from "../LogContext";

export class DefaultLayout implements Layout{
    doLayout(logEvent: LogEvent, logContext: LogContext): string {
        let timestamp = logEvent.timestamp;
        let level = LayoutLevelMap.get(logContext.level);

        let date = `${timestamp.getFullYear()}-${timestamp.getMonth()}-${timestamp.getDay()}`;
        let time = `${timestamp.getHours()}:${timestamp.getMinutes()}:${timestamp.getSeconds()}`;
        let layoutString = `[${date} ${time}]:${level}:${logContext.name}:> ${logEvent.message}`;
        return layoutString;
    }
}
