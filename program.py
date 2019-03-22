import folium
import pandas as pd

data_set = pd.read_csv('cities.csv')
#here few columns have chosen that are required for this task
data_set = data_set[['name_of_city', 'population_total', 'location','state_name']]
#sorting the dataset according to population of city(descending order) 
data_set.sort_values(by = 'population_total', ascending = False, inplace=True)

#creating a background india map
india_map = folium.Map(location=[20.5937, 78.9629],zoom_start=5)

for index,item in data_set.iterrows():
    #if the population of the city less than 5 lakh then break out of the loop (the dataset is sorted)
    if(item['population_total']<500000):    
        break
    
    city = item['name_of_city']

    #as location is a string in the dataset firstly latitude and longitude are separated then converted to float
    location = item['location'].split(',')
    loc = list(map(float, location))

    #putting marker on a city
    # tooltip(hover effect)- shows name of the city
    # popup(click effect)- shows little details about the city like population and state_name 
    folium.Marker(loc, popup='<i>population: {}<br>state: {}</i>'.format(item['population_total'],item['state_name']), tooltip='<i>{}</i>'.format(city)+'<br/>'+'click for more').add_to(india_map)

#saving the map to a html file
india_map.save('india_map.html')