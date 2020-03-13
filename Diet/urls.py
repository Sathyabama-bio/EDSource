from django.conf.urls import url

from Diet import views

urlpatterns = [

    url(r'^$',views.index,name='index'),

    url('^Dietplan/$',views.Dietplan),

]
