from django.urls import path,include,re_path
from .views import PaperListView,PaperView,TrainView,Quit_Train,CourseTrainView

app_name = 'Exams'

urlpatterns = [
    #试卷列表
    path("paperlist/", PaperListView.as_view(),name='paperlist'),
    path('paper/<paper_id>/', PaperView.as_view(), name="paper"),
    path('train/<question_id>/', TrainView.as_view(), name="train"),
    path('quittrain/<question_id>/', Quit_Train, name="quittrain"),
    path('coursetrain/', CourseTrainView.as_view(), name="coursetrain"),
    # path('train/', TrainView.as_view(), name="train"),

]