from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_teacher = models.BooleanField('Is teacher', default=False)
    is_student = models.BooleanField('Is student', default=False)



class Project(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=(
        ('in_progress', 'En cours'),
        ('submitted', 'Soumis'),
        ('corrected', 'Corrigé'),
        ('processed', 'Traité'),
        ('archived', 'Archivé'),
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    submission_deadline = models.DateTimeField()
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file = models.FileField(upload_to='projects/', null=True, blank=True)


class Submission(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to='submission_files/')
    submission_date = models.DateTimeField(auto_now_add=True)
    instructor_comments = models.TextField(null=True, blank=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)


class ArchivedProject(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    archived_project_file = models.FileField(
        upload_to='archived_project_files/')
    archived_date = models.DateTimeField(auto_now_add=True)


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class TeacherCourse(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class StudentCourse(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class ProjectInstruction(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    instructions = models.TextField()
