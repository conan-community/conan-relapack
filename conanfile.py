#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from conans import ConanFile, tools, CMake


class relapackConan(ConanFile):
    name = "relapack"
    version = "1.0"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    description = "Recursive LAPACK Collection"
    url = "https://github.com/conan-community/conan-lapack"
    homepage = "https://github.com/HPAC/ReLAPACK"
    author = "Conan Community"
    topics = ("conan", "relapack", "lapack", "recursive")
    license = "MIT"
    exports = "LICENSE.md"
    exports_sources = "CMakeLists.txt"
    generators = "cmake"
    requires = "lapack/3.7.1@conan/stable"
    deprecated = True
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
        if self.settings.compiler == "Visual Studio":
            self.options["lapack"].visual_studio = True

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        sha256 = "71740aee26a95de9f3226ea1c3d8bd7a9992e718593bb0101f8c772183147719"
        tools.get("%s/archive/v%s.tar.gz" % (self.homepage, self.version), sha256=sha256)
        extracted_dir = "ReLAPACK-%s" % self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_dir=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if self.settings.os == "Linux":
            self.cpp_info.libs.append('m')
