from django.urls import path

from . import views

app_name = 'polls'
# urlpatterns = [
#     # ex: /polls/ 로 뷰가호출된다는 의미.
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]


# URLconf 수정
# 두 번째와 세 번째 패턴의 경로 문자열에서 일치하는 패턴들의 이름이 <question_id>에서 <pk>로 변경.
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # pk값은 중복되지 않는다. 데이터 하나의 열.
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]