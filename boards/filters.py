from rest_framework import filters

class MyCustomFilter:
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(id__gt = 1)# сразу указываем параметр- фильтр обычно пользователь
        # gte === < или >
        # gt  === только >
