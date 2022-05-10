from django.http import HttpResponse
from django.shortcuts import render
from.models import carditem, oxyzendetail, submitinfo

def index(request):
    card_item=carditem.objects.all()
    return render(request,'index.html',{"carddetail":card_item})
    

def formsubmit(request):
    submit_in_fo=submitinfo.objects.all()
    
    if request.method=="POST":
        firstname=request.POST.get('firstname','default')
        lastname=request.POST.get('lastname','default')
        email=request.POST.get('email','default')
        password=request.POST.get('password','default')
        # selecttxt=request.POST.get('selecttxt','default')
        checkbox=request.POST.get('checkbox','off')
        selecttxt=request.POST.get('selecttxt','default')  
        submit_info=submitinfo(firstname=firstname,lastname=lastname,email=email,password=password,checkbox=checkbox,selecttxt=selecttxt)
        submit_info.save()
        
        return render(request, 'form.html',{"messages":submit_in_fo})
    else:
        return HttpResponse("error")
        # return render(request,'index.html',{"messages": submit_in_fo})
    
def contactme(request):
    submit_in_fo=submitinfo.objects.all()
    return render(request,'form.html',{"messages":submit_in_fo})
    # return render(request,'form.html')



    
    


    
        

    
