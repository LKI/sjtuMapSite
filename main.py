#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import sqlite3 as s

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class MainPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html");

class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("contact.html");

class PlaceHandler(tornado.web.RequestHandler):
    def get(self, pathname):
        cx = s.connect("sqlite.db")
        cu = cx.cursor()
        select_sql = "select name from place where url = ?"
        cu.execute(select_sql, [pathname])
        name = cu.fetchone()
        if name:
            self.render("place.html", path=pathname, name=name[0])
        else:
            self.render("place.html", path=pathname, name="无页面")

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
