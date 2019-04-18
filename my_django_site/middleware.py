import requests
from django.conf import settings

class StackOverflowMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self ,request, view_func, *view_args, **view_kwargs):
        if request.user.is_authenticated:
            print(request.user)
        else:
            print('User is not authenticated')
