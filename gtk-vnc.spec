%define api 1.0
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define libgvnc %mklibname gvnc %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define girgvnc %mklibname gvnc-gir %{api}
%define develname %mklibname -d %{name} %{api}
%define develgvnc %mklibname -d gvnc %{api}

%define gtk3_builddir gtk3-build
%define api3 2.0
%define libname3 %mklibname %{name} %{api3} %{major}
%define girname3 %mklibname %{name}-gir %{api3}
%define develname3 %mklibname -d %{name} %{api3}

Summary: A VNC viewer widget for GTK
Name: gtk-vnc
Version: 0.5.1
Release: 1
License: LGPLv2+
Group: System/Libraries
Url: http://gtk-vnc.sourceforge.net/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
Patch0:	gtk-vnc-0.5.0_NP_GetMIMEDescription.patch
Patch1:	gtk-vnc-0.3.10-new-xulrunner.patch

BuildRequires: intltool
BuildRequires: vala-tools
BuildRequires: gettext-devel
BuildRequires: libsasl-devel
BuildRequires: xulrunner-devel
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
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

%package -n %{libname3}
Summary: A VNC viewer widget for GTK3
Group: System/Libraries
Requires: gtk-vnc-common >= %{version}-%{release}

%description -n %{libname3}
This package contains the gtk-vnc shared library for %{name}.

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

%package -n %{girname3}
Summary: GObject Introspection interface library for %{name}
Group: System/Libraries
Requires: %{libname3} = %{version}-%{release}

%description -n %{girname3}
GObject Introspection interface library for %{name}.

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
Requires: %{girname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: %{name}%{api}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the development files for %{name}.

%package -n %{develgvnc}
Summary: A VNC viewer widget for GTK
Group: Development/C
Requires: %{libgvnc} = %{version}-%{release}
Requires: %{girgvnc} = %{version}-%{release}
Provides: gvnc%{api}-devel = %{version}-%{release}
Provides: gvnc-devel = %{version}-%{release}

%description -n %{develgvnc}
This package contains the development files for %{libgvnc}.

%package -n %{develname3}
Summary: A VNC viewer widget for GTK3
Group: Development/C
Requires: %{libname3} = %{version}-%{release}
Requires: %{girname3} = %{version}-%{release}
Provides: %{name}%{api3}-devel = %{version}-%{release}

%description -n %{develname3}
This package contains the development files for %{name}.

%package -n python-%{name}
Summary: A VNC viewer widget for Python/GTK
Group:Development/Python
Requires: %{libname} = %{version}-%{release}

%description -n python-%{name}
gtk-vnc is a VNC viewer widget for GTK. It is built using 
coroutines allowing it to be completely asynchronous while 
remaining single threaded. It provides a core C library, and
bindings for Python (PyGTK)

%package -n mozilla-%{name}
Group: Networking/Remote access
Summary: A VNC viewer widget for Mozilla browsers
Requires: %{libname} >= %{version}

%description -n mozilla-%{name}
gtk-vnc is a VNC viewer widget for GTK. This is a VNC viewer plugin
for Mozilla Firefox and other browsers based on gtk-vnc.

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
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}

%files common -f %{name}.lang

%files
%doc README NEWS AUTHORS
%{_bindir}/gvnccapture
%{_bindir}/gvncviewer
%{_mandir}/man1/gvnccapture.1*

%files -n mozilla-%{name}
%{_libdir}/mozilla/plugins/gtk-vnc-plugin.so

%files -n %{libname}
%{_libdir}/libgtk-vnc-%{api}.so.%{major}*

%files -n %{libgvnc}
%{_libdir}/libgvnc-%{api}.so.%{major}*

%files -n %{libname3}
%{_libdir}/libgtk-vnc-%{api3}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GtkVnc-%{api}.typelib

%files -n %{girgvnc}
%{_libdir}/girepository-1.0/GVnc-%{api}.typelib

%files -n %{girname3}
%{_libdir}/girepository-1.0/GtkVnc-%{api3}.typelib

%files -n %{develname}
%doc ChangeLog
%{_libdir}/libgtk-vnc-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_includedir}/gtk-vnc-%{api}
%{_datadir}/gir-1.0/GtkVnc-%{api}.gir

%files -n %{develgvnc}
%{_libdir}/libgvnc-%{api}.so
%{_libdir}/pkgconfig/gvnc-%{api}.pc
%{_includedir}/gvnc-%{api}
%{_datadir}/gir-1.0/GVnc-%{api}.gir

