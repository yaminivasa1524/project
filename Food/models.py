from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Exfd(models.Model):
	g =[('M','Male'),('FM','FeMale')]
	# clg = [('AANM',"AANM & VVRSR Polytechnic"),('SVGP',"S.V Govt polytechnic"),('AANMR',"AANM & VVRSR Polytechnic - RJYD")]
	d = models.OneToOneField(User,on_delete=models.CASCADE)
	age = models.IntegerField(null=True)
	gender = models.CharField(choices=g,max_length=10)
	# rollno = models.CharField(max_length=10)
	# collegename = models.CharField( max_length= 7,choices=clg)
	impf = models.ImageField(upload_to="Profile/",default="bulb.jpg")


@receiver(post_save,sender=User)
def Crpf(sender,instance,created,**kwargs):
	if created:
		Exfd.objects.create(d=instance)

class South(models.Model):
	g = [('al','Vada'),('ab','Wheat upma')]
	item= models.CharField(max_length=200,choices=g)
	price= models.IntegerField(null=True)
	quantity = models.IntegerField(null=True)
	category = models.CharField(max_length=10)




class Work(models.Model):
	wks = [('yes','completed'),('no','Not completed')]
	date = models.DateField()
	description = models.TextField()
	workstatus = models.CharField(max_length=5,choices=wks)
	m= models.ForeignKey(User,on_delete=models.CASCADE)

# class Item(models.Model):
# 	id 			= models.AutoField(primary_key=True)
# 	fname 		= models.CharField(max_length=30,blank=False)
# 	category 	= models.CharField(max_length=50,blank=False)

# 	def __str__(self):
# 		return self.fname

# class Room(models.Model):
# 	ROOM_CATEGORIES = [
# 	    ('YAC','AC'),
# 	    ('NAC','NON-AC'),
# 	    ('DEL','DELUXE'),
# 	    ('KIN','KING'),
# 	    ('QUE','QUEEN'),
# 	]
# 	number =models.IntegerField()
# 	category = models.CharField(max_length=3,choices=ROOM_CATEGORIES)
# 	beds = models.IntegerField()
# 	capacity = models.IntegerField()
# 	def __str__(self):
# 		return f'{self.number}.{self.category} with {self.beds}.{self.capacity} people'

# Create your models here.
