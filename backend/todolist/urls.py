from rest_framework.routers import DefaultRouter

from .views import TodoListViewSet

router = DefaultRouter()
router.register(r'',TodoListViewSet, basename='todolist')

todolist_urls = router.urls
