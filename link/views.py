from django.shortcuts import render, redirect
from .models import Linkmodel
from .forms import LinkForm
from .dele import idk
from django.contrib import messages


def direct(request, short):
    a=Linkmodel.objects.get(short=short)
    link= a.inputlink
    return redirect('http://'+link)







def shrink(request):
    form=LinkForm()

    if 'submit' in request.POST:
        link= request.POST.get('inputlink')
        print(link)

        short= idk(4)
        a=Linkmodel.objects.check(short=short)
        print(a)
        print(type(a))
        print(1234)
        if len(a) is 0:
            n=Linkmodel.objects.create(inputlink=link,short=short)
            n.save()

            return redirect('/shrinked/'+short+'/')
        else:
            messages.info(request, 'pls something went wrong, try again')
            

        

    return render(request, 'shrink.html', { 'form':form })

def shrinked(request, short):
    
    shortlink='127.0.0.1:8000/'+short
    link = '/'+short
    return render(request, 'shrinked.html',{ 'shortlink': shortlink, 'link': link })


# Create your views here.
