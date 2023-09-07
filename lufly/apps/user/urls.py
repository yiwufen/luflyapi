from django.urls import path

from lufly.apps.user.views import CustomTokenObtainPairView

urlpatterns = [

    path(r"login/", CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]