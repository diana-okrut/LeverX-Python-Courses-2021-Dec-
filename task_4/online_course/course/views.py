from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import viewsets

from .models import (
    Teacher,
    HomeAssignment,
    Student,
    Course,
    Lecture,
    HomeWork,
    Score,
    TeacherComment,
    StudentComment,
)
from .serializers import (
    TeacherSerializer,
    StudentSerializer,
    CourseSerializer,
    LectureSerializer,
    HomeWorkSerializer,
    ScoreSerializer,
    HomeAssignmentSerializer,
    TeacherCommentSerializer,
    StudentCommentSerializer,
)


class TeacherView(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.all()


class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()


class HomeAssignmentView(viewsets.ModelViewSet):
    serializer_class = HomeAssignmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return HomeAssignment.objects.all()


class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Course.objects.all()

    # def create(self, request, *args, **kwargs):
    #     pass

    def check_object_permissions(self, request, obj):
        if obj.user != request.user:
            raise PermissionDenied


class LectureView(viewsets.ModelViewSet):
    serializer_class = LectureSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Lecture.objects.all()


class HomeWorkView(viewsets.ModelViewSet):
    serializer_class = HomeWorkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return HomeWork.objects.all()


class ScoreView(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Score.objects.all()


class TeacherCommentView(viewsets.ModelViewSet):
    serializer_class = TeacherCommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return TeacherComment.objects.all()


class StudentCommentView(viewsets.ModelViewSet):
    serializer_class = StudentCommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return StudentComment.objects.all()
