Summary:	GtkHTML library
Summary(pl.UTF-8):	Biblioteka GtkHTML
Summary(pt_BR.UTF-8):	Biblioteca GtkHTML
Summary(ru.UTF-8):	GtkHTML - это библиотека рендеринга/редактирования HTML
Summary(uk.UTF-8):	GtkHTML - це бібліотека рендерингу/редагування HTML
Summary(zh_CN.UTF-8):	GtkHTML 库
Name:		gtkhtml
Version:	3.91.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkhtml/3.91/%{name}-%{version}.tar.bz2
# Source0-md5:	a2ebba331b211ef9940b07e04347ec5e
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.9
BuildRequires:	enchant-devel >= 1.1.7
BuildRequires:	gettext-devel
BuildRequires:	gnome-icon-theme >= 2.22.0
BuildRequires:	gtk+2-devel >= 2:2.22.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes >= 0.49
BuildRequires:	libsoup-devel >= 2.26.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gnome-icon-theme >= 2.22.0
Requires:	gtk+2 >= 2:2.22.0
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
Requires:	GConf2-devel >= 2.24.0
Requires:	gtk+2-devel >= 2:2.22.0
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

%{__sed} -i -e 's/^en@shaw//' po/LINGUAS
rm -f po/en@shaw.po

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--disable-deprecated-warning-flags \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{a,la}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_bindir}/gtkhtml-editor-test
%attr(755,root,root) %{_libdir}/libgtkhtml-3.14.so.*.*.*
%attr(755,root,root) %{_libdir}/libgtkhtml-editor-3.14.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkhtml-3.14.so.19
%attr(755,root,root) %ghost %{_libdir}/libgtkhtml-editor-3.14.so.0
%{_datadir}/%{name}-3.14

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkhtml-3.14.so
%attr(755,root,root) %{_libdir}/libgtkhtml-editor-3.14.so
%{_libdir}/libgtkhtml-3.14.la
%{_libdir}/libgtkhtml-editor-3.14.la
%{_includedir}/libgtkhtml-3.14
%{_pkgconfigdir}/libgtkhtml-3.14.pc
%{_pkgconfigdir}/gtkhtml-editor-3.14.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkhtml-3.14.a
%{_libdir}/libgtkhtml-editor-3.14.a
