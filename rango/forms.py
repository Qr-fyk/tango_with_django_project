
from django import forms
from rango.models import Page, Category
from django.contrib.auth.models import User
from rango.models import UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=Category.NAME_MAXLEN,
        help_text="Please enter the category name."
    )
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(
        max_length=Page.TITLE_MAXLEN,
        help_text="Please enter the title of the page."
    )
    url = forms.URLField(
        max_length=200,
        help_text="Please enter the URL of the page."
    )
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values; we may not want to include them.
        # Here, we are hiding the foreign key.
        # We can either exclude the category field from the form,
        exclude = ('category',)
        # or specify the fields to include (don't include the category field).
        # fields = ('title', 'url', 'views')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
    
        # If url is not empty and doesn't start with 'http://',
        # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')



#
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('YearEnrolled', 'CurrentYearStudent')

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('CourseID', 'Topics', 'file')  # Fields to include in the form
       
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get the user from kwargs
        self.edited = kwargs.pop('edited', None)  # Get the edited note creator from kwargs
        self.CourseID = kwargs.pop('CourseID', None)  # Get the CourseID from kwargs
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['CourseID'].empty_label = 'Select a Course'

        # If CourseID is provided, set it as a hidden field
        if self.CourseID:
            
            self.fields['CourseID'].initial = self.CourseID
            self.fields['CourseID'].widget = forms.HiddenInput()
        
    def save(self, commit=True):
        # Save the form but don't commit to the database yet
        instance = super(NoteForm, self).save(commit=False)
        
        # Set the user field to the current user
        if self.user:
            instance.user = self.user
        
        # Set the edited field to the provided creator (if any)
        if self.edited:
            instance.edited = self.edited
        
        if commit:
            instance.save()  # Save the instance to the database
        
        return instance

    