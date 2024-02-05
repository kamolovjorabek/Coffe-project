from django.shortcuts import render, redirect
from news.models import New, Category
from pages.models import Comment, ContactUs
from django.contrib import messages

def home(request):
    news = New.objects.all()
    categories = Category.objects.all()
    
    context = {
        'news': news.order_by('-id'),
        "last_three_news": news.order_by('-id')[:3],
        "categories": categories,
    }
    return render(request, 'index.html', context)


def new_detail(request, pk):
    news = New.objects.all()
    categories = Category.objects.all()
    comments = Comment.objects.filter(new_id=pk)
    
    context = {
        'new': news.get(id=pk),
        "last_three_news": news.order_by('-id')[:3],
        "categories": categories,
        "comments": comments
    }
    user = request.user
    if request.method == 'POST':
        req_data = request.POST
        comment = req_data.get('comment')
        new_comment = Comment.objects.create(
            comment=comment, user=user, new=news.get(id=pk)
        )
        return redirect('new_detail', pk=pk)
    return render(request, 'post-details.html', context)



def contact_us(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("user_login")
        req_data = request.POST
        print(req_data)
        name = req_data.get("name")
        email = req_data.get("email")
        subject = req_data.get("subject")
        message = req_data.get("message")
        
        contact_obj = ContactUs(
            name=name, email=email, subject=subject, message=message
        )
        contact_obj.user = request.user
        contact_obj.save()
        # ContactUs.objects.create(
        #     name=name, email=email, subject=subject, message=message, user=request.user
        # )
        messages.info(request, 'Arizangiz qabul qilindi')
        return redirect('contact_us')
    return render(request, 'contact.html')



def blog_etries(request):
    news = New.objects.all()
    categories = Category.objects.all()
    context = {
        "news": news,
        "categories": categories
    }
    return render(request, 'blog.html', context)
