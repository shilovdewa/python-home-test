import urllib.parse
import re
from models import QueryModel, QueryFilter, QuerySorting

class QueryBuilder:
    def buildQuery(self, query_string):
        result = QueryModel(list[QueryFilter](), list[QuerySorting](), list[str]())
        query = self.getParsedQuery(query_string)
        for key in query.keys():
            if key == "sort":
                result.sort = self.buildSorting(query.get(key))
            elif key == "fields":
                result.fields = str.join(",", query.get(key)).split(',')
            else:
                field = self.extractField(key)
                if field == None:
                    continue
                operation = self.extractOperation(key)
                for value in query.get(key):
                    result.filters.append(QueryFilter(field, operation, value))

        return result     
    
    def getParsedQuery(self, query_string: str) -> dict[str, list[str]]:
        result = dict[str, list[str]]()
        query = urllib.parse.parse_qs(query_string)
        for key_b in query.keys():
            key = key_b.decode('UTF-8')
            values = list[str]()
            for value in query.get(key_b):
                values.append(value.decode('UTF-8'))
            result[key] = values
        return result

    def extractOperation(self, key: str) -> str:
        op = re.search("\[(.*)\]$", key)
        if op == None or op.group(1) == "":
            return 'eq'
        return op.group(1)

    def extractField(self, key: str) -> str | None:
        op = re.search("(.*)\[(.*)\]$", key)
        if op == None or op.group(1) == "":
            return key
        return op.group(1)

    def buildSorting(self, values: list[str]) -> list[QuerySorting]:
        result = list[QuerySorting]()
        for value in str.join(",", values).split(','):
            ascending = True
            field = value
            if value.startswith("-"):
                ascending = False
                field = value.removeprefix("-")
            result.append(QuerySorting(field, ascending))
        return result