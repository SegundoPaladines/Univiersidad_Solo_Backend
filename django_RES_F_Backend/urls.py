from django.contrib import admin
from django.urls import path

##------------------------------------------------------------------------------------------------------##
##Dar visibilidad a los archivos de media:
from django.conf import settings
from django.conf.urls.static import static

##--------------------------------------------------------------------------------------------------------##
##REST FRAMEWORK
from django.urls import include
from .router import router

##---------------------------------------------------------------------------------------------------------##

urlpatterns = [
    path('admin/', admin.site.urls),
    ##----------------------------------------------------------------------------------------------------------------------------------------##
    ##REST FRAMEWORK
    path('', include(router.urls)),
    path('api/',include('rest_framework.urls', namespace='rest_framework')),
]

##---------------------------------------------------------------------------------------------------------##
##Dar visibilidad a los archivos de media:

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
