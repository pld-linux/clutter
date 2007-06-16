Summary:	Library for rich GUIs
Summary(pl.UTF-8):	Biblioteka do bogatych graficznych interfejsów użytkownika
Name:		clutter
Version:	0.2.3
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.clutter-project.org/sources/clutter/0.2/%{name}-%{version}.tar.gz
# Source0-md5:	1c6fd7e602d60d7017fac3b23c7b334b
URL:		http://www.clutter-project.org/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	pango-devel
BuildRequires:	freetype-devel
BuildRequires:	gtk-doc-common
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
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-*
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
