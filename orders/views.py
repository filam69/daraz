from django.shortcuts import render
from .models import Order
from qrcodes.models import Game
def order(request):
    orders = Order.objects.all()
    games = Game.objects.all()
    return render(request, 'orders_page.html', {'orders': orders, 'games': games})
