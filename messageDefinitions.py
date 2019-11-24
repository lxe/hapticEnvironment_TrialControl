'''Wrapper for messageDefinitions.h

Generated with:
ctypesgen.py --cpp=clang -E -a -o ../../RNEL_GIT/haptic_environment_task_control/messageDefinitions.py ../../RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=float("inf")):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=float("inf")):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=float("inf")):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=float("inf")):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=float("inf")):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=float("inf")):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=float("inf")):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError(e):
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        unix_lib_dirs_list = ['/lib', '/usr/lib', '/lib64', '/usr/lib64']
        if sys.platform.startswith('linux'):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            bitage = platform.architecture()[0]
            if bitage.startswith('32'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/i386-linux-gnu', '/usr/lib/i386-linux-gnu']
            elif bitage.startswith('64'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/x86_64-linux-gnu', '/usr/lib/x86_64-linux-gnu']
            else:
                # guess...
                unix_lib_dirs_list += glob.glob('/lib/*linux-gnu')
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# No libraries

# No modules

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 68
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    'serial_no',
    'msg_type',
    'reserved',
    'timestamp',
]
struct_anon_1._fields_ = [
    ('serial_no', c_int),
    ('msg_type', c_int),
    ('reserved', c_double),
    ('timestamp', c_double),
]

MSG_HEADER = struct_anon_1 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 68

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 77
class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    'header',
    'a',
    'b',
]
struct_anon_2._fields_ = [
    ('header', MSG_HEADER),
    ('a', c_int),
    ('b', c_int),
]

M_TEST_PACKET = struct_anon_2 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 77

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 81
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'header',
]
struct_anon_3._fields_ = [
    ('header', MSG_HEADER),
]

M_SESSION_START = struct_anon_3 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 81

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 85
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'header',
]
struct_anon_4._fields_ = [
    ('header', MSG_HEADER),
]

M_SESSION_END = struct_anon_4 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 85

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 90
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    'header',
    'trialNum',
]
struct_anon_5._fields_ = [
    ('header', MSG_HEADER),
    ('trialNum', c_int),
]

M_TRIAL_START = struct_anon_5 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 90

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 94
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'header',
]
struct_anon_6._fields_ = [
    ('header', MSG_HEADER),
]

M_TRIAL_END = struct_anon_6 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 94

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 99
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'header',
    'filename',
]
struct_anon_7._fields_ = [
    ('header', MSG_HEADER),
    ('filename', c_char * 128),
]

M_START_RECORDING = struct_anon_7 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 99

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 103
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'header',
]
struct_anon_8._fields_ = [
    ('header', MSG_HEADER),
]

M_STOP_RECORDING = struct_anon_8 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 103

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 108
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'header',
    'objectName',
]
struct_anon_9._fields_ = [
    ('header', MSG_HEADER),
    ('objectName', c_char * 128),
]

M_REMOVE_OBJECT = struct_anon_9 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 108

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 113
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'header',
    'keyname',
]
struct_anon_10._fields_ = [
    ('header', MSG_HEADER),
    ('keyname', c_char * 128),
]

M_KEYPRESS = struct_anon_10 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 113

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 117
class struct_anon_11(Structure):
    pass

struct_anon_11.__slots__ = [
    'header',
]
struct_anon_11._fields_ = [
    ('header', MSG_HEADER),
]

M_PAUSE_RECORDING = struct_anon_11 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 117

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 121
class struct_anon_12(Structure):
    pass

struct_anon_12.__slots__ = [
    'header',
]
struct_anon_12._fields_ = [
    ('header', MSG_HEADER),
]

M_RESUME_RECORDING = struct_anon_12 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 121

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 125
class struct_anon_13(Structure):
    pass

struct_anon_13.__slots__ = [
    'header',
]
struct_anon_13._fields_ = [
    ('header', MSG_HEADER),
]

M_RESET_WORLD = struct_anon_13 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 125

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 134
class struct_anon_14(Structure):
    pass

struct_anon_14.__slots__ = [
    'header',
    'cstName',
    'lambdaVal',
    'forceMagnitude',
    'visionEnabled',
    'hapticEnabled',
]
struct_anon_14._fields_ = [
    ('header', MSG_HEADER),
    ('cstName', c_char * 128),
    ('lambdaVal', c_double),
    ('forceMagnitude', c_double),
    ('visionEnabled', c_int),
    ('hapticEnabled', c_int),
]

M_CST_CREATE = struct_anon_14 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 134

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 139
class struct_anon_15(Structure):
    pass

struct_anon_15.__slots__ = [
    'header',
    'cstName',
]
struct_anon_15._fields_ = [
    ('header', MSG_HEADER),
    ('cstName', c_char * 128),
]

M_CST_DESTRUCT = struct_anon_15 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 139

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 144
class struct_anon_16(Structure):
    pass

struct_anon_16.__slots__ = [
    'header',
    'cstName',
]
struct_anon_16._fields_ = [
    ('header', MSG_HEADER),
    ('cstName', c_char * 128),
]

M_CST_START = struct_anon_16 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 144

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 149
class struct_anon_17(Structure):
    pass

struct_anon_17.__slots__ = [
    'header',
    'cstName',
]
struct_anon_17._fields_ = [
    ('header', MSG_HEADER),
    ('cstName', c_char * 128),
]

M_CST_STOP = struct_anon_17 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 149

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 155
class struct_anon_18(Structure):
    pass

struct_anon_18.__slots__ = [
    'header',
    'cstName',
    'visionEnabled',
]
struct_anon_18._fields_ = [
    ('header', MSG_HEADER),
    ('cstName', c_char * 128),
    ('visionEnabled', c_int),
]

M_CST_SET_VISUAL = struct_anon_18 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 155

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 161
class struct_anon_19(Structure):
    pass

struct_anon_19.__slots__ = [
    'header',
    'cstName',
    'hapticEnabled',
]
struct_anon_19._fields_ = [
    ('header', MSG_HEADER),
    ('cstName', c_char * 128),
    ('hapticEnabled', c_int),
]

M_CST_SET_HAPTIC = struct_anon_19 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 161

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 167
class struct_anon_20(Structure):
    pass

struct_anon_20.__slots__ = [
    'header',
    'cstName',
    'lambdaVal',
]
struct_anon_20._fields_ = [
    ('header', MSG_HEADER),
    ('cstName', c_char * 128),
    ('lambdaVal', c_double),
]

M_CST_SET_LAMBDA = struct_anon_20 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 167

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 174
class struct_anon_21(Structure):
    pass

struct_anon_21.__slots__ = [
    'header',
    'cursorX',
    'cursorY',
    'cursorZ',
]
struct_anon_21._fields_ = [
    ('header', MSG_HEADER),
    ('cursorX', c_double),
    ('cursorY', c_double),
    ('cursorZ', c_double),
]

M_CST_DATA = struct_anon_21 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 174

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 183
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'header',
    'cupsName',
    'escapeAngle',
    'pendulumLength',
    'ballMass',
    'cartMass',
]
struct_anon_22._fields_ = [
    ('header', MSG_HEADER),
    ('cupsName', c_char * 128),
    ('escapeAngle', c_double),
    ('pendulumLength', c_double),
    ('ballMass', c_double),
    ('cartMass', c_double),
]

M_CUPS_CREATE = struct_anon_22 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 183

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 188
class struct_anon_23(Structure):
    pass

struct_anon_23.__slots__ = [
    'header',
    'cupsName',
]
struct_anon_23._fields_ = [
    ('header', MSG_HEADER),
    ('cupsName', c_char * 128),
]

M_CUPS_DESTRUCT = struct_anon_23 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 188

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 193
class struct_anon_24(Structure):
    pass

struct_anon_24.__slots__ = [
    'header',
    'cupsName',
]
struct_anon_24._fields_ = [
    ('header', MSG_HEADER),
    ('cupsName', c_char * 128),
]

M_CUPS_START = struct_anon_24 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 193

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 198
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'header',
    'cupsName',
]
struct_anon_25._fields_ = [
    ('header', MSG_HEADER),
    ('cupsName', c_char * 128),
]

M_CUPS_STOP = struct_anon_25 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 198

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 204
class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'header',
    'ballPos',
    'cartPos',
]
struct_anon_26._fields_ = [
    ('header', MSG_HEADER),
    ('ballPos', c_double),
    ('cartPos', c_double),
]

M_CUPS_DATA = struct_anon_26 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 204

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 218
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'header',
    'posX',
    'posY',
    'posZ',
    'velX',
    'velY',
    'velZ',
    'forceX',
    'forceY',
    'forceZ',
    'collisions',
]
struct_anon_27._fields_ = [
    ('header', MSG_HEADER),
    ('posX', c_double),
    ('posY', c_double),
    ('posZ', c_double),
    ('velX', c_double),
    ('velY', c_double),
    ('velZ', c_double),
    ('forceX', c_double),
    ('forceY', c_double),
    ('forceZ', c_double),
    ('collisions', (c_char * 128) * 4),
]

M_HAPTIC_DATA_STREAM = struct_anon_27 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 218

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 224
class struct_anon_28(Structure):
    pass

struct_anon_28.__slots__ = [
    'header',
    'objectName',
    'enabled',
]
struct_anon_28._fields_ = [
    ('header', MSG_HEADER),
    ('objectName', c_char * 128),
    ('enabled', c_int),
]

M_HAPTICS_SET_ENABLED = struct_anon_28 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 224

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 230
class struct_anon_29(Structure):
    pass

struct_anon_29.__slots__ = [
    'header',
    'effectName',
    'enabled',
]
struct_anon_29._fields_ = [
    ('header', MSG_HEADER),
    ('effectName', c_char * 128),
    ('enabled', c_int),
]

M_HAPTICS_SET_ENABLED_WORLD = struct_anon_29 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 230

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 236
class struct_anon_30(Structure):
    pass

struct_anon_30.__slots__ = [
    'header',
    'objectName',
    'stiffness',
]
struct_anon_30._fields_ = [
    ('header', MSG_HEADER),
    ('objectName', c_char * 128),
    ('stiffness', c_double),
]

M_HAPTICS_SET_STIFFNESS = struct_anon_30 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 236

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 242
class struct_anon_31(Structure):
    pass

struct_anon_31.__slots__ = [
    'header',
    'bWidth',
    'bHeight',
]
struct_anon_31._fields_ = [
    ('header', MSG_HEADER),
    ('bWidth', c_double),
    ('bHeight', c_double),
]

M_HAPTICS_BOUNDING_PLANE = struct_anon_31 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 242

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 249
class struct_anon_32(Structure):
    pass

struct_anon_32.__slots__ = [
    'header',
    'effectName',
    'direction',
    'magnitude',
]
struct_anon_32._fields_ = [
    ('header', MSG_HEADER),
    ('effectName', c_char * 128),
    ('direction', c_double),
    ('magnitude', c_double),
]

M_HAPTICS_CONSTANT_FORCE_FIELD = struct_anon_32 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 249

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 255
class struct_anon_33(Structure):
    pass

struct_anon_33.__slots__ = [
    'header',
    'effectName',
    'viscosityMatrix',
]
struct_anon_33._fields_ = [
    ('header', MSG_HEADER),
    ('effectName', c_char * 128),
    ('viscosityMatrix', c_double * 9),
]

M_HAPTICS_VISCOSITY_FIELD = struct_anon_33 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 255

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 260
class struct_anon_34(Structure):
    pass

struct_anon_34.__slots__ = [
    'header',
    'effectName',
]
struct_anon_34._fields_ = [
    ('header', MSG_HEADER),
    ('effectName', c_char * 128),
]

M_HAPTICS_FREEZE_EFFECT = struct_anon_34 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 260

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 265
class struct_anon_35(Structure):
    pass

struct_anon_35.__slots__ = [
    'header',
    'effectName',
]
struct_anon_35._fields_ = [
    ('header', MSG_HEADER),
    ('effectName', c_char * 128),
]

M_HAPTICS_REMOVE_WORLD_EFFECT = struct_anon_35 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 265

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 271
class struct_anon_36(Structure):
    pass

struct_anon_36.__slots__ = [
    'header',
    'objectName',
    'enabled',
]
struct_anon_36._fields_ = [
    ('header', MSG_HEADER),
    ('objectName', c_char * 128),
    ('enabled', c_int),
]

M_GRAPHICS_SET_ENABLED = struct_anon_36 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 271

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 276
class struct_anon_37(Structure):
    pass

struct_anon_37.__slots__ = [
    'header',
    'color',
]
struct_anon_37._fields_ = [
    ('header', MSG_HEADER),
    ('color', c_float * 4),
]

M_GRAPHICS_CHANGE_BG_COLOR = struct_anon_37 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 276

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 289
class struct_anon_38(Structure):
    pass

struct_anon_38.__slots__ = [
    'header',
    'objectName',
    'height',
    'innerRadius',
    'outerRadius',
    'numSides',
    'numHeightSegments',
    'position',
    'rotation',
    'color',
]
struct_anon_38._fields_ = [
    ('header', MSG_HEADER),
    ('objectName', c_char * 128),
    ('height', c_double),
    ('innerRadius', c_double),
    ('outerRadius', c_double),
    ('numSides', c_uint),
    ('numHeightSegments', c_uint),
    ('position', c_double * 3),
    ('rotation', c_double * 9),
    ('color', c_float * 4),
]

M_GRAPHICS_PIPE = struct_anon_38 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 289

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 303
class struct_anon_39(Structure):
    pass

struct_anon_39.__slots__ = [
    'header',
    'objectName',
    'aLength',
    'shaftRadius',
    'lengthTip',
    'radiusTip',
    'bidirectional',
    'numSides',
    'direction',
    'position',
    'color',
]
struct_anon_39._fields_ = [
    ('header', MSG_HEADER),
    ('objectName', c_char * 128),
    ('aLength', c_double),
    ('shaftRadius', c_double),
    ('lengthTip', c_double),
    ('radiusTip', c_double),
    ('bidirectional', c_int),
    ('numSides', c_uint),
    ('direction', c_double * 3),
    ('position', c_double * 3),
    ('color', c_float * 4),
]

M_GRAPHICS_ARROW = struct_anon_39 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 303

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 309
class struct_anon_40(Structure):
    pass

struct_anon_40.__slots__ = [
    'header',
    'objectName',
    'color',
]
struct_anon_40._fields_ = [
    ('header', MSG_HEADER),
    ('objectName', c_char * 128),
    ('color', c_float * 4),
]

M_GRAPHICS_CHANGE_OBJECT_COLOR = struct_anon_40 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 309

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 318
class struct_anon_41(Structure):
    pass

struct_anon_41.__slots__ = [
    'header',
    'objectName',
    'numDots',
    'coherence',
    'direction',
    'magnitude',
]
struct_anon_41._fields_ = [
    ('header', MSG_HEADER),
    ('objectName', c_char * 128),
    ('numDots', c_int),
    ('coherence', c_double),
    ('direction', c_double),
    ('magnitude', c_double),
]

M_GRAPHICS_MOVING_DOTS = struct_anon_41 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 318

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 328
class struct_anon_42(Structure):
    pass

struct_anon_42.__slots__ = [
    'header',
    'objectName',
    'sizeX',
    'sizeY',
    'sizeZ',
    'localPosition',
    'color',
]
struct_anon_42._fields_ = [
    ('header', MSG_HEADER),
    ('objectName', c_char * 128),
    ('sizeX', c_double),
    ('sizeY', c_double),
    ('sizeZ', c_double),
    ('localPosition', c_double * 3),
    ('color', c_float * 4),
]

M_GRAPHICS_SHAPE_BOX = struct_anon_42 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 328

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 336
class struct_anon_43(Structure):
    pass

struct_anon_43.__slots__ = [
    'header',
    'objectName',
    'radius',
    'localPosition',
    'color',
]
struct_anon_43._fields_ = [
    ('header', MSG_HEADER),
    ('objectName', c_char * 128),
    ('radius', c_double),
    ('localPosition', c_double * 3),
    ('color', c_float * 4),
]

M_GRAPHICS_SHAPE_SPHERE = struct_anon_43 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 336

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 345
class struct_anon_44(Structure):
    pass

struct_anon_44.__slots__ = [
    'header',
    'objectName',
    'innerRadius',
    'outerRadius',
    'localPosition',
    'color',
]
struct_anon_44._fields_ = [
    ('header', MSG_HEADER),
    ('objectName', c_char * 128),
    ('innerRadius', c_double),
    ('outerRadius', c_double),
    ('localPosition', c_double * 3),
    ('color', c_float * 4),
]

M_GRAPHICS_SHAPE_TORUS = struct_anon_44 # /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 345

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 1
try:
    DEFAULT_IP = 'localhost:10000'
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 2
try:
    MAX_PACKET_LENGTH = 8192
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 3
try:
    MAX_STRING_LENGTH = 128
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 6
try:
    TEST_PACKET = 9000
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 10
try:
    SESSION_START = 1
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 11
try:
    SESSION_END = 2
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 12
try:
    TRIAL_START = 3
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 13
try:
    TRIAL_END = 4
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 14
try:
    START_RECORDING = 5
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 15
try:
    STOP_RECORDING = 6
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 16
try:
    REMOVE_OBJECT = 7
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 17
try:
    KEYPRESS = 8
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 18
try:
    PAUSE_RECORDING = 9
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 19
try:
    RESUME_RECORDING = 10
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 20
try:
    RESET_WORLD = 11
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 23
try:
    CST_CREATE = 500
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 24
try:
    CST_DESTRUCT = 501
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 25
try:
    CST_START = 502
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 26
try:
    CST_STOP = 503
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 27
try:
    CST_SET_VISUAL = 504
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 28
try:
    CST_SET_HAPTIC = 505
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 29
try:
    CST_SET_LAMBDA = 506
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 30
try:
    CST_DATA = 507
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 31
try:
    CUPS_CREATE = 508
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 32
try:
    CUPS_DESTRUCT = 509
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 33
try:
    CUPS_START = 510
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 34
try:
    CUPS_STOP = 511
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 35
try:
    CUPS_DATA = 512
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 38
try:
    HAPTIC_DATA_STREAM = 1000
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 39
try:
    HAPTICS_SET_ENABLED = 1001
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 40
try:
    HAPTICS_SET_ENABLED_WORLD = 1002
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 41
try:
    HAPTICS_SET_STIFFNESS = 1008
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 42
try:
    HAPTICS_BOUNDING_PLANE = 1009
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 43
try:
    HAPTICS_CONSTANT_FORCE_FIELD = 1010
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 44
try:
    HAPTICS_VISCOSITY_FIELD = 1011
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 45
try:
    HAPTICS_FREEZE_EFFECT = 1012
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 46
try:
    HAPTICS_REMOVE_WORLD_EFFECT = 1013
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 49
try:
    GRAPHICS_SET_ENABLED = 2000
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 50
try:
    GRAPHICS_CHANGE_BG_COLOR = 2001
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 51
try:
    GRAPHICS_PIPE = 2002
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 52
try:
    GRAPHICS_ARROW = 2003
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 53
try:
    GRAPHICS_CHANGE_OBJECT_COLOR = 2004
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 54
try:
    GRAPHICS_MOVING_DOTS = 2014
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 55
try:
    GRAPHICS_SHAPE_BOX = 2046
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 56
try:
    GRAPHICS_SHAPE_SPHERE = 2050
except:
    pass

# /home/mfl24/Documents/RNEL_GIT/haptic_environment_robot_control/common/messageDefinitions.h: 57
try:
    GRAPHICS_SHAPE_TORUS = 2051
except:
    pass

# No inserted files

