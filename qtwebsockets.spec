#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtwebsockets
Version  : 5.15.2
Release  : 32
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtwebsockets-everywhere-src-5.15.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtwebsockets-everywhere-src-5.15.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtwebsockets-lib = %{version}-%{release}
Requires: qtwebsockets-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Test)
Patch1: qtwebsockets-stable-branch.patch

%description
### Introduction
`QtWebSockets` is a pure Qt implementation of WebSockets - both client and server.
It is implemented as a Qt add-on module, that can easily be embedded into existing Qt projects. It has no other dependencies than Qt.

%package dev
Summary: dev components for the qtwebsockets package.
Group: Development
Requires: qtwebsockets-lib = %{version}-%{release}
Provides: qtwebsockets-devel = %{version}-%{release}
Requires: qtwebsockets = %{version}-%{release}

%description dev
dev components for the qtwebsockets package.


%package examples
Summary: examples components for the qtwebsockets package.
Group: Default
Requires: qtwebsockets-dev = %{version}-%{release}

%description examples
examples components for the qtwebsockets package.


%package lib
Summary: lib components for the qtwebsockets package.
Group: Libraries
Requires: qtwebsockets-license = %{version}-%{release}

%description lib
lib components for the qtwebsockets package.


%package license
Summary: license components for the qtwebsockets package.
Group: Default

%description license
license components for the qtwebsockets package.


%prep
%setup -q -n qtwebsockets-everywhere-src-5.15.2
cd %{_builddir}/qtwebsockets-everywhere-src-5.15.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1667237699
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtwebsockets
cp %{_builddir}/qtwebsockets-everywhere-src-%{version}/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtwebsockets/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qtwebsockets-everywhere-src-%{version}/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtwebsockets/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtwebsockets-everywhere-src-%{version}/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtwebsockets/e93757aefa405f2c9a8a55e780ae9c39542dfc3a || :
cp %{_builddir}/qtwebsockets-everywhere-src-%{version}/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtwebsockets/f45ee1c765646813b442ca58de72e20a64a7ddba || :
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtWebSockets/5.15.2/QtWebSockets/private/qdefaultmaskgenerator_p.h
/usr/include/qt5/QtWebSockets/5.15.2/QtWebSockets/private/qsslserver_p.h
/usr/include/qt5/QtWebSockets/5.15.2/QtWebSockets/private/qwebsocket_p.h
/usr/include/qt5/QtWebSockets/5.15.2/QtWebSockets/private/qwebsocketcorsauthenticator_p.h
/usr/include/qt5/QtWebSockets/5.15.2/QtWebSockets/private/qwebsocketdataprocessor_p.h
/usr/include/qt5/QtWebSockets/5.15.2/QtWebSockets/private/qwebsocketframe_p.h
/usr/include/qt5/QtWebSockets/5.15.2/QtWebSockets/private/qwebsockethandshakerequest_p.h
/usr/include/qt5/QtWebSockets/5.15.2/QtWebSockets/private/qwebsockethandshakeresponse_p.h
/usr/include/qt5/QtWebSockets/5.15.2/QtWebSockets/private/qwebsocketprotocol_p.h
/usr/include/qt5/QtWebSockets/5.15.2/QtWebSockets/private/qwebsocketserver_p.h
/usr/include/qt5/QtWebSockets/QMaskGenerator
/usr/include/qt5/QtWebSockets/QWebSocket
/usr/include/qt5/QtWebSockets/QWebSocketCorsAuthenticator
/usr/include/qt5/QtWebSockets/QWebSocketProtocol
/usr/include/qt5/QtWebSockets/QWebSocketServer
/usr/include/qt5/QtWebSockets/QtWebSockets
/usr/include/qt5/QtWebSockets/QtWebSocketsDepends
/usr/include/qt5/QtWebSockets/QtWebSocketsVersion
/usr/include/qt5/QtWebSockets/qmaskgenerator.h
/usr/include/qt5/QtWebSockets/qtwebsocketsversion.h
/usr/include/qt5/QtWebSockets/qwebsocket.h
/usr/include/qt5/QtWebSockets/qwebsocketcorsauthenticator.h
/usr/include/qt5/QtWebSockets/qwebsocketprotocol.h
/usr/include/qt5/QtWebSockets/qwebsockets_global.h
/usr/include/qt5/QtWebSockets/qwebsocketserver.h
/usr/lib64/cmake/Qt5WebSockets/Qt5WebSocketsConfig.cmake
/usr/lib64/cmake/Qt5WebSockets/Qt5WebSocketsConfigVersion.cmake
/usr/lib64/libQt5WebSockets.prl
/usr/lib64/libQt5WebSockets.so
/usr/lib64/pkgconfig/Qt5WebSockets.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_websockets.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_websockets_private.pri

