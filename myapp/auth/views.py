from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie

from http import HTTPStatus
import json

from .constants import USER_NOT_FOUND, PASSWORD_INCORRECT, LOG_IN_SUCCESSFUL


@ensure_csrf_cookie
@csrf_exempt
def SignInView(request):
    request_body = json.loads(request.body)
    username = request_body.get("username")
    password = request_body.get("password")

    try:
        existing_user = User.objects.get(username=username)
    except Exception:
        response = {"error": USER_NOT_FOUND}
        return JsonResponse(response, status=HTTPStatus.NOT_FOUND)

    user = authenticate(request, username=existing_user.username, password=password)

    if user is None:
        response = {"error": PASSWORD_INCORRECT}
        return JsonResponse(response, status=HTTPStatus.UNAUTHORIZED)

    # Set session
    # request.session["member_id"] = user.pk

    data = {
        "id": user.pk,
        "username": user.username
    }

    response = {
        "message": LOG_IN_SUCCESSFUL,
        "user": data,
        "csrfToken": get_token(request)
    }
    return JsonResponse(response, status=HTTPStatus.OK)
