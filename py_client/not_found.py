import requests

endpoint = "http://localhost:8000/api/products/0192873590172395712"

get_response = requests.get(endpoint)

print(get_response.json())
