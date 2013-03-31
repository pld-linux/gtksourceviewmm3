#
# Conditional build:
%bcond_without	apidocs		# don't generate documentation with doxygen
#
Summary:	A C++ binding of GtkSourceView3
Summary(pl.UTF-8):	Wiązania C++ dla GtkSourceView3
Name:		gtksourceviewmm3
Version:	3.2.0
Release:	2
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtksourceviewmm/3.2/gtksourceviewmm-%{version}.tar.xz
# Source0-md5:	4ddec81dae02d0681db3ca131a42c59e
URL:		http://www.gnome.org/projects/gtksourceviewmm/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	glibmm-devel >= 2.28.0
BuildRequires:	cairomm-devel
BuildRequires:	pangomm-devel
BuildRequires:	atkmm-devel
BuildRequires:	libsigc++-devel
BuildRequires:	gtkmm3-devel >= 3.2.0
BuildRequires:	gtksourceview3-devel >= 3.2.0
BuildRequires:	libtool
BuildRequires:	mm-common >= 0.9.5
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glibmm >= 2.28.0
Requires:	gtkmm3 >= 3.2.0
Requires:	gtksourceview3 >= 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSourceViewMM3 is a C++ binding of GtkSourceView3, an extension to
the text widget included in GTK+ 3.x adding syntax highlighting and
other features typical for a source file editor.

%description -l pl.UTF-8
GtkSourceViewMM3 to wiązania C++ dla GtkSourceView3 - rozszerzenia
tekstowego widgetu będącego częścią GTK+ 3.x, dodającego kolorowanie
składni oraz inne właściwości typowe dla edytora kodu źródłowego.

%package devel
Summary:	Header files for GtkSourceViewMM3 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GtkSourceViewMM3
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.28.0
Requires:	gtkmm3-devel >= 3.2.0
Requires:	gtksourceview3-devel >= 3.2.0

%description devel
Header files for GtkSourceViewMM3 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GtkSourceViewMM3.

%package static
Summary:	Static GtkSourceViewMM3 library
Summary(pl.UTF-8):	Statyczna biblioteka GtkSourceViewMM3
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GtkSourceViewMM3 library.

%description static -l pl.UTF-8
Statyczna biblioteka GtkSourceViewMM3.

%package apidocs
Summary:	GtkSourceViewMM3 API documentation
Summary(pl.UTF-8):	Dokumentacja API GtkSourceViewMM3
Group:		Documentation

%description apidocs
GtkSourceViewMM3 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GtkSourceViewMM3.

%prep
%setup -q -n gtksourceviewmm-%{version}

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{__enable_disable apidocs documentation} \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgtksourceviewmm-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtksourceviewmm-3.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceviewmm-3.0.so
%{_libdir}/gtksourceviewmm-3.0
%{_includedir}/gtksourceviewmm-3.0
%{_pkgconfigdir}/gtksourceviewmm-3.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtksourceviewmm-3.0.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_datadir}/devhelp/books/gtksourceviewmm-3.0
%{_docdir}/gtksourceviewmm-3.0
%endif
