from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


class PublishedManage(models.Manager):
    def get_queryset(self):
        return super(PublishedManage, self) \
            .get_queryset() \
            .filter(status='published')


# Create your models here.
class Books(models.Model):
    STATUS_CHOICE = (('draft', 'Draft'),
                     ('published', 'Published')
                     )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    objects = models.Manager()
    published = PublishedManage()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('app1:book_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class Chapter(models.Model):
    book = models.ForeignKey(Books,on_delete=models.CASCADE,related_name='chapter')
    slug = models.SlugField(max_length=250, unique_for_date='created')
    chapter = models.CharField(max_length=80)
    chapter_name = models.CharField(max_length=80,default='')
    body = RichTextField()
    attachment = models.ImageField(upload_to='images/',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f' {self.chapter_name} 在 {self.book} 一書'

    def delete(self, *args,**kwargs):
        self.attachment.delete()
        super().delete(*args,**kwargs)

    def get_url(self):
        return reverse('app1:ch_detail',
                       args=[self.id,
                             self.slug])


class Comment(models.Model):
    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE,related_name='comment',null=True)
    name = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment',null=True)
    comment = RichTextField()
    attachment = models.ImageField(upload_to='images/comment/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.name} 補充章節  {self.chapter}'

    def delete(self, *args, **kwargs):
        self.attachment.delete()
        super().delete(*args, **kwargs)