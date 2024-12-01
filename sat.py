import pgzrun
import random
from time import time

WIDTH=800
HEIGHT=600

TITLE="connecting satellite"

satellite=[]
lines=[]
next_satellite=0


start_time=0
total_time=0
end_time=0

Number_of_sat=8

def create_sat():
    for i in range(Number_of_sat):
        sat=Actor("satellite")
        sat.pos=random.randint(40,Width-40),random.randint(40,HEIGHT,-40)
        satellite.append(sat)


def draw():
    screen.blit("background",(0,0))
