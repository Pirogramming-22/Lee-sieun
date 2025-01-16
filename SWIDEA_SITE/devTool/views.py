from django.shortcuts import render,redirect
from .models import DevTool
from .forms import ToolForm

def list(request):
    devTool = DevTool.objects.all()
    return render(request, 'devTool/list.html', {'devTool':devTool})

def create(request):
    if request.method == 'GET' :
        form = ToolForm()
        return render(request, 'devTool/create.html', {'form':form})
    
    form = ToolForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('devTool:list')

def detail(request, pk):
    devTool = DevTool.objects.get(id=pk)
    return render(request, 'devTool/detail.html',{'devTool':devTool})


def delete(request, pk):
    DevTool.objects.get(id=pk).delete()
    return redirect('devTool:list')

def update(request, pk):
    devTool = DevTool.objects.get(id=pk)
    if request.method == 'GET':
        form = ToolForm(instance=devTool)
        ctx = {
            'form':form,
            'devTool':devTool,
        }
        return render(request, 'devTool/update.html', ctx)
    
    form = ToolForm(request.POST, instance=devTool)
    if form.is_valid():
        form.save()
    return redirect('devTool:list')