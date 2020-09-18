from django.urls import path
from .views import *

urlpatterns = [
    path('test/', test_view),
    path('list/', boards_list),
    path('list/ser/', BoardList.as_view()),
    path('list/create/', BoardsCreate.as_view()),
    #path('list/filter/<int:board_id>/', BoardFilter.as_view()),
    path('list/card/<int:column_id>/', BoardCardsList.as_view()),
    path('list/column/', BoardColumnsList.as_view()),
]
