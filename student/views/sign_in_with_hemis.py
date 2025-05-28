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
        return redirect(auth_url)
    
