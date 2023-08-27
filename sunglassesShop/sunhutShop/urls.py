from django.urls import path
from . import views

app_name= 'sunhutShop'


urlpatterns = [
    path('home/',views.all_products,name='all_products')

]