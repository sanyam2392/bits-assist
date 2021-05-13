from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Answer,Question




class AnswerForm(ModelForm):
    class Meta:
        model=Answer
        fields=('detail',)

class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=('title','detail','tags')

class ProfileForm(ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name','username')