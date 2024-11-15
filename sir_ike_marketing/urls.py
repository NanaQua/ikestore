from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload-product/', views.upload_product, name='upload_product'),
    path('search/', views.search_products, name='search_products'),
    path('adminpage/', views.adminPage),
    path('', views.home, name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


