from django.shortcuts import render,redirect
from PhoneDirectory.models import PhoneDirectory
from django.db.models.functions import Lower

# Create your views here.

def subscriber_list(request):
    subscriber_list = PhoneDirectory.objects.all().order_by(Lower('name'))
    return render(request,'PhoneDirectory/subscriber_list.html',{'subscriber_list':subscriber_list})

def subscriber_add(request):

    if request.method == 'POST':
        if len(request.POST['sphn']) != 10:
            return render(request,'PhoneDirectory/subscriber_add.html',{'msg':'phone number must be of 10 digit'})
        qe = PhoneDirectory(name = request.POST['sname'],phone_no = request.POST['sphn'])
        qe.save()
        return redirect('/')
    return render(request,'PhoneDirectory/subscriber_add.html')

def subscriber_delete(request,id):
    subscriber = PhoneDirectory.objects.get(id = id)
    subscriber.delete()
    return redirect('/')

def subscriber_update(request,id):
    subscriber = PhoneDirectory.objects.get(id = id)
    if request.method == 'POST':
        if len(request.POST['sphn']) != 10:
            return render(request,'PhoneDirectory/subscriber_add.html',{'msg':'phone number must be of 10 digit'})
        qe = PhoneDirectory(name = request.POST['sname'],phone_no = request.POST['sphn'])
        qe.save()
        subscriber.delete()
        return redirect('/')

    return render(request,'PhoneDirectory/subscriber_update.html',{'subscriber':subscriber})
