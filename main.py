#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class MainPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", error=None);

class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("contact.html", error=None);

class PlaceHandler(tornado.web.RequestHandler):
    def get(self, pathname):
        self.write(pathname)

def main():
    tornado.options.parse_command_line()
    settings = dict(
        template_path="templates",
        static_path="dist",
    )
    application = tornado.web.Application([
        (r"/", MainPageHandler),
        (r"/contact", ContactHandler),
        (r"/(.*)", PlaceHandler),
    ],
        **settings
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
