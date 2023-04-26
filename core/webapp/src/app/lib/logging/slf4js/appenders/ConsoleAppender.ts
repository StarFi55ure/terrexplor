import {Appender} from './Appender';
import {Layout} from "../layouts/Layout";
import {LogEvent} from "../LogEvent";
import {LogContext} from "../LogContext";

export class ConsoleAppender implements Appender {
    private layout: Layout;

    doAppend(logEvent: LogEvent): void {
        let finalmessage = this.layout.doLayout(logEvent, logEvent.context);
        console.log(finalmessage);
    }

    setLayout(layout: Layout): void {
        this.layout = layout;
    }
}
