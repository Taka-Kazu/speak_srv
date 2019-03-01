#!/usr/bin/env python
#! coding:utf-8

import rospy
from subprocess import call
from speak_srv.srv import Speak as SpeakSrv
from speak_srv.srv import SpeakResponse as SpeakSrvResponse

class Speaker:
  def __init__(self):
    self.cmd = "espeak"
    self.voice = "en+f4"
    self.pitch = "80"
    self.speed = "150"
    self.k = "20"

  def speak(self, sentence):
    call([self.cmd, "-v", self.voice, "-p", self.pitch, "-s", self.speed, "-k", self.k, sentence])

class SpeakServer:
  def __init__(self):
    rospy.init_node("speak_server")
    self.speaker = Speaker()
    srv = rospy.Service('speak', SpeakSrv, self.speak_server)
    print "===speak_server==="
    rospy.spin()

  def speak_server(self, request):
    print "Requested sentence : " + request.str
    self.speaker.speak(request.str)
    res = SpeakSrvResponse()
    res.str = request.str
    return res

if __name__=="__main__":
  ss = SpeakServer()

