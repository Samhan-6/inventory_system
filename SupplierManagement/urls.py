from django.urls import path, include
from . import views

urlpatterns = [
    path('add_supplier/', views.add_supplier, name='add_supplier'),
    path('add_supplier/<int:supplier_id>/', views.add_supplier, name='edit_supplier')
]

