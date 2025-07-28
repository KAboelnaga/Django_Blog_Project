#!/bin/bash

set -e

echo "🔄 Applying database migrations..."
python manage.py migrate --noinput

echo "✅ Creating required categories..."
python manage.py shell -c "
from blogs.models import Category;
Category.objects.get_or_create(id=1, defaults={'name': 'Sports'});
Category.objects.get_or_create(id=2, defaults={'name': 'Politics'});
Category.objects.get_or_create(id=3, defaults={'name': 'Economy'});
Category.objects.get_or_create(id=4, defaults={'name': 'Technology'});
Category.objects.get_or_create(id=5, defaults={'name': 'Culture'});
"

echo "📝 Loading initial posts if file exists..."
if [ -f posts.json ]; then
    python manage.py loaddata posts.json
else
    echo "⚠️  posts.json not found. Skipping post loaddata."
fi

echo "🖼️ Ensuring media directory exists and has correct permissions..."
mkdir -p /app/media
chmod -R 755 /app/media

echo "🚀 Starting server..."
exec "$@"
