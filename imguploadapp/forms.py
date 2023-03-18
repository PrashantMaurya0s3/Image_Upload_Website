from django import forms
from imguploadapp.models import ImageUploadModel


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = '__all__'
