from visits.models import Flat, House
from django import forms


class FlatsEditForm(forms.ModelForm):
    Flat_Number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    Flat_Owner = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    House = forms.ModelChoiceField(queryset=House.objects.all(), empty_label=None)

    class Meta:
        model = Flat
        fields = ('Flat_Number', 'Flat_House_Address', 'Flat_Owner', 'House')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['House'].label_from_instance = lambda \
            obj: f"{obj.House_Place} {obj.House_Street} {obj.House_Number}"

    def save(self, commit=True):
        flat = super().save(commit=False)
        flat.Flat_House_Address = self.cleaned_data['House']
        if commit:
            flat.save()
        return flat
