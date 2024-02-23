from django.urls import path
from .views import menu, hexadecimal_view, binary_view, octal_view, decimal_view, bases_to_binary

urlpatterns = [
    path('menu', menu, name='menu'),
    path('hexadecimal', hexadecimal_view, name='hexadecimal'),
    path('binario', binary_view, name='binario'),
    path('octal', octal_view, name='octal'),
    path('decimal', decimal_view, name='decimal'),
    
    path('bases_to_binary/<str:number>/<str:type>', bases_to_binary, name='bases_to_binary'),
]