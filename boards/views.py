from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import *
from  rest_framework import generics, filters#для фильтра по части текста
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MyCustomFilter
# from rest_framework.authentication import TokenAuthentication

def  test_view(request):
    return HttpResponse('Hello world')

def boards_list(request):
     boards = Board.objects.all()
     boards_list_str = ''
     for board in boards:
         boards_list_str = boards_list_str + '<li>' + board.id + '  ' + board.title + '  ' + board.board_owner_id + '  ' + board.create_time +'</li>'
     return HttpResponse(boards_list_str)
def board_list_json(request):
    boards= Board.objects.filter(id=2)
    board_data = list(boards.values('id', 'title', 'board_owner'))
    return JsonResponse(board_data, save=False)

class BoardsCreate(generics.CreateAPIView):  # наследуемся от другого класса ,
                                           # доступен только пост и опшион запросы
    serializer_class = BoardsSerializer  # не исп кверисет тк ничего не возвращаем

#Реализовать фильтры колонки по доскам, задачи по колонкам, подсписки по задачам, поиск задач по тексту задачи в рамках одной доски
#Обеспечить фильтрацию вывода данных с помощью кастомного класса в рамках авторизованного пользователя и исключающую архивные задачи

class BoardList(generics.ListAPIView): #:# возвращаем список того что в queryset
    queryset = Board.objects.all()
    #authentication_classes = [TokenAuthentication]
    serializer_class = BoardsSerializer # пишем название сериалайзера который импортируем
                                         # используем из файла serializers.py
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, MyCustomFilter] # перечень классов
    search_fields = ['title']#позволяет поиск по части слова
    filterset_fields = ['id', 'board_owner']#поиск по полному значению поля
    ordering_fields = ['id']# предлагает выбрать сортировку в прямом или обратном порядке

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

class BoardCardCreate(generics.CreateAPIView):
    serializer_class = BoardCardsSerializer




class BoardColumnsList(generics.ListAPIView):
    queryset = BoardColumns.objects.all()
    serializer_class = BoardColumnsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'board']
    search_fields = ['title']
    order_fields = ['create_time', 'sort_index']


