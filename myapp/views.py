from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import *
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import CustomPasswordResetForm
import os
# from payu import PayUmoneySdk


class login_functionality:
    @staticmethod
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
        return render(request, 'templates/login_func/register.html')
    @staticmethod
    def login(request):
        url = request.get_full_path()
        print(url)
        if (request.method == 'POST') :
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)

            if user is not None:
                auth.login(request, user)
                customer, created = Customer.objects.get_or_create(user=user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Credentials Invalid')
                return redirect('login')
            return render(request, 'templates/login_func/login.html')
        else:
            return render(request, 'templates/login_func/login.html')

    @staticmethod
    def logout(request):
        auth.logout(request)
        return redirect('/')

class pages:
    @staticmethod
    def home(request):
        features = Feature.objects.all()[:3]
        products = Product.objects.all()
        context = {
            'feature1': features[0] if len(features) > 0 else None,
            'feature2': features[1] if len(features) > 1 else None,
            'feature3': features[2] if len(features) > 2 else None,
            'products': products
        }
        return render(request, 'templates/pages/index.html', context)

    # def password_reset(request):
    #     form = CustomPasswordResetForm()
    #     return render(request, 'templates/users/password_reset.html', {'form': form})

        
    
    # def post(request,title):
    #     posts = Post.objects.get(title = title)
    #     return render(request, 'blog-single.html', {'posts': posts})
    @staticmethod
    def about(request):
        return render(request, 'templates/pages/about.html')
    
    @staticmethod
    def services(request):
        return render(request, 'templates/pages/services.html')

    @staticmethod
    def Templates(request):
        p1 = Product.objects.all()
        context = {'products': p1}
        return render(request, 'templates/pages/Templates.html', context)
    
    @staticmethod
    def blog(request):
        category_name = request.GET.get('category')
        posts = Post.objects.filter(is_published=True)
        
        if category_name:
            posts = posts.filter(category__name=category_name)
        
        paginator = Paginator(posts, 10)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        
        categories = Category.objects.all()
        
        context = {
            'posts': posts,
            'categories': categories
        }
        return render(request, 'templates/pages/blog.html', context)
    
    @staticmethod
    def blog_single(request, title):

        posts = Post.objects.get(title = title)
        recent_posts = Post.objects.filter(is_published=True).order_by('-posted_at')[:5]
        Categories = Category.objects.all()
        comments = Comment.objects.filter(post = posts)
        
        context = {'posts':posts, 'recent_posts':recent_posts , 'Categories': Categories, 'comments':comments}
        return render(request, 'templates/pages/blog-single.html', context)
    @staticmethod
    def search(request):
        search_query = request.GET.get('q')
        posts = Post.objects.filter(is_published=True, title__icontains=search_query)
        context = {
            'posts':posts
            }
        return render(request, 'templates/pages/blog.html', context)
        # rest of the view code
    
    @staticmethod
    def contact(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            c= Contact(name = name, email=email, subject= subject, message=message)
            c.save()
            return redirect('contact')
        return render(request, 'templates/pages/contact.html')
    
    @staticmethod
    @login_required
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


    @staticmethod
    def termsandconditions(request):
        return render(request, 'templates/pages/terms_and_conditions.html')
    @staticmethod
    def privacypolicy(request):
        return render(request, 'templates/pages/privacy_policy.html')
    @staticmethod
    def refundpolicy(request):
        return render(request, 'templates/pages/refund_policy.html')
    
    @staticmethod
    @login_required
    def dashboard(request):
        return render(request, 'reactbuilder/build/index.html')




#--------------------------------------------------------------------------------------------------
# ================================Not Required Code==================================================

class PaymentProcess:
    @login_required
    def checkout(request):
        if request.method == 'POST':
            product_id = request.POST.get('product_id')
            product = get_object_or_404(Product, id=product_id)
            return render(request, 'templates/users/checkout.html', {'product': product})

        return HttpResponseRedirect('/')


    # views.py
    @login_required
    def process_order(request):
        if request.method == 'POST':
            product_id = request.POST.get('product_id')
            customer_name = request.POST.get('customer_name')
            customer_email = request.POST.get('customer_email')
            customer_phone_number = request.POST.get('customer_phone_number')
            shipping_address = request.POST.get('shipping_address')
            payment_info = request.POST.get('payment_info')

            try:
                product = Product.objects.get(id=product_id)
                
            except Product.DoesNotExist:
                messages.error(request, 'Invalid product ID')
                return redirect('checkout')

            customer, created = Customer.objects.get_or_create(
                email=customer_email,
                defaults={
                    'name': customer_name,
                    'phone_number': customer_phone_number,
                    'shipping_address': shipping_address,
                    'payment_info': payment_info
                }
            )

            order_item = OrderItem.objects.create(
                product=product,
                customer=customer,
                ordered=True
            )


            # # Create Payment object
            # payment = Payment(
            #     amount=product.discounted_price,
            #     txnid=order_item.id,
            #     firstname=customer_name,
            #     email=customer_email,
            #     phone=customer_phone_number,
            #     productinfo=product.name,
            #     successurl=request.build_absolute_url(reverse('payment_success')),
            #     failureurl=request.build_absolute_url(reverse('payment_failure')),
            #     service_provider='payu_paisa',
            # )

            # # import payu_sdk
            # # client = payu_sdk.payUClient("<key>","<salt>")

            # # Initiate payment process
            # payumoney = PayUmoneySdk(
            #     merchant_key='your_merchant_key',
            #     merchant_id='your_merchant_id',
            #     salt='your_salt',
            #     test_mode=True,  # Change to False for production
            # )
            # payment_params = payumoney.payment_params(payment)
            # payment_url = payumoney.payment_url()

            # # Save Payment object
            # payment.save()

            # # Redirect to PayUmoney payment page
            # return redirect(payment_url + '?' + payment_params)
            files_admin = order_item.product.filesadmin_set.first()
            
            if files_admin:
                file_id = files_admin.id 
            else:
                None

            messages.success(request, 'Order placed successfully!')
            return redirect('placed_order', file_id=file_id)


        # Redirect to checkout page if not a POST request
        return redirect('checkout')


    # def payment_success(request):
    #     if request.method == 'POST':
    #         # Get the payment response from PayUmoney
    #         payumoney = PayUmoneySdk(
    #             merchant_key='your_merchant_key',
    #             merchant_id='your_merchant_id',
    #             salt='your_salt',
    #             test_mode=True,  # Change to False for production
    #         )
    #         response = payumoney.payment_response(request.POST)
    #         if response.get('status') == 'success':
    #             # Payment successful, update Payment object and serve file for download
    #             payment = Payment.objects.get(txnid=response.get('txnid'))
    #             payment.status = Payment.SUCCESS
    #             payment.payment_response = json.dumps(response)
    #             payment.save()

    @login_required
    def placed_order(request, file_id):
        features = Feature.objects.all()
        feature = {'feature1': features[0], 'feature2': features[1] , 'feature3': features[2], 'file_id':file_id}
        return render(request, 'templates/index.html', feature )
        
    @login_required
    def file_detail(request, file_id):
        file_obj = FilesAdmin.objects.get(id=file_id)
        customer = request.user.customer
        order_item = OrderItem.objects.filter(product__id=file_obj.product_id, customer=customer, ordered=True).first()
        context = {'order_item': order_item, 'file_obj': file_obj}
        return render(request, 'templates/users/file_detail.html', context)
        
    @login_required
    def download_file(request, file_id):
        # Get the file object and the current customer
        file_obj = get_object_or_404(FilesAdmin, id=file_id)
        customer = request.user.customer
        
        # Check if the customer has ordered the file
        # print(file_obj.title)
        order_item = OrderItem.objects.filter(product__id=file_obj.product_id, customer=customer, ordered=True).first()
        # print(order_item)
        if order_item:
            # If the customer has ordered the file, serve the file for download
            file_path = file_obj.adminupload.path
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type="application/force-download")
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                return response
        else:
            # If the customer has not ordered the file, return a 404 error
            raise Http404("The requested file does not exist or has not been ordered by you.")


