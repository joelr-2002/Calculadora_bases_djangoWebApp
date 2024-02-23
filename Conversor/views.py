from django.shortcuts import render
from django.http import HttpResponse
import json

# Vistas

def menu(request):
    return render(request, 'menu.html')

def hexadecimal_view(request):
    return render(request, 'hexadecimal.html')

def binary_view(request):
    return render(request, 'binario.html')

def octal_view(request):
    return render(request, 'octal.html')

def decimal_view(request):
    return render(request, 'decimal.html')


# Convertidores de bases: a binario

def bases_to_binary(request, number, type):
    
    # Convertir number a entero
    if type == 'hexadecimal':
        number = int(number, 16)
    elif type == 'octal':
        number = int(number, 8)
    else:
        number = int(number)
    
    if type == 'decimal':
        binario = bin(number)
    elif type == 'hexadecimal':
        binario = bin(number)
    elif type == 'octal':
        binario = bin(number)
        
    binario = binario.split("b")[1]
    cadena = "Binario: {}".format(binario)
    partes = cadena.split(": ")
    diccionario = {partes[0].strip(): partes[1].strip()}
    return HttpResponse(json.dumps(diccionario), content_type="application/json")
   
# Convertidores de bases: a octal