%files examples
%defattr(-,root,root,-)
/usr/share/qt5/examples/websockets/echoclient/echoclient.cpp
/usr/share/qt5/examples/websockets/echoclient/echoclient.h
/usr/share/qt5/examples/websockets/echoclient/echoclient.pro
/usr/share/qt5/examples/websockets/echoclient/main.cpp
/usr/share/qt5/examples/websockets/echoserver/echoclient.html
/usr/share/qt5/examples/websockets/echoserver/echoserver.cpp
/usr/share/qt5/examples/websockets/echoserver/echoserver.h
/usr/share/qt5/examples/websockets/echoserver/echoserver.pro
/usr/share/qt5/examples/websockets/echoserver/main.cpp
/usr/share/qt5/examples/websockets/qmlwebsocketclient/data.qrc
/usr/share/qt5/examples/websockets/qmlwebsocketclient/main.cpp
/usr/share/qt5/examples/websockets/qmlwebsocketclient/qml/qmlwebsocketclient/main.qml
/usr/share/qt5/examples/websockets/qmlwebsocketclient/qmlwebsocketclient.pro
/usr/share/qt5/examples/websockets/qmlwebsocketserver/data.qrc
/usr/share/qt5/examples/websockets/qmlwebsocketserver/main.cpp
/usr/share/qt5/examples/websockets/qmlwebsocketserver/qml/qmlwebsocketserver/main.qml
/usr/share/qt5/examples/websockets/qmlwebsocketserver/qmlwebsocketserver.pro
/usr/share/qt5/examples/websockets/simplechat/chatclient.html
/usr/share/qt5/examples/websockets/simplechat/chatserver.cpp
/usr/share/qt5/examples/websockets/simplechat/chatserver.h
/usr/share/qt5/examples/websockets/simplechat/main.cpp
/usr/share/qt5/examples/websockets/simplechat/simplechat.pro
/usr/share/qt5/examples/websockets/sslechoclient/main.cpp
/usr/share/qt5/examples/websockets/sslechoclient/sslechoclient.cpp
/usr/share/qt5/examples/websockets/sslechoclient/sslechoclient.h
/usr/share/qt5/examples/websockets/sslechoclient/sslechoclient.pro
/usr/share/qt5/examples/websockets/sslechoserver/localhost.cert
/usr/share/qt5/examples/websockets/sslechoserver/localhost.key
/usr/share/qt5/examples/websockets/sslechoserver/main.cpp
/usr/share/qt5/examples/websockets/sslechoserver/securesocketclient.qrc
/usr/share/qt5/examples/websockets/sslechoserver/sslechoclient.html
/usr/share/qt5/examples/websockets/sslechoserver/sslechoserver.cpp
/usr/share/qt5/examples/websockets/sslechoserver/sslechoserver.h
/usr/share/qt5/examples/websockets/sslechoserver/sslechoserver.pro
/usr/share/qt5/examples/websockets/websockets.pro

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5WebSockets.so.5
/usr/lib64/libQt5WebSockets.so.5.15
/usr/lib64/libQt5WebSockets.so.5.15.2
/usr/lib64/qt5/qml/Qt/WebSockets/qmldir
/usr/lib64/qt5/qml/QtWebSockets/libdeclarative_qmlwebsockets.so
/usr/lib64/qt5/qml/QtWebSockets/plugins.qmltypes
/usr/lib64/qt5/qml/QtWebSockets/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtwebsockets/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qtwebsockets/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qtwebsockets/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
/usr/share/package-licenses/qtwebsockets/f45ee1c765646813b442ca58de72e20a64a7ddba
