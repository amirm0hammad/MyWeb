from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse

from weblog.models import Post, Comment


# Create your views here.
def Home(request):
    login = '<a href="/weblog/login/"> Log in </a>'
    signup = '<a href="/weblog/signup/"> Sign Up </a>'
    return HttpResponse(signup + login)


def Login(request):
    logout(request)
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            # show_post = '<a href="/weblog/login/showpost"> Show Post </a>'
            # create_post = '<a href="/weblog/login/createpost/"> Create Post </a>'
            # update = '<a href="/weblog/login/update"> Update </a>'
            # delete = '<a href="/weblog/login/delete"> Delete </a>'
            #return render(request, "home_page.html")
            return  HttpResponseRedirect(reverse('HomePage'))
        else:
            return render(request, 'SignUp.html')
    else:
        return render(request, "Login.html")


def SignUp(request):
    if request.method == "POST":
        if not request.POST["username"] == "" and not request.POST["password"] == "":
            user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
            user.save()
            return render(request, "Login.html")
        else:
            return render(request, 'SignUperror.html')
    else:
        return render(request, "SignUp.html")


def weblog(request):
    return render(request, "home_page.html")
    # show_post = '<a href="/weblog/login/showpost"> Show Post </a>'
    # create_post = '<a href="/weblog/login/createpost/"> Create Post </a>'
    # update = '<a href="/weblog/login/update"> Update </a>'
    # delete = '<a href="/weblog/login/delete"> Delete </a>'
    # return HttpResponse(show_post + create_post + update + delete)


def Show_post(request):
    if request.method == "GET":
        tmp_list = []
        post = Post.objects.filter(username=request.user)
        for i in range(len(post)):
            tmp_list.append([post[i].post, post[i].pk])
        return render(request, "Show_Post.html", {"post": tmp_list})


def Create_post(request):
    if request.method == "POST":
        # tmp = request.POST.get('Like')
        # if not tmp:
        #     post = Post(username=request.user, post=request.POST['post'], title=request.POST['title'], like=False)
        # else:
        #     post = Post(username=request.user, post=request.POST['post'], title=request.POST['title'], like=True)
        post = Post(username=request.user, post=request.POST['post'], title=request.POST['title'])
        post.save()
        return HttpResponse("post saved ! " + '<a href="/weblog/login/homepage"> Homepage </a>')

    else:
        return render(request, 'weblog_page.html')


def Update(request):
    if request.method == "POST":
        post = Post.objects.get(title=request.POST['title'])
        post.post = request.POST['update']
        post.save()
        return HttpResponse("Update successful !")
    else:
        return render(request, 'Update_post.html')


def Delete(request):
    if request.method == "POST":
        Post.objects.filter(title=request.POST['title']).delete()
        return HttpResponse("Delete successful !")
    else:
        return render(request, 'Delete_post.html')


@login_required
def HomePage(request):
    return render(request, "home_page.html")


def add_comment_or_like(request, post_pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        comment = Comment(post=post, comment=request.POST['comment'])
        comment.save()
        tmp = request.POST.get('Like')
        if not tmp:
            post.like = False
        else:
            post.like = True
        post.save()

        return HttpResponse("saved !")
    else:
        return render(request, "Comment.html", {"post_pk": post_pk})

#
def Logout(request):
    logout(request)
    #'<a href="/weblog/login/homepage/logout"> Log out </a>'
    return HttpResponse("log out succesfully !" + '<a href="/weblog"> Log in  </a>')
