from django.http import HttpResponse
from django.shortcuts import render


class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Call From Middleware Before View")
        response = render(request, 'error.html')
        print('response')
        print("Call From Middleware After View ")
        return response

class MyProcessMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):

    response = self.get_response(request)
    return response

  def process_view(request, *args, **kwargs):
    print("This is Process View -  Test Before View")
    return HttpResponse("This is before view")
    #return None

class MyExceptionMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    response = self.get_response(request)
    return response

  def process_exception(self, request, exception):
    print("Exception Occured")
    msg = exception
    class_name = exception.__class__.__name__
    print(class_name)
    print(msg)
    return HttpResponse(msg)