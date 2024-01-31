#!/usr/bin/env python3

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
