from spack import *

class Trivial(Package):
    """Description"""

    homepage = "http://www.example.com"

    version('git', git='https://github.com/DavidPoliakoff/trivial.git', branch='master')

    def install(self, spec, prefix):
        cmake('.',*std_cmake_args)
        make()
        make("install")

