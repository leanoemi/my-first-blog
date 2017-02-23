from django.conf.urls import url
import views

urlpatterns = [
    url(r'^posts/([0-9]+)$', views.post),
]
