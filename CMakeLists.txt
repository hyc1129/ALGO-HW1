cmake_minimum_required(VERSION 3.10)
project(SortBenchmark)

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

