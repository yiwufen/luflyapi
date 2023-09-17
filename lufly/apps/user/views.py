from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.viewsets import ModelViewSet

from lufly.apps.user.utils import is_valid_captcha


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # 添加额外的响应参数到 token 中
        token['username'] = user.username
        token['id'] = user.id

        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        captcha_key = request.data.get('captcha_key')  # 验证码的键
        captcha_value = request.data.get('captcha_value')  # 用户输入的验证码值
        # print('captchakey: ', captcha_key)
        # print('captcha_value: ', captcha_value)
        # 验证码验证逻辑...
        if not is_valid_captcha(captcha_key, captcha_value):
            # print("Invalid captcha")
            return Response({'detail': '无效的验证码'}, status=status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)