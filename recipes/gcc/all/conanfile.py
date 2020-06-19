from conans import *

class GccConan(ConanFile):
    name = "gcc"
    description = "The GNU Compiler Collection"
    license = "GPL"
    settings = {"os": ["Linux"], "arch": ["x86_64", "armv8"]}
    build_requires = (
        "generators/1.0.0",
        "autotools/1.0.0",
        "binutils/[>=2.34]",
        "libmpc/[>=1.1.0]",
        "gcc-ada/[>=]",
        "doxygen/[>=1.8.18]",
        "lib32-glibc/[>=]",
        "lib32-gcc-libs/[>=]",
        "python/[>=3.8.3]",
        "git/[>=2.27.0]",
    )

    def source(self):
        tools.get(f"https://sourceware.org/pub/gcc/releases/gcc-{self.version}/gcc-{self.version}.tar.xz")

    def build(self):
        args = [
            "--disable-static",
        ]
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(args=args, configure_dir=f"{self.name}-{self.version}")
        autotools.make()
        autotools.install()
