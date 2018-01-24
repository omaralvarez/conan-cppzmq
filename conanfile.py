from conans import ConanFile


class CPPZMQConan(ConanFile):
    name = "cppzmq"
    version = "4.2.2"
    url = "https://github.com/omaralvarez/conan-cppzmq"
    requires = "zmq/4.2.2@bincrafters/stable"
    source_dir = "cppzmq"
    license = "GPLv3"
    description = """Simple C++ wrapper to libzmq, from https://github.com/zeromq/cppzmq
    """

    def source(self):
        self.run_command("git clone https://github.com/zeromq/cppzmq.git")
        self.run_command("git checkout -b %s.x" % (self.version), self.source_dir)

    def run_command(self, cmd, cwd=None):
        self.output.info(cmd)
        self.run(cmd, True, cwd)

    def package(self):
        self.copy("*.hpp", dst="include", src="%s" % self.source_dir)

    def package_info(self):
        self.cpp_info.libdirs = []