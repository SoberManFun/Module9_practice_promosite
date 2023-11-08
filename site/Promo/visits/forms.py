from visits.models import Flat, House, Company, Visit, VisitFlat, FlatContact, UserCompanies
from django import forms


class UserCompaniesForm(forms.ModelForm):
    Companies = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label=None)

    exclude = ('UserCompanies_User', 'UserCompanies_Company')

    class Meta:
        model = UserCompanies
        fields = ()


class FlatsAddForm(forms.ModelForm):
    Flat_Number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    Flat_Owner = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    House = forms.ModelChoiceField(queryset=House.objects.all(), empty_label=None)

    class Meta:
        model = Flat
        fields = ('Flat_Number', 'Flat_House_Address', 'Flat_Owner', 'House')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['House'].label_from_instance = lambda \
            obj: f"{obj.House_Place}, {obj.House_Street}, {obj.House_Number}"

    def save(self, commit=True):
        flat = super().save(commit=False)
        flat.Flat_House_Address = self.cleaned_data['House']
        if commit:
            flat.save()
        return flat


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
            obj: f"{obj.House_Place}, {obj.House_Street}, {obj.House_Number}"

    def save(self, commit=True):
        flat = super().save(commit=False)
        flat.Flat_House_Address = self.cleaned_data['House']
        if commit:
            flat.save()
        return flat


class FlatsContactEditForm(forms.ModelForm):
    FlatContact_Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate',
                                                                     'placeholder': 'Имя'}))
    FlatContact_Phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control validate',
                                                                         'placeholder': 'Телефон'}))
    FlatContact_Comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Комментарий', "cols": "40",
                                                                       "rows": "5"}))
    # FlatContact_Comment.widget.attrs.update("cols": "40", "rows": "10")
    exclude = ('Flat',)  # Исключаем поле Flat из формы

    class Meta:
        model = FlatContact
        fields = ('FlatContact_Name', 'FlatContact_Phone', 'FlatContact_Comment')


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

    def clean_my_field(self):
        data = self.cleaned_data['Company_Name']
        if "'" in data or '"' in data:
            raise forms.ValidationError("Поле не должно содержать символы одинарных или двойных кавычек")
        return data


class HousesAddForm(forms.ModelForm):
    House_Place = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate',
                                                                 'placeholder': 'Местонахождение'}))
    House_Street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate',
                                                                     'placeholder': 'Улица'}))
    House_Number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate',
                                                                   'placeholder': '№ дома'}))
    House_Floor_Numbers = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Этажность'}))
    House_Amount_Entrances = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Количество подъездов/парадных)))'}))
    House_Amount_Flats = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Количество квартир'}))

    class Meta:
        model = House
        fields = ('House_Place', 'House_Street', 'House_Number',
                  'House_Floor_Numbers', 'House_Amount_Entrances', 'House_Amount_Flats')


class HousesEditForm(forms.ModelForm):
    House_Place = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate', 'title': 'Местонахождение'}))
    House_Street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate', 'title': 'Улица'}))
    House_Number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate', 'title': 'Дом'}))
    House_Floor_Numbers = forms.IntegerField(widget=forms.TextInput(attrs={'title': 'Этажность'}))
    House_Amount_Entrances = forms.IntegerField(widget=forms.TextInput(attrs={'title': 'Количество подъездов\парадных'}))
    House_Amount_Flats = forms.IntegerField(widget=forms.TextInput(attrs={'title': 'Количество квартир'}))

    class Meta:
        model = House
        fields = ('House_Place', 'House_Street', 'House_Number',
                  'House_Floor_Numbers', 'House_Amount_Entrances', 'House_Amount_Flats')


class VisitsAddForm(forms.ModelForm):
    StatusDoor = (
        ("False", "Не открыли"),
        ("True", "Открыли"),
    )
    Reaction = (
        ("1", "Позитивно"),
        ("2", "Нейтрально"),
        ("3", "Негативно"),
        ("4", ""),
    )
    Visit_Num = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    Visit_Date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control validate', 'type': 'date', 'title': 'Пример 01.01.2000'}))
    Visit_Time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control validate', 'type': 'time',  'title': 'Пример 11:30'}))
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
        ("4", ""),
    )
    Visit_Num = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    Visit_Date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control validate', 'type': 'date'}))
    Visit_Time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control validate', 'type': 'time'}))
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
