from visits.models import Flat, House, Company, Visit, VisitFlat
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


class CompaniesEditForm(forms.ModelForm):
    Company_Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate',
                                                                 'placeholder': 'Наименование компании'}))
    Company_Director = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate',
                                                                     'placeholder': 'Директор'}))
    Company_INN = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control validate',
                                                                   'placeholder': 'ИНН'}))
    Company_Place = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Город, пгт, аул, итд'}))
    Company_Street = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Улица'}))
    Company_House_Number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Номер дома'}))

    class Meta:
        model = Company
        fields = ('Company_Name', 'Company_INN', 'Company_Director',
                  'Company_Place', 'Company_Street', 'Company_House_Number')


class VisitsAddForm(forms.ModelForm):
    StatusDoor = (
        ("False", "Не открыли"),
        ("True", "Открыли"),
    )
    Reaction = (
        ("1", "Позитивно"),
        ("2", "Нейтрально"),
        ("3", "Негативно"),
    )
    Visit_Num = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    Visit_Date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control validate'}))
    Visit_Time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control validate'}))
    Visit_Company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label=None)
    Visit_Employee = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    Visit_House = forms.ModelChoiceField(queryset=House.objects.all(), empty_label=None)
    Visit_Door = forms.ChoiceField(choices=StatusDoor)
    Visit_Reaction = forms.ChoiceField(choices=Reaction)
    exclude = ('User',)  # Исключаем поле user из формы

    class Meta:
        model = Visit
        fields = ('Visit_Num', 'Visit_Date', 'Visit_Time', 'Visit_Company', 'Visit_Employee',
                  'Visit_House', 'Visit_Door', 'Visit_Reaction')
       # fields = '__all__'


class VisitsFlatsAddForm(forms.ModelForm):
    VisitFlat_Flat = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    # VisitFlat_Flat = forms.CharField(widget=forms.Textarea)  # Поле ввода для списка квартир
    exclude = ('VisitFlat_Visit',)  # Исключаем поле VisitFlat_Visit из формы

    class Meta:
        model = VisitFlat
        fields = ('VisitFlat_Flat',)
       # fields = '__all__'


class VisitsEditForm(forms.ModelForm):
    StatusDoor = (
        ("False", "Не открыли"),
        ("True", "Открыли"),
    )
    Reaction = (
        ("1", "Позитивно"),
        ("2", "Нейтрально"),
        ("3", "Негативно"),
    )
    Visit_Num = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    Visit_Date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control validate'}))
    Visit_Time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control validate'}))
    Visit_Company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label=None)
    Visit_Employee = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    Visit_House = forms.ModelChoiceField(queryset=House.objects.all(), empty_label=None)
    Visit_Door = forms.ChoiceField(choices=StatusDoor)
    Visit_Reaction = forms.ChoiceField(choices=Reaction)
    exclude = ('User',)  # Исключаем поле user из формы

    class Meta:
        model = Visit
        fields = ('Visit_Num', 'Visit_Date', 'Visit_Time', 'Visit_Company', 'Visit_Employee',
                  'Visit_House', 'Visit_Door', 'Visit_Reaction')
       # fields = '__all__'


class VisitsFlatsEditForm(forms.ModelForm):
    VisitFlat_Flat = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    # VisitFlat_Flat = forms.CharField(widget=forms.Textarea)  # Поле ввода для списка квартир
    exclude = ('VisitFlat_Visit',)  # Исключаем поле VisitFlat_Visit из формы

    class Meta:
        model = VisitFlat
        fields = ('VisitFlat_Flat',)
       # fields = '__all__'
