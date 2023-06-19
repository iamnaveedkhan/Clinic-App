from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from clinicapp.models import Msg
import json

def add(request):
    if request.method=='GET':

        context = {}
        context['count']=Msg.objects.all()
        return render(request,'add.html',context)
    else:
        n=request.POST['uname']
        a=request.POST['uage']
        s=request.POST['symp']
        d=request.POST['desc']
        m=Msg(name=n,age=a,symptoms=s,description=d)

        m.save()
        context = {}
        context['count']=Msg.objects.all()
        return render(request,'add.html',context)
    

def delete(request):
    if request.method == 'POST':
        string_data =request.body.decode("utf-8")
        json_data = json.loads(string_data)
        k=Msg.objects.get(id=json_data.get('id'))

        k.delete()
        # return render({json_data})
        # return render(request,'add.html')
        return redirect('add')
    
    
    
def edit(request):
    if request.method == 'GET':
        kid=request.GET.get('id')
        k=Msg.objects.get(id=kid)
        
        context= {}
        context['data']= k
        
        return render(request, 'edit.html', context)
        
    else:
      
        eid=request.POST['id']
        ne=request.POST['uname']
        ae=request.POST['uage']
        se=request.POST['symp']
        de=request.POST['desc']
        j=Msg.objects.get(id=eid)
        j.name = ne
        j.age = ae
        j.symptoms = se
        j.description = de
        j.save()
        # j=Msg.objects.filter(id=eid).update(name=ne,age=ae)
        context={}
        context['data']=j
        return redirect('add')
        # return render(request,'add.html')