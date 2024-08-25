from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "ADPyBlog Administration"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to ADPyBlog Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('blog/', include("blog.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