%files -n %{develname3}
%{_libdir}/libgtk-vnc-%{api3}.so
%{_libdir}/pkgconfig/%{name}-%{api3}.pc
%{_includedir}/gtk-vnc-%{api3}
%{_datadir}/gir-1.0/GtkVnc-%{api3}.gir
%{_datadir}/vala/vapi/*

%files -n python-%{name}
%{py_platsitedir}/gtkvnc.so



%changelog
* Fri Jul 13 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.5.1-1
+ Revision: 809240
- update to new version 0.5.1

* Fri May 04 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.5.0-2
+ Revision: 795818
- plugin with gtk+3 builds now
- added p0 to remove build conflicts with new xulrunner

  + Alexander Khrukin <akhrukin@mandriva.org>
    - rel bump and rebuild

* Tue Mar 06 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.5.0-1
+ Revision: 782509
- new version 0.5.0
- split devel pkgs for api 1.0
- added gtk3 build needed for gnome3 builds

* Tue Mar 06 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.4.4-2
+ Revision: 782342
- rebuild
- split out libs and gir pkg
- cleaned up spec

* Fri Nov 11 2011 Götz Waschk <waschk@mandriva.org> 0.4.4-1
+ Revision: 729961
- new version
- xz tarball
- update build deps

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Fri Feb 18 2011 Götz Waschk <waschk@mandriva.org> 0.4.3-1
+ Revision: 638615
- update to new version 0.4.3

* Fri Nov 05 2010 Götz Waschk <waschk@mandriva.org> 0.4.2-1mdv2011.0
+ Revision: 593732
- update build deps
- new version

* Thu Nov 04 2010 Götz Waschk <waschk@mandriva.org> 0.4.1-5mdv2011.0
+ Revision: 593332
- rebuild for new python 2.7

* Thu Sep 16 2010 Götz Waschk <waschk@mandriva.org> 0.4.1-4mdv2011.0
+ Revision: 578943
- rebuild for new gobject-introspection

* Mon Aug 02 2010 Götz Waschk <waschk@mandriva.org> 0.4.1-3mdv2011.0
+ Revision: 565040
- rebuild

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 0.4.1-2mdv2011.0
+ Revision: 563305
- rebuild for new gobject-introspection

* Fri Jul 16 2010 Götz Waschk <waschk@mandriva.org> 0.4.1-1mdv2011.0
+ Revision: 554367
- update to new version 0.4.1

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2011.0
+ Revision: 551172
- new version
- drop patches 0, 101, 102
- update file list
- enable introspection support

* Thu Apr 29 2010 Frederik Himpe <fhimpe@mandriva.org> 0.3.10-3mdv2010.1
+ Revision: 540999
- Sync patches with Fedora:
  * Drop VNC connection if the server sends a update spaning outside
   bounds of desktop (rhbz #540810, Mandriva bug #58981)
  * Fix gcrypt threading initialization (rhbz #537489)

* Tue Jan 05 2010 Götz Waschk <waschk@mandriva.org> 0.3.10-2mdv2010.1
+ Revision: 486376
- fix build with new xulrunner

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 0.3.10-1mdv2010.0
+ Revision: 458934
- Fix BR
- Release 0.3.10
- Patch0 (GIT): fix build
- add source1: add missing header from xulrunner
- Put translation in a separate subpackage

* Tue Aug 11 2009 Götz Waschk <waschk@mandriva.org> 0.3.9-1mdv2010.0
+ Revision: 414886
- update build deps
- new version
- fix source URL
- drop patch

  + Christophe Fergeau <cfergeau@mandriva.com>
    - make sure autoreconf installs new libtool files to avoid libtool 1.5/2.2 clashes

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 0.3.8-2mdv2009.1
+ Revision: 319858
- rebuild for new python

* Sun Dec 07 2008 Götz Waschk <waschk@mandriva.org> 0.3.8-1mdv2009.1
+ Revision: 311659
- new version
- drop patches
- fix build

* Fri Nov 28 2008 Götz Waschk <waschk@mandriva.org> 0.3.7-6mdv2009.1
+ Revision: 307364
- build with libview

* Thu Nov 27 2008 Götz Waschk <waschk@mandriva.org> 0.3.7-5mdv2009.1
+ Revision: 307258
- fix build
- disable gtkglext again

* Fri Nov 21 2008 Götz Waschk <waschk@mandriva.org> 0.3.7-4mdv2009.1
+ Revision: 305446
- build with gl

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.7-3mdv2009.1
+ Revision: 301535
- rebuilt against new libxcb

* Tue Nov 04 2008 Frederik Himpe <fhimpe@mandriva.org> 0.3.7-2mdv2009.1
+ Revision: 299919
- Sync with Fedora patches
  * Fix mouse pointer ungrabbing in virt-manager when using virtual
    machines running Windows
  * Fix keyboard scancode translation if using evdev driver
  * Avoid bogus framebuffer updates for psuedo-encodings

* Sun Sep 07 2008 Götz Waschk <waschk@mandriva.org> 0.3.7-1mdv2009.0
+ Revision: 282150
- new version
- build with xulrunner

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Götz Waschk <waschk@mandriva.org> 0.3.6-1mdv2009.0
+ Revision: 201799
- new version

* Tue Apr 08 2008 Götz Waschk <waschk@mandriva.org> 0.3.5-1mdv2009.0
+ Revision: 192390
- new version

* Mon Feb 04 2008 Götz Waschk <waschk@mandriva.org> 0.3.3-1mdv2008.1
+ Revision: 161915
- new version
- add example client and mozilla plugin

* Tue Jan 22 2008 Funda Wang <fwang@mandriva.org> 0.3.2-2mdv2008.1
+ Revision: 156409
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 31 2007 Götz Waschk <waschk@mandriva.org> 0.3.2-1mdv2008.1
+ Revision: 139791
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Götz Waschk <waschk@mandriva.org> 0.3.1-1mdv2008.1
+ Revision: 119413
- new version

* Wed Dec 12 2007 Götz Waschk <waschk@mandriva.org> 0.3.0-1mdv2008.1
+ Revision: 118021
- new version

* Fri Sep 14 2007 Götz Waschk <waschk@mandriva.org> 0.2.0-1mdv2008.0
+ Revision: 85475
- new version

* Mon Sep 10 2007 Götz Waschk <waschk@mandriva.org> 0.1.0-1mdv2008.0
+ Revision: 84071
- Import gtk-vnc



* Mon Sep 10 2007 Götz Waschk <waschk@mandriva.org> 0.1.0-1mdv2008.0
- initial package
