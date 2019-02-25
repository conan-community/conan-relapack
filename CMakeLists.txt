cmake_minimum_required(VERSION 3.1.2)
project(relapack C)

include(CheckFunctionExists)
include(conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB SRC_FILES source_subfolder/src/*.c)
file(GLOB HEADER_FILES source_subfolder/inc/*.h source_subfolder/config.h)

list(APPEND RELAPACK_REQUIRED_LIBRARIES ${CONAN_LIBS})
check_function_exists(pow POW_FOUND)
if(POW_FOUND)
    list(APPEND RELAPACK_REQUIRED_LIBRARIES m)
endif()

add_library(${CMAKE_PROJECT_NAME} ${SRC_FILES} ${HEADER_FILES})
target_link_libraries(${CMAKE_PROJECT_NAME} ${RELAPACK_REQUIRED_LIBRARIES})
set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES C_STANDARD 99)
message(STATUS "CMAKE_C_COMPILER_ID: ${CMAKE_C_COMPILER_ID}")
if (CMAKE_COMPILER_IS_GNUC OR ${CMAKE_C_COMPILER_ID} MATCHES "Clang")
   target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE "-Wno-logical-op-parentheses")
endif()

if (WIN32 AND MSVC AND BUILD_SHARED_LIBS)
    set_target_properties(${PROJECT_NAME} PROPERTIES
                          PUBLIC_HEADER "${HEADERS}"
                          WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif()

export(TARGETS ${CMAKE_PROJECT_NAME}
       NAMESPACE ${CMAKE_PROJECT_NAME}::
       FILE "${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_PROJECT_NAME}-config.cmake")

install(TARGETS ${CMAKE_PROJECT_NAME}
        EXPORT ${CMAKE_PROJECT_NAME}-config
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

install(FILES source_subfolder/inc/relapack.h DESTINATION include)

install(EXPORT ${CMAKE_PROJECT_NAME}-config
        DESTINATION "${CMAKE_INSTALL_LIBDIR}/${CMAKE_PROJECT_NAME}/cmake"
        NAMESPACE ${CMAKE_PROJECT_NAME}::)