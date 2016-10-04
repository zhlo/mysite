from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	choice_number = models.IntegerField(default=1)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

class member(models.Model):
	name = models.CharField(max_length=50)
	sex = models.BooleanField(default=0)
	email = models.CharField(max_length=100)
	def __str__(self):
		return self.email