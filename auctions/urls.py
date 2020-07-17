from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"), 
    path("create-listing", views.create_listing, name="create_listing"),
    path("listing/<int:id>", views.listing, name="listing"), 
    path("add-watchlist/<int:id>", views.add_watchlist, name="add_watchlist"), 
    path("remove-watchlist/<int:id>", views.remove_watchlist, name="remove_watchlist"), 
    path("watchlist", views.watchlist, name="watchlist")
]
