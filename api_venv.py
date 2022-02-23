import requests

# data = requests.get('https://catfact.ninja/fact').json() #json() converts the text file into a python dictionary


# print(data)
try: 
    response = requests.get('https://catfact.ninja/fact')
    print(response.status_code) #by the value we can the error code: 200, 404, 300 (server error), etc.
    response.raise_for_status() #won't raise an exception for 200-299
    print(response.text)
    print(response.json)

    data = response.json()
    fact = data['fact']
    print(f'A random fact about cats: {fact}')
except Exception as e:
    print(e)
