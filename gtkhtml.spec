Summary:	GtkHTML library
Summary(pl.UTF-8):	Biblioteka GtkHTML
Summary(pt_BR.UTF-8):	Biblioteca GtkHTML
Summary(ru.UTF-8):	GtkHTML - это библиотека рендеринга/редактирования HTML
Summary(uk.UTF-8):	GtkHTML - це бібліотека рендерингу/редагування HTML
Summary(zh_CN.UTF-8):	GtkHTML 库
Name:		gtkhtml
Version:	3.23.4
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkhtml/3.23/%{name}-%{version}.tar.bz2
# Source0-md5:	297d28775b614bb2edfb0d177ef7fdac
Patch0:		%{name}-pixmap.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-crash.patch
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gail-devel >= 1.22.0
BuildRequires:	enchant-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-icon-theme >= 2.22.0
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes
BuildRequires:	libbonobo-devel >= 2.22.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.22.01
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	sed >= 4.0
Requires:	gnome-icon-theme >= 2.22.0
Requires:	gtk+2 >= 2:2.12.8
Requires:	libgnomeui >= 2.22.01
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
Requires:	GConf2-devel >= 2.22.0
Requires:	gtk+2-devel >= 2:2.12.8
Requires:	libglade2-devel >= 1:2.6.2
Requires:	libgnomeui-devel >= 2.22.01
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
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e 's#sr@Latn#sr@latin#' po/LINGUAS
mv po/sr@{Latn,latin}.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	idldir=%{_datadir}/idl \
	pkgconfigdir=%{_pkgconfigdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	idldir=%{_datadir}/idl

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
%attr(755,root,root) %{_libdir}/libgtkhtml-editor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkhtml-3.14.so.19
%attr(755,root,root) %ghost %{_libdir}/libgtkhtml-editor.so.0
%{_datadir}/%{name}-3.14
%{_pixmapsdir}/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkhtml-3.14.so
%attr(755,root,root) %{_libdir}/libgtkhtml-editor.so
%{_libdir}/libgtkhtml-3.14.la
%{_libdir}/libgtkhtml-editor.la
%{_includedir}/libgtkhtml-3.14
%{_pkgconfigdir}/libgtkhtml-3.14.pc
%{_pkgconfigdir}/gtkhtml-editor.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkhtml-3.14.a
%{_libdir}/libgtkhtml-editor.a
