from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    name = models.CharField("Название курса", max_length=256)

    def __str__(self):
        return str(self.name)


class Lecture(models.Model):
    name = models.CharField("Название лекции", max_length=256)
    file = models.FileField(upload_to='uploads/')
    course = models.ForeignKey(Course, related_name='lectures', on_delete=models.CASCADE)
    author = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    updated_at = models.DateTimeField()

    def __str__(self):
        return (
            f'{self.name}',
            f'{self.updated_at}',
        )


class HomeAssignment(models.Model):
    task = models.TextField('Задание')
    lecture = models.ForeignKey(Lecture, related_name='home_assignments', on_delete=models.CASCADE)
    author = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    updated_at = models.DateTimeField()
    score = models.OneToOneField('Score', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.task}'


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='teacher')
    courses = models.ManyToManyField(Course, related_name='teachers')


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='student')
    courses = models.ManyToManyField(Course, related_name='courses')


class HomeWork(models.Model):
    student = models.ForeignKey(Student, related_name='homeworks', on_delete=models.CASCADE)
    home_assignment = models.ForeignKey(HomeAssignment, on_delete=models.CASCADE)
    text = models.TextField()


class Score(models.Model):
    score = models.IntegerField("Оценка")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    homework = models.OneToOneField(HomeWork, on_delete=models.CASCADE)
    updated_at = models.DateTimeField()

    def __str__(self):
        return (
            f'{self.score}',
            f'{self.updated_at}'
        )


class Comment(models.Model):
    text = models.TextField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return (
            f'{self.text}',
            f'{self.updated_at}'
        )

    class Meta:
        abstract = True


class TeacherComment(Comment):
    teacher = models.ForeignKey(Score, related_name="t_comments",  on_delete=models.CASCADE)


class StudentComment(Comment):
    student = models.ForeignKey(Score, related_name="s_comments", on_delete=models.CASCADE)
