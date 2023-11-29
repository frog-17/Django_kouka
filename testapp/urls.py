from django.urls import path
from . import views

app_name = 'profileapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('custom/', views.IndexCustomView.as_view(), name='index_custom'),
    path('wareki/', views.WarekiViews.as_view(), name='wareki'),
    path('gpt/', views.GptViews.as_view(), name='gpt'),
    path('contact/', views.ContactViews.as_view(), name='contact')
]
