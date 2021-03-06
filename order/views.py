from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from .models import Order
from .forms import OrderForm
from page.models import Page
from .admin import OrderAdmin

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

class OrderView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    #model= Order
    context_object_name='order'
    

    #def get_queryset(self):
        #return Order.objects.filter(username=self.request.user)
    def get_queryset(self):
        return Order.objects.all()

    def get_context_data(self, **kwargs):
        context=super(OrderView, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context
    
class OrderList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    #model = Order
    context_object_name = 'all_orders'
    
    #def get_queryset(self):
       #return Order.objects.filter(username=self.request.user)
    def get_queryset(self):
        return Order.objects.all()

    def get_context_data(self, **kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context



def order_req(request):
    submitted = False
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/order/?submitted=True')
    else:
        form = OrderForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'order/order.html',
    {'form': form, 'page_list': Page.objects.all(),
    'submitted': submitted})

