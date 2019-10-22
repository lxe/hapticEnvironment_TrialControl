import sys 
sys.path.append("/home/monica/Documents/chaiProjects/hapticEnvironment_TrialControl/")
import numpy as np
import messageDefinitions as md
from ctypes import *
import Messenger as MR
import Globals 

def enableGraphics(objectName, setVal):
  name = create_string_buffer(bytes(objectName, 'utf-8'), md.MAX_STRING_LENGTH)
  namePtr = (c_char_p) (addressof(name))
  display = md.M_GRAPHICS_SET_ENABLED()
  display.header.msg_type = c_int(md.GRAPHICS_SET_ENABLED)
  display.objectName = namePtr.value
  display.enabled = c_int(setVal)
  packet = MR.makeMessage(display)
  MR.sendMessage(packet)
  return packet 

def changeColor(objectName, r, g, b, a):
  changeColor = md.M_GRAPHICS_CHANGE_OBJECT_COLOR()
  changeColor.header.msg_type = md.GRAPHICS_CHANGE_OBJECT_COLOR
  name = create_string_buffer(bytes(objectName, 'utf-8'), md.MAX_STRING_LENGTH)
  namePtr = (c_char_p)(addressof(name))
  changeColor.objectName = namePtr.value 
  changeColor.color = (c_float * 4) (r, g, b, a)
  packet = MR.makeMessage(changeColor)
  MR.sendMessage(packet)

def makeObject(name, shape, size, color, position):
  if shape == "circle":
    makeSphere(name, size, position, color, 0)
  elif shape == "box":
    makeBox(name, size, position, color, 0)

def makeSphere(objectName, radius, position, color, enabled):
  sphereObj = md.M_GRAPHICS_SHAPE_SPHERE()
  sphereObj.header.msg_type = c_int(md.GRAPHICS_SHAPE_SPHERE)
  name = create_string_buffer(bytes(objectName, 'utf-8'), md.MAX_STRING_LENGTH)
  namePtr = (c_char_p) (addressof(name))
  sphereObj.objectName = namePtr.value
  sphereObj.radius = c_double(radius)
  sphereObj.localPosition = (c_double * 3) (position[0], position[1], position[2])
  sphereObj.color = (c_float * 4) (color[0], color[1], color[2], color[3])
  packet = MR.makeMessage(sphereObj)
  MR.sendMessage(packet)
  enableGraphics(objectName, enabled)
  return packet 

def makeBox(objectName, size, position, color, enabled):
  box = md.M_GRAPHICS_SHAPE_BOX()
  box.header.msg_type = c_int(md.GRAPHICS_SHAPE_BOX)
  name = create_string_buffer(bytes(objectName, 'utf-8'), md.MAX_STRING_LENGTH)
  namePtr = (c_char_p) (addressof(name))
  box.objectName = namePtr.value 
  box.sizeX = c_double(size[0])
  box.sizeY = c_double(size[1])
  box.sizeZ = c_double(size[2])
  box.localPosition = (c_double*3) (position[0], position[1], position[2])
  box.color = (c_float*4) (color[0], color[1], color[2], color[3])
  packet = MR.makeMessage(box)
  MR.sendMessage(packet)

def setBackground(red, green, blue):
  bg = md.M_GRAPHICS_CHANGE_BG_COLOR()
  bg.header.msg_type = c_int(md.GRAPHICS_CHANGE_BG_COLOR)
  bg.color = (c_float * 4) (red, green, blue, 1.0)
  packet = MR.makeMessage(bg)
  MR.sendMessage(packet)
  return packet 

def makeArrow(objectName, length, sRadius, tLength, tRadius, bidir, direction, position, color, enabled):
  arrow = md.M_GRAPHICS_ARROW()
  arrow.header.msg_type = c_int(md.GRAPHICS_ARROW)
  arrowName = create_string_buffer(bytes(objectName, 'utf-8'), md.MAX_STRING_LENGTH)
  arrowNamePtr = (c_char_p) (addressof(arrowName))
  arrow.objectName = arrowNamePtr.value
  arrow.aLength = c_double(length)
  arrow.shaftRadius = c_double(sRadius)
  arrow.lengthTip = c_double(tLength)
  arrow.radiusTip = c_double(tRadius)
  arrow.bidirectional = c_int(bidir)
  arrow.direction = (c_double * 3) (direction[0], direction[1], direction[2])
  arrow.position = (c_double * 3) (position[0], position[1], position[2]) 
  arrow.color = (c_float * 4) (color[0], color[1], color[2], color[3])
  packet = MR.makeMessage(arrow)
  MR.sendMessage(packet)
  enableGraphics(objectName, enabled)
  return packet

def removeObject(objectName):
  name = create_string_buffer(bytes(objectName, 'utf-8'), md.MAX_STRING_LENGTH)
  namePtr = (c_char_p) (addressof(name))

  remove = md.M_REMOVE_OBJECT()
  remove.header.msg_type = c_int(md.REMOVE_OBJECT)
  remove.objectName = namePtr.value
  packet = MR.makeMessage(remove)
  MR.sendMessage(packet)
  return packet
