const fs = require('fs');
const path = require('path');

// Robust .env loader — handles quoted values, inline comments, and = inside values
const envPath = path.resolve(__dirname, '.env');
if (fs.existsSync(envPath)) {
  const envConfig = fs.readFileSync(envPath, 'utf8');
  envConfig.split(/\r?\n/).forEach(line => {
    const trimmed = line.trim();
    // Skip blank lines and comment lines
    if (!trimmed || trimmed.startsWith('#')) return;

    const equalsIndex = trimmed.indexOf('=');
    if (equalsIndex <= 0) return;

    const key = trimmed.substring(0, equalsIndex).trim();
    let value = trimmed.substring(equalsIndex + 1);

    // Strip inline comments only if value is NOT quoted
    // Detect if value starts with a quote
    const firstChar = value.trimStart()[0];
    if (firstChar === '"' || firstChar === "'") {
      // Quoted value: find matching closing quote
      const quote = firstChar;
      const inner = value.trimStart().slice(1);
      const closeIdx = inner.indexOf(quote);
      value = closeIdx >= 0 ? inner.substring(0, closeIdx) : inner;
    } else {
      // Unquoted: strip inline comment (# preceded by whitespace)
      value = value.replace(/\s+#.*$/, '').trim();
    }

    // Only set if not already defined in environment
    if (key && !process.env[key]) {
      process.env[key] = value;
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


