from django.db import models

# Create your models here.

from django.db import models

class product(models.Model):
        def __str__(self):
            return self.name
        name=models.CharField(max_length=50)
        des=models.CharField(max_length=150)
        img=models.ImageField(upload_to='picture')

class offerproduct(models.Model):
    def __str__(self):
        return self.offer_name
    offer_name=models.CharField(max_length=50)
    offer_desc=models.CharField(max_length=150)
    offer_img=models.ImageField(upload_to='offer')
    old_price=models.DecimalField(max_digits=10,decimal_places=2)
    offer_price=models.DecimalField(max_digits=10,decimal_places=2)

