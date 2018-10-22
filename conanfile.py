from conans import ConanFile, CMake, tools

class ArghConan(ConanFile):
    name = "argh"
    version = "1.2.1"
    url = "https://github.com/adishavit/argh"
    description = "Argh! A minimalist argument handler."
    license = "BSD 3-Clause"
    exports = ["LICENSE"]

    def source(self):
        self.run("git clone --depth 1 --branch v1.2.1 https://github.com/adishavit/argh.git")
        self.run("cd argh")

    def package(self):
        self.copy("argh.h", dst="include", src="argh")
