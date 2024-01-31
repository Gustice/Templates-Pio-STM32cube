# Project Template for STM32 based PlatformIO projects

## Install required tools

The most convenient way to develop CubeMX based project on Platform IO is to use
the [STM32PIO utility](https://github.com/ussserrr/stm32pio) referred from [Platform IO documentation](https://docs.platformio.org/en/latest/frameworks/stm32cube.html#id5)

The following listing shows the necessary steps for the very first run.

```sh
# install stm32pio package
pip install stm32pio

# Run init to create the ini file
stm32pio init
# adapt include_dir and src_dir to match pio standard

# Run patch to update pio-ini file
stm32pio patch

# Run generate to create project sources according to ioc-file
stm32pio generate

# run validate in case you run into problems
stm32pio validate
# this may pinpoint the problem
```

## Use freeRTOS from Platform IO config

Platform IO doesn't use the package internal freeRTOS sources for some reason.

There are two approaches to still be able to compile freeRTOS drivern projects. 

### Explicitly include freeRTOS sources

Open your IOC-file with STM32CubeMX and generate a makefile based project from it.
Place the middleware sources in `Src` directory and add some compiler commands.

```txt
Project
  + Inc
    - ...
  + Src
    + FreeRTOS
    | + Source
    | | ...
    | | ...
    | - main.c
      - ...
```

```ini
[env:bluepill_f103c8]
platform = ststm32
... 
build_flags =
    -I src/FreeRTOS/Source/CMSIS_RTOS_V2
    -I src/FreeRTOS/Source/include
    -I src/FreeRTOS/Source/portable/GCC/ARM_CM3
```

### Customize build configuration by extra scripts

Alternatively the build configuration can be bend to the Platform IO package directory
by placing a python script in the project folder and referencing it as pre-action.

```py
import os

Import("env")

platform = env.PioPlatform()
FRAMEWORK_DIR = platform.get_package_dir("framework-stm32cubef1")

env.Append(BUILD_FLAGS=[
    '-I ' '$PROJECT_PACKAGES_DIR/framework-stm32cubef1/Middlewares/Third_Party/FreeRTOS/Source/CMSIS_RTOS_V2',
    '-I ' '$PROJECT_PACKAGES_DIR/framework-stm32cubef1/Middlewares/Third_Party/FreeRTOS/Source/include',
    '-I ' '$PROJECT_PACKAGES_DIR/framework-stm32cubef1/Middlewares/Third_Party/FreeRTOS/Source/portable/GCC/ARM_CM3',
    '-L ' '$BUILD_DIR/external/FreeRTOS/Source/portable/GCC/ARM_CM3',
    '-L ' '$BUILD_DIR/external/FreeRTOS/Source/portable/MemMang',
    '-L ' '$BUILD_DIR/external/FreeRTOS/Source',
])

osSource = os.path.join(FRAMEWORK_DIR , "Middlewares", "Third_Party", "FreeRTOS")
osBuild = os.path.join("$BUILD_DIR", "external", "FreeRTOS")
env.BuildSources(osBuild, osSource, 
    "-<*> +<Source/*.c> +<Source/CMSIS_RTOS_V2/*.c> +<Source/portable/GCC/ARM_CM3/*.c> +<Source/portable/MemMang/heap_4.c>"
    )
```

```ini 
[env:bluepill_f103c8]
platform = ststm32
...
extra_scripts = pre:addMiddlewareForF103.py
```
