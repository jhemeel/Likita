from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.template.loader import render_to_string

from django.contrib import messages
from .models import Post, Topic, User, LikedPost, Comment, CommentReply, Categories, HealthTips
from .forms import PostForm, ReplyForm


# Create your views here.

def home(request):
    staffs = User.objects.filter(is_staff = True)
    published_posts = Post.objects.filter(status = Post.Status.PUBLISHED)
    latest_posts = published_posts.order_by("-created_at")[0:4]
    context= {
        'publishes_posts': published_posts,
        'latest_posts': latest_posts,
        'staffs': staffs
    }

    return render(request, 'base/home.html', context)
    

def blog(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    posts = Post.objects.order_by('-created_at').filter(
        Q(topic__title__icontains=q) |
        Q(owner__username__icontains=q) |
        Q(headline__icontains=q) |
        Q(body__icontains=q) ,
         status= Post.Status.PUBLISHED                                       
    )
    
    tips = HealthTips.objects.order_by('-created_at').all()
    
    
    topics = Topic.objects.filter(post__status = Post.Status.PUBLISHED)
    context = {'posts': posts, 'topics': topics, "tips": tips }
    return render(request, 'base/blog.html', context)

@login_required(login_url='login')
def create_post(request):
    page = 'create-post'
    page_title_content = "Create A Post"
    button_text = "Publish"
    topics = Topic.objects.all()
    category  = Categories.objects.all()
    form = PostForm()
    if request.user.is_superuser:
        if request.method == 'POST':
            topic_title = request.POST.get('topic')
            topic_subtitle = request.POST.get('subtitle')
            category_title = request.POST.get('category')
            
            topic, created = Topic.objects.get_or_create(title=topic_title, subtitle=topic_subtitle )
            categories, created = Categories.objects.get_or_create(title = category_title)
            post = Post.objects.create(
                topic=topic,
                categories = categories,
                overview = request.POST.get('overview'),
                headline=request.POST.get('headline'),
                body=request.POST.get('body'),
                image=request.FILES.get('image'),
                owner=request.user
            )
            post.save()
            return redirect('blog')

    else:
        messages.warning(request, 'Permission Denied')
        return redirect('profile', pk=request.user.username)

    context = {
                'form': form, 
               'topics': topics, 
               'categories': category,
               'page': page,
               'page_title_content': page_title_content,
               "button_text": button_text
               }
    return render(request, 'base/create-update-post.html', context)

    raise TypeError("Object of type Comment is not Json serializale pls")
    
  
def post(request, pk):
    tips = HealthTips.objects.all()
    posts = Post.objects.filter(id=pk, status=Post.Status.PUBLISHED)
    if posts:
        for post in posts:
            post 
        comment = post.comments.all()   
            
        if request.method == "POST":
            comment = Comment(post=post, sender=request.user, body = request.POST.get('body'))
            comment.save()
            
            if request.htmx:
                post = Post.objects.get(id=pk)
                context={"comment": comment}
                comment_html = render_to_string("base/single-comment.html", context)
                if post.comments.count() == 0:
                    oob_swap_command = {
                        "<div hx-swap-oob='true' id='no-comments-message'></div>"
                    }
                    comment_html += oob_swap_command
                return HttpResponse(comment_html)
            return redirect('post', id=pk)

    context={'post': post, 'tips': tips, 'comment': comment}    
    return render(request, 'base/post-detail.html', context)

@login_required(login_url='login')
def update_post(request, pk):
    page_title_content = "Update Post"
    button_text = 'Update'
    topics = Topic.objects.all()
    category  = Categories.objects.all()
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.user.is_superuser:
        if request.method == 'POST':
            topic_title = request.POST.get('topic')
            topic_subtitle = request.POST.get('subtitle')
            category_title = request.POST.get('category')
            topic, created = Topic.objects.get_or_create(title=topic_title, subtitle=topic_subtitle)
            categories, created = Categories.objects.get_or_create(title = category_title)
            
            post.topic = topic
            post.categories_set = categories
            post.headline = request.POST.get('headline')
            post.overview = request.POST.get('overview'),
            post.body = request.POST.get('body')
            post.image = request.FILES.get('image') if request.FILES.get('image') else post.image

            post.save()
            return redirect('blog')

    else:
        messages.warning(request, 'Permission Denied')
        return redirect('profile', pk=request.user.username)

    context = {
                'form': form, 
               'topics': topics,
               'categories': category,
               'post': post,
               'page_title_content': page_title_content,
               'button_text': button_text
               }
    return render(request, 'base/create-update-post.html', context)


def liked_post(request):
    user = request.user.name
    q = request.GET.get('q')

    post = Post.objects.get(id=q)
    liked_post_filter = LikedPost.objects.filter(post_id=q, user=user).first()
    if liked_post_filter == None:
        new_like = LikedPost.objects.create(post_id=q, user=user)
        new_like.save()
        post.no_of_liked_post += 1
        post.save()
        
    else:
        liked_post_filter.delete()
        post.no_of_liked_post -= 1
        post.save()
        
        
    if request.htmx:
        context = {'post' : post}
        likes_html = render_to_string("base/likes.html", context)
        return HttpResponse(likes_html)         
    return redirect('post', pk=post.id)
    
    
@login_required(login_url='login')
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.user == post.owner or request.user.is_superuser:
        if request.method == "POST":
            post.delete()
            return redirect('blog')
    context = {'post': post}
    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def reply_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    form = ReplyForm()

    comment_reply = comment.commentreply_set.all()
    if request.user.is_staff:
        replier = request.user

    else:
        return redirect('post', pk = comment.post.id)

    if request.method == "POST":
        reply = CommentReply.objects.create(
            replier=replier,
            body=request.POST.get('body'),
            comment=comment
        )
        messages.success(
            request, f'{comment} successfully replied: {reply.body[0:5]}')

        return redirect('post', pk=reply.comment.post.id)
    context = {'comment': comment,
               'comment_reply': comment_reply, 'form': form}
    return render(request, 'base/reply.html', context)


def delete_comment(request, pk):
    if request.method == "DELETE":
        comment = get_object_or_404(Comment, id=pk)
        comment.delete()
        
        if request.htmx:

            return HttpResponse(status=200, reason="comment deleted succesfully")

    return redirect('post', pk=comment.post.id)


def contact_us(request):

    return render(request, 'base/contact_us.html')


# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)
