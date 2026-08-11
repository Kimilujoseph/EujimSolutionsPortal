# Step-by-Step Production Deployment Guide

This guide provides complete, step-by-step instructions for deploying the **Eujim Solutions Portal** backend on a production server (Ubuntu 22.04 / 24.04 LTS recommended) using **PM2**, **Gunicorn**, **Celery**, **Redis**, and **Nginx**.

---

## Architecture Overview

```
                        +-----------------------+
                        |     Internet/Client   |
                        +-----------+-----------+
                                    |
                                    v (Port 80/443)
                        +-----------+-----------+
                        |         Nginx         |
                        | (Reverse Proxy/Static)|
                        +-----+-----------+-----+
                              |           |
            /static/ & /media/|           | HTTP & WebSockets (/ws/)
                              v           v
                     +--------+--+     +--+------------------------+
                     | Local File|     | Gunicorn + Uvicorn Worker |
                     | System    |     | (PM2: eujim-backend)      |
                     +-----------+     +-----------+---------------+
                                                   |
                                                   v
                                       +-----------+-----------+
                                       |      Redis Server     |
                                       +-----+-----------+-----+
                                             ^           ^
                                             |           |
                         +-------------------+--+     +--+-------------------+
                         | Celery Task Worker   |     | Celery Beat Scheduler|
                         | (PM2: celery-worker) |     | (PM2: celery-beat)   |
                         +----------------------+     +----------------------+
```

---

## Prerequisites

Before starting, ensure you have:
1. An **Ubuntu 22.04 LTS** or **24.04 LTS** server with `root` or `sudo` user access.
2. A registered domain name pointed to your server's public IP address via DNS A-records (`yourdomain.com` and `www.yourdomain.com`).
3. Running instances of **MySQL** database server and **Redis** server (either hosted on the same server or externally).

---

## Step 1: Install System Dependencies

Connect to your server via SSH and update package lists:

```bash
sudo apt update && sudo apt upgrade -y
```

Install Python development libraries, build tools, MySQL client headers, Git, and Redis:

```bash
sudo apt install -y python3-venv python3-pip python3-dev build-essential \
                    pkg-config default-libmysqlclient-dev nginx redis-server git curl
```

Ensure Redis server is enabled and running:

```bash
sudo systemctl enable redis-server
sudo systemctl start redis-server
sudo systemctl status redis-server
```

---

## Step 2: Install Node.js & PM2 Globally

PM2 requires Node.js runtime. Install Node.js (LTS) and PM2:

```bash
# Add NodeSource Node.js 20.x repository
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Install PM2 globally
sudo npm install -g pm2
```

Verify PM2 installation:

```bash
pm2 --version
```

---

## Step 3: Clone Repository & Setup Virtual Environment

Navigate to web root directory (e.g. `/var/www` or `/home/ubuntu`):

```bash
cd /var/www
sudo git clone https://github.com/Kimilujoseph/EujimSolutionsPortal.git
cd EujimSolutionsPortal

# Set correct ownership for current user
sudo chown -R $USER:$USER /var/www/EujimSolutionsPortal
```

Create and activate Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirement.txt
```

---

## Step 4: Configure Environment Variables (`.env`)

Create a `.env` file in the project root directory:

```bash
nano .env
```

Paste and adjust the following configuration according to your environment:

```env
# Production Django Settings
DEBUG=False
SECRET_KEY=your-secure-production-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com,127.0.0.1

# Database Settings (MySQL)
DB_NAME=eujim_db
DB_USER=eujim_user
DB_PASSWORD=your_secure_db_password
DB_HOST=127.0.0.1
DB_PORT=3306

# Redis & Celery Settings
REDIS_URL=
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
REDIS_USER=default
REDIS_PASSWORD=your_redis_password
REDIS_DB=0
CELERY_RESULT_BACKEND=

# Email Settings
DEFAULT_FROM_EMAIL=noreply@yourdomain.com
SUPPORT_EMAIL=support@yourdomain.com
SERVER_EMAIL=server@yourdomain.com
EMAIL_HOST=smtp.your-email-provider.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email_username
EMAIL_HOST_PASSWORD=your_email_password

# Site URLs
SITE_NAME="Eujim Solutions Portal"
FRONTEND_URL=https://yourdomain.com
BACKEND_URL=https://yourdomain.com/api/v1
```

Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

---

## Step 5: Execute Automated Deployment Script

Run the provided deployment script. This script creates runtime directories, applies database migrations, collects static assets, and launches PM2:

```bash
chmod +x deploy.sh
./deploy.sh
```

---

## Step 6: Configure Nginx Web Server

Copy the included `nginx_eujim.conf` file to Nginx's `sites-available` directory:

```bash
sudo cp nginx_eujim.conf /etc/nginx/sites-available/eujim
```

Edit `/etc/nginx/sites-available/eujim` to set your actual domain name and repository paths:

```bash
sudo nano /etc/nginx/sites-available/eujim
```

- Update `server_name yourdomain.com www.yourdomain.com;`
- Ensure static & media paths match your project location:
  - `alias /var/www/EujimSolutionsPortal/staticfiles/;`
  - `alias /var/www/EujimSolutionsPortal/media/;`

Enable the Nginx site configuration by creating a symbolic link:

```bash
sudo ln -s /etc/nginx/sites-available/eujim /etc/nginx/sites-enabled/
```

Test Nginx configuration for syntax errors:

```bash
sudo nginx -t
```

If test passes, restart Nginx:

```bash
sudo systemctl restart nginx
```

---

## Step 7: Configure PM2 Autostart on Server Reboot

To ensure your application automatically restarts if the server reboots:

```bash
pm2 save
pm2 startup
```

Copy and execute the exact `sudo env PATH=...` command generated by `pm2 startup` in your terminal.

---

## Step 8: Secure Server with SSL Certificate (HTTPS)

Install Certbot and the Nginx plugin:

```bash
sudo apt install -y certbot python3-certbot-nginx
```

Obtain and install SSL certificate for your domain:

```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

Certbot will automatically configure HTTPS redirect and set up automatic certificate renewal.

---

## Operational Commands & Troubleshooting

### Process Monitoring (PM2)

| Action | Command |
| :--- | :--- |
| View Process Status | `pm2 status` |
| View Real-time Logs | `pm2 logs` |
| View Specific Process Logs | `pm2 logs eujim-backend`<br>`pm2 logs eujim-celery-worker`<br>`pm2 logs eujim-celery-beat` |
| Restart All Processes | `pm2 restart ecosystem.config.js` |
| Stop All Processes | `pm2 stop ecosystem.config.js` |

### Application Logs Location

- **PM2 Logs**: `./logs/pm2_backend_out.log`, `./logs/pm2_celery_worker_out.log`, `./logs/pm2_celery_beat_out.log`
- **Gunicorn Logs**: `./logs/gunicorn_access.log`, `./logs/gunicorn_error.log`
- **Nginx Logs**: `/var/log/nginx/eujim_access.log`, `/var/log/nginx/eujim_error.log`

### Redeploying Code Updates

When pushing code updates in the future, run:

```bash
cd /var/www/EujimSolutionsPortal
git pull origin main
source .venv/bin/activate
pip install -r requirement.txt
./deploy.sh
```
