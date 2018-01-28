from django.http import HttpResponse
from django.template import Context, loader
from .fbgraph.facebook import Facebook


def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())


def logout(request):
    template = loader.get_template("logout.html")
    return HttpResponse(template.render())


def user(request, uid):
    access_token = request.GET['accessToken']
    fb = Facebook(uid, access_token)
    template = loader.get_template('user.html')
    context = {
        'image_link': fb.get_picture_url(),
        'user_name': fb.get_user_full_name()
    }
    return HttpResponse(template.render(context, request))




def revoke_access(request):
    pass

