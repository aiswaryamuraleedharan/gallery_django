from django.forms import ModelForm
from .models import Img

class ImgForm(ModelForm):
    class Meta:
        model=Img
        fields='__all__'