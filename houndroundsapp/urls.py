from django.conf.urls import patterns, url
from houndroundsapp import views

urlpatterns = patterns(
    '',
    url(r'signup',views.signup,name='signup'),
)
