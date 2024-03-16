from django.shortcuts import render
from .models import YourModel 

# Create your views here.
def home(request):
    return render(request,"home.html")

from django.shortcuts import render
from .models import YourModel

def index(request):
    # Assuming you have a model called YourModel and you want to pass its instance to the template
    detail = YourModel.objects.first()  # Fetching the first instance of YourModel
    authors = detail.authors.all()  # Assuming authors is a ManyToManyField in YourModel
    panelists = detail.panelists.all()  # Assuming panelists is a ManyToManyField in YourModel

    context = {
        'detail': detail,
        'authors': authors,
        'panelists': panelists,
    }
    return render(request, 'home.html', context)

