from django.db import models
from django.contrib.auth.models import User
from datetime import date
#


class HandiCrafts(models.Model):
	a=[('s',"Sarees"),('T',"Toys"),('D',"Decor")]
	category_type=models.CharField(max_length=10,choices=a)
	im=models.ImageField(upload_to='handcrafts/',default='b.jpg')
	quantity=models.IntegerField()
	price=models.DecimalField(max_digits=6,decimal_places=2)
	da = models.DateField(auto_now_add=True)
	uid=models.ForeignKey(User,on_delete=models.CASCADE)


