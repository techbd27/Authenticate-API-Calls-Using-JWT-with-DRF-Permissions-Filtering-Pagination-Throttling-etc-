from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, ContactViewSet, AuthorViewSet, BookViewSet


from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register("tasks", TaskViewSet)
router.register("contacts", ContactViewSet)
router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("api/", include(router.urls)),
]
