from django.db import models
from datetime import datetime

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u'昵称',default="")
    # 同时设计null 和blank 为空,才是默认是空。
    briday = models.DateField(verbose_name=u'生日',null=True, blank=True)
    gender = models.CharField(max_length=7,choices=(('male',u'男'),('female',u'女')),default='female')
    address = models.CharField(max_length=100,default=u'')
    # 电话
    mobile = models.CharField(max_length=11,null=True,blank=True)
    # 用户刚登录时，都会有个默认的头像。image在后台存储的时候实际上是字符串的类型，所以定义长度
    image = models.ImageField(upload_to='image/%Y/%m',default=u'image/default.png',max_length=100)

    class Meta:
        # verbose_name表示单数形式的显示，verbose_name_plural表示复数形式的显示
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    # 如果不重载这个方法，在UserProfile实例的时候，就不能打印自定义的字符串
    '''
    __unicode__()方法是在一个对象上调用unicode()时被调用的。
    因为Django的数据库后端会返回Unicode字符串给model属性，
    所以我们通常会给自己的model写一个__unicode__()方法。
    '''
    def __unicode__(self):
        return self.username

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u'验证码')
    email = models.EmailField(max_length=50,verbose_name=u'邮箱')
    send_type = models.CharField(choices=(('register',u'注册'),('forget',u'找回密码')),max_length=10)
    '''
    设置过期时间等 如果不去掉now的()，生成的时间是根据EmailVerifyRecord编译的时间
    来生成时间，去掉了才会根据class实例化的时候生成的时间。
    '''
    # send_time = models.DateTimeField(default=datetime.now())
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    '''
    1:图片 2：点击图片后地址 3：每个轮播图加序号控制前后顺序
    '''
    title = models.CharField(max_length=100, verbose_name=u'标题')
    # 保存到数据库的时候，存储的是路径地址，所有要有长度
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name=u'轮播图', max_length=100)
    # 点击之后的url跳转
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    # 添加字段控制每个轮播图的顺序
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    # 每个表都有的，当前记录的生成时间
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name
