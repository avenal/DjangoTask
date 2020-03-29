from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/add', views.add_user, name="add_user"),
    path('user/<int:id>', views.user, name="user"),
    path('user/<int:id>/edit', views.edit_user, name="edit_user"),
    path('user/<int:id>/delete', views.delete_user, name="delete_user"),
    path('user/csv', views.generate_csv, name="generate_csv")
]
