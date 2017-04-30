# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

# Create your views here.


def homePage(request):
    return render_to_response("base.html", {'user': request.user})



