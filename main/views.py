from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("Hello world!")


def test(request):
    return render(request, "test.html")

def third(request):
    return render(request, "This is page test3")