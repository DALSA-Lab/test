cmake_minimum_required(VERSION 3.10)
project(cpp_pkg)

set(CMAKE_CXX_STANDARD 17)

include_directories(include)

add_library(math_utils src/math_utils.cpp)
add_library(string_utils src/string_utils.cpp)

add_executable(test_main tests/test_main.cpp)
