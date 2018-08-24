#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtwebsockets
Version  : 5.11.1
Release  : 8
URL      : http://download.qt.io/official_releases/qt/5.11/5.11.1/submodules/qtwebsockets-everywhere-src-5.11.1.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.11/5.11.1/submodules/qtwebsockets-everywhere-src-5.11.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtwebsockets-lib
Requires: qtwebsockets-license
BuildRequires : cmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : qtbase-dev
BuildRequires : qtbase-extras

%description
This directory contains autotests and manual tests for the Qt WebSockets
module.

%package dev
Summary: dev components for the qtwebsockets package.
Group: Development
Requires: qtwebsockets-lib
Provides: qtwebsockets-devel

%description dev
dev components for the qtwebsockets package.


%package lib
Summary: lib components for the qtwebsockets package.
Group: Libraries
Requires: qtwebsockets-license

%description lib
lib components for the qtwebsockets package.


%package license
Summary: license components for the qtwebsockets package.
Group: Default

%description license
license components for the qtwebsockets package.


%prep
%setup -q -n qtwebsockets-everywhere-src-5.11.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1530975683
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/qtwebsockets
cp LICENSE.GPL3 %{buildroot}/usr/share/doc/qtwebsockets/LICENSE.GPL3
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/doc/qtwebsockets/LICENSE.GPL3-EXCEPT
cp LICENSE.GPL2 %{buildroot}/usr/share/doc/qtwebsockets/LICENSE.GPL2
cp LICENSE.LGPL3 %{buildroot}/usr/share/doc/qtwebsockets/LICENSE.LGPL3
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtWebSockets/5.11.1/QtWebSockets/private/qdefaultmaskgenerator_p.h
/usr/include/qt5/QtWebSockets/5.11.1/QtWebSockets/private/qsslserver_p.h
/usr/include/qt5/QtWebSockets/5.11.1/QtWebSockets/private/qwebsocket_p.h
/usr/include/qt5/QtWebSockets/5.11.1/QtWebSockets/private/qwebsocketcorsauthenticator_p.h
/usr/include/qt5/QtWebSockets/5.11.1/QtWebSockets/private/qwebsocketdataprocessor_p.h
/usr/include/qt5/QtWebSockets/5.11.1/QtWebSockets/private/qwebsocketframe_p.h
/usr/include/qt5/QtWebSockets/5.11.1/QtWebSockets/private/qwebsockethandshakerequest_p.h
/usr/include/qt5/QtWebSockets/5.11.1/QtWebSockets/private/qwebsockethandshakeresponse_p.h
/usr/include/qt5/QtWebSockets/5.11.1/QtWebSockets/private/qwebsocketprotocol_p.h
/usr/include/qt5/QtWebSockets/5.11.1/QtWebSockets/private/qwebsocketserver_p.h
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5WebSockets.so.5
/usr/lib64/libQt5WebSockets.so.5.11
/usr/lib64/libQt5WebSockets.so.5.11.1
/usr/lib64/qt5/qml/Qt/WebSockets/qmldir
/usr/lib64/qt5/qml/QtWebSockets/libdeclarative_qmlwebsockets.so
/usr/lib64/qt5/qml/QtWebSockets/plugins.qmltypes
/usr/lib64/qt5/qml/QtWebSockets/qmldir

%files license
%defattr(-,root,root,-)
/usr/share/doc/qtwebsockets/LICENSE.GPL2
/usr/share/doc/qtwebsockets/LICENSE.GPL3
/usr/share/doc/qtwebsockets/LICENSE.GPL3-EXCEPT
/usr/share/doc/qtwebsockets/LICENSE.LGPL3
