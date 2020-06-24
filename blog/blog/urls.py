from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from  posts.views import blog, blog_details

app_name = 'posts'

 
urlpatterns = [

    path('admin/', admin.site.urls),
    path('blog/', blog, ),
    path('blog_details/<id>/', blog_details, name='post-detail' ),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

