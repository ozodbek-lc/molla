from django.shortcuts import render

def blogs_list_view(request):
    return render(request,'blog-list.html')

def blogs_detail_view(request):
    return render(request,'blog-detail.html')