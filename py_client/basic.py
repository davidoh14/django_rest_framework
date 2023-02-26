import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint, params={"abc": 1234}, json={"query": "hello world"}) #http request
get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Hello world", "price": 123}) #http request
# get_response = requests.get(endpoint)
# print(get_response.headers)
# print(get_response.text)
print(get_response.json())
