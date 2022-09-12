import stripe
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from test_rishat.settings import STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY

from .models import Item

stripe.api_key = STRIPE_SECRET_KEY


def item(request, item_id=None):
    template = "index.html"
    items = get_object_or_404(Item, pk=item_id)
    context = {"items": items, "public_key": STRIPE_PUBLISHABLE_KEY}
    return render(request, template, context)


def order(request, user_id=None):
    template = "order.html"
    user = get_object_or_404(User, pk=user_id)
    products = user.orders.all()
    items = [item.product for item in products]
    context = {"items": items, "public_key": STRIPE_PUBLISHABLE_KEY}
    return render(request, template, context)


def buy(request, item_id=None):
    item = get_object_or_404(Item, pk=item_id)
    product = stripe.Product.create(name=item.name)
    price = stripe.Price.create(
        product=product, unit_amount=item.price * 100, currency=item.currency
    )
    session = stripe.checkout.Session.create(
        line_items=[{"price": price, "quantity": 1}],
        mode='payment',
        success_url='http://localhost:8000/success/?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='http://localhost:8000/cancel/',
    )
    return JsonResponse({"session_id": session["id"]})


def buy_order(request, user_id=1):
    usd = 60
    eur = 60
    user = request.user
    products = []
    items = user.orders.all()
    for item in items:
        if item.product.currency == "usd":
            price = item.product.price * usd
        elif item.product.currency == "eur":
            price = item.product.price * eur
        else:
            price = item.product.price
        product = stripe.Product.create(name=item.product.name)
        price = stripe.Price.create(
            product=product,
            unit_amount=price * 100,
            currency="rub",
        )
        products.append({"price": price, "quantity": 1})
    session = stripe.checkout.Session.create(
        line_items=products,
        mode='payment',
        success_url='http://localhost:8000/success/?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='http://localhost:8000/cancel/',
    )
    return JsonResponse({"session_id": session["id"]})


def success(request):
    template = "success.html"
    session_id = request.GET["session_id"]
    session = stripe.checkout.Session.retrieve(session_id)
    customer = session["customer_details"]["name"]
    context = {"customer": customer}
    return render(request, template, context)


def cancel(request):
    template = "cancel.html"
    return render(request, template)
