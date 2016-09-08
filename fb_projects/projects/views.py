from django.conf import settings
from django.http.response import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext

from models import FbProjects, FbPages


def index(request):


    user = request.user
    if not user.is_authenticated:
        return HttpResponseForbidden()
    my_projects = FbPages.objects.filter(
        account__user=user
    )

    return render_to_response(
        'table_list.tpl',
        {
            'projects': my_projects
        },
        content_type=RequestContext(request)
    )


def logout(request):
    if hasattr(settings, 'USE_HTTPS') and settings.USE_HTTPS:
        request.environ['wsgi.url_scheme'] = 'https'
    try:
        del request.session['user']
        request.session.flush()
    except KeyError:
        pass
    return HttpResponseRedirect('/')



def save_mail(request):
    data = request.POST
    fb_id = data.get('pk')
    email = data.get('value')
    FbPages.objects.filter(fb_id=fb_id).update(email=email)
    return HttpResponse('')
