#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hellotornado.hellotornado import application
from tornado.testing import AsyncHTTPTestCase, gen_test


class HelloWorldTest(AsyncHTTPTestCase):
    def get_app(self):
        return application

    @gen_test
    def test_helloworld(self):
        response = yield self.http_client.fetch(self.get_url('/'))
        self.assertEqual(str(response.body, 'utf-8'), "Hello, world")
