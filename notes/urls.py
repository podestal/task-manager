from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('notes', views.NotesViewSet, basename='notes')

urlpatterns = router.urls

