from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/create/', ExpenseCreate.as_view(), name='expense_create'), 
]