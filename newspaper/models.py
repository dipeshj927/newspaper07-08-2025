from django.db import models

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True # do not create table for this model


class Category(TimeStampModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    


class Tag(TimeStampModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    


class Post(TimeStampModel):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    published_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    views_count = models.PositiveBigIntegerField(default=0)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    # Fat model and thin Views
    @property
    def latest_comments(self):
        comments = Comment.objects.filter(post=self).order_by("-created_at")
        return comments 
    

class Contact(TimeStampModel):
    message = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Newsletter(TimeStampModel):
    email = models.EmailField()

    def __str__(self):
        return self.email
    

class Comment(TimeStampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.comment


    
    

    


