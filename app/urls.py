from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('profile/<email>',views.profile,name='profile'),
    path('editprofile/<email>', views.editpro, name='editprofile'),
    path('addoffer/<email>', views.addoffer, name='addoffer'),
    path('logout',views.logout,name="logout"),
    path('offers/<email>',views.offers,name="offers"),
    path('shop_search/',views.shop_search, name='shop_search'),
    path("about",views.about,name="about"),
    path("delete/<email>/<int:id>",views.delete,name="delete"),
    path("payment",views.payment,name="payment"),
]
