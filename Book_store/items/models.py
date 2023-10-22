from django.db import models
from django.contrib.auth.models import User


# pass : i٢z0zYij']
# Create your models here.
class Category(models.Model):
    
    # NOTE!!!!! please keep in mind that you need 
    # to do this every time you do somethig here..
    # after you Done!
    # use makemigrations afer then use migrate!
    # lasty register that at admin.py!
    name = models.CharField(max_length=255)
    
    # change the objects 's'
    class Meta:
        ordering  = ('name', )
        verbose_name_plural = 'Categoreis'
        
    def __str__(self):
        return self.name

# Item object in the DataBase Admin!!!
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    descripion = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_image', blank='True', null=True)    
    sold_out = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
