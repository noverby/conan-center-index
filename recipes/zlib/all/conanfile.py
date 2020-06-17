import conans

class ZlibConan(conans.ConanFile):
    name = "zlib"
    version = conans.tools.get_env("GIT_TAG", "1.2.11")
    license = "Zlib"
    description = "A Massively Spiffy Yet Delicately Unobtrusive Compression Library " "(Also Free, Not to Mention Unencumbered by Patents)"
    settings = "os", "arch", "compiler", "build_type"

    def build_requirements(self):
        self.build_requires("generators/1.0.0@%s/stable" % self.user)
        self.build_requires("autotools/[>=1.0.0]@%s/stable" % self.user)

    def source(self):
        conans.tools.get("https://github.com/madler/zlib/archive/v%s.tar.gz" % self.version)

    def build(self):
        args = ["--enable-shared"]
        autotools = conans.AutoToolsBuildEnvironment(self)
        autotools.configure(args=args, configure_dir="%s-%s" % (self.name, self.version))
        autotools.make()
        autotools.install()
