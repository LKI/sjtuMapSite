#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import sqlite3 as s

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

def db_exec(sql, value):
    cx = s.connect("sqlite.db")
    cu = cx.cursor()
    cu.execute(sql, value)
    return cu.fetchone()

class MainPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html");

class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("contact.html");

class RandomHandler(tornado.web.RequestHandler):
    def get(self):
        random_sql = "select url, name from place order by RANDOM() limit 1"
        name = db_exec(random_sql, [])
        self.render("place.html", path=name[0], name=name[1])

class PlaceHandler(tornado.web.RequestHandler):
    def get(self, pathname):
        select_sql = "select name from place where url = ?"
        name = db_exec(select_sql, [pathname])
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
        (r"/random", RandomHandler),
        (r"/(.*)", PlaceHandler),
    ],
        **settings
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
