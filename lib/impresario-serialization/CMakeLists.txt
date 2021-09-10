cmake_minimum_required(VERSION 3.13)
project(impresario-serialization VERSION 0.1)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_POLICY_DEFAULT_CMP0048 NEW)

include(lib/cmake-utils/dependency-integrator.cmake)

SET(FLATBUFFERS_BUILD_TESTS OFF)
SET(FLATBUFFERS_INSTALL OFF)
SET(FLATBUFFERS_BUILD_FLATC OFF)
SET(FLATBUFFERS_BUILD_FLATHASH OFF)
SET(FLATBUFFERS_INSTALL OFF)
SET(FLATBUFFERS_INSTALL OFF)
integrate_cmake_dependency(
        NAME flatbuffers
        GIT_URL git@github.com:google/flatbuffers.git
        GIT_TAG 6df40a2471737b27271bdd9b900ab5f3aec746c7
)

add_library(impresario-serialization INTERFACE)
target_include_directories(impresario-serialization INTERFACE include)
target_link_libraries(impresario-serialization INTERFACE flatbuffers)
