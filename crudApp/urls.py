from django.urls import path
from . import views




urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/',views.create_item, name='create_item'),
    path('update/<int:pk>', views.update_item, name='update_item'),
    path('delete/<int:pk>', views.delete_item, name='delete_item'),
]