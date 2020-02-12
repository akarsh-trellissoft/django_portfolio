from django.shortcuts import render
from.models import Author

def allblogs(request):
    blogs=Author.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})
