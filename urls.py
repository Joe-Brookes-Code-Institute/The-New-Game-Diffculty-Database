from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game_difficulty_database.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('allauth.urls')),
]

from django.urls import get_resolver
resolver = get_resolver()
for url_pattern in resolver.url_patterns:
    print(url_pattern)