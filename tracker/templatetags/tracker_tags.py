from django import template
from datetime import datetime, timedelta
from django.utils.safestring import mark_safe
from django.db.models import Sum, Avg, Count
import time
from ..models import Budget, Expense


register = template.Library()
today = datetime.today()


def get_week():
    _weekday = today.weekday()        
    first_day_of_week = today - timedelta(days=(1+ _weekday))
    last_day_of_week = today + timedelta(days=(5 - _weekday))   
    return first_day_of_week, last_day_of_week


@register.simple_tag
def days_of_week():    
    first_day_of_week, last_day_of_week = get_week()  
    return f'{first_day_of_week.strftime("%m/%d/%y")} - {last_day_of_week.strftime("%m/%d/%y")}'

@register.simple_tag
def monthly_expenses(user):
    _month = today.month
    expenses_for_month = Expense.objects.filter(user=user,date__month=_month)
    avg_expenses = expenses_for_month.aggregate(_avg = Avg('amount'))
    sum_expenses = expenses_for_month.aggregate(_sum = Sum('amount'))
    count_expenses =  expenses_for_month.aggregate(_count = Count('amount'))
    r = f'${sum_expenses["_sum"]:.2f}' +'<sup> total</sup><br>'\
        +f'${avg_expenses["_avg"]:.2f}'+'<sup> avg</sup><br><small>'+f'{count_expenses["_count"]}'+' transactions</small>'
    return mark_safe(r)

@register.simple_tag
def weekly_expenses(user):
    first_day_of_week, last_day_of_week = get_week()
    expenses_for_week = Expense.objects.filter(user=user, date__range=[first_day_of_week.strftime("%Y-%m-%d"), last_day_of_week.strftime("%Y-%m-%d")])
    avg_expenses = expenses_for_week.aggregate(_avg = Avg('amount'))
    sum_expenses = expenses_for_week.aggregate(_sum = Sum('amount'))
    count_expenses =  expenses_for_week.aggregate(_count = Count('amount'))    
    r = f'${sum_expenses["_sum"]:.2f}' +'<sup> total</sup><br>'\
        +f'${avg_expenses["_avg"]:.2f}'+'<sup> avg</sup><br><small>'+f'{count_expenses["_count"]}'+' transactions</small>'
    return mark_safe(r)




