from conans import ConanFile, tools, AutoToolsBuildEnvironment
import os


class lapackConan(ConanFile):
    name = "relapack"
    version = "1.0"
    url = "https://github.com/HPAC/ReLAPACK"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    requires = "lapack/3.7.1@danimtb/testing"

    def source(self):
        source_url = ("%s/archive/v%s.zip" % (self.url, self.version))
        tools.get(source_url)
        os.rename("%s-%s" % (self.name, self.version), "sources")

    def build(self):
        with tools.chdir("sources"):
            env_build = AutoToolsBuildEnvironment(self)
            env_build.make()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src="sources", ignore_case=True, keep_path=False)
        self.copy(pattern="*.h", dst="include", src="sources/inc", keep_path=False)
        self.copy(pattern="*relapack*.dll", dst="bin", src="bin", keep_path=False)
        self.copy(pattern="*relapack*.so*", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*relapack*.dylib", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*relapack*.lib", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*relapack*.a", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*relapack*.a", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["relapack"]
