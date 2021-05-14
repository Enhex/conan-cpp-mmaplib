from conans import ConanFile, tools
import os


class CppmmaplibConan(ConanFile):
	name = "cpp-mmaplib"
	version = "master"
	license = "MIT"
	url = ""
	description = "C++11 header-only memory mapped file library."
	# No settings/options are necessary, this is header only

	def source(self):
		self.run("git clone --depth 1 https://github.com/Enhex/cpp-mmaplib.git .")

	def package(self):
		self.copy("*.h", src='./', dst='include')
