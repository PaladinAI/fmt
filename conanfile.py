from conans import ConanFile
from conans import tools

class FmtConan(ConanFile):
    name = "fmt"
    version = "4.0.0"
    description = "A modern formatting library."
    url = "https://github.com/fmtlib/fmt"
    license = "MIT"
    exports_sources = "fmt/*"
    no_copy_source = True

    def package(self):
        self.copy("*.h", src="fmt", dst="include/fmt")
        self.copy("*.cc", src="fmt", dst="include/fmt")

    def package_info(self):
        self.info.header_only()
        self.cpp_info.defines = ['FMT_HEADER_ONLY']
