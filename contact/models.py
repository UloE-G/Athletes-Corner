from django.db import models

# Create your models here.
class Return(models.Model):
    order_number = models.CharField(max_length=254)
    reason = (
        ('Wrong color', 'Wrong color'),
        ('Wrong items', 'Wrong items'),
        ('Order did not fit', 'Order did not fit'),
        ('Order arrived too late', 'Order arrived too late'),
        ('Order was not as described', 'Order was not as described'),
        ('Other', 'Other'),
    )
    reasons = models.CharField(max_length=254, choices=reason, 
                               blank=True, 
                               null=True)
    other = models.TextField()

    def __str__(self):
        return self.order_number
