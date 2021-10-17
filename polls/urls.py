from django.urls import path

from . import views

app_name = 'polls' # namespace for urls, using as polls:detail in html

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # 例如: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # 例如: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('table/', views.table, name='table'),
    path('search/', views.search, name='search'),
    path('charts/', views.echarts, name='echarts'),
    path('forms/', views.form, name='form'),
    path('ajax_post', views.ajax_post, name='ajax_post'),
]