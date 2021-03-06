from rest_framework import serializers
from .models import *

class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board # указываем с какой моделью и полями будем работать
                           # и использовать в несколькиз views
        fields = '__all__'# если работаем со всеми полями['id', 'title', 'create_time']

class BoardUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardUsers
        fields = '__all__'
class BoardUserExecutorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardUserExecutors
        fields = '__all__'

class BoardCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardCards # указываем с какой моделью и полями будем работать
                           # и использовать в несколькиз views
        fields = '__all__'# если работаем со всеми полями['board', 'title', 'create_time', 'sort_index', 'column', 'description']

class BoardColumnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardColumns
        fields = '__all__'# ['board', 'title', 'create_time', 'sort_index']

class BoardCardCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardCardComments
        fields = '__all__' #['user', 'card','comment', 'create_time']


