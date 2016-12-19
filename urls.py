from django.conf.urls import url
from . import views as simple_auth_views
urlpatterns = [
    url(
        r'log-in',
        simple_auth_views.SimpleLogin.as_view(),
        name="log_in"
    ),
    url(
        r'log-out',
        simple_auth_views.SimpleLogout.as_view(),
        name="log_out"
    )
]