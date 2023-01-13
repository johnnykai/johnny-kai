from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Message
from expenses.models import Expense

class MessageList(ListView):
    model = Message
    ordering = ['-id'] #change -id into -score

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        for msg in ctx['message_list']:
            score = 0
            expense_list = Expense.objects.filter(target=msg.id)

            if expense_list.exists():
                for exp in expense_list:
                    score += exp.score
                msg.score = round(score / len(expense_list), 1)
            else:
                msg.score = "No one has commented🥸"
            
            #msg.expense_form = Expense.objects.filter(target=msg.id)

        #ctx['expense_form'] = msg.expense_form
        return ctx

class MessageDetail(DetailView):
    model = Message

class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'subject', 'content']
    success_url = reverse_lazy('msg_list')

class MessageDelete(DeleteView):
    model = Message
    success_url = reverse_lazy('msg_list')


# Create your views here.

