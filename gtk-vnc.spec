%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1.0
%define major	0
%define libname %mklibname %{name} %{api} %{major}
%define libgvnc %mklibname gvnc %{api} %{major}
%define pulsevn %mklibname vncpulse %{api} %{major}
%define pulsegr %mklibname vncpulse-gir %{api}
%define girname %mklibname %{name}-gir %{api}
%define girgvnc %mklibname gvnc-gir %{api}
%define devname %mklibname -d %{name} %{api}
%define develgvnc %mklibname -d gvnc %{api}

%define gtk3_builddir gtk3-build
%define api3	2.0
%define libname3 %mklibname %{name} %{api3} %{major}
%define girname3 %mklibname %{name}-gir %{api3}
%define devname3 %mklibname -d %{name} %{api3}

%define _disable_ld_no_undefined 1

Summary:	A VNC viewer widget for GTK
Name:		gtk-vnc
Version:	0.5.3
Release:	4
License:	LGPLv2+
Group:		System/Libraries
Url:		http://gtk-vnc.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gtk-vnc/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	vala-tools
BuildRequires:	gettext-devel
BuildRequires:	sasl-devel
#BuildRequires:	xulrunner-devel
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(libview)
BuildRequires:	pkgconfig(libgcrypt)

%description
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

%package -n %{libname}
Summary:	A VNC viewer widget for GTK
Group:		System/Libraries
Requires:	gtk-vnc-common >= %{version}-%{release}

%description -n %{libname}
This package contains the gtk-vnc shared library for %{name}.

%package -n %{libgvnc}
Summary:	A VNC viewer widget for GTK
Group:		System/Libraries
Conflicts:	%{_lib}gtk-vnc1.0_0 < 0.4.4-2

%description -n %{libgvnc}
This package contains the gvnc shared library for %{name}.

%package -n %{pulsevn}
Summary:	A VNC viewer widget for GTK
Group:		System/Libraries

%description -n %{pulsevn}
This package contains the gvnc shared library for %{name}.

%package -n %{pulsegr}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
Requires:	%{pulsevn} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{pulsegr}
GObject Introspection interface library for %{libgvnc}.

%package -n %{libname3}
Summary:	A VNC viewer widget for GTK3
Group:		System/Libraries
Requires:	gtk-vnc-common >= %{version}-%{release}

%description -n %{libname3}
This package contains the gtk-vnc shared library for %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{_lib}gtk-vnc1.0_0 < 0.4.4-2

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{girgvnc}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
Requires:	%{libgvnc} = %{version}-%{release}
Conflicts:	%{_lib}gtk-vnc1.0_0 < 0.4.4-2

%description -n %{girgvnc}
GObject Introspection interface library for %{libgvnc}.

%package -n %{girname3}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
Requires:	%{libname3} = %{version}-%{release}

%description -n %{girname3}
GObject Introspection interface library for %{name}.

%package common
Summary:	A VNC viewer widget for GTK
Group:		System/Libraries

%description common
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

This package contains translations used by gtk-vnc

%package -n %{devname}
Summary:	A VNC viewer widget for GTK
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}%{api}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%package -n %{develgvnc}
Summary:	A VNC viewer widget for GTK
Group:		Development/C
Requires:	%{libgvnc} = %{version}-%{release}
Requires:	%{girgvnc} = %{version}-%{release}
Provides:	gvnc%{api}-devel = %{version}-%{release}
Provides:	gvnc-devel = %{version}-%{release}

%description -n %{develgvnc}
This package contains the development files for %{libgvnc}.

%package -n %{devname3}
Summary:	A VNC viewer widget for GTK3
Group:		Development/C
Requires:	%{libname3} = %{version}-%{release}
Requires:	%{girname3} = %{version}-%{release}
Provides:	%{name}%{api3}-devel = %{version}-%{release}

%description -n %{devname3}
This package contains the development files for %{name}.

%package -n python-%{name}
Summary:	A VNC viewer widget for Python/GTK
Group:Development/Python
Requires:	%{libname} = %{version}-%{release}

%description -n python-%{name}
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

%prep
%setup -q
%apply_patches

mkdir ../%{gtk3_builddir}
cp -a . ../%{gtk3_builddir}
mv ../%{gtk3_builddir} .

%build
%configure2_5x \
	--disable-static \
	--with-examples \
	--enable-plugin \
	--with-gtk=2.0

%make LIBS='-lgmodule-2.0 -lz'

pushd %{gtk3_builddir}
%configure2_5x \
	--disable-static \
	--with-examples \
	--disable-plugin \
	--with-gtk=3.0

%make LIBS='-lgmodule-2.0 -lz'
popd

%install
%makeinstall_std
%makeinstall_std -C %{gtk3_builddir}

%find_lang %{name}

%files common -f %{name}.lang

%files
%doc README NEWS AUTHORS
%{_bindir}/gvnccapture
%{_bindir}/gvncviewer
%{_mandir}/man1/gvnccapture.1*

%files -n %{libname}
%{_libdir}/libgtk-vnc-%{api}.so.%{major}*

%files -n %{libgvnc}
%{_libdir}/libgvnc-%{api}.so.%{major}*

%files -n %{pulsevn}
%{_libdir}/libgvncpulse-%{api}.so.%{major}*

%files -n %{libname3}
%{_libdir}/libgtk-vnc-%{api3}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GtkVnc-%{api}.typelib

%files -n %{girgvnc}
%{_libdir}/girepository-1.0/GVnc-%{api}.typelib

%files -n %{girname3}
%{_libdir}/girepository-1.0/GtkVnc-%{api3}.typelib

%files -n %{pulsegr}
%{_libdir}/girepository-1.0/GVncPulse-1.0.typelib

%files -n %{devname}
%doc ChangeLog
%{_libdir}/libgtk-vnc-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_includedir}/gtk-vnc-%{api}
%{_datadir}/gir-1.0/GtkVnc-%{api}.gir

%files -n %{develgvnc}
%{_libdir}/libgvnc-%{api}.so
%{_libdir}/libgvncpulse-%{api}.so
%{_libdir}/pkgconfig/gvnc-%{api}.pc
%{_libdir}/pkgconfig/gvncpulse-%{api}.pc
%{_includedir}/gvnc-%{api}
%{_datadir}/gir-1.0/GVnc-%{api}.gir
%{_datadir}/gir-1.0/GVncPulse-%{api}.gir

%files -n %{devname3}
%{_libdir}/libgtk-vnc-%{api3}.so
%{_libdir}/pkgconfig/%{name}-%{api3}.pc
%{_includedir}/gtk-vnc-%{api3}
%{_includedir}/gvncpulse-%{api}/*.h
%{_datadir}/gir-1.0/GtkVnc-%{api3}.gir
%{_datadir}/vala/vapi/*

%files -n python-%{name}
%{py_platsitedir}/gtkvnc.so

