cmake_minimum_required(VERSION 3.1.2)
project(relapack C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB SRC_FILES source_subfolder/src/*.c)
file(GLOB HEADER_FILES source_subfolder/inc/*.h source_subfolder/config.h)

add_library(${CMAKE_PROJECT_NAME} ${SRC_FILES} ${HEADER_FILES})
set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES C_STANDARD 99)
message(STATUS "CONAN_LIBS: ${CONAN_LIBS}")
target_link_libraries(${CMAKE_PROJECT_NAME} ${CONAN_LIBS})

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