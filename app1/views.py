from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from app1.forms import ChapterForm, CommentForm
from app1.models import Books, Chapter, Comment


def index(request):
    return HttpResponse('媽～我在這裡')


def books(request):
    object_list = Books.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


#由books中接收/year/month/day/slug 參數,
def book_detail(request, year, month, day, post):
    books = get_object_or_404(Books, slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'blog/post/detail.html', {'books': books})



#利用book.get_url 來呼叫
# path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.chapter_detail  ,name = 'book_detail'),
def chapter_detail(request, year, month, day, post):
    books = get_object_or_404(Books, slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    chapters = books.chapter.filter(active=True)

    new_chapter: Chapter
    new_chapter = None
    chapter: Chapter
    if request.method == 'POST':
        chapter_form = ChapterForm(request.POST, request.FILES)

        if chapter_form.is_valid():
            new_chapter = chapter_form.save(commit=False)
            new_chapter.book = books
            new_chapter.save()
    else:
        chapter_form = ChapterForm()

    return render(request, 'blog/post/detail.html', {'books': books,
                                                     'chapters': chapters,
                                                     'new_chapter': new_chapter,
                                                     'chapter_form': chapter_form})



#在章節中，可對之前的文章進行編輯
# 利用，
#  1.request.FILES, 可從新換圖
#  2. instance=chapter 可在編輯介面中帶出舊資料
def chapter_edit(request,id):
    chapter = get_object_or_404(Chapter,id = id)
    chapter_form = ChapterForm(request.POST,request.FILES,instance=chapter)
    if chapter_form.is_valid():
        post = chapter_form.save(commit=True)
        post.save()
        chapters = Chapter.objects.all()
        return redirect(reverse('app1:book_detail',args=[chapter.book.publish.year,
                             chapter.book.publish.month,
                             chapter.book.publish.day,
                             chapter.book.slug]))
    else:
         chapter_form = ChapterForm(instance=chapter)
         context = {'chapter':chapter,'chapter_form':chapter_form}

    return render(request,'blog/post/edit_chapter.html',context)



#刪除書本
def delete(request,id):
    if request.method == 'POST':
        chapter = get_object_or_404(Chapter,id = id)
        chapter.delete()
    return redirect(reverse('app1:book_detail',args=[chapter.book.publish.year,
                             chapter.book.publish.month,
                             chapter.book.publish.day,
                             chapter.book.slug]))


#chapetr 詳細說明
def ch_detail(request, id, chapter):
    chapter = get_object_or_404(Chapter, slug=chapter,id = id )
    comments = chapter.comment.all()
    return render(request,'blog/post/comment_list.html',{'chapter':chapter,'comments':comments})


#我要補充
def comment_add(request,id):
    chapter = get_object_or_404(Chapter,id=id)
    form = CommentForm(request.POST,request.FILES)
    if request.method =='POST':
        if form.is_valid():
            comments: Comment
            comments = form.save(commit = False)
            comments.chapter = chapter
            comments.save()
            return redirect(reverse('app1:ch_detail',args=[id,chapter.slug]) )
    else:
        context = {'form':form}
    return render(request,'blog/post/add_comment.html',context)


#TODO  補充說明需要可以變更
def comment_edit(request,id,comment):
    return HttpResponse('媽~我在這裡')