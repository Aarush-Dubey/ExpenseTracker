from django.shortcuts import render, get_object_or_404, redirect
from .models import SavingGoal
from .forms import SavingGoalForm, DepositForm
from django.contrib.auth.decorators import login_required
from django.db import transaction

@login_required
def add_saving_goal(request):
    if request.method == 'POST':
        form = SavingGoalForm(request.POST)
        if form.is_valid():
            saving_goal = form.save(commit=False)
            saving_goal.user = request.user
            saving_goal.save()
            return redirect('saving_goals_list')
        else:
            return render(request, 'savings/add_saving_goal.html', {'form': form, 'error': 'Please correct the errors below.'})
    else:
        form = SavingGoalForm()
    return render(request, 'savings/add_saving_goal.html', {'form': form})

@login_required
def edit_saving_goal(request, pk):
    saving_goal = get_object_or_404(SavingGoal, pk=pk, user=request.user)
    if request.method == "POST":
        form = SavingGoalForm(request.POST, instance=saving_goal)
        if form.is_valid():
            form.save()
            return redirect('saving_goals_list')
    else:
        form = SavingGoalForm(instance=saving_goal)
    return render(request, 'savings/edit_saving_goal.html', {'form': form})

@login_required
def delete_saving_goal(request, pk):
    saving_goal = get_object_or_404(SavingGoal, pk=pk, user=request.user)
    if request.method == "POST":
        saving_goal.delete()
        return redirect('saving_goals_list')
    return render(request, 'savings/delete_saving_goal.html', {'saving_goal': saving_goal})

@login_required
def deposit_to_saving_goal(request, pk):
    saving_goal = get_object_or_404(SavingGoal, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            with transaction.atomic(): 
                saving_goal.amount_saved += amount
                saving_goal.save()
            return redirect('saving_goals_list')
    else:
        form = DepositForm()
    return render(request, 'savings/deposit_to_saving_goal.html', {'form': form, 'saving_goal': saving_goal})

@login_required
def saving_goals_list(request):
    goals = SavingGoal.objects.filter(user=request.user)
    for goal in goals:
        goal.excess_amount = max(0, goal.amount_saved - goal.target_amount)
        goal.is_achieved = goal.amount_saved >= goal.target_amount
        goal.progress_value = min(100, (goal.amount_saved / goal.target_amount) * 100) if goal.target_amount else 0
    return render(request, 'savings/saving_goals_list.html', {'saving_goals': goals})
