from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomPagination(pagination.LimitOffsetPagination):
    max_limit = 10
    