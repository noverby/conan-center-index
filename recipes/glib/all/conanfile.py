from conans import *

class GlibConan(ConanFile):
    name = "glib"
    description = "Common C routines used by Gtk+ and other libs"
    license = "LGPL"
    settings = {"os": ["Linux"], "arch": ["x86_64", "armv8"]}
    build_requires = (
        "generators/1.0.0",
        "autotools/1.0.0",
    )
    requires = (
        "glibc/[>=2.31]",
        "sh/[>=]",
    )

    def source(self):
        tools.get(f"ftp://ftp.gnome.org/pub/gnome/sources/glib/1.2/glib-{self.version}.tar.gz")

    def build(self):
        args = [
            "--disable-static",
        ]
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(args=args, configure_dir=f"{self.name}-{self.version}")
        autotools.make()
        autotools.install()
