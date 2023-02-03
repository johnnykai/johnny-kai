from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Expense


class ExpenseCreate(LoginRequiredMixin, CreateView):
    model = Expense
    fields = ['score']                  
    template_name = 'expense_form.html'        

    def form_valid(self, form):
        form.instance.target = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('msg_list')  

