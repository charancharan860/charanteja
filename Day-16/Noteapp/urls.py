from django.urls import path
from Noteapp import views
from django.contrib.auth import views as ad

urlpatterns = [
path('',views.home,name='ch'),
path('a/',views.about,name='cg'),
path('b/',views.contact,name='ci'),
path('lg/', ad.LoginView.as_view(template_name='html/login.html'),name='log'),
path('rg/',views.regi,name='rg'),
path('ds/',views.dashboard, name='dsh'),
path('lgo/', ad.LogoutView.as_view(template_name='html/logut.html'),name='logo'),

]