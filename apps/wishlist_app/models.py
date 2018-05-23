from __future__ import unicode_literals
from django.db import models
from ..loginreg_app.models import User
from datetime import datetime
datetime.now()

class ItemManager(models.Manager):
    def createItem(self, postData, user_id):
        now = datetime.now()
        response = {
        'status' : False,
        'errors' : []
        }
        if len(postData['wishlist_item']) < 3:
            response['errors'].append('Please provide an item name longer than 3 characters!')
        if len(response['errors']) == 0:
            response['status'] = True
            me = User.objects.get(id=user_id)
            item = Item.objects.create(
                wishlist_item = postData['wishlist_item'],
                item_creator = me
            )
            item.wantingtobuys.add(me)
            item.save()
        return response
    # def deleteItem(self, postData, user_id):
    #     response = {
    #     'status' : False,
    #     'errors' : []
    #     }
    #     if 'user_info' != User.objects.get(id=user_id):
    #         response['errors'].append('Sorry, you cannot do that!')
    #     if len(response['errors']) == 0:
    #         response['status'] = True
    #         item = Item.objects.get(id = id).delete()
    #     return response

class Item(models.Model):
    wishlist_item= models.CharField(max_length=255)
    wantingtobuys = models.ManyToManyField(User, related_name="wantingtobuy_items")
    item_creator = models.ForeignKey(User, related_name="created_items")
    created_at= models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ItemManager()
    def __repr__(self):
        return "<User object: {} {} >".format(self.wishlist_item)
