QT += core
QT -= gui

CONFIG += c++11

TARGET = faceDetector
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app

SOURCES += main.cpp

# The following define makes your compiler emit warnings if you use
# any feature of Qt which as been marked deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

LIBS += -pthread
CONFIG += link_pkgconfig
PKGCONFIG += x11

#INCLUDEPATH += /usr/local/include
#LIBS += -L/usr/local/lib
INCLUDEPATH += /home/felipecrispim/Downloads/dlib-19.7
LIBS += -L/home/felipecrispim/Downloads/dlib-19.7/build/dlib
LIBS += -ldlib
