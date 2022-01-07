from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Teacher, HomeAssignment, Student, Course, Lecture, HomeWork, Score, TeacherComment, StudentComment


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        return user

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}

        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
        )


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = (
            'score',
            'teacher',
            'homework',
            'author',
            'updated_at',
        )


class TeacherCommentSerializer(serializers.ModelSerializer):
    score = ScoreSerializer

    class Meta:
        model = TeacherComment
        fields = (
            'text',
            'updated_at',
            'teacher',
            'score',
        )


class StudentCommentSerializer(serializers.ModelSerializer):
    score = ScoreSerializer

    class Meta:
        model = StudentComment
        fields = (
            'text',
            'updated_at',
            'student',
            'score',
        )


class HomeWorkSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True)

    class Meta:
        model = HomeWork
        fields = (
            'student',
            'home_assignment',
            'text',
            'scores',
        )


class StudentSerializer(serializers.ModelSerializer):
    homeworks = HomeWorkSerializer(many=True)

    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'email',
            'courses',
            'homeworks',
            )


class TeacherSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True)

    class Meta:
        model = Teacher
        fields = (
            'first_name',
            'last_name',
            'email',
            'courses',
            'scores',
        )


class HomeAssignmentSerializer(serializers.ModelSerializer):
    home_works = HomeWorkSerializer(many=True)

    class Meta:
        model = HomeAssignment
        fields = (
            'task',
            'lecture',
            'author',
            'updated_at',
            'score',
            'home_works',

        )


class LectureSerializer(serializers.ModelSerializer):
    home_assignments = HomeAssignmentSerializer(many=True)

    class Meta:
        model = Lecture
        fields = (
            'name',
            'file',
            'course',
            'author',
            'updated_at',
            'home_assignments',
        )


class CourseSerializer(serializers.ModelSerializer):
    lectures = LectureSerializer(many=True)
    teachers = TeacherSerializer(many=True)
    students = StudentSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            'name',
            'lectures',
            'teachers',
            'students',
        )


