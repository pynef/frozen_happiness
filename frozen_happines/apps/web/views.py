#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404



from datetime import date
import datetime

def web(request):
    cntxt = {
    # user : 'user',
    }
    return render(request,'web/index.html', cntxt)