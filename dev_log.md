### 问题: Xadmin不兼容的Django版本 [解决：改用django-jet:4]

# 2023/09/08: 
1. 使用django-simple-captcha 添加验证吗功能
```angular2html
/captcha/ : captcha.urls

/captcha/refresh/ :  获取生成验证码数据，包括图片，图片地址，图片value、图片key等并存储到数据库中
格式如下：
{"key": "815d19cbaff75de26ba04cfd75bb0b63fc423ce7", "image_url": "/user/captcha/image/815d19cbaff75de26ba04cfd75bb0b63fc423ce7/", "audio_url": null}
注意请求header需要为 request.headers.get("x-requested-with") == "XMLHttpRequest"
```
2. 覆盖login/ 中的CustomTokenObtainPairView中的post方法，添加验证码认证的功能

待完成： 安装redies，添加定时任务，删除过期的验证码数据