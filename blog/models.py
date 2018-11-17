from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): #Definimos un objeto y "Post" es el nombre. lo de los parentesis significa que es un modelo de django
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)#numero limitado de caracteres
	text = models.TextField()#texto largo sin límites
	created_date = models.DateTimeField(
		default=timezone.now)#fecha y hora
	published_date = models.DateTimeField(
		blank=True, null=True)#relación link

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self): #los dos guiones se llaman dunder
		return self.title
