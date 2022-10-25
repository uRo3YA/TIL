from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
import os

# from xml.etree.ElementTree import Comment
# ????

# Create your views here.

# 요청 정보를 받아서..
def index(request):
    # 게시글을 가져와서..
    articles = Article.objects.order_by("-pk")
    # Template에 전달한다.
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


# def new(request):
#     article_form = ArticleForm()
#     context = {
#         'article_form': article_form
#     }
#     return render(request, 'articles/new.html', context=context)


@login_required
def create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            # 로그인한 유저 => 작성자네!
            article.user = request.user
            article.save()
            messages.success(request, "글 작성이 완료되었습니다.")
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {"article_form": article_form}
    return render(request, "articles/form.html", context=context)


def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # template에 객체 전달
    context = {
        "article": article,
        "comments": article.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


# @login_required
# def update(request, pk):
#     article = Article.objects.get(pk=pk)
#     if request.user == article.user:
#         if request.method == "POST":
#             # POST : input 값 가져와서, 검증하고, DB에 저장
#             article_form = ArticleForm(request.POST, request.FILES, instance=article)
#             if article_form.is_valid():
#                 # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
#                 article_form.save()
#                 messages.success(request, "글이 수정되었습니다.")
#                 return redirect("articles:detail", article.pk)
#             # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
#         else:
#             # 작성자가 아닐 때
#             # (1) 403 에러메시지를 던져버린다.
#             # from django.http import HttpResponseForbidden
#             # return HttpResponseForbidden()
#             # (2) flash message 활용!
#             messages.warning(request, "작성자만 수정할 수 있습니다.")
#             return redirect("articles:detail", article.pk)
@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            # if len(request.FILES) != 0:
            #     if len(article.image) > 0:
            #         os.remove(article.image.path)
            if article_form.is_valid():
                article_form.save()
                messages.success(request, "글이 수정되었습니다.")
                print(request.FILES)
                return redirect("articles:detail", article.pk)
        else:
            article_form = ArticleForm(instance=article)
        context = {"article_form": article_form}
        print(request.FILES)
        return render(request, "articles/update.html", context)
    else:
        messages.warning(request, "작성자만 수정할 수 있습니다.")
        return HttpResponseForbidden()


@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect("articles:detail", article.pk)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect("accounts:detail", request.user.pk)


def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect("articles:detail", article_pk)


@login_required
def like(request, pk):
    article = Article.objects.get(pk=pk)
    # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,
    # if article.like_users.filter(id=request.user.id).exists():
    if request.user in article.like_users.all():
        # 좋아요 삭제하고
        article.like_users.remove(request.user)
    else:
        # 좋아요 추가하고
        article.like_users.add(request.user)
    # 상세 페이지로 redirect
    return redirect("articles:detail", pk)
