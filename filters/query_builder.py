import urllib.parse
import re
from models import QueryModel, QueryFilter, QuerySorting

class QueryBuilder:
    
    @staticmethod
    def buildQuery(query_string):
        result = QueryModel(list[QueryFilter](), list[QuerySorting](), list[str]())
        query = QueryBuilder.getParsedQuery(query_string)
        for key in query.keys():
            if key == "sort":
                result.sort = QueryBuilder.buildSorting(query.get(key))
            elif key == "fields":
                result.fields = str.join(",", query.get(key)).split(',')
            else:
                field = QueryBuilder.extractField(key)
                if field == None:
                    continue
                operation = QueryBuilder.extractOperation(key)
                for value in query.get(key):
                    result.filters.append(QueryFilter(field, operation, value))

        return result     
    
    @staticmethod
    def getParsedQuery(query_string: str) -> dict[str, list[str]]:
        result = dict[str, list[str]]()
        query = urllib.parse.parse_qs(query_string)
        for key_b in query.keys():
            key = key_b.decode('UTF-8')
            values = list[str]()
            for value in query.get(key_b):
                values.append(value.decode('UTF-8'))
            result[key] = values
        return result

    @staticmethod
    def extractOperation(key: str) -> str:
        op = re.search("\[(.*)\]$", key)
        if op == None or op.group(1) == "":
            return 'eq'
        return op.group(1)

    @staticmethod
    def extractField(key: str) -> str | None:
        op = re.search("(.*)\[(.*)\]$", key)
        if op == None or op.group(1) == "":
            return key
        return op.group(1)

    @staticmethod
    def buildSorting(values: list[str]) -> list[QuerySorting]:
        result = list[QuerySorting]()
        for value in str.join(",", values).split(','):
            ascending = True
            field = value
            if value.startswith("-"):
                ascending = False
                field = value.removeprefix("-")
            result.append(QuerySorting(field, ascending))
        return result