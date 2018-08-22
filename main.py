import requests
import turtle
import time
from turtle import Turtle


def astronauts():
    name = []
    ship = []
    r = requests.get('http://api.open-notify.org/astros.json')
    content = r.json()
    i = 0
    while i < len(content.values())+3:
        name.append(str(content.values()[2][i].values()[1])) 
        ship.append(str(content.values()[2][i].values()[0])) 
        i += 1

    name_with_ship = zip(name, ship)

    print "     total number of people in space: ", len(name_with_ship)
    print

    for tup in enumerate(name_with_ship):
        a, b = tup
        print " is on spacecraft ".join(b)

def current_geo_coords():
    coords = []
    r = requests.get('http://api.open-notify.org/iss-now.json')
    content = r.json()
    lat_long = content.values()[2]
    latitude = lat_long.values()[0]
    longitude = lat_long.values()[1]
    print
    print " timestamp: ", content.values()[0]
    print
    print " current latitude: ", latitude
    print
    print " current longitude: ", longitude
    print
    coords.append(latitude)
    coords.append(longitude)
    return coords


def draw():
    current_lat_long = current_geo_coords()
    latitude = int(float((current_lat_long[0])))
    longitude = int(float((current_lat_long[1])))
    
    screen = turtle.Screen()
    """create the screen"""
    screen.setup(720,360)
    screen.title("ISS locator")
    screen.bgpic("map.gif")
    screen.setworldcoordinates(-180,-90, 180, 90)
    image = "iss.gif"
    screen.addshape(image)

    """create the turle for ISS"""
    ship = turtle.Turtle()
    ship.shape(image)
    ship.setheading(90)
    ship.penup()
    ship.goto(longitude, latitude)

    """create the turtle for Indy"""
    dot = turtle.Turtle()
    dot.color("yellow")
    dot.shape("circle")
    dot.setheading(90)
    dot.pensize(2)
    dot.penup()
    """Indianapolis"""
    dot.goto(-86.1581, 39.7684)
    dot.write("next passover time: {}".format(when_will_it_pass()), font=("arial", 16, "normal"))
    screen.exitonclick()


def when_will_it_pass():
    """see when the ISS will pass over Indy"""
    passover_times = []
    latitude = 39.7684
    longitude = -86.5181
    payload = {"lat": str(latitude), "lon": str(longitude)}
    r = requests.get('http://api.open-notify.org/iss-pass.json', payload)
    content = r.json()
    for things in content.values()[2]:
        passover_times.append(int(things.values()[1]))
    times = sorted(passover_times, reverse = True)
    for pass_time in times:
        next = time.ctime(pass_time)
    return next

if __name__ == "__main__":
    astronauts()
    current_geo_coords()
    draw()
    

