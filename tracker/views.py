from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.core import serializers
from .models import Budget
from .forms import BudgetForm

def index(request):
    return render(request, 'index.html')

@require_POST
def post_budget(request):
    budget, _ = Budget.objects.get_or_create(user=request.user)
    form = BudgetForm(request.POST)  
    
    if form.is_valid(): 
        periodic = form.cleaned_data['budget_periodic']
        amount = abs(form.cleaned_data['budget_amount'])

        if periodic == 0:
            budget.week = amount
            budget.month = round((30/7)*amount,2)
            budget.annual = 52*amount
        elif periodic == 1:
            budget.week = round((7/30)*amount, 2)
            budget.month = amount
            budget.annual = 52*amount
        elif periodic == 2:
            budget.week = round((7/30)*amount/52, 2)
            budget.month = round(amount/12, 2)
            budget.annual = amount
        else:
            return HttpResponse("{'message':'Unable to save'}", content_type='application/json')
    
        budget.save() 
        
    else:        
        return JsonResponse(form.errors, safe=False, status=200)
    return HttpResponse(serializers.serialize("json", [budget]), content_type='application/json')
