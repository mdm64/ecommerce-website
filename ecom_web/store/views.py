from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product, OrderItem1, ShippingAddress
import json
from django.views.generic import CreateView
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.contrib.auth.decorators import login_required


def home(request):
    members = Product.objects.all()
    context = {
        'members': members
    }
    return render(request, 'store/home.html', context)

def help(members):
    items     = 0
    price     = 0
    prod_dict = []

    for x in members:
        prod   = Product.objects.get(name = x.product)
        img    = prod.image.url

        items += x.quantity
        price += x.quantity*prod.price

        prod_dict.append(
            {
                'total':x.quantity*prod.price, 
                'prod_price':prod.price, 
                'img': img,
                'id': prod.id,
            }
        )

    return (items, price, prod_dict)

@login_required
def cart(request):
    members = OrderItem1.objects.filter(user = request.user)
    
    items, price, prod_dict = help(members)
    
    my_zip = zip(members, prod_dict)

    context = {
        'my_zip': my_zip,
        'price': price,
        'items':items,
    }

    return render(request, 'store/cart.html', context)

def updateItem(request):
    data        = json.loads(request.body)
    productId   = data['productID']
    action      = data['action']

    prod          = Product.objects.get(id=productId)
    
    order1  = OrderItem1.objects.filter(product=prod)
    order   = order1.filter(user=request.user).first()

    if order == None:
        order = OrderItem1.objects.create(user=request.user, product=prod)
        order.save()

    if action == 'add':
        order.quantity += 1
    elif action == 'remove':
         order.quantity -= 1
    order.save()

    if  order.quantity <= 0:
        order.delete()

    return JsonResponse('Item was added', safe=False)

@login_required
def ordersummary(request):
    order   = OrderItem1.objects.filter(user=request.user)
    info    = ShippingAddress.objects.filter(user=request.user).first()
    
    items, price, prod_dict = help(order)
    
    my_zip = zip(order, prod_dict)

    context = {
        'my_zip': my_zip,
        'price': price,
        'items':items,
        'info': info,
    }

    return render(request, 'store/ordersummary.html', context)

class creatCheckout(CreateView):
    model = ShippingAddress
    template_name = 'store/checkout.html'
    fields = ['username', 'address', 'city', 'state', 'zipcode']
    success_url = '/ordersummary/'

    def form_valid(self, form):
        form.instance.user = self.request.user # to tell that only user can create the post
        return super().form_valid(form)

@login_required
def send_html_template(request):
    order   = OrderItem1.objects.filter(user=request.user)
    info    = ShippingAddress.objects.filter(user=request.user).first()

    items, price, prod_dict = help(order)

    prod = [f'{x.product.name} x {x.quantity}' for x in order]

    subject, from_email, to = "Hello! You have recieved a new order", "djangouser64@gmail.com", "mehramayank0906@gmail.com"

    text_content = f"Hello! a new order has been recieved. \n Adress : \n{info.address} \n {info.city}, \n {info.state}, \n {info.zipcode} \n Products list: {prod} \n Total No. Of Items are {items} \n Total: Rs{price} "
    email = EmailMultiAlternatives(subject, text_content, from_email, [to])
    email.send()
    
    for i in order:
        i.delete()
    
    info.delete()

    return render(request, 'store/orderplaced.html')

def about(request):
    return render(request, 'store/about.html')