# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 11:19:25 2018

@author: laoer123
"""

#!/usr/bin/python

import **.**.**.**loop

import tornado.web



class MainHandler(tornado.web.RequestHandler):

	def get(self):

		self.write("Hello, world")



if __name__ == "__main__":

	setting = {

		"debug": True,

		"static_path": "/Users/phithon/pro/python/wooyun/tornado-file-read/static/",

	}



	application = tornado.web.Application([

		(r"/", MainHandler),

	], **setting)

	application.listen(8888)

	**.**.**.**loop.IOLoop.instance().start()