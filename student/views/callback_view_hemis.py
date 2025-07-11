from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth import login, get_user_model
from student.clinet import oAuth2Client
from django.contrib import messages
from student.utils import save_user_and_student
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
            messages.success(request, "Qandaydur xatolik bor! \n ")
            return redirect('main:index')
            

        client = oAuth2Client(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            authorize_url=AUTHORIZE_URL,
            token_url=TOKEN_URL,
            resource_owner_url=RESOURCE_OWNER_URL,
        )

        # Step 1: get access token
        token_data = client.get_access_token(code)
        access_token = token_data.get('access_token')
        if not access_token:
            messages.success(request, "Qandaydur xatolik bor! \n ")
            return redirect('main:index')
            # return render(request, 'error.html', {'error': 'Access token not found.'})

        user_info = client.get_user_details(access_token)        
        user, student = save_user_and_student(user_info)
        
        login(request, user)
        messages.success(request, "Ariza yuborishingiz mumkin!")
        return redirect('main:index')
