from conans import *

class GzipConan(ConanFile):
    name = "gzip"
    description = "GNU compression utility"
    license = "GPL3"
    settings = {"os": ["Linux"], "arch": ["x86_64", "armv8"]}
    build_requires = (
        "generators/1.0.0",
        "autotools/1.0.0",
    )

    def source(self):
        tools.get(f"https://ftp.gnu.org/pub/gnu/gzip/gzip-{self.version}.tar.xz")

    def build(self):
        args = [
            "--disable-static",
        ]
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(args=args, configure_dir=f"{self.name}-{self.version}")
        autotools.make()
        autotools.install()
