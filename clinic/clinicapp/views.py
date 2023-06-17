from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from clinicapp.models import Msg
import json
# Create <divyour views here.
def create(request):
    if request.method=='GET':

        context = {}
        context['count']=Msg.objects.all()
        return render(request,'create.html',context)
    else:
        n=request.POST['uname']
        a=request.POST['uage']
        m=Msg(name=n,age=a)
        
        m.save()
        context = {}
        context['count']=Msg.objects.all()
        return render(request,'create.html',context)
def delete(request):
    if request.method == 'POST':
        string_data =request.body.decode("utf-8")
        if string_data is None:
            return JsonResponse({'status': 'error', 'message': 'Missing or invalid "id" parameter.'})
        try:
            json_data = json.loads(string_data)
            k=Msg.objects.get(id=json_data.get('id'))
           
            k.delete()
            # Process the JSON data as needed
            return JsonResponse({'status': 'success', 'data': json_data})
        except json.JSONDecodeError:
            # Handle the case where the string is not valid JSON
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON string.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
    
def edit(request):
    if request.method == 'GET':
        try:
            kid=request.GET.get('id')
            k=Msg.objects.get(id=kid)
           
            context= {}
            context['data']= k
            # Process the JSON data as needed
            return render(request, 'edit.html', context)
        except json.JSONDecodeError:
            # Handle the case where the string is not valid JSON
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON string.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})