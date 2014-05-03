import os
from djangomako.shortcuts import render_to_response
def hello_view(request):
    # print os.path.dirname(__file__)
    return render_to_response('hello.html', {'name':'sand'})
# from mako.template import Template
# print Template("hello ${data}!").render(data="world")
# print os.path.dirname(os.path.dirname(__file__))