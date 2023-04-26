import {Logger, LoggerLevel} from "./Logger";
import {BasicLogger} from "./loggers/BasicLogger";
import {ConsoleAppender} from "./appenders/ConsoleAppender";
import {DefaultLayout} from "./layouts/DefaultLayout";
import {LogContext} from "./LogContext";

class LoggerFactory {

    private static loggers: Map<string, Logger> = new Map<string, Logger>();
    private static rootLogger: Logger;

    static getLogger(loggerName: string = '.'): Logger {
        // TODO: must have a null logger by default. Only create a basic logger when explictly
        //  asked for

        if (loggerName === '.') {
            if (!this.rootLogger) {
                this.rootLogger = new BasicLogger();

                let consoleAppender = new ConsoleAppender();
                consoleAppender.setLayout(new DefaultLayout());

                this.rootLogger.clearAppenders();
                this.rootLogger.addAppender(consoleAppender);

                let rootContext = new LogContext();
                rootContext.name = 'ROOT';
                rootContext.level = LoggerLevel.DEBUG;

                this.rootLogger.setContext(rootContext);
            }
            return this.rootLogger;
        }

        if (this.loggers.has(loggerName)) {
            return this.loggers.get(loggerName);
        } else {
            let new_logger = new BasicLogger();
            let nextAncestor = this.getNextAncestor(loggerName);
            if (nextAncestor) {
                let ancestorLogger = this.getLogger(nextAncestor);
                new_logger.setAncestor(ancestorLogger);
                let newContext = new LogContext();
                newContext.name = loggerName;
                if (ancestorLogger.getContext()) {
                    newContext.level = ancestorLogger.getContext().level;
                } else {
                    newContext.level = LoggerLevel.DEBUG;
                }
                new_logger.setContext(newContext);
            }
            this.loggers.set(loggerName, new_logger);
            return new_logger;
        }
    }


    private static getNextAncestor(loggerName: string): string {
        let nameElements = loggerName.split('.');
        nameElements.pop();

        if (nameElements.length === 0) {
            return '.';
        } else {
            let parentName = nameElements.join('.');
            if (this.loggers.has(parentName)) {
                return parentName;
            } else {
                return this.getNextAncestor(parentName);
            }
        }
    }
}

export default LoggerFactory;

