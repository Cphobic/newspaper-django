from django import forms
from .models import Post

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Field, Fieldset, Div
from crispy_forms.layout import Layout, Submit, Row, Column


class CustomTextarea(Field):
    template = 'paper/custom_texarea.html'


class CustomeTextInput(Field):
    template = 'paper/custom_textinput.html'


class CustomImageInput(Field):
    template = 'paper/custom_imageinput.html'


class PostCreateForm(forms.Form):

    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': ''
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': ''
    }))
    cover_photo = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            CustomeTextInput('title'),
            CustomTextarea(
                'content', css_class='md-textarea form-control'),
            CustomImageInput('cover_photo'),
            Submit('submit', 'Post',
                   css_class='btn btn-outline-info btn-rounded btn-block my-4 waves-effect z-depth-0'),
        )

    # def clean(self):
    #     cleaned_data = super(PostCreateForm, self).clean()
    #     return cleaned_data

# class PostCreateForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'cover_photo']


class PostUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        print(kwargs)
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        print(dir(self.fields['cover_photo'].widget_attrs))
        self.helper = FormHelper()
        self.helper.layout = Layout(
            CustomeTextInput('title'),
            CustomTextarea(
                'content', css_class='md-textarea form-control'),
            CustomImageInput('cover_photo', css_class=''),
            Submit('submit', 'Post',
                   css_class='btn btn-outline-info btn-rounded btn-block my-4 waves-effect z-depth-0'),
        )
        print((self.helper['_form_style']))

    class Meta:
        model = Post
        fields = ('title', 'content', 'cover_photo')
