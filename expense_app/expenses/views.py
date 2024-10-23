from rest_framework import generics
import csv
from django.http import HttpResponse
from .models import User, Expense, ExpenseSplit
from .serializers import UserSerializer, ExpenseSerializer
from django.http import JsonResponse

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddExpenseView(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

# Balance sheet retrieval
def balance_sheet(request, user_id):
    user = User.objects.get(id=user_id)
    expenses = Expense.objects.filter(added_by=user)
    total_expense = sum(exp.total_amount for exp in expenses)
    
    return JsonResponse({
        'user': user.name,
        'total_expense': total_expense,
        'expenses': list(expenses.values())
    })

def download_balance_sheet(request, user_id):
    user = User.objects.get(id=user_id)
    expenses = Expense.objects.filter(added_by=user)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="balance_sheet_{user_id}.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Description', 'Total Amount', 'Split Method', 'Date'])
    
    for expense in expenses:
        writer.writerow([expense.description, expense.total_amount, expense.split_method, expense.created_at])
    
    return response
