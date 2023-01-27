from django.shortcuts import render

rooms = [
    {"id": 1, "name": "Room first"},
    {"id": 2, "name": "Room second"},
    {"id": 3, "name": "Room third"},

]


# Create your views here.
def home(request):
    return render(request, "base/home.html")


def room(request):
    return render(request, "base/room.html", {"rooms": rooms})
