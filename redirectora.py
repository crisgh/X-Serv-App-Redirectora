#! /usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import random

class aleat(webapp.webApp):
    def process(self,parsedRequest):
        numero = random.randint(1 , 99999)
        return("301 Moved Permanently" , "\r\n"
                + "<html><body><h1><a href = '" +str(numero)+"'>Dame otra</h1></body></hmtl>")
if __name__ == "__main__":
    testWebApp = aleat("localhost",2312)
