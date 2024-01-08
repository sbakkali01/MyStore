from django.urls import path
from . import views

app_name="store"

# TODO lire la doc de url dispatcher : voir doc de path
urlpatterns=[
    path('',views.all_products),
    path('item/<slug:slug>/',views.product_details,name='product_details'),
    path('search/<slug:category_slug>',views.category_list,name='category_list')
]