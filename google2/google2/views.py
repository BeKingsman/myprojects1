from django.views.generic import TemplateView
from allauth.socialaccount.models import SocialLogin, SocialAccount   #important
from django.http import HttpResponse
from django.shortcuts import  render
from django.contrib.auth.decorators import login_required

@login_required
def details(request):

    socialaccount = SocialAccount.objects.get(user=request.user)
    det = socialaccount.extra_data
    return render (request , 'test.html', {'det' : det})


class Home(TemplateView):
    template_name = 'home.html'
