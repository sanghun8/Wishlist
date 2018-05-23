from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(r):
    
    print("You're back at the index!")
    return render(r, 'loginreg_app/index.html')

def processReg(r):
    print("you made t")
    result = User.objects.validateRegistration(r.POST)
    if result['status']:
        r.session['user_id'] = result['user_id']
        return redirect('/wishlist_app')
    else:
        for error in result['errors']:
            messages.error(r, error)
    print("You're at the processReg!")
    return redirect('/')
    
def processLogin(r):
    result = User.objects.validateLogin(r.POST)
    if result['status']:
        r.session['user_id'] = result['user_id']
        return redirect('/wishlist_app')
    else:
        for error in result['errors']:
            messages.error(r, error)
    return redirect('/')

# def success(r):
#     return render(r, 'loginreg_app/success.html')
# YOU DELETED THE URL ROUTE AS WELL SO THIS WON'T WORK IF YOU UNCOMMENT AKA url(r'^success$', views.success),

def logout(r):
    r.session.clear()
    return redirect('/')