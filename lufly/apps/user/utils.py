from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils import timezone


class UsernameOrMobileModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            # 检查是否有匹配的用户名或手机号
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

from captcha.models import CaptchaStore

def is_valid_captcha(key, value):
    try:
        # 获取与给定键关联的CaptchaStore对象
        captcha = CaptchaStore.objects.get(hashkey=key)
    except CaptchaStore.DoesNotExist:
        # 如果没有找到匹配的CaptchaStore对象，那么验证码无效
        return False

    if captcha.response == value.lower() and captcha.expiration > timezone.now():
        captcha.delete()
        return True
    return False
