""""
Arquivo que consolida todos os links do blog teste
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list')
]
