from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Comment, Bid


def index(request):
    return render(request, "auctions/index.html", { 
    "listings": Listing.objects.filter(active = True)
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        bid = int(request.POST['bid'])
        image_url = request.POST['image_url']
        category = request.POST['category']
        user = request.user

        l = Listing(title=title, description=description, bid=bid,
                    image_url=image_url, category=category)
        l.save()
        l.owner.add(user)
        return HttpResponseRedirect(reverse('index'))

    else:
        return render(request, "auctions/create-listing.html")

def listing(request, id):
    l = Listing.objects.get(id=id)
    user = request.user

    if user:
        in_watchlist = user.watchlist.filter(id=id)

    return render(request, "auctions/listing.html", {
        "listing": l, 
        "owner": l.owner.first(), 
        "in_watchlist": in_watchlist
    })

def add_watchlist(request, id):
    if request.method == 'POST':
        l = Listing.objects.get(id=id)
        user = request.user
        user.watchlist.add(l)

    return HttpResponseRedirect(reverse('listing', kwargs={'id': id}))



def remove_watchlist(request, id):
    if request.method == 'POST':
        l = Listing.objects.get(id=id)
        user = request.user
        user.watchlist.remove(l)

    return HttpResponseRedirect(reverse('listing', kwargs={'id': id}))