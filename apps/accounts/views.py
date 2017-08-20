from django.shortcuts import render


def profile(request):
    context = {
        'todo': 'TODO'
    }
    return render(request, 'accounts/profile.html', context=context)
