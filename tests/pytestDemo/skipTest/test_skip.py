# Skip the Test Based on Some Condition

# We can have test cases only for Mac and Windows
# test_1 -> Mac
# test_2 -> Win

import pytest
import sys

# sys.platform can have for different operating systems:
# 'linux': Linux Operating System
# 'linux2': Older alias for Linux (not used anymore in recent Python Versions)
# 'darwin': macOS (Mac OS X) operating system
# 'win32': Windows Operating System (32-bit or 64-bit)
# 'cygwin': Cygwin environment on Windows
# 'freebsd7', 'freebsd8', 'freebsd9'...: Various Versions of FreeBSD
# 'sunos5': Solaris Operating System

@pytest.mark.skipif(sys.platform == "win32", reason="Not Supported Win")
def test_mac():
    print("Mac Only")


@pytest.mark.skipif(sys.platform == "darwin", reason="Not Supported Mac")
def test_win():
    print("Win Only")