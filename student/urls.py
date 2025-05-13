from django.urls import path
from .views.sign_in_with_hemis import SignInWithHemis
from .views.callback_view_hemis import HemisCallbackView

urlpatterns = [
    path("login/", SignInWithHemis.as_view(), name="login_with_hemis"),
    path("data/", HemisCallbackView.as_view(), name="hemis_callback")

]
 