
from .query_filter import QueryFilter
from .query_sort import QuerySorting

class QueryModel:
    def __init__(self, filters: list[QueryFilter], sort: list[QuerySorting], fields: list[str]):
        self.filters = filters
        self.sort = sort
        self.fields = fields