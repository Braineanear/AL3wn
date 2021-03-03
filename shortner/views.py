from django.shortcuts import render, redirect
from .models import Url

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    url_details.views = url_details.views +1
    url_details.save()
    return redirect(url_details.link)