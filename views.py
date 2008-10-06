# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from google.appengine.api import users
from google.appengine.api import urlfetch

from google.appengine.ext import db
from google.appengine.ext.db import djangoforms

import django
from django import http
from django import shortcuts

def respond(request, user, template, params=None):
  if params is None:
    params = {}
  if not template.endswith('.html'):
    template += '.html'
  return shortcuts.render_to_response(template, params)

def index(request):
  user = users.GetCurrentUser()
  return respond(request, user, 'base')

def ssapi(request):
    cat = request.POST['cat']
    count = request.POST['count']
    filters = request.POST['filters']
    user = users.GetCurrentUser()
    url = "http://www.shopstyle.com/action/apiSearch?fts=jeans&pid=onsugar&format=JSON&min=0&count="+count+"&cat="+cat+filters
    result = urlfetch.fetch(url)
    return respond(request,user,'api',{'gifts':result.content})