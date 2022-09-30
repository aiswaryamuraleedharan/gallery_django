from django.shortcuts import render,redirect
from media.forms import ImgForm
from .models import Img

def Home(request):
    data=Img.objects.all()
    form=ImgForm()
    context ={'form':form, 'data':data}
    if request.method=='POST':
        form1=ImgForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()

    return render(request,'index.html',context)
    
    
