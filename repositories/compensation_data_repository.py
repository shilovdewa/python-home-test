import pandas as pd
import os
import io
from models import CompansationHeadersMapping, QueryModel, QueryFilter, QuerySorting

class CompensationDataRepository():	
    def __init__(self):
        self.data = pd.read_csv(os.environ['DATA_PATH'], sep=",", parse_dates=True, dayfirst=False, date_format="%m/%d/%y %H:%M:%S")
        map_obj = CompansationHeadersMapping()
        mapping = CompansationHeadersMapping.getMapping(map_obj)
        self.data = self.data.rename(columns=mapping)

        #Fix timestamp parsing
        for element in map_obj.mapping:
            if element['type'] == "timestamp":
                self.data[element['map']]= pd.to_datetime(self.data[element['map']])
    
    def readData(self, query: QueryModel):
        data = self.data
        map_obj = CompansationHeadersMapping()

        #Filter
        if len(query.filters) > 0:
            expr = self.buildFilterExpression(query.filters, map_obj)
            if not(expr == "" or expr.isspace()):
                data = data.query(expr)

        #Sorting
        if len(query.sort) > 0:
            sorting = self.buildSortFields(query.sort)
            data = data.sort_values(by=sorting[0], ascending=sorting[1])

        #Select
        if len(query.fields) > 0:
            data = data.filter(items=query.fields)

        with io.StringIO() as output:
            data.to_json(output, 
                        orient="records",
                        lines=True, date_format="iso",
                        double_precision=10, force_ascii=True,
                        date_unit="ms", default_handler=None)
            return output.getvalue()

    def buildFilterExpression(self, filters: list[QueryFilter], mapping: CompansationHeadersMapping) -> str:
        result: list[str] = list[str]()
        for filter in filters:
            if filter.operation == "like":
                result.append(f'{filter.field}.str.contains("{filter.value}")')
            else:
                field_type = mapping.getType(filter.field)
                if field_type == "float64":
                    result.append(f'{filter.field} {self.getFilterOperation(filter.operation)} {filter.value}')
                else:
                    result.append(f'{filter.field} {self.getFilterOperation(filter.operation)} "{filter.value}"')
        return str.join(" and ", result)

    def buildSortFields(self, sorts: list[QuerySorting]) -> tuple:
        result = (list[str](), list[bool]())
        for sort in sorts:
            result[0].append(sort.field)
            result[1].append(sort.ascending)
        return result
    
    def getFilterOperation(self, op: str) -> str:
        match op:
            case "gt":
                return ">"
            case "lt":
                return "<"
            case "gte":
                return ">="
            case "lte":
                return "<="
            case _:
                return "=="