from datetime import datetime

from django.db import models


from  users.models import UserProfile

from courses.models import Course


class UserAsk(models.Model):
    '''
    用户咨询
    '''
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'手机')
    course_name = models.CharField(max_length=50, verbose_name=u'课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    '''
    用户课程评论
    涉及到User和Course,所有需要引入
    '''
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    comments = models.CharField(max_length=200, verbose_name=u'评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    '''
    用户收藏
    '''
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    '''
    course = models.ForeignKey(Course, verbose_name=u'课程')
    teacher =
    org =
    fav_type =
    可以分别定义这几种类型的收藏，来指明我们收藏的是哪一种。
    也可以采用另外一种方法，节省字段，也不用做条件判断
    '''
    fav_id = models.IntegerField(choices=((1,'课程'),(2,'课程机构'),(3,'讲师')),default=1, verbose_name=u'收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    '''
    用户消息
    不用外键：消息分为两种：一：定向发给某一个user的，二：系统发给所有人员的消息
    '''
    # 这里default为0 指明为发给所有用户的消息，不为0，则值代表用户的id，这样在读取消息的
    # 时候就能读取出两种消息，1：user等于0的，2：user等于登录用户Id的user
    user = models.IntegerField(default=0, verbose_name=u'接收用户')
    message = models.CharField(max_length=500, verbose_name=u'添加时间')
    # 点击消息之后，显示为空。是否读过消息,前面是has或者is，就说明是Bool类型，其他人能看懂
    has_read = models.BooleanField(default=False, verbose_name=u'是否已读')

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    '''
    UserCourse-用户学习的课程
    '''
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name

