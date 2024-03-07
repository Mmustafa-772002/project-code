from django.db import models

# Create your models here.


class textlang(models.Model):
	CHOICES = (
		('hi', 'Hindi'),
        ('mr', 'Marathi'),
        ('pa', 'Punjabi'),
        ('ta', 'Tamil'),
        ('te', 'Telugu'),
        ('bn', 'Bengali'),
        ('gu', 'Gujarati'),
        ('kn', 'Kannada'),
        ('ml', 'Malayalam'),
        ('or', 'Odia'),
        ('ur', 'Urdu'),
		)
	text = models.CharField(max_length=150)
	lang1 = models.CharField(max_length=15,choices=CHOICES)
	lang2 = models.CharField(max_length=15,choices=CHOICES)

	def __self__(self):
		return self.text,self.lang