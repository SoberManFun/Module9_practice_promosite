from django.db import models


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
    Flat_Number = models.IntegerField(5)
    Flat_Owner = models.CharField(max_length=150)
    House = models.ForeignKey(to=House, on_delete=models.CASCADE)
  # Visits = models.ForeignKey(to=Visits, on_delete=models.CASCADE)

    def __str__(self):
        return f'Квартира: {self.Flat_Number} | Дом: {self.Flat_House_Address} | Владелец: {self.Flat_Owner}'

class Flat_Contact(models.Model):
    Flat_Contact_Name = models.CharField(max_length=150)
    Flat_Contact_Phone = models.IntegerField(32)
    Flat_Contact_Comment = models.TextField(null=True, blank=True)
    Flat = models.ForeignKey(to=Flat, on_delete=models.CASCADE)
