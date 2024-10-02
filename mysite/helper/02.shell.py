from django.contrib.auth.models import User 
from blog.models import Post 
user = User.objects.get(username='admin')
post = Post(title='Another post',
            slug = 'another-post',
            body='Post body',
            author=user)
post.save()

user = User.objects.get(username='admin')

post = Post(title='Another post', slug='another-post', body='Post body.',
author=user)

post.save()
Post.objects.create(title='One more post',
                slug='one-more-post',
                body='Post body.',
                author=user)
user, created = User.objects.get_or_create(username='user2')
post.title = 'New title'

post.save()
all_posts = Post.objects.all()
Post.objects.all()
Post.objects.filter(title='Who was Django Reinhardt?')
posts = Post.objects.filter(title='Who was Django Reinhardt?')
print(posts.query)
Post.objects.filter(id__exact=1)
Post.objects.filter(id=1)
Post.objects.filter(title__iexact='who was django reinhardt?')
Post.objects.filter(title__icontains='django')
