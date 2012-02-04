Summary:	Library for rich GUIs
Summary(pl.UTF-8):	Biblioteka do bogatych graficznych interfejsów użytkownika
Name:		clutter
Version:	1.8.4
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://source.clutter-project.org/sources/clutter/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	bb9136323317b6acb0a399f66168345a
Patch0:		gtkdoc.patch
Patch1:		missing.patch
URL:		http://www.clutter-project.org/
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	atk-devel >= 1:2.1.5
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.10
BuildRequires:	cairo-gobject-devel >= 1.10
BuildRequires:	cogl-devel >= 1.8.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	gtk-doc >= 1.13
BuildRequires:	json-glib-devel >= 0.12
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxslt-progs
BuildRequires:	pango-devel >= 1:1.20
BuildRequires:	pkgconfig
BuildRequires:	python-modules
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel >= 0.4
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel >= 4
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xz
Requires:	atk >= 1:2.1.5
Requires:	cairo-gobject >= 1.10
Requires:	cogl >= 1.8.0
Requires:	glib2 >= 1:2.28.0
Requires:	json-glib >= 0.12
Requires:	pango >= 1:1.20
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
Requires:	atk-devel >= 1:2.1.5
Requires:	cairo-gobject-devel >= 1.10
Requires:	cogl-devel >= 1.8.0
Requires:	gdk-pixbuf2-devel >= 2.0
Requires:	glib2-devel >= 1:2.28.0
Requires:	json-glib-devel >= 0.12.0
Requires:	pango-devel >= 1:1.20
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXcomposite-devel >= 0.4
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel >= 4
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
	--with-flavour=glx \
	--enable-docs \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libclutter-glx-1.0.la

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
%attr(755,root,root) %{_libdir}/libclutter-glx-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclutter-glx-1.0.so.0
%{_libdir}/girepository-1.0/Cally-1.0.typelib
%{_libdir}/girepository-1.0/Clutter-1.0.typelib
%{_libdir}/girepository-1.0/ClutterX11-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-glx-1.0.so
%{_includedir}/clutter-1.0
%{_datadir}/gir-1.0/Cally-1.0.gir
%{_datadir}/gir-1.0/Clutter-1.0.gir
%{_datadir}/gir-1.0/ClutterX11-1.0.gir
%{_pkgconfigdir}/cally-1.0.pc
%{_pkgconfigdir}/clutter-1.0.pc
%{_pkgconfigdir}/clutter-cogl-1.0.pc
%{_pkgconfigdir}/clutter-glx-1.0.pc
%{_pkgconfigdir}/clutter-x11-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-glx-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cally
%{_gtkdocdir}/clutter
%{_gtkdocdir}/clutter-cookbook
