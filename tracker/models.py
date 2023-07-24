from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    help_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expense')
    title = models.CharField(max_length=100)    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='order')
    date = models.DateField(default = timezone.now)
    amount = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    deductible = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='budget')
    week = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    month = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    annual = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.user.username} (#{self.user.id})'