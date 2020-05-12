from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import admin


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content =  models.TextField()
	date_posted = models.DateTimeField(default=timezone.now())
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	url = models.SlugField(max_length=500, blank=True)


	def save(self, *args, **kwargs):
		self.url= slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title 

	def get_absolute_url(self):
		#return reverse('article_detail', kwargs={'slug': self.slug})
		#return reverse('post-detail', kwargs={'pk_slug': self.slug})
		return reverse('post-detail', kwargs={'pk': self.pk})



class Comment(models.Model):

	#The foriegn key is linked to the ID field in the Post model
	#id = models.IntegerField(primary_key=True, blank=False)
	post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
	nameid = models.ForeignKey(User,on_delete=models.CASCADE,related_name='commentsid')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField() 
	created_on= models.DateTimeField(default = timezone.now())
	active = models.BooleanField(default=True)
	url= models.SlugField(max_length=500, blank=True)
	#id = models.AutoField(primary_key=True)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return 'Comment {} by {}'.format(self.body, self.name)

	def save(self, *args, **kwargs):
		self.url= slugify(self.post)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('article_detail', kwargs={'slug': self.slug})
    	#return self.post.get_absolute_url()
    	#url= models.SlugField(max_length=500, unique=True, blank=True)
#self.url= slugify(self.name)

class CommentAdmin(admin.ModelAdmin):
	readonly_fields = ('id')
