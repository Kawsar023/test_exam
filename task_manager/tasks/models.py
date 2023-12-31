from django.db import models

class category(models.Model):
    cat_name = models.CharField(max_length=255)

class product(models.Model):
    product_name = models.CharField(max_length=255)
    product_qtt = models.IntegerField()
    product_price = models.FloatField()
    cat          = models.ForeignKey(category, on_delete=models.CASCADE)
    



class product_pic(models.Model):
    product_image = models.ImageField(upload_to='product_image/', blank=True, null= True)
    pro           = models.ForeignKey(product,on_delete=models.CASCADE)


