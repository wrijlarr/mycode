#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""
import pprint

import requests

URL= "https://opentdb.com/api.php?amount=3&category=15&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    
    for question in data.get("results"):
        print(data.get("question"))
        print(data.get("correct_answer"))
        

    
if __name__ == "__main__":
    main()

