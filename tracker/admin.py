from django.contrib import admin
from . import models

admin.site.register(models.Budget)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'help_text']
    prepopulated_fields = {'slug':('title',)}
    ordering = ['id']

@admin.register(models.Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'amount', 'date']
    list_filter = ['category', 'date']
    search_fields = ['title', 'category', 'amount', 'date']
    date_hierarchy = 'date'
    ordering = ['date', 'updated']