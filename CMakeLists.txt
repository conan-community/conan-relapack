cmake_minimum_required(VERSION 3.1.2)
project(relapack C)

include(CheckFunctionExists)
include(conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB SRC_FILES source_subfolder/src/cgemm_tr.c
                    source_subfolder/src/cgetrf.c
                    source_subfolder/src/chegst.c
                    source_subfolder/src/chetrf.c
                    source_subfolder/src/chetrf_rec2.c
                    source_subfolder/src/chetrf_rook.c
                    source_subfolder/src/chetrf_rook_rec2.c
                    source_subfolder/src/clauum.c
                    source_subfolder/src/cpotrf.c
                    source_subfolder/src/csytrf.c
                    source_subfolder/src/csytrf_rec2.c
                    source_subfolder/src/csytrf_rook.c
                    source_subfolder/src/csytrf_rook_rec2.c
                    source_subfolder/src/ctgsyl.c
                    source_subfolder/src/ctrsyl.c
                    source_subfolder/src/ctrsyl_rec2.c
                    source_subfolder/src/ctrtri.c
                    source_subfolder/src/dgemm_tr.c
                    source_subfolder/src/dgetrf.c
                    source_subfolder/src/dlauum.c
                    source_subfolder/src/dpotrf.c
                    source_subfolder/src/dsygst.c
                    source_subfolder/src/dsytrf.c
                    source_subfolder/src/dsytrf_rec2.c
                    source_subfolder/src/dsytrf_rook.c
                    source_subfolder/src/dsytrf_rook_rec2.c
                    source_subfolder/src/dtgsyl.c
                    source_subfolder/src/dtrsyl.c
                    source_subfolder/src/dtrsyl_rec2.c
                    source_subfolder/src/dtrtri.c
                    source_subfolder/src/f2c.c
                    source_subfolder/src/lapack_wrappers.c
                    source_subfolder/src/sgemm_tr.c
                    source_subfolder/src/sgetrf.c
                    source_subfolder/src/slauum.c
                    source_subfolder/src/spotrf.c
                    source_subfolder/src/ssygst.c
                    source_subfolder/src/ssytrf.c
                    source_subfolder/src/ssytrf_rec2.c
                    source_subfolder/src/ssytrf_rook.c
                    source_subfolder/src/ssytrf_rook_rec2.c
                    source_subfolder/src/stgsyl.c
                    source_subfolder/src/strsyl.c
                    source_subfolder/src/strsyl_rec2.c
                    source_subfolder/src/strtri.c
                    source_subfolder/src/zgemm_tr.c
                    source_subfolder/src/zgetrf.c
                    source_subfolder/src/zhegst.c
                    source_subfolder/src/zhetrf.c
                    source_subfolder/src/zhetrf_rec2.c
                    source_subfolder/src/zhetrf_rook.c
                    source_subfolder/src/zhetrf_rook_rec2.c
                    source_subfolder/src/zlauum.c
                    source_subfolder/src/zpotrf.c
                    source_subfolder/src/zsytrf.c
                    source_subfolder/src/zsytrf_rec2.c
                    source_subfolder/src/zsytrf_rook.c
                    source_subfolder/src/zsytrf_rook_rec2.c
                    source_subfolder/src/ztgsyl.c
                    source_subfolder/src/ztrsyl.c
                    source_subfolder/src/ztrsyl_rec2.c
                    source_subfolder/src/ztrtri.c)
file(GLOB HEADER_FILES source_subfolder/inc/relapack.h source_subfolder/config.h)

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