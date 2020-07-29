from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from app1.forms import ChapterForm
from app1.models import Post, Chapter


def index(request):
    return HttpResponse('媽～我在這裡')


def list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def book_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'blog/post/detail.html', {'post': post})


def chapter_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    chapters = post.chapter.filter(active=True)
    new_chapter: Chapter
    new_chapter = None
    chapter_form: ChapterForm
    chapter: Chapter
    if request.method == 'POST':
        chapter_form = ChapterForm(request.POST, request.FILES)
        if chapter_form.is_valid():
            new_chapter = chapter_form.save(commit=False)
            new_chapter.post = post
            new_chapter.save()
    else:
        chapter_form = ChapterForm()

    return render(request, 'blog/post/detail.html', {'post': post,
                                                     'chapters': chapters,
                                                     'new_chapter': new_chapter,
                                                     'chapter_form': chapter_form})


def delete(request,id):
    if request.method == 'POST':
        chapter = get_object_or_404(Chapter,id = id)
        chapter.delete()
    return redirect(reverse('app1:book_detail',args=[chapter.post.publish.year,
                             chapter.post.publish.month,
                             chapter.post.publish.day,
                             chapter.post.slug]))