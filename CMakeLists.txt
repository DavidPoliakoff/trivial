project(trivial)
cmake_minimum_required(VERSION 2.8)

add_executable(a a.c)
install(TARGETS a RUNTIME DESTINATION bin) 
