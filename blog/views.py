from django.shortcuts import render, HttpResponse
from blog.models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, BlogComment
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

def blogpage(request):
    allposts=Post.objects.all()
    print(allposts)
    context={'allposts':allposts}
    return render(request,'blog/blogpage.html',context)


def blogPost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = BlogComment.objects.filter(post=post, parents=None).order_by('-timestamp')
    comment_count = comments.count()  

    if request.method == "POST":
        if request.user.is_authenticated:
            comment_text = request.POST.get("comment")
            BlogComment.objects.create(
                comment=comment_text,
                user=request.user,
                post=post
            )
            return redirect(f"/blog/{post.slug}")
        else:
            return redirect("/login/?next=/blog/{}/".format(post.slug))

    return render(request, "blog/blogpost.html", {
        "post": post,
        "comments": comments,
        "comment_count": comment_count  
    })
