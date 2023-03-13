
from .models import TodoList
from .serializers import TodoListSerializer
from rest_framework import viewsets
# Create your views here.

class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()


""" class TodoListApiView(APIView):
    def get(self, request):
        todolist = TodoList.objects.all()
        serializador = TodoListSerializer(todolist, many=True)
        return Response(serializador.data)
    
#     def post(self, request):
#         return Response(output)
todolist_view = TodoListApiView.as_view()    
 """
