#!/usr/bin/env bash
# ==============================================================================
# Production Deployment & Startup Script for Eujim Solutions Portal
# ==============================================================================
set -e

echo "==> Starting production deployment routine..."

# 1. Check for .env file
if [ ! -f ".env" ]; then
    echo "ERROR: .env file not found in current directory!"
    exit 1
fi

# 2. Activate Virtual Environment if present
if [ -d ".venv" ]; then
    echo "==> Activating virtual environment (.venv)..."
    source .venv/bin/activate || source .venv/Scripts/activate
elif [ -d "venv" ]; then
    echo "==> Activating virtual environment (venv)..."
    source venv/bin/activate || source venv/Scripts/activate
fi

# 3. Create required runtime directories
echo "==> Ensuring runtime directories exist (logs, media, staticfiles)..."
mkdir -p logs media staticfiles
chmod -R 755 media staticfiles

# 4. Run database migrations
#echo "==> Running database migrations..."
#python manage.py migrate --noinput

# 5. Collect static files for production web server (Nginx)
echo "==> Collecting static files..."
python manage.py collectstatic --noinput

# 6. PM2 Process Management
if command -v pm2 &> /dev/null; then
    echo "==> Starting / reloading PM2 process instances..."
    pm2 startOrReload ecosystem.config.js --env production
    pm2 save
    echo "==> PM2 Process Status:"
    pm2 status
else
    echo "WARNING: PM2 is not installed globally or not in PATH."
    echo "Please install PM2 via 'npm install -g pm2' to manage background processes automatically."
fi

echo "==> Production deployment completed successfully!"
