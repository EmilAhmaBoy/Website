from django.urls import path
from .views import index, info, forum, signin, signup

urlpatterns = [
  path('', index, name='index'),
  path('info', info, name='info'),
  path('forum', forum, name='forum'),
  path('signin', signin, name='signin'),
  path('signup', signup, name='signup'),
]