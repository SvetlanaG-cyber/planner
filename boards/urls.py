from django.urls import path
from .views import *

urlpatterns = [
    #path('test/', test_view),
    #path('list/', boards_list),
    path('board/list/', BoardList.as_view()),
    path('board/create/', BoardsCreate.as_view()),
    path('board/rud/', BoardRUD.as_view()),
    #path('list/filter/<int:board_id>/', BoardFilter.as_view()),
    path('card/list/<int:column_id>/', BoardCardsList.as_view()),
    path('card/create/', BoardCardCreate.as_view()),
    path('card/rud/<int:column_id>/', BoardCardRUD.as_view()),
    path('user/list/', BoardUsersList.as_view()),
    path('user/create/', BoardUsersCreate.as_view()),
    path('user/rud/', BoardUsersRUD.as_view()),
    path('exec/list/', BoardUserExecutorsList.as_view()),
    path('exec/create/', BoardUserExecutorsCreate.as_view()),
    path('exec/rud/', BoardUserExecutorsRUD.as_view()),
    path('column/list/', BoardColumnsList.as_view()),
    path('column/create/', BoardCollumnsCreate.as_view()),
    path('column/rud/', BoardCollumnsRUD.as_view()),
    path('comment/list/<int:user_id>/', BoardCardsCommentsList.as_view()),
    path('comment/create/', BoardCardCommentCreate.as_view()),
    path('comment/rud/', BoardCardCommentRUD.as_view()),
]
