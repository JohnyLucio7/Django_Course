from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'published','status' )
    list_filter = ('status', 'created', 'published', 'author')
    date_hierarchy = 'published'
    raw_id_fields = ('author',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}

'''
 title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='rascunho')
'''
# Register your models here.
