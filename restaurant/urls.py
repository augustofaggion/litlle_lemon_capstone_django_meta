from django.urls import path
from . import views

app_name = "restaurant"

urlpatterns = [
    path("", views.index, name="index"),  # /restaurant/
    path("menu-items/", views.MenuItemView.as_view(), name="menu_item_list"),
    path("menu-items/<int:pk>/", views.SingleMenuItemView.as_view(), name="menu_item_detail"),
]
