from django.urls import path
from chat import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('add-product/', views.add_product, name='add_product'),
    # path('success/', views.success_view, name='success'),
      path('home/', views.home, name='home'),  # URL for the test view
       path('history/', views.history_view, name='history'),
]



