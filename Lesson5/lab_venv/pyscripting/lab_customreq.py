import requests

# Search GitHub's repositories for requests
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

print(response)

# Inspect some attributes of the `requests` repository
# returns a JSON object of the result (if the result was written in JSON format, if not it raises an error:
json_response = response.json()

repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')
print(f'Repository description: {repository["description"]}')
