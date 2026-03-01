from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class OptionalLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

    def paginate_queryset(self, queryset, request, view=None):
        if ('limit' not in request.query_params
                and 'offset' not in request.query_params):
            return None
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        if data is None:
            return Response([])
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
