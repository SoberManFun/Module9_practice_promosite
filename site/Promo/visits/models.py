from django.db import models
from users.models import User


class House(models.Model):
    House_Place = models.CharField(max_length=32)
    House_Street = models.CharField(max_length=150)
    House_Number = models.CharField(max_length=32)
    House_Floor_Numbers = models.IntegerField(3, default=0)
    House_Amount_Entrances = models.IntegerField(3)
    House_Amount_Flats = models.IntegerField(5, default=0)

    def __str__(self):
        return self.House_Number


class Flat(models.Model):
    Flat_House_Address = models.TextField(null=True, blank=True)
    Flat_Number = models.IntegerField(5, default=0)
    Flat_Owner = models.CharField(max_length=150)
    House = models.ForeignKey(to=House, on_delete=models.CASCADE)

    def __str__(self):
        return f'Квартира: {self.Flat_Number} | Дом: {self.Flat_House_Address} | Владелец: {self.Flat_Owner}'


class FlatContact(models.Model):
    FlatContact_Name = models.CharField(max_length=150)
    FlatContact_Phone = models.IntegerField(32, default=0)
    FlatContact_Comment = models.TextField(null=True, blank=True)
    Flat = models.ForeignKey(to=Flat, on_delete=models.CASCADE)


class Visit(models.Model):
    Visit_Num = models.IntegerField
    Visit_Date = models.DateField
    Visit_Company = models.CharField(max_length=150)
    Visit_Employee = models.CharField(max_length=150)
    Visit_House = models.TextField(null=True, blank=True)
    Visit_Door = models.BooleanField
    Visit_Reaction = models.CharField(max_length=25)
    User = models.ForeignKey(to=User, on_delete=models.PROTECT)

    def __str__(self):
        return f'Обход №: {self.Visit_Num} | Дом: {self.Visit_House} | Сотрудник: {self.Visit_Employee} ' \
               f'| Компания: {self.Visit_Company}'


class VisitFlat(models.Model):
    VisitFlat_Visit = models.ForeignKey(to=Visit, on_delete=models.CASCADE)
    VisitFlat_Flat = models.IntegerField(5, default=0)


class Company(models.Model):
    Company_Name = models.CharField(max_length=150)
    Company_INN = models.IntegerField(25, default=0)
    Company_Director = models.CharField(max_length=150)
    Company_Place = models.CharField(max_length=32)
    Company_Street = models.CharField(max_length=150)
    Company_House_Number = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.Company_Name}'

#    def __str__(self):
#        return f'Компания: {self.Company_Name} | Директор: {self.Company_Director}'


class UserCompanies(models.Model):
    UserCompanies_User = models.ForeignKey(to=User, on_delete=models.CASCADE)
    UserCompanies_Company = models.ForeignKey(to=Company, on_delete=models.CASCADE)


class CompaniesHouse(models.Model):
    CompaniesHouse_Company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    CompaniesHouse_House = models.ForeignKey(to=House, on_delete=models.CASCADE)
