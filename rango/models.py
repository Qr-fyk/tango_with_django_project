import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    NAME_MAXLEN = 128

    name = models.CharField(max_length=NAME_MAXLEN, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    TITLE_MAXLEN = 128

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAXLEN)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
    
    ##
class Students(models.Model):
    YearEnrolled = models.IntegerField()
    CurrentYearStudent = models.IntegerField(default= 1)
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    def __str__(self):
        return self.user.username
    

class Courses(models.Model):
    CourseID = models.CharField(primary_key= True, max_length=10)
    CourseName = models.CharField(max_length=200)
    def __str__(self):
        return self.CourseID + ": "+self.CourseName

class Enrolls(models.Model):
    user = models.ForeignKey(Students, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(Courses, on_delete= models.CASCADE)

class Note(models.Model):
    user = models.ForeignKey(Students, on_delete= models.CASCADE)
    DateUploaded = models.DateTimeField(auto_now_add=True)
    CourseID = models.ForeignKey(Courses, on_delete= models.CASCADE)
    Topics = models.CharField(max_length=200)
    NoteID = models.AutoField(primary_key=True)
    file = models.FileField(upload_to="Documents/")
    edited = models.IntegerField(null = True)
