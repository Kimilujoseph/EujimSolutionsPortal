import os
import multiprocessing

# ---------------------------------------------
#  LOW-MEMORY CONFIGURATION FOR SHOWCASE PROJECT
#  Goal: Keep total RAM usage below 500 MB
# ---------------------------------------------

# Bind to local port (Nginx will proxy to this)
bind = os.getenv("GUNICORN_BIND", "127.0.0.1:8000")
backlog = 64  # reduce backlog to save a bit

# ---------------------------------------------
#  WORKERS & THREADS (single worker, no threads)
#  - One worker process loads the entire app once.
#  - No threading (threads=1) means each request is handled sequentially.
#  - For a showcase (low traffic), this is perfectly fine.
# ---------------------------------------------
workers = 1                    # Only ONE worker process
threads = 1                    # Only ONE thread per worker
worker_class = "sync"          # Standard synchronous worker (no extra async overhead)

# ---------------------------------------------
#  MEMORY MANAGEMENT
#  - Restart worker after processing a number of requests to prevent memory leaks.
#  - This ensures the memory footprint stays under control.
# ---------------------------------------------
max_requests = 200             # Restart after 200 requests
max_requests_jitter = 50       # Randomize restart to avoid stampedes

# ---------------------------------------------
#  TIMEOUTS
#  - Keep timeouts moderate to release stuck connections.
# ---------------------------------------------
timeout = 60                   # 60 seconds for a request (more than enough)
keepalive = 2                  # Keep connections alive briefly

# ---------------------------------------------
#  LOGGING (minimal)
#  - Log to files in the 'logs' directory.
# ---------------------------------------------
os.makedirs("logs", exist_ok=True)
accesslog = "logs/gunicorn_access.log"
errorlog = "logs/gunicorn_error.log"
loglevel = "info"            


proc_name = "eujim_gunicorn"
pidfile = "logs/gunicorn.pid"
daemon = False                 # PM2 will manage the process