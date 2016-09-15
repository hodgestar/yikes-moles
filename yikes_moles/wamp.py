""" WAMP networking. """

import asyncio
from queue import Queue
from threading import Thread

from autobahn.asyncio.wamp import ApplicationRunner, ApplicationSession
from autobahn.wamp.types import PublishOptions


class WampMoles(object):
    def __init__(self):
        self._thread = None
        self._loop = asyncio.new_event_loop()
        self._loop.add_signal_handler = self._add_signal_handler
        self._queue = Queue()

    def __call__(self):
        asyncio.set_event_loop(self._loop)
        runner = ApplicationRunner(
            url=u"wss://demo.crossbar.io/ws", realm=u"realm1")
        runner.run(MolesComponent)

    def _add_signal_handler(self, *args, **kw):
        raise NotImplementedError("Don't try this in threads or Windows")

    def send(self, msg):
        self._queue.put(msg)

    def join(self):
        if self._thread is not None:
            self._loop.stop()
            self._thread.join()
            self._thread = None

    def start(self):
        self._thread = Thread(target=self)
        self._thread.daemon = True
        self._thread.start()


class MolesComponent(ApplicationSession):
    @asyncio.coroutine
    def onJoin(self, details):
        print("session ready")

        def on_msg(msg):
            print("event received: {0}", msg)

        try:
            yield from self.subscribe(on_msg, u'net.za.hodgestar.moles')
            print("subscribed to topic")
        except Exception as e:
            print("could not subscribe to topic: {0}".format(e))

        counter = 0
        options = PublishOptions(exclude_me=False)
        while True:
            self.publish(
                u'net.za.hodgestar.moles', "msg %d" % counter, options=options)
            counter += 1
            yield from asyncio.sleep(1)
