from django.forms import ModelForm

from .models import CoverLetter



class TemporalCoverLetterForm(ModelForm):
    class Meta:
        model = CoverLetter
        fields = '__all__'
