"""
Django settings for Mxonline project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import sys
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# os.path.abspath:获取当前文件路径
# os.path.dirname：获取当前文件的上级文件夹路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取项目基础路径
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))  # 将apps模块添加到python搜索路径（Path环境变量）的第一个
sys.path.insert(0,os.path.join(BASE_DIR, 'extra_apps'))  # 将extra_apps模块添加到python搜索路径（Path环境变量）的第一个
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+1nruftzf9)mi3mb!0_wpsmw=pne(717j(xszq_ghmap9n03sw'

# 开启调试
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 允许你设置哪些域名可以访问，即使在 Apache 或 Nginx 等中绑定了，这里不允许的话，也是不能访问的。
# 当 DEBUG=False 时，这个为必填项，如果不想输入，可以用 ALLOW_HOSTS = ['*'] 来允许所有的。
ALLOWED_HOSTS = ['*']


# Application definition 注册我们的app
# 设置邮箱和用户名均可登录
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

# 应用注册列表
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'courses',
    'operation',
    'organization',
    'xadmin',# xadmin必须
    'crispy_forms', # xadmin必须
    'captcha',
    'pure_pagination',
    'DjangoUeditor',
]
# 此处重载是为了使我们的UserProfile生效
AUTH_USER_MODEL = "users.UserProfile"
# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Django安全机制之一，禁止跨站请求
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Mxonline.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 模板索引目录
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.i18n",
                'django.template.context_processors.media',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'Mxonline.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mxonline3',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST':'127.0.0.1'

    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# 下面两个属性是xadmin的配置
# 语言改为中文
LANGUAGE_CODE = 'zh-hans'
# 时区改为上海
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# 数据库存储使用时间，True时间会被存为UTC的时间
USE_TZ = False


# static 是静态文件所有目录
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'

# 一般来说我们只要把静态文件放在 APP 中的 static 目录下，
# 部署时用 python manage.py collectstatic 就可以把静态文件收集到（复制到）STATIC_ROOT 目录，
# 但是有时我们有一些共用的静态文件，这时候可以设置 STATICFILES_DIRS 另外弄一个文件夹，如下：
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# 发送邮件的setting设置
EMAIL_HOST = "smtp.qq.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "mxonline@yanghl.cn"
EMAIL_HOST_PASSWORD = "ystfiwntwmonjebe"
EMAIL_USE_TLS= True
EMAIL_FROM = "mxonline@yanghl.cn"

# 设置我们上传文件的路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')