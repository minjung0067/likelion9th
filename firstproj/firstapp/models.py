from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category

class Blog(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body=models.TextField()


    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, default=1)
    image = models.ImageField(upload_to='images/',default= "")
    # 기존에 이미  업로드 된 글이 있으면 오류 메세지 뜸 

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.TextField(max_length=20)
    content = models.TextField()

