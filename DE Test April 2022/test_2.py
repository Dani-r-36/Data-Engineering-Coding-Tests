# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "number": null,
        "cci_code": null,
        "magistrate_code": null,
        "slug": "central-london-employment-tribunal",
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
            "postcode": "WC2B 6EX",
            "town": "London",
            "type": "Visiting"
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],
        "displayed": true,
        "hide_aols": false,
        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    },
    etc
]
"""

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type

#mysteps 
#        - read csv file and format 
#        - access api and get required details - test if i got what i want 
#        - get required details from api
#        - 
from urllib.request import urlopen
import json
import os
import csv
URL = "https://courttribunalfinder.service.gov.uk/search/results.json"
CSV = "./people.csv"

def open_csv():
    data_list = []
    if os.path.exists(CSV):
     with open(CSV) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)
    else:
        raise Exception ("Invaild location for CSV")

def get_csv_data():
    csv_list = open_csv()
    people_dict={}
    for data in csv_list[1:]:
        if len(data) != 3:
            continue
        people_dict['name'] = data[0]
        people_dict['postcode'] = data[1]
        people_dict['court'] = data[2]
        court_details = api_data(people_dict['postcode'])
    return people_dict, court_details

def people_data(people_dict, court_details):
    for courts in court_details:
        if people_dict['court'] in courts['types']:
            print(courts)

def api_data(postcode):
    try:
        response = urlopen(f"{URL}?postcode={postcode}")
        data_json = json.loads(response.read())
        return data_json
    except Exception as err:
        print(err)
        return("Invalid postcode")



if __name__ == "__main__":
    people_dict, details = get_csv_data()
    people_data(people_dict, details)
