import os

from conans import ConanFile, Meson, tools


class GLibConan(ConanFile):
    description = "GLib provides the core application building blocks for libraries and applications written in C"
    license = "LGPL-2.1"
    settings = "os", "arch", "compiler", "build_type"

    def build_requirements(self):
        self.build_requires("generators/1.0.0@%s/stable" % self.user)
        self.build_requires("meson/[>=0.51.2]@%s/stable" % self.user)

    def requirements(self):
        self.requires("zlib/[>=1.2.11]@%s/stable" % self.user)
        self.requires("libffi/[>=3.3]@%s/stable" % self.user)

    def source(self):
        tools.get("https://github.com/GNOME/glib/archive/%s.tar.gz" % self.version)
        # Disable broken gio tests until fixed by upstream (https://gitlab.gnome.org/GNOME/glib/issues/1897)
        # Use tools.replace_in_file()
        self.run("sed %s-%s/gio/meson.build -i -e 's/build_tests = .*/build_tests = false/'" % (self.name, self.version))

    def build(self):
        args = [
            "--auto-features=disabled",
            "-Dman=False",
            "-Dgtk_doc=False",
            "-Dlibmount=False",
            "-Dinternal_pcre=False",
        ]
        meson = Meson(self)
        meson.configure(source_folder="%s-%s" % (self.name, self.version), args=args, pkg_config_paths=os.environ["PKG_CONFIG_PATH"].split(":"))
        meson.install()