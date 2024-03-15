from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 10
    # last_page_strings = 'end'


# http://127.0.0.1:8000/api/pagination/?page=2&page_size=10
# http://127.0.0.1:8000/api/pagination/?page=last
    


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 4
    limit_query_param =  'l'
    offset_query_param = 'o'
    max_limit =  10

# http://127.0.0.1:8000/api/pagination/limitoffset/?limit=4&offset=20
    


class CustomCursorPagination(CursorPagination):
    page_size = 10
    ordering = 'age'