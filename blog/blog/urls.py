from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from  posts.views import blog, blog_details
from product.views import product_detail

app_name = 'posts'


urlpatterns = [

    path('admin/', admin.site.urls),
    path('blog/', blog, name='blog'),
    path('<int:month>/<int:day>/<slug:post>/', blog_details, name='blog_details'),
    path('product_detail/', product_detail, name='product-detail' )


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

