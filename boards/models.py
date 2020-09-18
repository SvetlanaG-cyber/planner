from django.db import models
from datetime import timezone
from django.contrib.auth import get_user_model# для переопределения модели юзера
User = get_user_model()


class Board(models.Model):
    class Meta:
        db_table = "boards"
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    title = models.CharField(blank=False, null=False, max_length=50, verbose_name="Board title")
    #board_owner = models.ForeignKey(User, default=1, blank=False, null=False, verbose_name='User', on_delete=models.CASCADE)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='Create time')
    def __str__(self):
        return self.title

class BoardColumns(models.Model):
    class Meta:
        db_table = "board_columns"
        verbose_name = "Column"
        verbose_name_plural = "Columns"

    board = models.ForeignKey(Board, default=1, blank=False, null=False, verbose_name='Board', on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=50, verbose_name="Column title")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name ='Create time')
    sort_index = models.IntegerField(blank=False, null=False, verbose_name="Index")

    def __str__(self):
        return self.title



class BoardCards(models.Model):
    class Meta:
        db_table = "board_cards"
        verbose_name = "Card"
        verbose_name_plural = "Cards"

    board = models.ForeignKey(Board, default=1, blank=False, null=False, verbose_name='Board', on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=50, verbose_name=" title")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name ='Create time')
    sort_index = models.IntegerField(blank=False, null=False, verbose_name="Index")
    column = models.ForeignKey(BoardColumns, blank=False, null=False, verbose_name='Column', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, default='Add description')

    def __str__(self):
        return self.title



class BoardUserExecutors(models.Model):
    class Meta:
        db_table = "board_user_executor"
        verbose_name = "Executor"
        verbose_name_plural = "Executors"

    user = models.CharField(blank=True, null=True, max_length=50, verbose_name="Executor")
    card = models.ForeignKey(BoardCards, blank=False, null=True, verbose_name='Task', on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class BoardUsers(models.Model):
    class Meta:
        db_table = "board_users"
        verbose_name = "board user"
        verbose_name_plural = "Board Users"

    user = models.ForeignKey(BoardUserExecutors, default=1, blank=False, null=False, verbose_name='User', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, default=1, blank=False, null=False, verbose_name='Board', on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=True, blank=False, verbose_name="Is owner")
    is_reader = models.BooleanField(default=True, blank=False, verbose_name="Is reader only")

    # def __str__(self):
    #     return self.user



class BoardCardComments(models.Model):
    class Meta:
        db_table = "board_user_comment"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    user = models.ForeignKey(BoardUserExecutors, blank=False, null=True, verbose_name='Assigned to', on_delete=models.CASCADE)
    card = models.ForeignKey(BoardCards, blank=False, null=True, verbose_name='Task', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Create time')
    comment = models.TextField(blank=True, null=True, verbose_name='Add comment')

    # def __str__(self):
    #     return self.user