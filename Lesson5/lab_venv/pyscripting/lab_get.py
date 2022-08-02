import requests

response = requests.get('http://google.com')

print(response)
print("The response code is: ", response.status_code)

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
    
print("Contents in string: ", response.text)
print("\nResponse Headers: ", response.headers)