#
# Conditional build:
%bcond_without	egl	# EGL framebuffer backend
%bcond_without	wayland	# Wayland backend
%bcond_without	evdev	# evdev support for input events
%bcond_with	tslib	# TSLib support for input events (outdated?)

Summary:	Library for rich GUIs
Summary(pl.UTF-8):	Biblioteka do bogatych graficznych interfejsów użytkownika
Name:		clutter
Version:	1.22.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/clutter/1.22/%{name}-%{version}.tar.xz
# Source0-md5:	788c488d795103e4c201fae1b032cb89
Patch0:		gtkdoc.patch
Patch1:		missing.patch
URL:		http://www.clutter-project.org/
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	atk-devel >= 1:2.5.3
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.14.0
BuildRequires:	cairo-gobject-devel >= 1.14.0
BuildRequires:	cogl-devel >= 1.20.0
%{?with_wayland:BuildRequires:	cogl-devel(wayland) >= 1.20.0}
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.39.0
BuildRequires:	gobject-introspection-devel >= 1.39.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	gtk-doc >= 1.20
BuildRequires:	json-glib-devel >= 0.12.0
%{?with_evdev:BuildRequires:	libevdev-devel}
%{?with_evdev:BuildRequires:	libinput-devel >= 0.8.0}
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxslt-progs
BuildRequires:	pango-devel >= 1:1.30
BuildRequires:	pkgconfig >= 1:0.16
BuildRequires:	python-modules
BuildRequires:	tar >= 1:1.22
%{?with_tslib:BuildRequires:	tslib-devel >= 1.1}
%{?with_evdev:BuildRequires:	udev-devel >= 1:136}
%{?with_evdev:BuildRequires:	udev-glib-devel}
# wayland-client wayland-cursor (for client), wayland-server (for compositor)
%{?with_wayland:BuildRequires:	wayland-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel >= 0.4
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel >= 4
BuildRequires:	xorg-lib-libXi-devel
%if %{with evdev} || %{with wayland}
BuildRequires:	xorg-lib-libxkbcommon-devel
%endif
BuildRequires:	xz
Requires:	atk >= 1:2.5.3
Requires:	cairo-gobject >= 1.14.0
Requires:	cogl >= 1.20.0
%{?with_wayland:Requires:	cogl(wayland) >= 1.20.0}
Requires:	glib2 >= 1:2.39.0
Requires:	gtk+3 >= 3.4.0
Requires:	json-glib >= 0.12.0
%{?with_evdev:Requires:	libinput >= 0.8.0}
Requires:	pango >= 1:1.30
%{?with_evdev:Requires:	udev-libs >= 1:136}
%{?with_evdev:Provides:	clutter(evdev) = %{version}-%{release}}
Obsoletes:	clutter-cairo < 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clutter is an open source software library for creating fast, visually
rich graphical user interfaces. The most obvious example of potential
usage is in media center type applications. We hope however it can be
used for a lot more.

Clutter uses OpenGL (and soon optionally OpenGL ES) for rendering but
with an API which hides the underlying GL complexity from the
developer. The Clutter API is intended to be easy to use, efficient
and flexible.

%description -l pl.UTF-8
Clutter to biblioteka o otwartych źródłach do tworzenia szybkich,
bogatych wizualnie graficznych interfejsów użytkownika. Najbardziej
oczywistym przykładem potencjalnego zastosowania są aplikacje typu
centrum multimedialne. Jednak autorzy mają nadzieję, że znajdzie się
więcej zastosowań.

Clutter wykorzystuje OpenGL (i wkrótce opcjonalnie OpenGL ES) do
renderowania, ale API ukrywa złożoność warstwy GL przed programistami.
API biblioteki Clutter ma być łatwe w użyciu, wydajne i elastyczne.

%package devel
Summary:	Header files for clutter library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki clutter
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLX-devel
Requires:	atk-devel >= 1:2.5.3
Requires:	cairo-gobject-devel >= 1.14.0
Requires:	cogl-devel >= 1.20.0
%{?with_wayland:Requires:	cogl-devel(wayland) >= 1.20.0}
Requires:	gdk-pixbuf2-devel >= 2.0
Requires:	glib2-devel >= 1:2.39.0
Requires:	gtk+3-devel >= 3.4.0
Requires:	json-glib-devel >= 0.12.0
%{?with_evdev:Requires:	libinput-devel >= 0.8.0}
Requires:	pango-devel >= 1:1.30
%{?with_evdev:Requires:	udev-devel >= 1:136}
%{?with_wayland:Requires: wayland-devel}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXcomposite-devel >= 0.4
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel >= 4
%if %{with evdev} || %{with wayland}
Requires:	xorg-lib-libxkbcommon-devel
%endif
%{?with_evdev:Provides:	clutter-devel(evdev) = %{version}-%{release}}
Obsoletes:	clutter-cairo-devel < 1.0

%description devel
Header files for clutter library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki clutter.

%package static
Summary:	Static clutter library
Summary(pl.UTF-8):	Statyczna biblioteka clutter
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
%{?with_evdev:Provides:	clutter-static(evdev) = %{version}-%{release}}
Obsoletes:	clutter-cairo-static < 1.0

%description static
Static clutter library.

%description static -l pl.UTF-8
Statyczna biblioteka clutter.

%package apidocs
Summary:	clutter API documentation
Summary(pl.UTF-8):	Dokumentacja API clutter
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
clutter API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API clutter.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-docs \
	%{?with_egl:--enable-egl-backend} \
	%{?with_evdev:--enable-evdev-input} \
	--enable-gdk-backend \
	--enable-gtk-doc \
	--enable-static \
	%{?with_tslib:--enable-tslib-input} \
%if %{with wayland}
	--enable-wayland-backend \
	--enable-wayland-compositor \
%endif
	--enable-xinput \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libclutter-1.0.la

# move to %{_examplesdir} and package in -examples?
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/clutter-1.0/cookbook/examples

%find_lang clutter-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f clutter-1.0.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libclutter-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclutter-1.0.so.0
%attr(755,root,root) %{_libdir}/libclutter-glx-1.0.so.0
%{_libdir}/girepository-1.0/Cally-1.0.typelib
%{_libdir}/girepository-1.0/Clutter-1.0.typelib
%{_libdir}/girepository-1.0/ClutterGdk-1.0.typelib
%{_libdir}/girepository-1.0/ClutterX11-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-1.0.so
%attr(755,root,root) %{_libdir}/libclutter-glx-1.0.so
%{_includedir}/clutter-1.0
%{_datadir}/gir-1.0/Cally-1.0.gir
%{_datadir}/gir-1.0/Clutter-1.0.gir
%{_datadir}/gir-1.0/ClutterGdk-1.0.gir
%{_datadir}/gir-1.0/ClutterX11-1.0.gir
%{_pkgconfigdir}/cally-1.0.pc
%{_pkgconfigdir}/clutter-1.0.pc
%{_pkgconfigdir}/clutter-cogl-1.0.pc
%{_pkgconfigdir}/clutter-gdk-1.0.pc
%{_pkgconfigdir}/clutter-glx-1.0.pc
%{_pkgconfigdir}/clutter-x11-1.0.pc
%{_pkgconfigdir}/clutter-egl-1.0.pc
%{_pkgconfigdir}/clutter-wayland-1.0.pc
%{_pkgconfigdir}/clutter-wayland-compositor-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cally
%{_gtkdocdir}/clutter
%{_gtkdocdir}/clutter-cookbook
