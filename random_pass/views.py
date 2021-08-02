from django.shortcuts import render
from django.contrib import messages
import string
import random
# Create your views here.


def password(request):
    rand_pass = ''
    characters = string.ascii_lowercase

    if request.GET.get('upper'):
        characters += string.ascii_uppercase

    if request.GET.get('number'):
        characters += string.digits

    if request.GET.get('special'):
        characters += '!@#$%^&*'

    # set default value to 0 in order to get empty alert..[ disappeared ]
    length = int(request.GET.get('length', 0))
    for i in range(length):
        rand_pass += random.choice(characters)

    messages.success(request, rand_pass)
    return render(request, 'random_pass/pass.html', {'password': rand_pass})

