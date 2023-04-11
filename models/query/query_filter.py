class QueryFilter:
    def __init__(self, field: str, operation: str, value: str):
        self.field = field
        self.operation = operation
        self.value = value