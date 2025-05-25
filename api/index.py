import json

def handler(request, response):
    # Enable CORS
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    # Load marks data
    with open("marks.json", "r") as f:
        marks_data = json.load(f)

    # Get names from query
    names = request.query.getlist("name")
    marks = [marks_data.get(name, None) for name in names]

    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    response.body = json.dumps({"marks": marks})
    return response
