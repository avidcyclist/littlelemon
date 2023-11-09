from django.db import models


#booking model
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name
#menu model
class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title
