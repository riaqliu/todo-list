from django.urls import path
from .views import TodosView

urlpatterns = [
    path('', TodosView.as_view())
]
