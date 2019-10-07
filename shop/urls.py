from django.urls import path
from . import views

app_name='shop'
urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('aboutus/', views.aboutUs, name='aboutUs'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name='ProdCatDetail'),

]
