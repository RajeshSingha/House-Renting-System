from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.views import View
from django.core.urlresolvers import reverse

def redirectTo(url):
    return HttpResponseRedirect(reverse(url))

def Index(request):
    return render(request, 'index.html', {'user': request.user})


def profile(request):
    return HttpResponse("Hello " + request.user.username)

