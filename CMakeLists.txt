cmake_minimum_required(VERSION 3.10)
project(SortBenchmark)

if(CMAKE_SIZEOF_VOID_P EQUAL 4)
    message(FATAL_ERROR "This project requires a 64-bit compiler to handle 4GB arrays. Please use a 64-bit compiler (e.g. Visual Studio x64 prompt or CMake -A x64).")
endif()

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_BUILD_TYPE Release)

file(GLOB SRCS "src/*.cpp")

add_executable(sortbench ${SRCS})

# Enable optimization flags
if(MSVC)
    target_compile_options(sortbench PRIVATE /O2 /W3)
else()
    target_compile_options(sortbench PRIVATE -O2 -Wall -Wextra)
endif()

