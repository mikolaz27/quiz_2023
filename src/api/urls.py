from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import CustomerViewSet, QuestionDetailView, QuizListView

app_name = "api"
router = routers.DefaultRouter()
router.register("customers", CustomerViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Quiz API",
        default_version="v1",
        description="API for passing questions",
        term_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.jwt")),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="swagger_docs"),
    path("quiz/<int:pk>/question/<int:order>/", QuestionDetailView.as_view(), name="question_details"),
    path("quiz/", QuizListView.as_view(), name="quiz_list"),
]
