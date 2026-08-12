const fs = require('fs');
const path = require('path');

// Robust .env loader — handles quoted values, inline comments, CRLF, and UTF-8 BOM
const envPath = path.resolve(__dirname, '.env');
if (fs.existsSync(envPath)) {
  // Strip UTF-8 BOM (\uFEFF) that Windows editors sometimes prepend to files
  const rawContent = fs.readFileSync(envPath, 'utf8').replace(/^\uFEFF/, '');
  rawContent.split(/\r?\n/).forEach(line => {
    // Strip any stray non-printable/BOM chars from the line itself
    const trimmed = line.replace(/[\uFEFF\u200B]/g, '').trim();
    // Skip blank lines and comment lines
    if (!trimmed || trimmed.startsWith('#')) return;

    const equalsIndex = trimmed.indexOf('=');
    if (equalsIndex <= 0) return;

    // Sanitize key: only allow word characters (letters, digits, underscore)
    const key = trimmed.substring(0, equalsIndex).trim().replace(/[^\w]/g, '');
    let value = trimmed.substring(equalsIndex + 1);

    // Strip inline comments only if value is NOT quoted
    const firstChar = value.trimStart()[0];
    if (firstChar === '"' || firstChar === "'") {
      // Quoted value: find the matching closing quote
      const quote = firstChar;
      const inner = value.trimStart().slice(1);
      const closeIdx = inner.indexOf(quote);
      value = closeIdx >= 0 ? inner.substring(0, closeIdx) : inner.trim();
    } else {
      // Unquoted: strip trailing inline comment (# preceded by whitespace)
      value = value.replace(/\s+#.*$/, '').trim();
    }

    // Only set if key is valid and not already defined in the environment
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


