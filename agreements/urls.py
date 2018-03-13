from django.conf.urls import url

from .views import *


urlpatterns =[
url(r'^$', EdibleHome.index, name='index'),
        url(r'^agreements/$',  GeneratePDF.as_view(),name='agree'),
        url(r'agreehtml$', EdibleHome.agree1,name='agreehtml'),
        url(r'newenroll/', Enrollment.as_view(),name='enrolling'),
        ]
