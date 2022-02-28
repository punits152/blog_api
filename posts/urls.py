from django.urls import path
from .views import PostDetail, PostList, UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("users",UserViewSet)

urlpatterns = [
    #ADDING THESE ROUTES TO URLPATTERN

    # Using simple views for views
    path('<int:pk>',PostDetail.as_view()),
    path('',PostList.as_view())

] + router.urls
