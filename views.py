from django.shortcuts import redirect, render
from django import http
from django.http import HttpResponse
from vehicle.forms import vehForm
from vehicle.models import veh
from django.views.generic import View, TemplateView, RedirectView, FormView

class home(TemplateView):
    template_name = 'home.html'

class delete_view(RedirectView):
    url ='/retrieve.html'
    def get_redirect_url(self, *args, **kwargs):
        del_id=kwargs['id']
        veh.objects.get(id=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)

class add(View):
    def get(self, request):
        form=vehForm()
        return render(request,'add.html',{'form':form})
    def post(self,request):
        form=vehForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('retrieve.html')

class read(TemplateView):
  def get(self,request):
    vehicle = veh.objects.all()
    return render(request,'retrieve.html',{'vehicle' : vehicle})

class update(View):
    def get(self,request, id):
        vehicle = veh.objects.get(id=id)
        form=vehForm(instance=vehicle)
        return render(request, 'update.html', {'form':form})
    def post(self, request, id):
        vehicle = veh.objects.get(id=id)
        form=vehForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
        return render(request, 'update.html', {'form':form})


#def add(request):
#  form=vehForm()
#  if request.method == 'POST':
#       form = vehForm(request.POST)
#       if form.is_valid():
#           form.save()
#           return redirect('retrieve.html')
#   return render(request,'add.html',{'form':form})

#def read(request):
#    vehicle = veh.objects.all()
#    return render(request,'retrieve.html',{'vehicle' : vehicle})

#def delete_view(request,id):
#   vehicle = veh.objects.get(id=id)
#   vehicle.delete()
#   return redirect('/retrieve.html')

'''def update(request,id):
     vehicle = veh.objects.get(id=id)
     if request.method == 'POST':
       form = vehForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/')   
     return render(request,'update.html',{'vehicle': vehicle})'''
