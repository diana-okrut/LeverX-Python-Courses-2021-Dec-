"""online_course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from course.views import (
    TeacherView,
    StudentView,
    HomeAssignmentView,
    CourseView,
    LectureView,
    HomeWorkView,
    ScoreView,
    TeacherCommentView,
    StudentCommentView,
)

router = routers.SimpleRouter()

router.register("teachers", TeacherView, basename="teachers")
router.register("students", StudentView, basename="students")
router.register("home-assignments", HomeAssignmentView, basename="home_assignments")
router.register("courses", CourseView, basename="courses")
router.register("lectures", LectureView, basename="lectures")
router.register("home-works", HomeWorkView, basename="home_works")
router.register("scores", ScoreView, basename="scores")
router.register("teacher-comments", TeacherCommentView, basename="teacher_comments")
router.register("student-comments", StudentCommentView, basename="student_comments")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
urlpatterns += router.urls
