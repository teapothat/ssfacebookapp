from django.http import HttpResponse
from django.template import Context, loader
from .manager import usermanager


def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())


def logout(request):
    template = loader.get_template("logout.html")
    return HttpResponse(template.render())


def user(request, uid):
    access_token = request.GET['accessToken']
    context = usermanager.handle_user(uid, access_token)
    template = loader.get_template('user.html')
    return HttpResponse(template.render(context, request))


def deregister(request):
    payload = request.POST['signed_request']
    usermanager.deactivate_user(payload)
    return HttpResponse('OK')

