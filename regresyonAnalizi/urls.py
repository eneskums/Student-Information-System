from django.conf.urls import url
from .views import machineLearning

app_name = 'regresyonAnalizi'

urlpatterns = [
    url(r'^regresyonAnalizi/$',machineLearning, name='regresyonAnalizi'),
]