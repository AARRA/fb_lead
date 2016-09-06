from django.conf import settings
from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext

from models import FbProjects


def index(request):


    user = request.user
    if not user.is_authenticated:
        return HttpResponseForbidden()
    my_projects = FbProjects.objects.filter(
        user=user
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
