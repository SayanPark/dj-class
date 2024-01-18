from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='starting_page'),
    path('posts', views.posts, name='post_page'),
    path('posts/<slug:slug>', views.single_post, name='page_detail'),
    path('products', views.list_of_products),
    path('<slug:slug>', views.details_of_product)
]
