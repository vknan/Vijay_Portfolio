from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature, Post, Category, Comment, Contact
from django.core.paginator import Paginator




def home(request):
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'For My Clients'
    # feature1.details = 'My service is Very Quick'

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'No. of Projects'
    # feature2.details = '5'

    # feature3 = Feature()
    # feature3.id = 2 
    # feature3.name = 'Happy Clients'
    # feature3.details = '1'

    features = Feature.objects.all()
    feature = {'feature1': features[0], 'feature2': features[1] , 'feature3': features[2]}
    return render(request, 'index.html', feature )  


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already Used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, email =email, password = password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    return render(request, 'users/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'users/user_login.html')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
        return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

# def post(request,title):
#     posts = Post.objects.get(title = title)
#     return render(request, 'blog-single.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def blog(request):
    # posts = Post.objects.filter(is_published=True)
    category_name = request.GET.get('category')
    
    if category_name:
        
        posts = Post.objects.filter(is_published=True, category__name=category_name)
        paginator = Paginator(posts, 1)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    else:
        posts = Post.objects.filter(is_published=True)
        paginator = Paginator(posts, 1)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    Categories = Category.objects.all()
    
    context = {
        'posts':posts,
        'Categories': Categories
    }
    return render(request, 'blog.html', context)

def blog_single(request, title):

    posts = Post.objects.get(title = title)
    recent_posts = Post.objects.filter(is_published=True).order_by('-posted_at')[:5]
    Categories = Category.objects.all()
    comments = Comment.objects.filter(post = posts)
    
    context = {'posts':posts, 'recent_posts':recent_posts , 'Categories': Categories, 'comments':comments}
    return render(request, 'blog-single.html', context)

def search(request):
    search_query = request.GET.get('q')
    posts = Post.objects.filter(is_published=True, title__icontains=search_query)
    context = {
        'posts':posts
        }
    return render(request, 'blog.html', context)

    # rest of the view code
   

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c= Contact(name = name, email=email, subject= subject, message=message)
        c.save()
        return redirect('contact')
    return render(request, 'contact.html')


def post_comment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        website = request.POST.get('website')
        post_id = request.POST.get('id')
        
        post = Post.objects.get(id=post_id)

        c= Comment(name = name, email=email, comment= comment, website=website, post = post)
        c.save()
        return redirect('blog_single', title=post.title)

    
    return redirect('blog')