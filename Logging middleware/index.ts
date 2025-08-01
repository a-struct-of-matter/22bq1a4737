import { Log } from './middleware_logging';


async function simulateLogs() {
    await Log("backend", "error", "handler", "received string, expected bool");
    await Log("backend", "fatal", "db", "Critical database connection failure.");
    await Log("frontend", "debug", "api", "Profile API fetched successfully.");
    
    
    await Log("frontend", "warn", "db" as any, "Invalid usage test");
}

simulateLogs();