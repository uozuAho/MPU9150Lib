import glob
import sys

sys.path.append('../git_submodules/doit_helpers')
from doit_helpers.arduino import env2

# DOIT_CONFIG = {'default_tasks': ['build_exe']}

# ---------------------------------------------------------------------
# Build settings

PROJECT_NAME = 'due_mpu9150'

PROJECT_ROOT = '..'

BUILD_DIR = 'build'

INCLUDE_DIRS = [
    PROJECT_ROOT + '/libraries/CalLib',
    PROJECT_ROOT + '/libraries/DueFlash',
    PROJECT_ROOT + '/libraries/I2CDev',
    PROJECT_ROOT + '/libraries/MotionDriver',
    PROJECT_ROOT + '/libraries/MPU9150Lib',
]

CPP_SOURCES = ['Due9150.ino']
CPP_SOURCES += glob.glob(PROJECT_ROOT + '/libraries/**/*.cpp')

ARDUINO_ROOT = 'D:/programs_win/arduino-1.5.2'

ARDUINO_HARDWARE = 'Due'

ARDUINO_ENV = env2.ArduinoEnv(
    PROJECT_NAME, BUILD_DIR, ARDUINO_ROOT, ARDUINO_HARDWARE)

ARDUINO_ENV.set_cpp_source_files(CPP_SOURCES)
ARDUINO_ENV.set_include_dirs(INCLUDE_DIRS)

SERIAL_PORT = 'COM8'


# ---------------------------------------------------------------------
# tasks

def task_build():
    for task in ARDUINO_ENV.get_build_tasks():
        yield task


def task_upload():
    for task in ARDUINO_ENV.get_upload_tasks(SERIAL_PORT):
        yield task
