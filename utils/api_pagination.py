from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 1000


class PaginationSmall(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 30
