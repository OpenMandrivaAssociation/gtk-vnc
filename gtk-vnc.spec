%define name gtk-vnc
%define version 0.4.3
%define release %mkrel 1
%define api 1.0
%define major 0
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name %api

Summary: A VNC viewer widget for GTK
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch1: gtk-vnc-0.3.10-new-xulrunner.patch
# Fedora patches

License: LGPLv2+
Group: System/Libraries
Url: http://gtk-vnc.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk+2-devel
BuildRequires: libgnutls-devel
BuildRequires: pygtk2.0-devel
BuildRequires: xulrunner-devel
BuildRequires: libview-devel
BuildRequires: libsasl-devel
BuildRequires: gobject-introspection-devel
BuildRequires: perl-Text-CSV
BuildRequires: intltool
Requires: %libname >= %version

%description
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

%package -n %libname
Summary: A VNC viewer widget for GTK
Group: System/Libraries
Requires: gtk-vnc-common >= %{version}-%{release}

%description -n %libname
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

%package common
Summary: A VNC viewer widget for GTK
Group: System/Libraries

%description common
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

This package contains translations used by gtk-vnc

%package -n %develname
Summary: A VNC viewer widget for GTK
Group: Development/C
Requires: %libname = %version-%release
Provides: lib%name-devel = %version-%release
Provides: lib%name%api-devel = %version-%release

%description -n %develname
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

%package -n python-%name
Summary: A VNC viewer widget for Python/GTK
Group:Development/Python
Requires: %libname = %version-%release

%description -n python-%name
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

%package -n mozilla-gtk-vnc
Group: Networking/Remote access
Summary: A VNC viewer widget for Mozilla browsers
Requires: %libname >= %version

%description -n mozilla-gtk-vnc
gtk-vnc is a VNC viewer widget for GTK. This is a VNC viewer plugin
for Mozilla Firefox and other browsers based on gtk-vnc.

%prep
%setup -q
%patch1 -p1

%build
%configure2_5x --with-examples --enable-plugin
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/*.a %buildroot%py_platsitedir/*.*a %buildroot%_libdir/mozilla/plugins/gtk-vnc-plugin.*a

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/gvnccapture
%_bindir/gvncviewer
%_mandir/man1/gvnccapture.1*

%files -n mozilla-gtk-vnc
%defattr(-,root,root)
%_libdir/mozilla/plugins/gtk-vnc-plugin.so

%files -n %libname
%defattr(-,root,root)
%doc README NEWS AUTHORS
%_libdir/libgtk-vnc-%{api}.so.%{major}*
%_libdir/libgvnc-%{api}.so.%{major}*
%_libdir/girepository-1.0/GVnc-%api.typelib
%_libdir/girepository-1.0/GtkVnc-%api.typelib

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog
%_libdir/lib*.so
%_libdir/lib*.la
%_libdir/pkgconfig/%name-%{api}.pc
%_libdir/pkgconfig/gvnc-%{api}.pc
%_includedir/gvnc-%api
%_includedir/gtk-vnc-%api
%_datadir/gir-1.0/GVnc-%api.gir
%_datadir/gir-1.0/GtkVnc-%api.gir

%files -n python-%name
%defattr(-,root,root)
%py_platsitedir/gtkvnc.so

%files common -f %{name}.lang
%defattr(-,root,root)
