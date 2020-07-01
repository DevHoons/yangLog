from django.db import models


class Article(models.Model):

    DEVELOPMENT = "dv"
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "개발이야기"),
        (PERSONAL, "일상이야기"),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=2, choices=CATEGORY_CHOICES, default=DEVELOPMENT
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    def __str__(self):
        return "{}의 댓글: {}".format(self.article.title, self.content)


class HashTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
