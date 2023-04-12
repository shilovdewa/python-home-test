from flask import Flask, request, Response
from repositories import CompensationDataRepository
from filters.query_builder import QueryBuilder

app = Flask(__name__)
repo = CompensationDataRepository()

@app.route('/compensation_data', methods=['GET'])
def compensation_data():
    query = QueryBuilder().buildQuery(request.query_string)
    data = repo.readData(query)
    return Response(data, mimetype='application/json')