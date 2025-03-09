from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User

from http import HTTPStatus
import json

from auth.constants import INCOMPLETE_FIELDS
from .constants import TODO_CREATED_SUCCESS, TODO_DELETED_SUCCESS, TODO_UPDATED_SUCCESS
from .models import Todo


# @method_decorator(login_required, name="dispatch")
class TodosView(View):
    model = Todo
    query_set = Todo.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put']

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

        response = {
            "message": TODO_CREATED_SUCCESS,
            "created_todo": created_todo
        }
        return JsonResponse(response, status=HTTPStatus.OK)

    def delete(self, request, *args, **kwargs):
        data = json.loads(request.body)
        todoID = data.get("todoID")

        todo = Todo.objects.get(pk=todoID)
        todo.is_removed = True
        todo.save()

        return JsonResponse({"message": TODO_DELETED_SUCCESS}, status=HTTPStatus.OK)

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)["data"]
        todoID = data.get("todoID")
        updated_title = data.get("updatedTitle", None)
        updated_is_done = data.get("isDone", None)

        if updated_title is None and updated_is_done is None:
            response = {"error": INCOMPLETE_FIELDS}
            return JsonResponse(response, status=HTTPStatus.BAD_REQUEST)

        print('work?')

        todo = Todo.objects.get(pk=todoID)
        todo.title = updated_title or todo.title
        todo.is_done = updated_is_done or todo.is_done

        todo.save()

        return JsonResponse({"message": TODO_UPDATED_SUCCESS}, status=HTTPStatus.OK)
