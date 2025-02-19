from .models import Todo

from django.http import HttpResponse, JsonResponse
from http import HTTPStatus
from django.views.generic import View
from django.contrib.auth.models import User
from django.core import serializers

from auth.constants import *

import json

class TodosView(View):
    model = Todo
    query_set = Todo.objects.all()
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        creator_id = request.GET.get("userID")

        if not creator_id:
            response = {"error": INCOMPLETE_FIELDS}
            return JsonResponse(response, status=HTTPStatus.BAD_REQUEST)

        todos = self.query_set.filter(creator_id=creator_id, is_removed=False)
        response = list(todos.values())
        return JsonResponse(response, status=HTTPStatus.OK, safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)["data"]
        creator_id = data.get("userID")

        print('creator_id', data)

        if not creator_id:
            response = {"error": INCOMPLETE_FIELDS}
            return JsonResponse(response, status=HTTPStatus.BAD_REQUEST)

        title = data.get("title")
        user_creator = User.objects.get(id=creator_id)
        fields = {
            "creator": user_creator,
            "title": title
        }

        newTodo = Todo.objects.create(**fields)
        created_todo = {
            "id": newTodo.id,
            "title": newTodo.title,
            "is_done": newTodo.is_done
        }

        print('newTodo', newTodo)
        response = {
            "message": TODO_CREATED_SUCCESS,
            "created_todo": created_todo
        }
        return JsonResponse(response, status=HTTPStatus.OK)
