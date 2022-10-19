"""P9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.auth.views import LoginView
from django.contrib import admin
from django.urls import path
import authentication.views
import flux.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('home/', flux.views.home, name='home'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('flux/create_ticket', flux.views.create_ticket, name='ticket_create'),
    path('flux/create_review', flux.views.create_review, name='review_create'),
    path('flux/subscribe', flux.views.follow_users, name='subscription'),
    path('flux/post', flux.views.post, name='post'),
    path('flux/<int:id>/update_ticket/', flux.views.update_ticket, name='ticket_update'),
    path('flux/<int:id>/delete_ticket', flux.views.delete_ticket, name='ticket_delete'),
    path('flux/<int:id>/update_review', flux.views.update_review, name='review_update'),
    path('flux/<int:id>/delete_review', flux.views.delete_review, name='review_delete'),
    path('flux/<int:id>/unsubscribe', flux.views.unsubscribe, name='unsubscribe'),
    path('flux/<int:id>/create_review_onticket', flux.views.create_review_onticket, name='create_review_onticket'),
]
# code pour flux
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
