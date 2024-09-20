from lib2to3.fixes.fix_input import context
from.models import Post
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
context={
    "posts" : Post.objects.all()
}
def home(request):
    return render(request,'blog/home.html',context)