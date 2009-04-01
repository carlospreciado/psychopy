#! /usr/local/bin/python2.5
from psychopy import visual, core, event
import numpy, time    
win = visual.Window([800,800])

handVerts = numpy.array([ [0,0.8],[-0.05,0],[0,-0.05],[0.05,0] ])#vertices (using numpy means we can scale them easily)

second = visual.ShapeStim(win, vertices= [[0,-0.1], [0.1,0.8]],
    lineRGB=[1,-1,-1],fillRGB=None, lineWidth=2)
minute = visual.ShapeStim(win, vertices=handVerts,
    lineRGB=[1,1,1],fillRGB=[0.8,0.8,0.8])
hour = visual.ShapeStim(win, vertices=handVerts/2.0,
    lineRGB=[-1,-1,-1],fillRGB=[-0.8,-0.8,-0.8])
clock = core.Clock()

while True: #ie forever
    t = time.localtime()
    
    minPos = numpy.floor(t[4])*360/60 #NB floor will round down to previous minute
    minute.setOri(minPos)
    minute.draw()
    
    hourPos = (t[3])*360/12#this one can be smooth
    hour.setOri(hourPos)
    hour.draw()
    
    secPos = numpy.floor(t[5])*360/60#NB floor will round down to previous second
    second.setOri(secPos)
    second.draw()
    
    win.flip()
    if 'q' in event.getKeys():
        break
    event.clearEvents()
    
