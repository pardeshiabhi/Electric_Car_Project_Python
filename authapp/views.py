from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact,CarType,Selectcarbrand,Carbooking
from authapp.models import Carrenting,rentingType,carbrand,Services,About,Team

# Create your views here.
def Home(request):
    return render(request,"index.html")

def team(request):
    posts=Team.objects.all()
    context={"posts":posts}
    return render(request,"team.html",context)

def about(request):
    posts=About.objects.all()
    context={"posts":posts}
    return render(request,"about.html",context)

def services(request):
    posts=Services.objects.all()
    context={"posts":posts}
    return render(request,"services.html",context)

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Plaese Login and Try Again")
        return redirect('/login')
    user_phone=request.user
    posts=Carbooking.objects.filter(Phonenumber=user_phone)
    print(posts)
    context={"posts":posts}
    return render(request,"profile.html",context)



def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
    
        
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone number is Taken")
                return redirect('/signup')
        
        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
            
        except Exception as identifier:
            pass

        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
    

    return render(request,"signup.html")


def handlelogin(request):
    if request.method=="POST":
        usernumber=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=usernumber,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successfull")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')


    return render(request,"handlelogin.html")

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout success")
    return redirect('/login')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        myquery=Contact(name=name,email=email,phonenumber=number)
        myquery.save()
        messages.info(request,"Thanks For Contacting us we will get back to you soon")
        return redirect('/contact')
 
    return render(request,"contact.html")

def Booking(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Plaese Login and Try Again")
        return redirect('/login')
    cartitle=CarType.objects.all()
    carbrand=Selectcarbrand.objects.all()
    context={"cartitle":cartitle,"carbrand":carbrand}
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        Phonenumber=request.POST.get('Phonenumber')
        DOB=request.POST.get('DOB')
        Cars=request.POST.get('Cars')
        Features=request.POST.get('Features')
        refrence=request.POST.get('refrence')
        address=request.POST.get('address')
        query=Carbooking(FullName=FullName,email=email,Gender=gender,
        Phonenumber=Phonenumber,DOB=DOB,Selectcar=Cars,selectfeatures=Features,
        refrence=refrence,address=address)
        query.save()
        messages.success(request,"Thanks For Booking")
        return redirect('/EVcars')

    return render(request,"Booking.html",context)


def Rental(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Plaese Login and Try Again")
        return redirect('/login')
    Cartitle=rentingType.objects.all()
    Carbrand=carbrand.objects.all()
    context={"Cartitle":Cartitle,"Carbrand":Carbrand}
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        Email=request.POST.get('Email')
        Gender=request.POST.get('Gender')
        Phonenumber=request.POST.get('Phonenumber')
        DOB=request.POST.get('DOB')
        Car=request.POST.get('Car')
        Feature=request.POST.get('Feature')
        Refrence=request.POST.get('Refrence')
        Address=request.POST.get('Address')
        query=Carrenting(FullName=FullName,Email=Email,Gender=Gender,
        Phonenumber=Phonenumber,DOB=DOB,Selectcar=Car,selectfeatures=Feature,
        Refrence=Refrence,Address=Address)
        query.save()
        messages.success(request,"Thanks For Renting")
        return redirect('/Rental')

    return render(request,"Rental.html",context)

