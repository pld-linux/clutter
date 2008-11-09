Summary:	Library for rich GUIs
Summary(pl.UTF-8):	Biblioteka do bogatych graficznych interfejsów użytkownika
Name:		clutter
Version:	0.6.4
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.clutter-project.org/sources/clutter/0.6/%{name}-%{version}.tar.gz
# Source0-md5:	d28dec49517475c2ea0de884d7b87268
URL:		http://www.clutter-project.org/
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	glib2-devel >= 1:2.10
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	libtool
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel >= 4
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
Requires:	glib2-devel >= 1:2.10
Requires:	gtk+2-devel >= 1:2.0
Requires:	pango-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXfixes-devel >= 4

%description devel
Header files for clutter library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki clutter.

%package static
Summary:	Static clutter library
Summary(pl.UTF-8):	Statyczna biblioteka clutter
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

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
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libclutter-glx-0.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclutter-glx-0.6.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-glx-0.6.so
%{_libdir}/libclutter-glx-0.6.la
%{_includedir}/clutter-0.6
%{_pkgconfigdir}/clutter-0.6.pc
%{_pkgconfigdir}/clutter-glx-0.6.pc
%{_pkgconfigdir}/clutter-x11-0.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-glx-0.6.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
