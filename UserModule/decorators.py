from django.http import HttpResponse
from django.shortcuts import redirect


def authenticatedUser(take_a_view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return take_a_view_func(request, *args, **kwargs)

    return wrapper_func
