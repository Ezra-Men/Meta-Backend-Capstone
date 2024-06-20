from django.db import models

# Create your models here.
class Booking (models.Model):
	id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=255)
	no_of_guest = models.IntegerField()
	booking_date = models.DateTimeField()

class MenuItem (models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	inventory = models.SmallIntegerField(default=0)

	def get_item(self):
		return f'{self.Title} : {str(self.Price)}'
