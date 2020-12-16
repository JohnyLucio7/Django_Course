from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                           .filter(status='publicado')


class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='rascunho')

    objects          = models.Manager()
    publishedManager = PublishedManager()

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    class Meta:
        ordering = ('published',)

    def __str__(self):
        return self.title



    '''
    Post.objects.bulk_create([
        Post(title='Testando o shell do Django com Bulk',slug='testando-o-shell-do-django-com-bulk',content='Testando o shell do Django com Bulk',author=user),
        Post(title='Testando o shell do Django com Bulk 2',slug='testando-o-shell-do-django-com-bulk-2',content='Testando o shell do Django com Bulk 2',author=user),
        Post(title='Testando o shell do Django com Bulk 3',slug='testando-o-shell-do-django-com-bulk-3',content='Testando o shell do Django com Bulk 3',author=user),
    ])
    '''