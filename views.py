from django.shortcuts import render, get_object_or_404
from django.views import generic

from gctest.models import App, Build, Developer
from gctest.forms import AppForm, BuildForm, DeveloperForm

from random import sample

def index(request):
    apps = App.objects.all()
    if apps.count() > 10:
        rand_apps = sample(xrange(1, apps.count()), 10)
        apps = apps.filter(id__in=rand_apps)
    developers = Developer.objects.all()
    if developers.count() > 10:
        rand_developers = sample(xrange(1, developers.count()), 10)
        developers = developers.filter(id__in=rand_developers)
    return render(request, 'gctest/index.html', 
                  {'app_list' : apps,
                   'developer_list' : developers})

class AppListView(generic.ListView):
    template_name = 'gctest/list_app.html'
    model = App

class DeveloperListView(generic.ListView):
    template_name = 'gctest/list_developer.html'
    model = Developer

def app(request, app_id):
    app = get_object_or_404(App, pk=app_id)
    builds = Build.objects.filter(app=app_id)
    developers = Developer.objects.filter(apps=app_id)
    return render(request, 'gctest/app.html', 
                  {'app' : app,
                   'build_list' : builds,
                   'developer_list' : developers})

class DeveloperDetailView(generic.DetailView):
    template_name = 'gctest/developer.html'
    model = Developer

class BuildDetailView(generic.DetailView):
    template_name = 'gctest/build.html'
    model = Build

def delete_app(request, app_id):
    app = get_object_or_404(App, pk=app_id)
    app.delete()
    return render(request, 'gctest/confirm.html', {'result' : "deleted"})

def delete_developer(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    developer.delete()
    return render(request, 'gctest/confirm.html', {'result' : "deleted"})

def delete_build(request, build_id):
    build = get_object_or_404(Build, pk=build_id)
    build.delete()
    return render(request, 'gctest/confirm.html', {'result' : "deleted"})

def edit_app(request, app_id):
    app = get_object_or_404(App, pk=app_id)
    form = AppForm(request.POST or None, instance=app)
    if form.is_valid():
        form.save()
        return render(request, 'gctest/confirm.html', {'result' : "updated"})
    return render(request, 'gctest/edit.html', {'form' : form, 'view_url' : 'edit_app'})

def edit_developer(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    form = DeveloperForm(request.POST or None, instance=developer)
    if form.is_valid():
        form.save()
        return render(request, 'gctest/confirm.html', {'result' : "updated"})
    return render(request, 'gctest/edit.html', {'form' : form, 'view_url' : 'edit_developer'})

def edit_build(request, build_id):
    build = get_object_or_404(Build, pk=build_id)
    form = BuildForm(request.POST or None, instance=build)
    if form.is_valid():
        form.save()
        return render(request, 'gctest/confirm.html', {'result' : "updated"})
    return render(request, 'gctest/edit.html', {'form' : form, 'view_url' : 'edit_build'})

def new_app(request):
    form = AppForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'gctest/confirm.html', {'result' : "added"})
    return render(request, 'gctest/new.html', {'form' : form, 'view_url' : 'new_app'})

def new_developer(request):
    form = DeveloperForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'gctest/confirm.html', {'result' : "added"})
    return render(request, 'gctest/new.html', {'form' : form, 'view_url' : 'new_developer'})

def new_build(request):
    form = BuildForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'gctest/confirm.html', {'result' : "added"})
    return render(request, 'gctest/new.html', {'form' : form, 'view_url' : 'new_build'})
