from django.contrib import admin
from django.urls import path,include
import blog.views
import portfolio.views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',blog.views.home,name='home'),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('portfolio/',portfolio.views.portfolio,name="portfolio"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
