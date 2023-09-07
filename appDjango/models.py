from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_title = models.CharField(max_length=250,null=True,blank=True)
    item_description = models.TextField(max_length=9000,null=True,blank=True)
    item_image = models.ImageField(upload_to='item/',null=True,blank=True)

    def __str__(self):
        return f'{self.item_title}'