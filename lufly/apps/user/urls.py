from django.urls import path, include

from lufly.apps.user.views import CustomTokenObtainPairView

from captcha.views import  captcha_refresh

urlpatterns = [

    path(r"login/", CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('captcha/', include('captcha.urls'), name='captcha'),
    path('refresh_captcha/', captcha_refresh, name='refresh_captcha'),
]