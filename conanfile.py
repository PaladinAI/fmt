from conans import ConanFile
from conans import tools

class FmtConan(ConanFile):
    name = "fmt"
    version = "5.2.1"
    description = "A modern formatting library."
    url = "https://github.com/fmtlib/fmt"
    license = "MIT"
    exports_sources = "include/fmt/*", "src/*", "LICENSE.txt"

    def build(self):
        pass

    def package(self):
        self.copy("*.h", src="include/fmt", dst="include/fmt")
        self.copy("*.cc", src="src", dst="include/fmt")

    def package_info(self):
        self.info.header_only()
        self.cpp_info.defines = ['FMT_HEADER_ONLY']
