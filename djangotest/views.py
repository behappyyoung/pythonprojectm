__author__ = 'young'

from django.shortcuts import render_to_response
from django.template import RequestContext


def IndexView(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))