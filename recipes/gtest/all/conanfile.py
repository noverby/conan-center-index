from conans import *

class GtestConan(ConanFile):
    name = "gtest"
    description = "Google Test - C++ testing utility"
    license = "BSD"
    settings = {"os": ["Linux"], "arch": ["x86_64", "armv8"]}
    build_requires = (
        "generators/1.0.0",
        "python/[>=3.8.3]",
        "cmake/[>=3.17.3]",
    )

    def source(self):
        tools.get(f"https://github.com/google/googletest/archive/release-{self.version}.tar.gz")

    def build(self):
        cmake = CMake(self, generators="Ninja")
        cmake.configure(source_folder=f"{self.name}-{self.version}")
        cmake.build()
        cmake.install()
