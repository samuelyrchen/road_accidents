import csv
from api.models import Accident


from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

def load_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile) 
        for row in reader: 
            for (k,v) in row.items(): 
                columns[k].append(v) 

    # list_ln_string_float = columns['Location_Northing_OSGR']
    # num_of_location_northing = []
    # for num in list_ln_string_float:
    #     num_of_location_northing.append(float(num))

    list_accident_severity_string_float = columns['Accident_Severity']
    num_of_accident_severity = []
    for num in list_accident_severity_string_float:
        num_of_accident_severity.append(int(num))
    
    Accident.objects.create(
        accident_index=columns['Accident_Index'],
        location_easting=columns.get('Location_Easting_OSGR'),
        location_northing=columns['Location_Northing_OSGR'],
        # location_northing=num_of_location_northing,
        longitude=columns['Longitude'],
        latitude=columns['Latitude'],
        accident_severity=columns['Accident_Severity'],
        number_of_vehicles=columns['Number_of_Vehicles'],
        number_of_casualties=columns['Number_of_Casualties'],
        date=columns['Date']
    )

# python manage.py shell
# from api.load_data import load_csv
# load_csv('/Users/yurongchen/Desktop/web-app(v2)/road_accidents1.csv')