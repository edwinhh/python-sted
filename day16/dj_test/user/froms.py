from .models import Article
from utils.tools import FormatFormError
from django.forms import ModelForm
class ArticleForm(ModelForm,FormatFormError):
    class Meta:
        model = Article
        fields = '__all__'
