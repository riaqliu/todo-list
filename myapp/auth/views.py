from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from http import HTTPStatus
import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .constants import *

def SignInView(request):
    request_body = json.loads(request.body)
    username = request_body.get("username")
    password = request_body.get("password")

    try:
        existing_user = User.objects.get(username=username)
    except:
        response = {"error": USER_NOT_FOUND}
        return JsonResponse(response, status=HTTPStatus.NOT_FOUND)


    user = authenticate(request, username=existing_user.username, password=password)

    if user is None:
        response = {"error": PASSWORD_INCORRECT}
        return JsonResponse(response, status=HTTPStatus.UNAUTHORIZED)

    data = {
        "id": user.pk,
        "username": user.username
    }

    response = {
        "message": LOG_IN_SUCCESSFUL,
        "user": data
    }
    return JsonResponse(response, status=HTTPStatus.OK)