from django.shortcuts import render

def inicio(request):
	return render(request, "inicio.html")

def base_layout(request):
	return render(request, "base.html")
