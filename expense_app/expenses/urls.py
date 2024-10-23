from django.urls import path
from .views import CreateUserView, AddExpenseView, balance_sheet, download_balance_sheet

urlpatterns = [
    path('user/', CreateUserView.as_view(), name='create_user'),
    path('expense/', AddExpenseView.as_view(), name='add_expense'),
    path('balance_sheet/<int:user_id>/', balance_sheet, name='balance_sheet'),
    path('download_balance_sheet/<int:user_id>/', download_balance_sheet, name='download_balance_sheet'),
]
