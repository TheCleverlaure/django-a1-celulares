from django.db import models
from django.shortcuts import reverse


CATEGORY_CHOICES = (
    ('A', 'Auriculares'),
    ('F', 'Forros'),
    ('VT', 'Vidrio Templado'),
    ('C', 'Cargador'),
    ('CU', 'Cable USB'),
    ('AD', 'Adaptadores')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default='A')
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, default='P')
    stock = models.IntegerField(default=1)
    image_url = models.CharField(max_length=2083, default='../static_in_env/img/no-photo-available.png')
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("store:product", kwargs={
            'slug': self.slug
        })
    
    def get_add_to_cart_url(self):
        return reverse("store:add_to_cart", kwargs={
            'slug': self.slug
        })
    
    def get_remove_from_cart_url(self):
        return reverse("store:remove_from_cart", kwargs={
            'slug': self.slug
        })

