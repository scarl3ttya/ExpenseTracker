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

@register.inclusion_tag('includes/expense_widget.html')
def show_weekly_expenses(user):
    first_day_of_week, last_day_of_week = get_week()
    expenses_for_week = Expense.objects.filter(user=user, date__range=[first_day_of_week.strftime("%Y-%m-%d"),
                            last_day_of_week.strftime("%Y-%m-%d")])
    budget, _ = Budget.objects.get_or_create(user=user)
    _budget= '{:0,.2f}'.format(budget.week)
    avg_expenses = expenses_for_week.aggregate(_avg = Avg('amount'))
    sum_expenses = expenses_for_week.aggregate(_sum = Sum('amount'))
    count_expenses =  expenses_for_week.aggregate(_count = Count('amount'))  
    expenses = {'budget_title':'Weekly Budget', 'expense_title':'Weekly Expenses',
                 'color':'success', 'budget':_budget, 'span':days_of_week(), 
                 'avg':f'{avg_expenses["_avg"]:.2f}', 'sum':f'{sum_expenses["_sum"]:.2f}',
                'count':count_expenses["_count"], 'expense_name':'weekly_expense_div', 'budget_name':'weekly_budget_div' }
    
    return expenses

@register.inclusion_tag('includes/expense_widget.html')
def show_monthly_expenses(user):
    _month = today.month
    expenses_for_month = Expense.objects.filter(user=user,date__month=_month)
    budget, _ = Budget.objects.get_or_create(user=user)
    _budget= '{:0,.2f}'.format(budget.month)
    avg_expenses = expenses_for_month.aggregate(_avg = Avg('amount'))
    sum_expenses = expenses_for_month.aggregate(_sum = Sum('amount'))
    count_expenses =  expenses_for_month.aggregate(_count = Count('amount'))
    
    expenses = {'budget_title':'Monthly Budget', 'expense_title':'Monthly Expenses',
                 'color':'primary', 'span':today.strftime("%B \'%y"), 'budget':_budget,
                 'avg':f'{avg_expenses["_avg"]:.2f}', 'sum':f'{sum_expenses["_sum"]:.2f}',
                'count':count_expenses["_count"], 'expense_name':'monthly_expense_div', 'budget_name':'monthly_budget_div' }
    
    return expenses

@register.inclusion_tag('includes/expense_widget.html')
def show_annual_expenses(user):
    _year = today.year
    budget, _ = Budget.objects.get_or_create(user=user)
    _budget= '{:0,.2f}'.format(budget.annual)
    
    expenses_for_year = Expense.objects.filter(user=user,date__year=_year)
    avg_expenses = expenses_for_year.aggregate(_avg = Avg('amount'))
    sum_expenses = expenses_for_year.aggregate(_sum = Sum('amount'))
    count_expenses =  expenses_for_year.aggregate(_count = Count('amount'))
    
    expenses = {'budget_title':'Monthly Budget', 'expense_title':'Monthly Expenses',
                'color':'primary', 'span':today.strftime("%Y"), 'budget':_budget,
                'avg':f'{avg_expenses["_avg"]:.2f}', 'sum':f'{sum_expenses["_sum"]:.2f}',
                'count':count_expenses["_count"], 'name':'annual_expense_div', 'expense_name':'annual_expense_div', 'budget_name':'annual_budget_div'}
    
    return expenses


