import {Layout} from "../layouts/Layout";
import {LogEvent} from "../LogEvent";
import {LogContext} from "../LogContext";

export interface Appender {

    doAppend(logEvent: LogEvent): void;
    setLayout(layout: Layout): void;
}

