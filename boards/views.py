from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import *
from  rest_framework import generics, filters, permissions#для фильтра по части текста
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MyCustomFilter
from rest_framework.authentication import TokenAuthentication

# def  test_view(request):
#     return HttpResponse('Hello world')
#
# def boards_list(request):
#      boards = Board.objects.all()
#      boards_list_str = ''
#      for board in boards:
#          boards_list_str = boards_list_str + '<li>' + board.id + '  ' + board.title + '  ' + board.board_owner_id + '  ' + board.create_time +'</li>'
#      return HttpResponse(boards_list_str)
# def board_list_json(request):
#     boards= Board.objects.filter(id=2)
#     board_data = list(boards.values('id', 'title', 'board_owner'))
#     return JsonResponse(board_data, save=False)


#Реализовать фильтры колонки по доскам, задачи по колонкам, подсписки по задачам, поиск задач по тексту задачи в рамках одной доски
#Обеспечить фильтрацию вывода данных с помощью кастомного класса в рамках авторизованного пользователя и исключающую архивные задачи

#Board ['id', 'title', 'create_time']
class BoardList(generics.ListAPIView): #:# возвращаем список того что в queryset
    queryset = Board.objects.all()
    #authentication_classes = [TokenAuthentication] # говорит о том что исп токен для авторизации пользователя
    # чтоб не прописывать в каждом классе импортируем по умолчанию в
    serializer_class = BoardsSerializer # пишем название сериалайзера который импортируем
    permission_classes = [permissions.IsAuthenticated]    # используем из файла serializers.py
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, MyCustomFilter] # перечень классов
    search_fields = ['title']#позволяет поиск по части слова
    filterset_fields = ['id']#поиск по полному значению поля
    ordering_fields = ['create_time']# предлагает выбрать сортировку в прямом или обратном порядке

class BoardsCreate(generics.CreateAPIView):  # наследуемся от другого класса ,
                                            # доступен только пост и опшион запросы
     serializer_class = BoardsSerializer  # не исп queryset тк ничего не возвращаем

class BoardRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#BoardCards ['id', 'board', 'title', 'create_time', 'sort_index', 'column', 'description']['column']
class BoardCardsList(generics.ListAPIView):
    queryset = BoardCards.objects.all()
    serializer_class = BoardCardsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,
                       MyCustomFilter]  # перечень классов MyCustomFilter из папки filters не виден
                                        # как поисковая строка сразу выдает фильтрованный ответ
                                        # используем фильтр только в get запросе
    search_fields = ['title', 'description']  # позволяет поиск по части слова
    filterset_fields = ['id', 'board']  # поиск по полному значению поля
    ordering_fields = ['sort_index', 'create_time']  # предлагает выбрать сортировку в прямом или обратном порядкe  id // -id

    def get_queryset(self):  # метод фильтра у  ListAPIView
        return BoardCards.objects.filter(board_id=self.kwargs['column_id'])

class BoardCardRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardCards.objects.all()
    serializer_class = BoardCardsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BoardCardCreate(generics.CreateAPIView):
    serializer_class = BoardCardsSerializer

# BoardUsers ['id', 'user', 'board', 'is_owner', 'is_reader']
class BoardUsersList(generics.ListAPIView):
    queryset = BoardUsers.objects.all()
    serializer_class = BoardUsersSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,
                       MyCustomFilter]
    search_fields = ['user']  # позволяет поиск по части слова
    filterset_fields = ['id', 'board']  # поиск по полному значению поля
    ordering_fields = ['is_owner', 'is_reader']  # предлагает выбрать сортировку в прямом или обратном порядкe  id // -id

    # def get_queryset(self):  # метод фильтра у  ListAPIView
    #     return BoardUsers.objects.filter(board_id=self.kwargs['column_id'])

class BoardUsersRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardUsers.objects.all()
    serializer_class = BoardUsersSerializer

class BoardUsersCreate(generics.CreateAPIView):
    serializer_class = BoardUsersSerializer

#BoardUserExecutors ['id', 'user', 'card']
class BoardUserExecutorsList(generics.ListAPIView):
    queryset = BoardUserExecutors.objects.all()
    serializer_class = BoardUserExecutorsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,
                       MyCustomFilter]
    search_fields = ['user']  # позволяет поиск по части слова
    filterset_fields = ['id']  # поиск по полному значению поля
    ordering_fields = ['card']  # предлагает выбрать сортировку в прямом или обратном порядкe  id // -id

    # def get_queryset(self):  # метод фильтра у  ListAPIView
    #     return BoardUsers.objects.filter(board_id=self.kwargs['column_id'])

class BoardUserExecutorsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardUserExecutors.objects.all()
    serializer_class = BoardUserExecutorsSerializer

class BoardUserExecutorsCreate(generics.CreateAPIView):
    serializer_class = BoardUserExecutorsSerializer

#BoardCardComments ['id', 'user', 'card', 'comment', 'create_time']

class BoardCardsCommentsList(generics.ListAPIView):
    queryset = BoardCardComments.objects.all()
    serializer_class = BoardCardCommentsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,
                       MyCustomFilter]  # перечень классов MyCustomFilter из папки filters не виден
                                        # как поисковая строка сразу выдает фильтрованный ответ
                                        # используем фильтр только в get запросе
    search_fields = ['comment']  # позволяет поиск по части слова
    filterset_fields = ['id', 'user', 'card']  # поиск по полному значению поля
    ordering_fields = ['create_time']  # предлагает выбрать сортировку в прямом или обратном порядкe  id // -id

    def get_queryset(self):  # метод фильтра у  ListAPIView
        return BoardCards.objects.filter(board_id=self.kwargs['user'])

class BoardCardCommentRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardCardComments.objects.all()
    serializer_class = BoardCardCommentsSerializer


class BoardCardCommentCreate(generics.CreateAPIView):
    serializer_class = BoardCardCommentsSerializer

#BoardColumns ['id', 'board', 'title', 'create_time', 'sort_index']

class BoardColumnsList(generics.ListAPIView):
    queryset = BoardColumns.objects.all()
    serializer_class = BoardColumnsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'board']
    search_fields = ['title']
    order_fields = ['create_time', 'sort_index']

class BoardCollumnsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardColumns.objects.all()
    serializer_class = BoardColumnsSerializer


class BoardCollumnsCreate(generics.CreateAPIView):
    serializer_class = BoardColumnsSerializer


