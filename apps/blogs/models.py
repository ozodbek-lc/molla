from django.db import models
from django.db.models import CASCADE


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CategoryModel(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class AuthorModel(BaseModel):
    full_name = models.CharField(max_length=128)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

class TagModel(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class PostModel(BaseModel):
    author = models.ForeignKey(AuthorModel,on_delete=CASCADE,related_name='post')
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='posts/',blank=True,null=True,default='default/default.png')
    category = models.ForeignKey(CategoryModel,on_delete=CASCADE)
    tags = models.ManyToManyField(TagModel,related_name='post')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

