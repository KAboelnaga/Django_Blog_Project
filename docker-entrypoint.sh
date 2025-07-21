#!/bin/bash

set -e

echo "🔄 Applying database migrations..."
python manage.py migrate --noinput

echo "📦 Loading initial post data if file exists..."
if [ -f posts.json ]; then
    python manage.py loaddata posts.json
else
    echo "⚠️  posts.json not found. Skipping loaddata."
fi

echo "🖼️ Ensuring media directory exists..."
if [ -d media ]; then
    echo "✅ Media directory found."
else
    echo "⚠️  Media directory not found. Creating empty one..."
    mkdir media
fi

echo "🚀 Starting server..."
exec "$@"
