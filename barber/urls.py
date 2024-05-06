from django.urls import path
from .views import product_list
from .views import product_detail, category_filter
from .views import signup, user_login
urlpatterns = [
    path('', product_list, name='products_list'),
    path('<int:pk>/<slug:slug>/',product_detail, name='product_detail'),
    path('category/<int:pk>/', category_filter,name='category'),
    path('signup/',signup,name='signup'),
    path('login', user_login, name='login'),
]