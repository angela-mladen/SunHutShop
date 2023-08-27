from django.db import models

# Create your models here.
PRODUCT_CATEGORIES = (
    ('men','men'),
    ('women','women')
)

class Brand(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    model_code=models.CharField(max_length=255)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    price=models.FloatField()
    category=models.CharField(max_length=10,choices=PRODUCT_CATEGORIES)
    image=models.ImageField(upload_to="product_images/",null=True)
    slug=models.SlugField()

    def __str__(self):
        return f"{self.brand} - {self.model_code}"





