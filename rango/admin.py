from django.contrib import admin
from .models import Category, Page
from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)  
admin.site.register(UserProfile)

#

# Register the Students model
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'YearEnrolled', 'CurrentYearStudent')
    search_fields = ('user__username',)


# Register other models
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('CourseID', 'CourseName')
    search_fields = ('CourseID', 'CourseName')

@admin.register(Enrolls)
class EnrollsAdmin(admin.ModelAdmin):
    list_display = ('user', 'CourseID')
    search_fields = ('user__username', 'CourseID__CourseID')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('user','user_id', 'CourseID', 'Topics', 'DateUploaded',"NoteID",'edited')
    search_fields = ('user__username', 'CourseID__CourseID', 'Topics',"NoteID",'edited')
