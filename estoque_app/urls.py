from estoque_app.views import EstoqueList, EstoqueCreate,EstoqueDetailChangeAndDelete 
from django.urls import path

urlpatterns = [
    path('', EstoqueList.as_view()),
    path('post/', EstoqueCreate.as_view()),
    path('<int:pk>/', EstoqueDetailChangeAndDelete.as_view()),
]