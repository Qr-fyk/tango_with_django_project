# Generated by Django 2.2.28 on 2025-03-18 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('CourseID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('CourseName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('YearEnrolled', models.IntegerField()),
                ('CurrentYearStudent', models.IntegerField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('DateUploaded', models.DateTimeField(auto_now_add=True)),
                ('Topics', models.CharField(max_length=200)),
                ('NoteID', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='Documents/')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Students')),
            ],
        ),
        migrations.CreateModel(
            name='Enrolls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Students')),
            ],
        ),
        migrations.CreateModel(
            name='EditedNotes',
            fields=[
                ('EditedID', models.AutoField(primary_key=True, serialize=False)),
                ('DateUploaded', models.DateField(auto_now_add=True)),
                ('file', models.FileField(null=True, upload_to='Edited_Note/')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Courses')),
                ('NoteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Note')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Students')),
            ],
        ),
    ]
