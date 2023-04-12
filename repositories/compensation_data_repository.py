from collections import namedtuple
import pandas as pd
import os
from models import CompansationHeadersMapping, QueryModel, QueryFilter, QuerySorting

class CompensationDataRepository():	
    mapping_object = CompansationHeadersMapping()

    def __init__(self):
        self.data = pd.read_csv(os.environ['DATA_PATH'], sep=",", parse_dates=True, dayfirst=False, date_format="%m/%d/%y %H:%M:%S")
        mapping = CompansationHeadersMapping.getMapping(self.mapping_object)
        self.data = self.data.rename(columns=mapping)

        #Fix timestamp parsing
        for element in self.mapping_object.mapping:
            element_mapping = self.mapping_object.mapping[element]
            if element_mapping['type'] == "timestamp":
                self.data[element]= pd.to_datetime(self.data[element])
    
    def readData(self, query: QueryModel):
        data = self.data.copy(deep=True)
        
        #Filter
        if len(query.filters) > 0:
            expr = CompensationDataRepository.buildFilterExpression(query.filters, self.mapping_object)
            if not(expr == "" or expr.isspace()):
                data = data.query(expr)

        #Sorting
        if len(query.sort) > 0:
            sorting = CompensationDataRepository.buildSortFields(query.sort)
            data = data.sort_values(by=sorting.field, ascending=sorting.ascending)

        #Select
        if len(query.fields) > 0:
            data = data.filter(items=query.fields)

        return data.to_json(orient="records", date_format="iso",
                        double_precision=10, force_ascii=True,
                        date_unit="ms", default_handler=None)

    @staticmethod
    def buildFilterExpression(filters: list[QueryFilter], mapping: CompansationHeadersMapping) -> str:
        result: list[str] = list[str]()
        for filter in filters:
            if not(filter.field in mapping.mapping):
                continue
            field_type = mapping.getType(filter.field)
            if field_type == "float64":
                result.append(f'{filter.field} {CompensationDataRepository.getFilterOperation(filter.operation)} {filter.value}')
            else:
                result.append(f'{filter.field} {CompensationDataRepository.getFilterOperation(filter.operation)} "{filter.value}"')
        return str.join(" and ", result)

    @staticmethod
    def buildSortFields(sorts: list[QuerySorting]) -> namedtuple:
        Sorting = namedtuple('Sorting', ['field', 'ascending'])
        result = Sorting(list[str](), list[bool]())
        for sort in sorts:
            result.field.append(sort.field)
            result.ascending.append(sort.ascending)
        return result
    
    @staticmethod
    def getFilterOperation(op: str) -> str:
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