from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

class Expense(models.Model):
    description = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    EQUAL = 'equal'
    EXACT = 'exact'
    PERCENTAGE = 'percentage'
    SPLIT_METHOD_CHOICES = [
        (EQUAL, 'Equal'),
        (EXACT, 'Exact'),
        (PERCENTAGE, 'Percentage'),
    ]
    
    split_method = models.CharField(max_length=10, choices=SPLIT_METHOD_CHOICES)

class ExpenseSplit(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_owed = models.DecimalField(max_digits=10, decimal_places=2)
    percentage_owed = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

