from conans import *
import os


class LlvmConan(ConanFile):
    description = "Compiler toolchain"
    license = "custom"
    settings = {"os": ["Linux"], "arch": ["x86_64", "armv8"]}

    def source(self):
        tools.get(f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{self.version}/llvm-{self.version}.src.tar.xz")

    def build(self):
        cmake = CMake(self, generator="Ninja")
        cmake.definitions["LLVM_BUILD_LLVM_DYLIB"] = True
        cmake.definitions["LLVM_LINK_LLVM_DYLIB"] = True
        cmake.definitions["LLVM_INSTALL_UTILS"] = True
        cmake.definitions["LLVM_ENABLE_RTTI"] = True
        cmake.definitions["LLVM_ENABLE_PROJECTS"] = "lld"
        cmake.configure(source_folder=f"{self.name}-{self.version}.src")
        cmake.build()
        cmake.install()

    def package_info(self):
        self.env_info.LD = os.path.join(self.package_folder, "bin", "lld")
        self.env_info.AS = os.path.join(self.package_folder, "bin", "llvm-as")
        self.env_info.ADDR2LINE = os.path.join(self.package_folder, "bin", "llvm-addr2line")
        self.env_info.AR = os.path.join(self.package_folder, "bin", "llvm-ar")
        self.env_info.NM = os.path.join(self.package_folder, "bin", "llvm-nm")
        self.env_info.OBJCOPY = os.path.join(self.package_folder, "bin", "llvm-objcopy")
        self.env_info.OBJDUMP = os.path.join(self.package_folder, "bin", "llvm-objdump")
        self.env_info.RANLIB = os.path.join(self.package_folder, "bin", "llvm-ranlib")
        self.env_info.READELF = os.path.join(self.package_folder, "bin", "llvm-readelf")
        self.env_info.SIZE = os.path.join(self.package_folder, "bin", "llvm-size")
        self.env_info.STRINGS = os.path.join(self.package_folder, "bin", "llvm-strings")
        self.env_info.STRIP = os.path.join(self.package_folder, "bin", "llvm-strip")
