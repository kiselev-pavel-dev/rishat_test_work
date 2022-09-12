from django.urls import path

from . import views

urlpatterns = [
    path("item/<int:item_id>/", views.item, name="item"),
    path("buy/<int:item_id>/", views.buy, name="buy"),
    path("order/<int:user_id>/", views.order, name="order"),
    path("buy_order/", views.buy_order),
    path('success/', views.success, name="success"),
    path('cancell/', views.cancel, name="cancel"),
]
