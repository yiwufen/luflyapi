from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    label = 'my_home'  # this replaces "home"
    verbose_name = '我的首页'


"""
Django 中的每个应用都需要一个 AppConfig 类，或者是继承自 AppConfig 的子类。这个类提供了应用的全局设置，例如应用的名称 (name) 和额外的配置参数。

在你的 HomeConfig 类中：

default_auto_field 是新建模型时默认使用的主键字段类型。
name 是当前应用的全路径名，它告诉 Django 这个应用的位置。
label 是当前应用的标签，它是系统内部使用的名称。通常情况下，这个标签就是应用的最后一段路径名，但你可以通过在 AppConfig 子类中指定 label 属性来覆盖它。在你这个例子，'my_home' 将会覆盖默认的 'home'。
verbose_name 是更人性化的应用名称，它在 Django admin 中显示出来。
"""
