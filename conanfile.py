import os
from conans import ConanFile, tools, AutoToolsBuildEnvironment


class relapackConan(ConanFile):
    name = "relapack"
    version = "1.0"
    url = "https://github.com/HPAC/ReLAPACK"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    requires = "lapack/3.7.1@conan/stable"

    @property
    def source_subfolder(self):
        return "sources"

    def config_options(self):
        if self.settings.compiler == "Visual Studio":
            self.options["lapack"].visual_studio = True

    def source(self):
        source_url = ("%s/archive/v%s.zip" % (self.url, self.version))
        tools.get(source_url)
        os.rename("%s-%s" % (self.name, self.version), self.source_subfolder)

    def build(self):
        with tools.chdir(self.source_subfolder):
            autotools = AutoToolsBuildEnvironment(self)
            make = tools.get_env("CONAN_MAKE_PROGRAM", "make")
            if tools.which("mingw32-make"):
                make = "mingw32-make"
            autotools.make(make_program=make)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder, keep_path=False)
        self.copy(pattern="*.h", dst="include", src="%s/inc" % self.source_subfolder, keep_path=False)
        self.copy(pattern="*relapack*.dll", dst="bin", src="bin", keep_path=False)
        self.copy(pattern="*relapack*.so*", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*relapack*.dylib", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*relapack*.lib", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*relapack*.a", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*relapack*.a", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
