from django.conf.urls import url, include
from django.contrib.auth import views as v
from accounts.forms import LoginForm
from accounts import views as account_views
from accounts.views import ResetPasswordRequestView
from accounts.views import PasswordResetConfirmView


urlpatterns = [
    url(r'^login/$', v.login, {'template_name': 'accounts/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', v.logout, {'next_page': '/'},  name='logout'),
    url(r'^change_password$', account_views.change_password, name='change_password'),
    url(r'^edit_profile/$', account_views.user_profile, name='edit_profile'),
    url(r'^signup/$', account_views.signup, name='signup'),
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),name='reset_password_confirm'),
    url(r'^password_success/$', account_views.password_success, name='password_success'),
    url(r'^forgot/$', ResetPasswordRequestView.as_view(), name='forgot'),
    url(r'^dashboard/$', account_views.dashboard, name='dashboard'),
    url(r'^match/dashboard/(?P<plan>[\w]+)/(?P<id>[\d]+)/(?P<idp>[\d]+)$', account_views.match_dashboard, name='match_dashboard'),
    url(r'^get/dashboard/(?P<plan>[\w]+)/(?P<id>[\d]+)/(?P<idp>[\d]+)$', account_views.get_dashboard, name='get_dashboard'),
    url(r'^match/wait/dashboard/$', account_views.match_wait_dashboard, name='match_wait_dashboard'),
    url(r'^get/wait/dashboard/$', account_views.get_wait_dashboard, name='get_wait_dashboard'),
    url(r'^account/details/$', account_views.account, name='account_details'),
    url(r'^plans/', include('ponzify.urls'), name='pick_a_plan'),
    url(r'^selected/plan/(?P<id>[\d]+)/(?P<plan>[\w]+)$', account_views.selected_plan, name='selected_plan'),
    url(r'^confirm_payment/1/(?P<user_id>[\d]+)/(?P<id>[\d]+)$', account_views.confirm_payment1, name='confirm_payment1'),
    url(r'^confirm_payment/2/(?P<user_id>[\d]+)/(?P<id>[\d]+)$', account_views.confirm_payment2, name='confirm_payment2'),
]