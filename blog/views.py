from contextlib import redirect_stdout
from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Page, Paginator
from .models import blog #데이터가져와
from .forms import BlogForm 
# Create your views here.

def home(request):
    blogs = blog.objects.order_by('-pud_data')
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        blogs = blog.objects.exclude(writer = author).order_by('-pud_data')
        return render(request, 'home.html', {'blogs':blogs})
        
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs}) 

def detail(request, id):
    blogs = get_object_or_404(blog, pk = id) # pk 몇번째 객체 호출하는가, 객체 구분하는 이름표  #404 -> 없는 객체 호출했을 때 에러페이지
    return render(request, 'detail.html', {'blogs':blogs})

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form': form})

def Create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pud_data = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect('home')

def edit(request, id):
    edit_blog =  blog.objects.get(id = id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = blog.objects.get(id = id) # 아이디 값에 따라 페이지 다르게 
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pud_data = timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id) #url 주소를 변경

def delete(request, id):
    delete_blog = blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('home')