#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os


class ZMQConan(ConanFile):
    name = "cppzmq"
    version = "4.4.1"
    url = "https://github.com/ulricheck/conan-cppzmq"
    description = "CPP headers for ZeroMQ is a community of projects focused on decentralized messaging and computing"
    license = "https://github.com/someauthor/somelib/blob/master/LICENSES"
    exports_sources = ["LICENSE"]
    no_copy_source = True
    requires = "zmq/4.3.2@camposs/stable"

    def source(self):
        extracted_dir = "cppzmq-%s" % self.version
        archive_name = "%s.tar.gz" % self.version
        source_url = "https://github.com/zeromq/cppzmq/archive/v%s" % (archive_name)
        tools.get(source_url)
        os.rename(extracted_dir, "sources")

    def build(self):
        pass

    def package(self):
        self.copy(pattern="LICENSE", src='sources')
        self.copy(pattern='*.hpp', src='sources', dst='include', keep_path=True)

    def package_id(self):
        self.info.header_only()
