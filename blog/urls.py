
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>', detail, name ='detail'),
    path('new/', new, name = 'new'),
    path('create/', Create, name = 'create'),
    path('edit/<str:id>', edit, name ='edit'),
    path('update/<str:id>',update, name = 'update'),
    path('delete/<str:id>', delete, name = 'delete'), # pathconverter: 각 개체를 받아서 저장 html로 넘겨줘
]