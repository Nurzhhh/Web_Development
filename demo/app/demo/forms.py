from django.forms import ModelForm
from .models import Demo

class Demoform(ModelForm):
    class Meta:
        model = Demo
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'What\'s on your mind?'})