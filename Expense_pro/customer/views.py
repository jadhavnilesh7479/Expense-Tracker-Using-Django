from django.shortcuts import render,redirect
from .models import Expense


# Create your views here.


def read(request):

    ex = Expense.objects.all()
    return render(request,'index.html',{'ex':ex})


def add(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        comments = request.POST.get('comments')  

    ex = Expense(
        category = category,
        amount = amount,
        comments = comments,
    ) 
    ex.save()
    return redirect('/')



def edit(request):
    ex = Expense.objects.all()
    context = {
        'ex':ex
    }
    return redirect('/',context)


def update(request,id):
    if request.method == 'POST':
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        comments = request.POST.get('comments')

    ex = Expense(
        id = id,
        category = category,
        amount = amount,
        comments = comments,
    )

    ex.save()
    return redirect('/')



def delete(request,id):
    ex = Expense.objects.filter(id = id)
    ex.delete()
    return redirect('/')