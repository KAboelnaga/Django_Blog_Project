from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Regular HTML views
    path('', include('blogs.urls') ),
    path('subscriptions/', include('subscriptions.urls', namespace='subscriptions')),
    path('forbidden/', include('forbidden.urls')),
    path('', include('users.urls', namespace='users')),
    # API routes
    path('api/comments/', include('comments.urls')),  # change to 'api/comments/'
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
