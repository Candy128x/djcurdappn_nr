from django.shortcuts import render
from .models import Destination


# Create your views here.


def index(request):
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The city that never sleeps..'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 700
    # dest1.offer = False
    #
    # dest2 = Destination()
    # dest2.name = 'Hydrabad'
    # dest2.desc = 'First Biryani, Then Sherwani'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 1350
    # dest2.offer = True
    #
    # dest3 = Destination()
    # dest3.name = 'Bengaluru'
    # dest3.desc = 'My kind of IT world'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 1100
    # dest3.offer = True
    #
    # # create lists
    # dests = [dest1, dest2, dest3]


    # fetch value from database
    dests = Destination.objects.all()

    return render(request, 'index.html', {'datasets': dests, 'eMailId': 'test@g.com'})
