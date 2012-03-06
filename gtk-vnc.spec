%define api 1.0
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define libgvnc %mklibname gvnc %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define girgvnc %mklibname gvnc-gir %{api}
%define develname %mklibname -d %{name} %{api}

Summary: A VNC viewer widget for GTK
Name: gtk-vnc
Version: 0.4.4
Release: 2
License: LGPLv2+
Group: System/Libraries
Url: http://gtk-vnc.sourceforge.net/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
Patch1: gtk-vnc-0.3.10-new-xulrunner.patch
# Fedora patches

BuildRequires: intltool
BuildRequires: xulrunner-devel
BuildRequires: libsasl-devel
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(pygtk-2.0)
BuildRequires: pkgconfig(libview)

%description
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

%package -n %{libname}
Summary: A VNC viewer widget for GTK
Group: System/Libraries
Requires: gtk-vnc-common >= %{version}-%{release}

%description -n %{libname}
This package contains the gtk-vnc shared library for %{name}.

%package -n %{libgvnc}
Summary: A VNC viewer widget for GTK
Group: System/Libraries
Conflicts: %{_lib}gtk-vnc1.0_0 < 0.4.4-2

%description -n %{libgvnc}
This package contains the gvnc shared library for %{name}.

%package -n %{girname}
Summary: GObject Introspection interface library for %{name}
Group: System/Libraries
Requires: %{libname} = %{version}-%{release}
Conflicts: %{_lib}gtk-vnc1.0_0 < 0.4.4-2

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{girgvnc}
Summary: GObject Introspection interface library for %{name}
Group: System/Libraries
Requires: %{libgvnc} = %{version}-%{release}
Conflicts: %{_lib}gtk-vnc1.0_0 < 0.4.4-2

%description -n %{girgvnc}
GObject Introspection interface library for %{libgvnc}.

%package common
Summary: A VNC viewer widget for GTK
Group: System/Libraries

%description common
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

This package contains translations used by gtk-vnc

%package -n %{develname}
Summary: A VNC viewer widget for GTK
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Requires: %{libgvnc} = %{version}-%{release}
Requires: %{girname} = %{version}-%{release}
Requires: %{girgvnc} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: %{name}%{api}-devel = %{version}-%{release}

%description -n %{develname}
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

%package -n python-%{name}
Summary: A VNC viewer widget for Python/GTK
Group:Development/Python
Requires: %{libname} = %{version}-%{release}

%description -n python-%{name}
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

%package -n mozilla-gtk-vnc
Group: Networking/Remote access
Summary: A VNC viewer widget for Mozilla browsers
Requires: %{libname} >= %{version}

%description -n mozilla-gtk-vnc
gtk-vnc is a VNC viewer widget for GTK. This is a VNC viewer plugin
for Mozilla Firefox and other browsers based on gtk-vnc.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--with-examples \
	--enable-plugin

%make LIBS='-lgmodule-2.0 -lz'

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}

%files common -f %{name}.lang

%files
%doc README NEWS AUTHORS
%{_bindir}/gvnccapture
%{_bindir}/gvncviewer
%{_mandir}/man1/gvnccapture.1*

%files -n mozilla-gtk-vnc
%{_libdir}/mozilla/plugins/gtk-vnc-plugin.so

%files -n %{libname}
%{_libdir}/libgtk-vnc-%{api}.so.%{major}*

%files -n %{libgvnc}
%{_libdir}/libgvnc-%{api}.so.%{major}*

%files -n %{girgvnc}
%{_libdir}/girepository-1.0/GVnc-%{api}.typelib

%files -n %{girname}
%{_libdir}/girepository-1.0/GtkVnc-%{api}.typelib

%files -n %{develname}
%doc ChangeLog
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/pkgconfig/gvnc-%{api}.pc
%{_includedir}/gvnc-%{api}
%{_includedir}/gtk-vnc-%{api}
%{_datadir}/gir-1.0/GVnc-%{api}.gir
%{_datadir}/gir-1.0/GtkVnc-%{api}.gir

%files -n python-%{name}
%{py_platsitedir}/gtkvnc.so

