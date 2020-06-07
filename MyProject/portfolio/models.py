from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image

# Create your models here.

# class Post(models.Model):
#     author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
#     title = models.CharField(max_length = 200)
#     text = models.TextField()
#     create_date = models.DateTimeField(default = timezone.now())
#     published_date = models.DateTimeField(blank = True, null = True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def approve_comments(self):
#         return self.comments.filter(approved_comment = True)

#     def get_absolute_url(self):
#         return reverse('post_detail', kwargs = {'pk':self.pk})

#     def __str__(self):
#         return self.title

# class Comment(models.Model):
#     post = models.ForeignKey('portfolio.Post', related_name = 'comments', on_delete = models.CASCADE)
#     author = models.CharField(max_length = 200)
#     text = models.TextField()
#     create_date = models.DateTimeField(default = timezone.now())
#     approved_comment = models.BooleanField(default = False)

#     def approve(self):
#         self.approved_comment = True
#         self.save()

#     def get_absolute_url(self):
#         return reverse('post_list')

#     def __str__(self):
#         return self.text

class Project(models.Model):
    project_title = models.CharField(max_length = 50)
    project_short_summary = models.CharField(max_length = 100, default = "Short summary")
    project_summary = models.TextField()
    project_content = models.TextField()
    project_published = models.DateTimeField("date_published", auto_now_add=True, blank=True)
    project_author = models.CharField(max_length = 200, default = "No author")
    project_github = models.CharField(max_length = 255, default = "No link")
    project_image = models.ImageField(default = "notfound.jpg", upload_to='portfolio_logo')

    class Meta:
        ordering = ['-project_published']

    # def save(self):
    #     super().save()  # saving image first

    #     img = Image.open(self.project_image.path) # Open image using self

    #     if img.height > 1024 or img.width > 1024:
    #         new_img = (1024, 1024)
    #         img.thumbnail(new_img)
    #         img.save(self.project_image.path)  # saving image at the same path

    def __str__(self):
        return self.project_title

    def get_absolute_url(self):
        return reverse("portfolio:detail",kwargs={'pk':self.pk})

