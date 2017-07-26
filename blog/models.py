from django.db import models

# Create your models here.

from django.db import models

# 文章添加
class Article(models.Model):
    title = models.CharField("标题",max_length=50 )#(max_length=50,null=True) 允许标题为空，不写默认必须有值，blank意思其实差不多
    writer = models.CharField("作者",max_length=50)
    create_date = models.DateField("创建日期",auto_now_add=True) # 年月日用DateField 详细时间用 DateTimeFiled DateField.auto_now_add表示创建时自动添加
    modify_date = models.DateField("修改日期",auto_now=True) # 修改的时间自动记录
    content = models.TextField() # 默认不限字数  可以max_length=50
    is_show = models.BooleanField() # 控制文章是否显示，这东西默认值是None

    class Meta:  # 保存到数据库中，在数据库中是一个什么名字
        db_table = 'Article'

    def __str__(self):
        return self.title
