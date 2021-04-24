from django.urls import path
from App import views
from django.contrib.auth import views as ay
from django.contrib.auth import views as ad
urlpatterns = [
	path('',views.home,name='hm'),
	path('lg/',ay.LoginView.as_view(template_name="html/login.html"),name="log"),
	path('reg/',views.register,name="rg"),
	path('con/',views.contact,name='cn'),
	path('hcft/',views.hc,name='hct'),
	path('lgo/', ad.LogoutView.as_view(template_name='html/logout.html'),name='logo'),
	path('pro/',views.profile,name='p'),
]