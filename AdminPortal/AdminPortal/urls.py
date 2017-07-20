
from django.conf.urls import url
from django.contrib import admin
from assessment import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='assessment-home'),
    url(r'^assessment/$',views.home1, name= 'assessment-add'),
    url(r'^assessment/list$', views.AssessmentList.as_view(), name='assessment-list'),
    url(r'assessment/(?P<pk>.*)/edit/$', views.QuestionUpdate.as_view(), name='assessment-update'),
    url(r'assessment/(?P<pk>.*)/delete/$', views.DeleteAssessment.as_view(), name='assessment-delete'),
    url(r'assessment/(?P<pk>.*)/detail/$', views.DetailAssessment.as_view(), name='assessment-detail'),
]
