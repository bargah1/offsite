from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

def index(request):
    if 'user' in request.session:
        current_user=request.session['user']
        return redirect("profile", current_user)
    else:
        shop=shopsmodel.objects.filter(is_subscribed=True)

        return render(request, "index.html",{"shops":shop})
def login(request):
    if request.method == 'POST':
        form_id = request.POST.get('form_id')
        if form_id == 'singupform':
            form = SignupForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                confpass = request.POST["confpass"]
                data1 = shopsmodel.objects.filter(email=email)
                if data1:
                    messages.error(request, "User already exist.")
                else:
                    if len(password) < 8:
                        messages.error(request, "Password must be at least 8 characters long.")
                    if not any(char.isdigit() for char in password):
                        messages.error(request, "Password must contain at least one digit.")
                    if not any(char.isalpha() for char in password):
                        messages.error(request, "Password must contain at least one letter.")
                    if password != confpass:
                        messages.error(request, "Passwords do not match.")
                    if confpass == password:
                        data = shopsmodel.objects.create(email=email, password=password)
                        data.save()
                        messages.success(request, "Registered successfully")
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field.capitalize()}: {error}")
        elif form_id == 'loginform':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                try:
                    user = shopsmodel.objects.filter(email=email)
                    for i in user:
                        if password==i.password:
                            request.session['user'] = email
                            return redirect('profile', email=email)
                        else:
                            messages.error(request, "Invalid password.")
                except shopsmodel.DoesNotExist:
                    messages.error(request, "User not found.")
            else:

                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field.capitalize()}: {error}")

        else:
            messages.error(request, "Invalid email or password.")
    return render(request,"login.html",)
def profile(request,email):
    if request.session.get('user') != email:
        messages.error(request, "You are not authorized to view That page.pls login")
        return redirect('login')
    data = shopsmodel.objects.filter(email=email)
    shop = get_object_or_404(shopsmodel, email=email)
    offer = offermodel.objects.filter(shop=shop)
    return render(request, "profile.html", {"data": data, "offers": offer})
def editpro(request,email):
    data = shopsmodel.objects.filter(email=email)
    shop = get_object_or_404(shopsmodel, email=email)
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            shop.name = cleaned_data['name']
            shop.bio = cleaned_data['bio']
            shop.location = cleaned_data['location']
            shop.email = cleaned_data['email']
            shop.phone = cleaned_data['phone']
            shop.locationlink = cleaned_data['locationlink']
            if 'photo1' in request.FILES:
                shop.photo1 = request.FILES['photo1']
            if 'photo2' in request.FILES:
                shop.photo2 = request.FILES['photo2']
            if 'photo3' in request.FILES:
                shop.photo3 = request.FILES['photo3']
            shop.save()
            return redirect("profile",email)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

    return render(request, "proedit.html", {"data": data})
def addoffer(request,email):
    data=get_object_or_404(shopsmodel, email=email)
    if request.method=="POST":
        form=offerForm(request.POST,request.FILES)
        if form.is_valid():
            name =form.cleaned_data['name']
            descrip = form.cleaned_data['description']
            photo = form.cleaned_data['photo']
            offer = offermodel(shop=data, name=name, description=descrip, photo=photo)
            offer.save()
            return redirect("profile", email)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    return render(request,"addoffer.html")
def logout(request):
    try:
        del request.session["user"]
    except:
        return redirect("index")
    return redirect('index')
def offers(request,email):
    data=shopsmodel.objects.filter(email=email)
    shop=get_object_or_404(shopsmodel, email=email)
    offer=offermodel.objects.filter(shop=shop)
    return render(request,"offers.html",{"data":data,"offers":offer})
def shop_search(request):
    form = ShopSearchForm(request.GET or None)
    shops = shopsmodel.objects.all()
    if form.is_valid():
        location = form.cleaned_data.get('location')
        if location:
            shops = shopsmodel.objects.filter(location=location)
    return render(request, "index.html", {'form': form, 'shops': shops})
def about(request):
    return render(request,"about.html")
def delete(request,email,id):
    shop=get_object_or_404(shopsmodel, email=email)
    offer=offermodel.objects.filter(shop=shop,id=id)
    offer.delete()
    return redirect("profile",email)
def payment(request):
    return render(request,"payment.html")