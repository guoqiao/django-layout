from django.shortcuts import render


def home(request):
    context = {
        'todo': 'TODO'
    }
    return render(request, 'home.html', context=context)
