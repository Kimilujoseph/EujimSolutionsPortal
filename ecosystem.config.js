const fs = require('fs');
const path = require('path');

// Load .env file into process.env if present
const envPath = path.resolve(__dirname, '.env');
if (fs.existsSync(envPath)) {
  const envConfig = fs.readFileSync(envPath, 'utf8');
  envConfig.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const equalsIndex = trimmed.indexOf('=');
      if (equalsIndex > 0) {
        const key = trimmed.substring(0, equalsIndex).trim();
        const value = trimmed.substring(equalsIndex + 1).trim().replace(/^['"]|['"]$/g, '');
        if (!process.env[key]) {
          process.env[key] = value;
        }
      }
    }
  });
}

module.exports = {
  apps: [
    {
      name: 'eujim-backend',
      script: 'gunicorn',
      args: '-c gunicorn.conf.py backend.asgi:application',
      interpreter: 'none',
      cwd: './',
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: '600M',
      env: {
        ...process.env,
        NODE_ENV: 'production',
        PYTHONUNBUFFERED: '1'
      },
      out_file: './logs/pm2_backend_out.log',
      error_file: './logs/pm2_backend_err.log',
      log_date_format: 'YYYY-MM-DD HH:mm:ss Z'
    },
    {
      name: 'eujim-celery-worker',
      script: 'celery',
      args: '-A backend worker --loglevel=info --pool=solo',
      interpreter: 'none',
      cwd: './',
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: '150M',
      env: {
        ...process.env,
        PYTHONUNBUFFERED: '1'
      },
      out_file: './logs/pm2_celery_worker_out.log',
      error_file: './logs/pm2_celery_worker_err.log',
      log_date_format: 'YYYY-MM-DD HH:mm:ss Z'
    },
    {
      name: 'eujim-celery-beat',
      script: 'celery',
      args: '-A backend beat --loglevel=info',
      interpreter: 'none',
      cwd: './',
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: '100M',
      env: {
        ...process.env,
        PYTHONUNBUFFERED: '1'
      },
      out_file: './logs/pm2_celery_beat_out.log',
      error_file: './logs/pm2_celery_beat_err.log',
      log_date_format: 'YYYY-MM-DD HH:mm:ss Z'
    }
  ]
};


