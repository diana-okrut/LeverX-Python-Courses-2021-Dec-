from django.contrib import admin

from .models import Teacher, HomeAssignment, Student, Course, Lecture, HomeWork, Score, TeacherComment, StudentComment


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(HomeWork)
admin.site.register(Score)
admin.site.register(HomeAssignment)
admin.site.register(TeacherComment)
admin.site.register(StudentComment)
