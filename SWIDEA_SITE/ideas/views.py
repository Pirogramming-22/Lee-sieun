from django.shortcuts import render,redirect,get_object_or_404
from .models import Ideas
from .forms import UserForm
from devTool.models import DevTool

def list(request):
    ideas = Ideas.objects.all()
    return render(request, 'ideas/list.html', {'ideas':ideas})

def sort(request):
    order_by = request.GET.get('order_by', 'created_at')  
    ideas = Ideas.objects.all().order_by(order_by)  
    return render(request, 'ideas/list.html', {'ideas': ideas, 'order_by': order_by})

def create(request):
    if request.method == 'GET' :
        form = UserForm()
        return render(request, 'ideas/create.html', {'form':form})
    
    form = UserForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('ideas:list')

def detail(request, pk):
    ideas = Ideas.objects.get(id=pk)
    return render(request, 'ideas/detail.html',{'ideas':ideas})

def delete(request, pk):
    Ideas.objects.get(id=pk).delete()
    return redirect('ideas:list')

def update(request, pk):
    idea = Ideas.objects.get(id=pk)
    if request.method == 'GET':
        form = UserForm(instance=idea)
        ctx = {
            'form':form,
            'ideas':idea,
        }
        return render(request, 'ideas/update.html', ctx)
    
    form = UserForm(request.POST, request.FILES, instance=idea)
    if form.is_valid():
        form.save()
    return redirect('ideas:list')


def toggle_star(request, pk):
    idea = get_object_or_404(Ideas, pk=pk)
    idea.is_starred = not idea.is_starred  
    idea.save()
    return redirect('ideas:list')

def devtool_detail(request, pk):
    dev_tool = get_object_or_404(DevTool, pk=pk)
    return render(request, 'devTool/detail.html', {'dev_tool': dev_tool})