import axios from 'axios';

type Stack = 'backend' | 'frontend';
type Level = 'debug' | 'info' | 'warn' | 'error' | 'fatal';
type BackendPackage = 'cache' | 'controller' | 'cron_job' | 'db' | 'domain' | 'handler' | 'repository' | 'route' | 'service';
type FrontendPackage = 'api';
type Package = BackendPackage | FrontendPackage;

const LOGGING_API_URL = 'http://20.244.56.144/evaluation-service/logs';

/**
 * Log function to send structured logs to theserver.
 * @param stack 
 * @param level 
 * @param pkg 
 * @param message
 */
export async function Log(stack: Stack, level: Level, pkg: Package, message: string): Promise<void> {
    // Validation
    const backendPackages: BackendPackage[] = ["cache", "controller", "cron_job", "db", "domain", "handler", "repository", "route", "service"];
    const frontendPackages: FrontendPackage[] = ["api"];

    const isValidPackage =
        (stack === 'backend' && backendPackages.includes(pkg as BackendPackage)) ||
        (stack === 'frontend' && frontendPackages.includes(pkg as FrontendPackage));

    if (!isValidPackage) {
        console.error(`Invalid package "${pkg}" for stack "${stack}"`);
        return;
    }

    try {
        await axios.post(LOGGING_API_URL, {
            stack,
            level,
            package: pkg,
            message
        });
        console.log(`[LOGGED] [${stack.toUpperCase()}] [${level.toUpperCase()}] ${pkg}: ${message}`);
    } catch (error) {
        console.error('Failed to send log to server:', error);
    }
}


