# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def login(request):
	return render(request, "inicio/index.html")#,{'nombre':nombre})

def about(request):
	return render(request, "inicio/about.html")