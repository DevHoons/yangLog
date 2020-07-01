from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article, Comment, HashTag


def index(request):

    category = request.GET.get("category")
    hashtag = request.GET.get("hashtag")

    hashtag_list = HashTag.objects.all()

    if not category and not hashtag:
        article_list = Article.objects.all()
    elif category:
        article_list = Article.objects.filter(category=category)
        hashtag_list = HashTag.objects.all()
    else:
        article_list = Article.objects.filter(hashtag__name=hashtag)

    category_list = set(
        [(article.category, article.get_category_display()) for article in article_list]
    )
    # print(category_list)
    ctx = {
        "article_list": article_list,
        "hashtag_list": hashtag_list,
        "category_list": category_list,
    }
    return render(request, "index.html", ctx)


def detail(request, article_id):

    article = Article.objects.get(id=article_id)
    # commnet_list = Comment.objects.filter(article__id=article_id)
    hashtag_list = HashTag.objects.all()
    ctx = {
        "article": article,
        # "comment_list": commnet_list,
        "hashtag_list": hashtag_list,
    }
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        content = request.POST.get("content")
        Comment.objects.create(
            article=article, username=username, content=content,
        )
        # print(username, content)
        return HttpResponseRedirect("/{}/".format(article_id))

    return render(request, "detail.html", ctx)


# def about(request):
#    pass
