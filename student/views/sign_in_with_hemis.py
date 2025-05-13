from django.shortcuts import render
from student.clinet import oAuth2Client
from django.views import View
from django.shortcuts import redirect
from core.settings import (
    CLIENT_SECRET,
    CLIENT_ID,
    REDIRECT_URI,
    RESOURCE_OWNER_URL,
    TOKEN_URL,
    AUTHORIZE_URL,
)


class SignInWithHemis(View):
    def get(self, request):
        client = oAuth2Client(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            authorize_url=AUTHORIZE_URL,
            token_url=TOKEN_URL,
            resource_owner_url=RESOURCE_OWNER_URL,
        )
        auth_url = client.get_authorization_url()

        print("#" * 50)
        print("Auth URL: ", auth_url)
        print("#" * 50)

        return redirect(auth_url)
    






# class OAuthAuthorizationView(View):
#     def get(self, request, *args, **kwargs):
#         client = oAuth2Client(
#             client_id=CLIENT_ID,
#             client_secret=CLIENT_SECRET,
#             redirect_uri=REDIRECT_URI,
#             authorize_url=AUTHORIZE_URL,
#             token_url=TOKEN_URL,
#             resource_owner_url=RESOURCE_OWNER_URL
#         )
#         authorization_url = client.get_authorization_url()
#         context = {
#             'authorization_url': authorization_url
#         }
#         return render(request, 'student/authorize.html', context)

# class OAuthCallbackView(View):
#     def get(self, request, *args, **kwargs):
#         auth_code = request.GET.get('code')  # GET parametrlardan olib ishlatamiz
#         if not auth_code:
#             return HttpResponseBadRequest("Authorization code is missing.")

#         client = oAuth2Client(
#             client_id=CLIENT_ID,
#             client_secret=CLIENT_SECRET,
#             redirect_uri=REDIRECT_URI,
#             authorize_url=AUTHORIZE_URL,
#             token_url=TOKEN_URL,
#             resource_owner_url=RESOURCE_OWNER_URL
#         )
#         access_token_response = client.get_access_token(auth_code)

#         if 'access_token' in access_token_response:
#             access_token = access_token_response['access_token']
#             user_details = client.get_user_details(access_token)
#             context = {
#                 'user_details': user_details,
#                 'access_token': access_token
#             }
#             return render(request, 'oauth/callback.html', context)
#         else:
#             return HttpResponseBadRequest("Failed to obtain access token.")
