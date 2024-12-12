#!/usr/bin/python3

# standard library
import json

# 3rd party library
import requests

# Define URL as a global constant (this will not change)
MAJORTOM = 'http://api.spacexdata.com/v3/dragons'

def main():
    """making API requests"""
    
    # Call the web service
    resp = requests.get(MAJORTOM)  # sends an HTTP GET
    
    # strip JSON data off response and convert
    # to python data types
    data = resp.json()
            
    # display our Pythonic data
    print("\n\nConverted Python data")
    print(data)
    
    #print('\n\nPeople in Space: ', data.get('number'))
    

    # for-loop across astros
    # display names of those in space
    for item in data:
        print(f"name is is:", item['name'])

if __name__ == '__main__':
    main()

