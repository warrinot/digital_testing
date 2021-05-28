from rest_framework import pagination


class CallPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 150
    page_size_query_param = 'page_size'
