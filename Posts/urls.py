"""Опеределение схемы URl для приложения"""

from django.urls import path
from . import views

app_name = 'Posts'

urlpatterns = [
    #Домашняя страница
    path('',views.index, name = 'index'),
	path('info/',views.info,name = 'info'),
    path('topics/',views.topics, name = 'topics'),
    path('history/',views.history, name = 'history'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/',views.new_topic,name = 'new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('search/',views.SearchResultsView.as_view(),name = 'search'),
    path('profile/',views.profiler,name = 'profile'),
    path('test/',views.p_test, name = 'test'),
    path('upload_test/',views.upload_test, name = 'upload_test'),
]
