from django.shortcuts import render

from django.views.generic import View

from budget.models import Transaction

from django import forms

class TransactionForm(forms.ModelForm):

    class Meta:
        model=Transaction
        exclude=("created_date",)
        # fields="__all__"
        # fields=["field1","field2",]


# Create your views here.
# view for listing all transaction
# url:localhost:8000/transactions/all/
# method:get

class TransactionListView(View):
    def get(self,request,*args,**kwargs):
        qs=Transaction.objects.all()
        return render(request,"transaction_list.html",{"data":qs})
    

# view for creating transaction
# url:localhost:8000/transactions/add/
# method:get,post
    
class TransactionCreateView(View):
    def get(self,request,*args,**kwargs):
        form=TransactionForm()
        return render(request,"transaction_add.html",{"form":form})
    
    





