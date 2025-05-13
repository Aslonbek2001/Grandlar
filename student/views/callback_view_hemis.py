from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth import login, get_user_model
from student.clinet import oAuth2Client
from core.settings import (
    CLIENT_SECRET,
    CLIENT_ID,
    REDIRECT_URI,
    RESOURCE_OWNER_URL,
    TOKEN_URL,
    AUTHORIZE_URL,
)


User = get_user_model()

class HemisCallbackView(View):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return render(request, 'error.html', {'error': 'Code not found in callback.'})

        client = oAuth2Client(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            authorize_url=AUTHORIZE_URL,
            token_url=TOKEN_URL,
            resource_owner_url=RESOURCE_OWNER_URL,
        )
        print("!!"*50)
        print("Code: ", code)
        print("!!"*50)

        # Step 1: get access token
        token_data = client.get_access_token(code)
        access_token = token_data.get('access_token')
        print("!!"*50)
        print("Access_TOKEN: \n", access_token, "\n")
        print("!!"*50)
        if not access_token:
            return render(request, 'error.html', {'error': 'Access token not found.'})

        # # Step 2: get user info
        user_info = client.get_user_details(access_token)

        print("!!"*50)
        print("User Info: ", user_info)
        print("!!"*50)
        
        # # Step 3: log user in or create
        # username = user_info.get('username') or user_info.get('email')
        # user, _ = User.objects.get_or_create(username=username, defaults={
        #     'email': user_info.get('email', ''),
        #     'first_name': user_info.get('first_name', ''),
        #     'last_name': user_info.get('last_name', '')
        # })

        # login(request, user)
        return redirect('main:index')
