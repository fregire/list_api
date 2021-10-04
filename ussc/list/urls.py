from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ItemsView.as_view()),
    path('list/<int:pk>', views.ItemView.as_view())
]