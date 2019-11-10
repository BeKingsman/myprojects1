from django.db.models.signals import post_save
from allauth.account.signals import user_logged_in
from django.shortcuts import redirect




def user_details(sender,instance,**kwargs):
   return redirect("www.facebook.com")

post_save.connect(user_details,sender = user_logged_in)

