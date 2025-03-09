from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from http import HTTPStatus
import json

from auth.constants import INCOMPLETE_FIELDS, TODO_CREATED_SUCCESS
from .models import Todo


# @method_decorator(login_required, name="dispatch")
class TodosView(View):
    model = Todo
    query_set = Todo.objects.all()
    http_method_names = ['get', 'post', 'delete']

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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

    def delete(self, request, *args, **kwargs):
        print('being deleted')
        return JsonResponse({"message": "yuh"}, status=HTTPStatus.OK)
