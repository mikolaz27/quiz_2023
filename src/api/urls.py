from django.urls import include, path
from rest_framework import routers

from api.views import CustomerViewSet, QuestionDetailView, QuizListView

app_name = "api"
router = routers.DefaultRouter()
router.register("customers", CustomerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("quiz/<int:pk>/question/<int:order>/", QuestionDetailView.as_view(), name="question_details"),
    path("quiz/", QuizListView.as_view(), name="quiz_list"),
]
