from django.conf.urls import url
from ponzify import views as ponzify_views
from accounts import views as account_views

urlpatterns = [
    url(r'^$', ponzify_views.select_plan, name='pick_a_plan'),

]