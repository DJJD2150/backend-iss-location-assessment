#!/usr/bin/env python

__author__ = """DJJD2150, Mike A., Janelle Kuhns, Ybrayym Abamov, Jaspal
Singh, Tiffany McLean, Daniel Lomelino's turtle program study hall
video/ repository, the #after-hours-work group video 7/16/2020."""


import requests
import time
import turtle


def get_astronauts():
    # gets the information from the API and assigns it to a variable
    response = requests.get('http://api.open-notify.org/astros.json')
    # converts the specified API info to JSON format and returns it to
    # the main function
    response.raise_for_status()
    return response.json()['people']


def get_iss_location():
    # gets the information from the API and assigns it to a variable
    response = requests.get('http://api.open-notify.org/iss-now.json')
    # converts the specified API info to JSON format, assigns it to
    # a variable, and returns the API's latitude and longitude
    # values to the main function
    iss_location = response.json()['iss_position']
    lat = float(iss_location['latitude'])
    lon = float(iss_location['longitude'])
    return lat, lon


def next_time_overhead(lat, lon):
    # creates a dictionary storing the latitude and longitude
    # coordinates/ function arguments for Indianapolis as values
    # and assigning the dictionary to a variable
    indy_coordinates = {'lat': lat, 'lon': lon}
    # gets the information from the API and assigns it to a variable
    response = requests.get('http://api.open-notify.org/iss-pass.json',
                            params=indy_coordinates)
    response.raise_for_status()
    # converts the specified API info to JSON format, assigns it to
    # a variable, and returns the API's calculated time when the
    # ISS passes over Indianapolis to the main function as a timestamp
    time_overhead = response.json()['response'][1]['risetime']
    return time.ctime(time_overhead)


def get_world_map(lat, lon):
    # creates a variable for the background screen
    screen = turtle.Screen()
    # sets the screen's width and height
    screen.setup(720, 360)
    # selects the image for the screen
    screen.bgpic('map.gif')
    # sets the world coordinates for the screen
    screen.setworldcoordinates(-180, -90, 180, 90)
    # registers the image for the ISS
    screen.register_shape('iss.gif')
    # creates a variable for the ISS turtle
    iss = turtle.Turtle()
    # selects the image for the ISS
    iss.shape('iss.gif')
    # sets the initial position for the ISS turtle
    iss.setheading(90)
    # makes sure there is no drawing the movement pattern
    # of the ISS turtle
    iss.penup()
    # puts the ISS turtle at the coordinates it's currently at
    # according to its API information and timestamp
    iss.goto(lon, lat)
    return screen


def plot_overhead(lat, lon):
    # creates a dictionary storing the latitude and longitude
    # coordinates/ function arguments for the International Space
    # Station as values and assigning the dictionary to a variable
    po_coordinates = {'lat': lat, 'lon': lon}
    # gets the information from the API and assigns it to a variable
    response = requests.get('http://api.open-notify.org/iss-pass.json',
                            params=po_coordinates)
    # converts the specified API info to JSON format, assigns it to
    # a variable, and returns the API's calculated timestamp for the ISS
    # to the main function
    overhead_time = response.json()['response'][1]['risetime']
    return time.ctime(overhead_time)
    # if everything works
    try:
        indy_latitude = 39.768403
        indy_longitude = -86.158068
        # assigns the Indianapolis turtle to a variable
        indy_turtle_location = turtle.Turtle()
        # prevents the pen from marking Indianapolis
        indy_turtle_location.penup()
        indy_turtle_location.color('yellow')
        # puts Indianapolis's turtle at its correct coordinates
        indy_turtle_location.goto(indy_longitude, indy_latitude)
        indy_turtle_location.dot(5)
        indy_turtle_location.hideturtle()
        indy_location = next_time_overhead(indy_latitude, indy_longitude)
        city_name = ' Indianapolis, Indiana'
        indy_turtle_location.write(indy_location + city_name, align='center',
                                   font=('Arial', 12, 'normal'))
    # if there's an error
    except RuntimeError as error:
        print('Error: Problem loading graphics: ' + str(error))


def main():
    # prints list of astronauts
    print('List of Astronauts: ' + str(get_astronauts()))
    # prints number of astronauts by counting length of the ones listed
    print('Number of Astronauts: ' + str(len(get_astronauts())))
    # prints the coordinates of the International Space Station
    print('ISS Coordinates: ' + str(get_iss_location()))
    # prints the International Space Station's timestamp
    lat, lon = get_iss_location()
    print('Timestamp: ' + str(plot_overhead(lat, lon)))
    # sets the screen variable to none when the program isn't running
    screen = None
    # if everything works
    try:
        # sets the screen variable to the background image when the
        # program runs correctly
        screen = get_world_map(lat, lon)
        indy_latitude = 39.768403
        indy_longitude = -86.158068
        # assigns the Indianapolis turtle to a variable
        indy_turtle_location = turtle.Turtle()
        # prevents the pen from marking Indianapolis
        indy_turtle_location.penup()
        indy_turtle_location.color('yellow')
        # puts Indianapolis's turtle at its correct coordinates
        indy_turtle_location.goto(indy_longitude, indy_latitude)
        # makes the Indianapolis turtle a dot and sizes it
        indy_turtle_location.dot()
        indy_turtle_location.hideturtle()
        indy_location = next_time_overhead(indy_latitude, indy_longitude)
        city_name = ' Indianapolis, Indiana'
        # writes Indianapolis's city name and the timestamp of when the ISS
        # will next hover over the city above its turtle and styles its font
        indy_turtle_location.write(indy_location + city_name, align='center',
                                   font=('Arial', 12, 'normal'))
    # print something to recognize if there's an error
    except RuntimeError as error:
        print('Error: Problem loading graphics: ' + str(error))
    # gives you an option to exit the screen by clicking on it
    if screen is not None:
        print('Click on screen to exit.')
        screen.exitonclick()


if __name__ == '__main__':
    main()
