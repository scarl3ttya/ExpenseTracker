from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.core import serializers
from django.db.models import Avg, Count
from datetime import datetime
from .models import Budget, Expense, Category
from .forms import BudgetForm, ExpenseForm

def index(request):
    return render(request, 'index.html')

@require_POST
def post_budget(request):
    budget, _ = Budget.objects.get_or_create(user=request.user)
    form = BudgetForm(request.POST)  
    
    if form.is_valid(): 
        periodic = form.cleaned_data['budget_periodic']
        amount = abs(form.cleaned_data['budget_amount'])

        if periodic == 0: #week
            budget.week = amount
            budget.month = round((30/7)*amount,2)
            budget.annual = 52*amount
        elif periodic == 1: #month
            budget.week = round((7/30)*amount, 2)
            budget.month = amount
            budget.annual = 52*amount
        elif periodic == 2: #year
            budget.week = round((7/30)*amount/52, 2)
            budget.month = round(amount/12, 2)
            budget.annual = amount
        else:
            return HttpResponse("{'message':'Unable to save'}", content_type='application/json')
    
        budget.save() 
        
    #else:        
        #return JsonResponse(form.errors, safe=False, status=200)
    
    return HttpResponse(serializers.serialize("json", [budget]), content_type='application/json')

@require_POST
def list_expense(request):
    current_year = datetime.now().year
    expense = Expense.objects.filter(user=request.user).filter(date__year=current_year)
    if expense.exists() and expense.count():
        return HttpResponse(serializers.serialize("json", list(expense,)), content_type='application/json')
    else:
        return HttpResponse('{"message":"Empty Object"}', content_type='application/json')    
    
@require_POST
def post_expense(request):
    form = ExpenseForm(request.POST)
    print(form.data)
    
    if form.is_valid():
        cd = form.cleaned_data
        expense = Expense(user=request.user)
        cat = Category.objects.get(title=cd['expense_form_category'] )
        expense.title = cd['expense_form_title']    
        expense.category = cat
        expense.date = cd['expense_form_date']
        expense.amount = cd['expense_form_amount']
        expense.deductible = cd['expense_form_deductible']
        expense.comment = cd['expense_form_comment']
        expense.save()
        return HttpResponse(serializers.serialize("json", [expense]), content_type='application/json')
    else:
        return JsonResponse(form.errors, safe=False, status=200)
    #return HttpResponse('{"message":"Empty Object"}', content_type='application/json')   
