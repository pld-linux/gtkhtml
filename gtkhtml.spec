Summary:	GtkHTML library
Summary(pl.UTF-8):	Biblioteka GtkHTML
Summary(pt_BR.UTF-8):	Biblioteca GtkHTML
Summary(ru.UTF-8):	GtkHTML - это библиотека рендеринга/редактирования HTML
Summary(uk.UTF-8):	GtkHTML - це бібліотека рендерингу/редагування HTML
Summary(zh_CN.UTF-8):	GtkHTML 库
Name:		gtkhtml
Version:	4.6.0
Release:	3
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkhtml/4.6/%{name}-%{version}.tar.xz
# Source0-md5:	722151a70555a0a48e117fb150711b53
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	enchant-devel >= 1.1.7
BuildRequires:	gettext-devel
BuildRequires:	gnome-icon-theme >= 3.0.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.0.2
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes >= 0.49
BuildRequires:	libsoup-devel >= 2.26.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xz
Requires:	gnome-icon-theme >= 3.0.0
Requires:	gtk+3 >= 3.0.2
Obsoletes:	gal
Obsoletes:	libgtkhtml20
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is GtkHTML, a lightweight HTML rendering/printing/editing engine.
It was originally based on KHTMLW, but is now being developed
independently of it.

%description -l pl.UTF-8
GtkHTML jest "lekką" biblioteką do renderingu, drukowania i edycji
HTML. Pierwotne źródła tej biblioteki bazują na KHTMLW ale teraz
GtkHTML jest rozwijana niezależnie od KHTMLW.

%description -l pt_BR.UTF-8
Este é o GtkHTML, uma ferramenta de renderizar/imprimir/editar HTML
leve e pequeno

%description -l ru.UTF-8
Это GtkHTML, легкий "движок" рендеринга/печати/редактирования HTML.
Сначала он базировался на KHTMLW, но теперь разрабатывается
независимо.

%description -l uk.UTF-8
Це GtkHTML, легке ядро рендерингу/друку/редагування HTML. Воно
спочатку базувалось на KHTMLW, але тепер розробляється незалежно від
нього.

%package devel
Summary:	Header files etc. neccessary to develop GtkHTML applications
Summary(es.UTF-8):	Bibliotecas, archivos de inclusión, e etc. para desarrollar aplicaciones GtkHTML
Summary(pl.UTF-8):	Pliki nagłówkowe i inne niezbędne do tworzenia aplikacji używających GtkHTML
Summary(pt_BR.UTF-8):	Bibliotecas, arquivos de inclusão, e etc para desenvolver aplicações GtkHTML
Summary(ru.UTF-8):	Файлы, необходимые для разработки программ с использованием GtkHTML
Summary(uk.UTF-8):	Файли, необхідні для розробки програм з використанням GtkHTML
Summary(zh_CN.UTF-8):	GtkHTML开发库
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3-devel >= 3.0.2
Requires:	iso-codes >= 0.49
Obsoletes:	gal-devel
Obsoletes:	libgtkhtml20-devel

%description devel
Header files etc. neccessary to develop GtkHTML applications.

%description devel -l es.UTF-8
Bibliotecas, archivos de inclusión, y etc para desarrollar
aplicaciones GtkHTML.

%description devel -l pl.UTF-8
Pliki nagłówkowe i reszta niezbędnych przy tworzeniu aplikacji
wykorzystujących GtkHTML.

%description devel -l pt_BR.UTF-8
Bibliotecas, arquivos de inclusão, e etc para desenvolver aplicações
GtkHTML.

%description devel -l ru.UTF-8
Файлы, необходимые для разработки программ с использованием GtkHTML.

%description devel -l uk.UTF-8
Файли, необхідні для розробки програм з використанням GtkHTML.

%package static
Summary:	Static GtkHTML libraries
Summary(es.UTF-8):	Bibliotecas estáticas para desarrollar aplicaciones GtkHTML
Summary(pl.UTF-8):	Biblioteki statyczne GtkHTML
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolver aplicações GtkHTML
Summary(ru.UTF-8):	Статические библиотеки для разработки программ с GtkHTML
Summary(uk.UTF-8):	Статичні бібліотеки для розробки програм з GtkHTML
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	gal-static

%description static
Static GtkHTML libraries.

%description static -l es.UTF-8
Bibliotecas estáticas para desarrollar aplicaciones GtkHTML.

%description static -l pl.UTF-8
Biblioteki statyczne GtkHTML.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolver aplicações GtkHTML.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang gtkhtml-4.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f gtkhtml-4.0.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_bindir}/gtkhtml-editor-test
%attr(755,root,root) %{_libdir}/libgtkhtml-4.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libgtkhtml-editor-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkhtml-4.0.so.0
%attr(755,root,root) %ghost %{_libdir}/libgtkhtml-editor-4.0.so.0
%{_datadir}/%{name}-4.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkhtml-4.0.so
%attr(755,root,root) %{_libdir}/libgtkhtml-editor-4.0.so
%{_includedir}/libgtkhtml-4.0
%{_pkgconfigdir}/libgtkhtml-4.0.pc
%{_pkgconfigdir}/gtkhtml-editor-4.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkhtml-4.0.a
%{_libdir}/libgtkhtml-editor-4.0.a
