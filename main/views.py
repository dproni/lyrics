from django.shortcuts import render_to_response, get_list_or_404, HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.decorators import login_required
from main.models import *


def info(request):

    return HttpResponse('Hello Dimon')