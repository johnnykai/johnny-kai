from django.urls import path
from .views import *

urlpatterns = [
    path('', ExpenseList.as_view(), name='expense_list'), 
    path('<int:pk>/create/', ExpenseCreate.as_view(), name='expense_create'), 
]