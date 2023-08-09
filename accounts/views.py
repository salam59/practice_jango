from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
# Create your views here.
def login_view(request):

    if request.method == "POST" :
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password) #don't ever push this into the real code just for testing purposes
        user = authenticate(username=username,password=password)
        if user is None:
            context = {
                "error": "Invalid username or password"
            }
            return render(request,"accounts/login.html",context=context)
        login(request,user)
        return redirect("/") 
    return render(request,"accounts/login.html",{})