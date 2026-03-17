# Importing the Request Library 
import requests 
try:

    # Send a get Request to a API 
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    # Unccomment to test Error Handling 
    #response = requests.get("https://jsonplaceholder.typicode.com/invalidendpoint")

    # Raises an error for bad HTTP status codes
    response.raise_for_status()

    # Convert the JSON Format to python data 
    data = response.json()

    # Print the name of the first user 
    print(data[0]["name"])

# Error Handling 
except requests.RequestException:
    print("API error!!!")