import os
import signal

import tornado.ioloop
import tornado.web

from tornado import httpserver

class JSONHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({'message': 'Hello, World!'})

def sig_handler(sig, frame):
    loop = tornado.ioloop.IOLoop.instance()
    loop.add_callback(shutdown)

def shutdown():
    loop = tornado.ioloop.IOLoop.instance()
    loop.stop()
    if os.path.exists('pid'):
        os.remove('pid')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/json', JSONHandler),
    ])

    with open('pid', 'w') as f:
        f.write(str(os.getpid()))

    server = httpserver.HTTPServer(app)
    server.bind(os.environ.get('PORT'), os.environ.get('HOST'))
    server.start(2)

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    tornado.ioloop.IOLoop.current().start()
