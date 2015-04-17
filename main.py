#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os.path

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, mainpage")


class PageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", error=None);


def main():
    tornado.options.parse_command_line()
    settings = dict(
        template_path="templates",
        static_path="dist",
    )
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/somewhere", PageHandler),
    ],
        **settings
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
