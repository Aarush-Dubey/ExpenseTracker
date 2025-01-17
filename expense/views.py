from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense, Category
from .forms import ExpenseForm , CategoryForm
from django.contrib.auth.decorators import login_required




@login_required
def category_list(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('category_list')
    else:
        category_form = CategoryForm()

    return render(request, 'expense/category_list.html', {'categories': categories, 'category_form': category_form})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.session.get('referrer_url', 'expense_list'))
    else:
        form = CategoryForm()
        request.session['referrer_url'] = request.META.get('HTTP_REFERER', 'expense_list')

    return render(request, 'expense/add_category.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expense/add_expense.html', {'form': form})



@login_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')  
    else:
        form = CategoryForm(instance=category)

    return render(request, 'expense/edit_category.html', {'form': form})


from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Expense
from django.contrib.auth.decorators import login_required
from django.db import transaction

@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    default_category = Category.objects.get_or_create(name='Uncategorized')[0]  

    if request.method == 'POST':
        with transaction.atomic():  
            expenses = Expense.objects.filter(category=category)
            expenses.update(category=default_category)
            category.delete()
        return redirect('category_list')
    
    return render(request, 'expense/delete_category.html', {'category': category})


@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expense/expense_list.html', {'expenses': expenses})

@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user 
            expense.save()
            return redirect('expense_list') 
    else:
        form = ExpenseForm()
    
    return render(request, 'expense/add_expense.html', {'expense_form': form})

@login_required
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense/edit_expense.html', {'form': form})

@login_required
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expense/delete_expense.html', {'expense': expense})
