from django.urls import path
from . import views 

urlpatterns = [
 
    path('',views.home , name='home'),
    path('logout/' , views.logout_user , name="logout"),
    path('register/', views.register_user , name="register"),
    path('record/<int:pk>', views.customer_records , name="record"),
    path('delete/<int:pk>', views.delete_records , name="delete"),
    path('add_record/', views.add_records , name="add_records"),
    path('update_record/<int:pk>', views.update_records , name="update_record"),
]