from django.conf import settings # Import Settings Variables
from django.shortcuts import redirect # Import Django Redirect Module
##########################################################################################################################

class LoginRequiredMiddleware: # Authentication Middleware to require authentication to access private pages

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        protected_path = ['/candidate/hub','/candidate/logout','/candidate/show_file','/candidate/delete','/candidate/update'] # Private Pages List

        if request.path in protected_path and not request.user.is_authenticated: # If the user is not authenticated
            return redirect(settings.LOGIN_URLS[0]) # Redirect to the login page

        return self.get_response(request)