import glob
import sys

sys.path.append('../git_submodules/doit_helpers')
from doit_helpers.arduino import env2

DOIT_CONFIG = {'default_tasks': ['build']}

# ---------------------------------------------------------------------
# Build settings

PROJECT_NAME = 'due_mpu9150'

PROJECT_ROOT = '..'

BUILD_DIR = 'build'

ARDUINO_ROOT = 'D:/programs_win/arduino-1.5.2'

INCLUDE_DIRS = [
    PROJECT_ROOT + '/libraries/CalLib',
    PROJECT_ROOT + '/libraries/DueFlash',
    PROJECT_ROOT + '/libraries/I2CDev',
    PROJECT_ROOT + '/libraries/MotionDriver',
    PROJECT_ROOT + '/libraries/MPU9150Lib',
    ARDUINO_ROOT + '/hardware/arduino/sam/libraries/Wire'
]

CPP_SOURCES = ['Due9150.ino']
CPP_SOURCES += glob.glob(PROJECT_ROOT + '/libraries/**/*.cpp')
CPP_SOURCES += [ARDUINO_ROOT + '/hardware/arduino/sam/libraries/Wire/Wire.cpp']

ARDUINO_HARDWARE = 'Due'
SERIAL_PORT = 'COM8'

ARDUINO_ENV = env2.ArduinoEnv(
    PROJECT_NAME, BUILD_DIR, ARDUINO_ROOT, ARDUINO_HARDWARE)

ARDUINO_ENV.set_cpp_source_files(CPP_SOURCES)
ARDUINO_ENV.add_include_dirs(INCLUDE_DIRS)
ARDUINO_ENV.set_serial_port(SERIAL_PORT)


# ---------------------------------------------------------------------
# utilities

def print_info():
    print ARDUINO_ENV.arduino_core_env


# ---------------------------------------------------------------------
# tasks

def task_info():
    """ Print info about the user build system """
    return {
        'actions': [print_info],
        'targets': ['print info'],
        'verbosity': 2
    }


def task_build():
    for task in ARDUINO_ENV.get_build_tasks():
        yield task


def task_upload():
    for task in ARDUINO_ENV.get_upload_tasks():
        yield task
