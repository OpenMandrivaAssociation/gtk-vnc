%define name gtk-vnc
%define version 0.3.1
%define release %mkrel 1
%define api 1.0
%define major 0
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name %api

Summary: A VNC viewer widget for GTK
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/gtk-vnc/%{name}-%{version}.tar.gz
License: LGPLv2
Group: System/Libraries
Url: http://gtk-vnc.sourceforge.net/
BuildRequires: gtk+2-devel
BuildRequires: libgnutls-devel
BuildRequires: pygtk2.0-devel

%description
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

%package -n %libname
Summary: A VNC viewer widget for GTK
Group: System/Libraries

%description -n %libname
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

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

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/*.a %buildroot%py_platsitedir/*.*a

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%doc README NEWS AUTHORS
%_libdir/libgtk-vnc-%{api}.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog
%_libdir/lib*.so
%_libdir/lib*.la
%_libdir/pkgconfig/%name-%{api}.pc
%_includedir/gtk-vnc-%api

%files -n python-%name
%defattr(-,root,root)
%py_platsitedir/gtkvnc.so
