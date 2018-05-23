
from django.shortcuts import render, HttpResponse, redirect
import datetime
from django.contrib import messages
now = datetime.datetime.now()
date = (now.strftime("%B %d %Y %I:%M:%S %p"))
from ..loginreg_app.models import User
from .models import Item

def index(r):
    if 'user_id' not in r.session:
        return redirect ('/')
    print(r.session['user_id'])
    print("You hit the Index!")
    
    context = {
        'user_info' : User.objects.get(id=r.session['user_id']),
        'my_items' : Item.objects.filter(wantingtobuys=r.session['user_id']),
        'not_my_items' : Item.objects.exclude(wantingtobuys=r.session['user_id']),
        'all_users': User.objects.all(),
        'all_items': Item.objects.all()
    }
    print(Item.item_creator)
    return render(r, 'wishlist_app/index.html', context)

def new(r):
    if 'user_id' not in r.session:
        return redirect ('/')
    print("You hit the new item page!")

    return render(r, 'wishlist_app/additem.html')

def createItem(r):
    print("you hit the create function!")
    response = Item.objects.createItem(r.POST, r.session['user_id'])
    if response['status'] == True:
        return redirect('/wishlist_app')
    else:
        for error in response['errors']:
            messages.error(r, error)
    return redirect('/wishlist_app/new')
    print(response)
    return redirect('/wishlist_app')

def wishlist_item(r, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'wishlist_item' : item,
        'wantingtobuys' : item.wantingtobuys.exclude(id=item.item_creator.id)
    }
    return render(request, 'wishlist_app/planneditems.html', context)


def show(r, id):
    if 'user_id' not in r.session:
        return redirect ('/')
    print("You hit the item user page!")
    item = Item.objects.get(id= id)
    context = {
        'wishlist_item' : item,
        'wantingtobuys' : item.wantingtobuys.exclude(id=item.item_creator.id)
    }
    return render(r, 'wishlist_app/planneditems.html', context)

def join(r, id):
    me = User.objects.get(id = r.session['user_id'])
    item = Item.objects.get(id = id)
    item.wantingtobuys.add(me)
    item.save()
    return redirect('/wishlist_app', id)

def remove(r, id):
    me = User.objects.get(id = r.session['user_id'])
    item = Item.objects.get(id = id)
    item.wantingtobuys.remove(me)
    item.save()
    return redirect('/wishlist_app', id)

def delete(r, id):


            # item_creator = Item.objects.get(id =item_creator.name)
            # context = {
            #     'user_info' : User.objects.get(id=r.session['user_id']),
            #     'my_items' : Item.objects.filter(wantingtobuys=r.session['user_id']),
            #     'not_my_items' : Item.objects.exclude(wantingtobuys=r.session['user_id']),
            #     'all_users': User.objects.all()
            # }
            # response = Item.objects.deleteItem(r.POST,  str('user_info'))
            # if response['status'] == True:
            #     return redirect('/wishlist_app')
            # else:
            #     for error in response['errors']:
            #         messages.error(r, error)
            # print(response)
            # return redirect('/wishlist_app', context)
            
            # if r.user == item_creator:
            #     item.delete()
            # else:
            #     raise PermissionDenied

    me = User.objects.get(id = r.session['user_id'])
            # # items = Item.objects.filter(user=User.objects.get(id = ))
            # # if me == items:
            
            # # if me == User.objects.get(id = Item.objects.user_id):
    item = Item.objects.get(id = id).delete()
    return redirect('/wishlist_app')

def goback(r):
    return redirect ('/')

def clear(r):
    r.session.clear()
    return redirect ('/')

def logout(r):
    r.session.clear()
    return redirect('/')
    