from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home, name='Home'),
    url(r'^login/$', views.Login, name='Login'),
    url(r'^signup/$', views.SignUp, name='SignUp'),
    # url(r'^login/$', views.weblog, name='weblog'),
    url(r'^login/homepage/$',views.HomePage,name='HomePage'),
    url(r'^login/homepage/showpost/$', views.Show_post, name='show_post'),
    url(r'^login/homepage/createpost/$', views.Create_post, name='create_post'),
    url(r'^login/homepage/update/$', views.Update, name='update'),
    url(r'^login/homepage/delete/$', views.Delete, name='delete'),
    url(r'^login/homepage/showpost/(?P<post_pk>[0-9]+)', views.add_comment_or_like, name="add_comment"),
    url(r'^login/homepage/logout/$', views.Logout, name='logout'),


]
