#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
import echo

# Your test case class goes here


class TestEcho(unittest.TestCase):

    def setUp(self):
        self.parser = echo.create_parser()

    def test_parser(self):
        args = ["--lower", "--upper", "--title", "HELLO"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        self.assertTrue(ns.upper)
        self.assertTrue(ns.title)
        self.assertTrue(ns.text)
        self.assertEquals(echo.main(args), "Hello")

    def test_lower(self):
        args = ["--lower", 'HELLO']
        self.assertEquals(echo.main(args), 'hello')

    def test_upper(self):
        args = ["--upper", 'hello']
        self.assertEquals(echo.main(args), 'HELLO')

    def test_title(self):
        args = ["--title", 'hello']
        self.assertEquals(echo.main(args), 'Hello')

    def test_help_output(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)


if __name__ == '__main__':
    unittest.main()
