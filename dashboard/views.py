from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import VideoIdea
from .forms import CustomUserRegistrationForm,VideoIdeaForm,ResourceLinkForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request,"home.html")

def about(request):
    return render(request, 'about.html')

@login_required(login_url='login/')

def creator_dashboard(request):
    my_videos=VideoIdea.objects.filter(user=request.user).order_by('-created_at')
    context={
        'videos':my_videos
    }
    return render(request,"dashboard.html",context)

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Account created successfully! Welcome to CreatorHub, {user.username}.")
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserRegistrationForm()
        
    return render(request, 'register.html', {'form': form})

@login_required(login_url='/login/')
def add_video(request):
    if request.method == 'POST':
        form = VideoIdeaForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            
            video.user = request.user 
            
            video.save()
            
            messages.success(request, f"'{video.title}' was added to your pipeline!")
            return redirect('dashboard')
    else:
        form = VideoIdeaForm()
        
    return render(request, 'add_video.html', {'form': form})

@login_required(login_url='/login/')
def edit_video(request, pk):
    video = get_object_or_404(VideoIdea, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = VideoIdeaForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, f"'{video.title}' has been updated!")
            return redirect('dashboard')
    else:
        form = VideoIdeaForm(instance=video)
        
    return render(request, 'edit_video.html', {'form': form, 'video': video})

@login_required(login_url='/login/')
def delete_video(request, pk):
    video = get_object_or_404(VideoIdea, pk=pk, user=request.user)
    
    if request.method == 'POST':
        title = video.title 
        video.delete()
        messages.warning(request, f"'{title}' was removed from your pipeline.")
        return redirect('dashboard')
        
    return render(request, 'delete_video.html', {'video': video})

@login_required(login_url='/login/')
def manage_resources(request, pk):
    video = get_object_or_404(VideoIdea, pk=pk, user=request.user)
    
    existing_links = video.resources.all()
    
    if request.method == 'POST':
        form = ResourceLinkForm(request.POST)
        if form.is_valid():
            new_link = form.save(commit=False)
            new_link.video = video
            new_link.save()
            
            messages.success(request, "Resource link added successfully!")
            return redirect('manage_resources', pk=video.id)
    else:
        form = ResourceLinkForm()
        
    context = {
        'video': video,
        'links': existing_links,
        'form': form
    }
    return render(request, 'manage_resources.html', context)