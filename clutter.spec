Summary:	Library for rich GUIs
Summary(pl.UTF-8):	Biblioteka do bogatych graficznych interfejsów użytkownika
Name:		clutter
Version:	1.4.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.clutter-project.org/sources/clutter/1.4/%{name}-%{version}.tar.bz2
# Source0-md5:	5a3c6d8414d4e286aba0a936f344c9b1
URL:		http://www.clutter-project.org/
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.10
BuildRequires:	cairo-devel >= 1.6
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	json-glib-devel >= 0.10.4-3
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.20
BuildRequires:	pkgconfig
BuildRequires:	python-modules
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel >= 4
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
Requires:	glib2-devel >= 1:2.16
Requires:	gtk+2-devel >= 1:2.0
Requires:	json-glib-devel >= 0.8.0
Requires:	xorg-lib-libX11-devel
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

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-json=system \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang clutter-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f clutter-1.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libclutter-glx-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclutter-glx-1.0.so.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-glx-1.0.so
%{_libdir}/libclutter-glx-1.0.la
%{_includedir}/clutter-1.0
%{_datadir}/gir-1.0/*.gir
%{_pkgconfigdir}/cally-1.0.pc
%{_pkgconfigdir}/clutter-1.0.pc
%{_pkgconfigdir}/clutter-glx-1.0.pc
%{_pkgconfigdir}/clutter-x11-1.0.pc
%{_pkgconfigdir}/cogl-1.0.pc
%{_pkgconfigdir}/cogl-gl-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-glx-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cally
%{_gtkdocdir}/clutter
%{_gtkdocdir}/cogl
