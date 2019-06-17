from django.db import models

# Create your models here.
from django.contrib import admin

class Category(models.Model):
    category=models.CharField(max_length=20)
    count=models.IntegerField(default=0)
    class Meta:
        db_table='category'
        verbose_name_plural='分类'
@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    list_display=('category','count')

class MovieModel(models.Model):
    category=models.ForeignKey(Category,related_name='movies',on_delete=models.CASCADE)
    title=models.CharField(max_length=100,unique=True,null=False)
    pic=models.CharField(max_length=200,null=False)
    type=models.CharField(max_length=20,null=False)
    country=models.CharField(max_length=20,null=False)
    year=models.CharField(max_length=30,null=True)
    director=models.CharField(max_length=30,null=False)
    zhuyan =models.CharField(max_length=50,null=False)
    story=models.TextField(null=False)
    url=models.CharField(max_length=300,null=False)
    time=models.DateTimeField(auto_now_add=True)
    video=models.CharField(max_length=10)

    class Meta:
        db_table='movie'
        verbose_name_plural='电影'
        ordering=('time',)
@admin.register(MovieModel)
class UserAdmin(admin.ModelAdmin):
    list_display=("title","pic",'type','country','year','director','zhuyan','story','url','time')
    search_fields = ('title', )

class TVModel(models.Model):
    category=models.ForeignKey(Category,related_name='TVs',on_delete=models.CASCADE)
    title=models.CharField(max_length=100,unique=True,null=False)
    pic=models.CharField(max_length=200,null=False)
    type=models.CharField(max_length=20,null=False)
    country=models.CharField(max_length=20,null=False)
    year=models.CharField(max_length=30,null=True)
    director=models.CharField(max_length=30,null=False)
    zhuyan =models.CharField(max_length=50,null=False)
    story=models.TextField(null=False)
    url=models.CharField(max_length=300,null=False)
    url_lists=models.TextField(null=False)
    time=models.DateTimeField(auto_now_add=True)
    video = models.CharField(max_length=10)


    class Meta:
        db_table='TV'
        verbose_name_plural='电视剧'
        ordering=('time',)
@admin.register(TVModel)
class UserAdmin(admin.ModelAdmin):
    list_display=("title","pic",'type','country','year','director','zhuyan','story','time')
    search_fields = ('title',)

class CartoonModel(models.Model):
    category=models.ForeignKey(Category,related_name='Cartoons',on_delete=models.CASCADE)
    title=models.CharField(max_length=100,unique=True,null=False)
    pic=models.CharField(max_length=200,null=False)
    type=models.CharField(max_length=20,null=False)
    country=models.CharField(max_length=20,null=False)
    year=models.CharField(max_length=30,null=True)
    director=models.CharField(max_length=30,null=False)
    zhuyan =models.CharField(max_length=50,null=False)
    story=models.TextField(null=False)
    url=models.CharField(max_length=300,null=False)
    url_lists=models.TextField(null=False)
    time=models.DateTimeField(auto_now_add=True)
    video = models.CharField(max_length=10)

    class Meta:
        db_table='cartoon'
        verbose_name_plural='动漫'
        ordering=('time',)
@admin.register(CartoonModel)
class UserAdmin(admin.ModelAdmin):
    list_display=("title","pic",'type','country','year','director','zhuyan','story','time')
    search_fields = ('title',)

class ZongyiModel(models.Model):
    category=models.ForeignKey(Category,related_name='zongyis',on_delete=models.CASCADE)
    title=models.CharField(max_length=100,unique=True,null=False)
    pic=models.CharField(max_length=200,null=False)
    type=models.CharField(max_length=20,null=False)
    country=models.CharField(max_length=20,null=False)
    year=models.CharField(max_length=30,null=True)
    director=models.CharField(max_length=30,null=False)
    zhuyan =models.CharField(max_length=50,null=False)
    story=models.TextField(null=False)
    url=models.CharField(max_length=300,null=False)
    url_lists=models.TextField(null=False)
    time=models.DateTimeField(auto_now_add=True)
    video = models.CharField(max_length=10,default='movie')

    class Meta:
        db_table='zongyi'
        verbose_name_plural='综艺'
        ordering=('time',)
@admin.register(ZongyiModel)
class UserAdmin(admin.ModelAdmin):
    list_display=("title","pic",'type','country','year','director','zhuyan','story','time')
    search_fields = ('title',)