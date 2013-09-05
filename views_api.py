from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from gctest.models import App, Build
from gctest.serializers import AppSerializer, BuildSerializer

def app_detail(request, app_id):
    """
    Api to deal with single app instances, get, put (add) or delete.
    """
    app = get_object_or_404(App, pk=app_id)

    if request.method == 'GET':
        serializer = AppSerializer(app)
        return HttpResponse(JSONRenderer().render(serializer.data), {'content_type' : 'application/json'})

    elif request.method == 'PUT':
        serializer = AppSerializer(app, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), {'content_type' : 'application/json'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def build_detail(request, build_id):
    """
    Api to deal with single build instances, get, put (add) or delete.
    """
    build = get_object_or_404(Build, pk=build_id)

    if request.method == 'GET':
        serializer = BuildSerializer(build)
        return HttpResponse(JSONRenderer().render(serializer.data), {'content_type' : 'application/json'})

    elif request.method == 'PUT':
        serializer = BuildSerializer(build, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), {'content_type' : 'application/json'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        build.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def app_list(request):
    """
    Api to deal with all app instances, get, put (add).
    """
    if request.method == 'GET':
        apps = App.objects.all()
        serializer = AppSerializer(apps, many=True)
        return HttpResponse(JSONRenderer().render(serializer.data), {'content_type' : 'application/json'})

    elif request.method == 'POST':
        serializer = AppSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), {'content_type' : 'application/json'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def build_list(request):
    """
    Api to deal with all build instances, get, put (add).
    """
    if request.method == 'GET':
        builds = Build.objects.all()
        serializer = BuildSerializer(builds, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BuildSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), {'content_type' : 'application/json'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
