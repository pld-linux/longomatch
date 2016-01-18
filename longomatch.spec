Summary:	LongoMatch - video analysis tool oriented to sports and coaches
Summary(pl.UTF-8):	LongoMatch - narzędzie do analizy obrazu zorientowane na sport i treningi
Name:		longomatch
Version:	1.0.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Video
Source0:	http://ftp.gnome.org/pub/GNOME/sources/longomatch/1.0/%{name}-%{version}.tar.xz
# Source0-md5:	f73267559c704e7505e9423af383269f
Patch0:		%{name}-missing.patch
URL:		http://www.longomatch.com/open-source/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.11
#TODO: pkgconfig(db4o) ???
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.0
BuildRequires:	dotnet-newtonsoft-json-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gstreamer0.10-devel >= 0.10
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	mono-addins-devel
BuildRequires:	mono-devel >= 2.8
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk-update-icon-cache
Requires:	gtk+2 >= 2:2.8
Requires:	hicolor-icon-theme
Requires:	mono >= 2.8
Requires:	mono-addins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LongoMatch is a video analysis tool oriented to sports and coaches, to
assist them on making game video analysis. It simplifies video
analysis by providing a set of intuitive tools to tag, review and edit
the most important plays of the game. It allows to group plays by
categories and adjust the lead and lag time of each play frame by
frame through a timeline. It also has support for playlists, an easy
way to create presentations with plays from different games and
provides a video editor to create new videos from your favorite plays.
Even if primary focused to sports, LongoMatch can be used for any task
that requires tagging and reviewing segments of a video file, and can
be applied to fields like cinema, medics or conferences.

%description -l pl.UTF-8
LongoMatch to narzędzie do analizy obrazu zorientowane na sporty i
treningi, mające pomagać w analizie nagrań z rozgrywek. Upraszcza
analizę obrazu dostarczając zbiór intuicyjnych narzędzi do oznaczania,
przeglądania i edycji najważniejszych partii rozgrywek. Pozwala na
grupowanie rozgrywek po kategoriach i regulować czas trwania akcji i
oczekiwania ramka po ramce. LongoMatch ma także obsługę list
odtwarzania, łatwy sposób tworzenia prezentacji z partiami z różnych
rozgrywek oraz edytor obrazu do tworzenia nowych filmów z ulubionymi
rozgrywkami. Mimo że LongoMatch jest pomyślany głównie z myślą o
sporcie, może być używany do dowolnych zadań wymagających oznaczania
oraz przeglądania fragmentów pliku wideo; może mieć zastosowanie w
kinie, medycynie czy przy konferencjach.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I build/m4 -I build/m4/shamrock
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# C API not exported
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcesarplayer.{la,so}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/longomatch
%attr(755,root,root) %{_libdir}/libcesarplayer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcesarplayer.so.0
%dir %{_libdir}/longomatch
%{_libdir}/longomatch/LongoMatch.exe
%{_libdir}/longomatch/LongoMatch.exe.mdb
%{_libdir}/longomatch/LongoMatch.*.dll
%{_libdir}/longomatch/LongoMatch.*.dll.config
%{_libdir}/longomatch/LongoMatch.*.dll.mdb
%{_libdir}/longomatch/OxyPlotMono.dll
%{_libdir}/longomatch/OxyPlotMono.dll.mdb
%dir %{_libdir}/longomatch/plugins
%{_libdir}/longomatch/plugins/LongoMatch.Plugins.dll
%{_libdir}/longomatch/plugins/LongoMatch.Plugins.dll.mdb
%{_libdir}/longomatch/plugins/LongoMatch.Plugins.*.dll
%{_libdir}/longomatch/plugins/LongoMatch.Plugins.*.dll.mdb
%{_datadir}/longomatch
%{_desktopdir}/longomatch.desktop
%{_iconsdir}/hicolor/48x48/apps/longomatch.png
%{_iconsdir}/hicolor/scalable/apps/longomatch.svg

%if 0
%package devel
# not needed for now; when packaging, use:
#Requires:	dotnet-gtk-sharp2-devel >= 2.0
#Requires:	dotnet-newtonsoft-json-devel
#Requires:	mono-addins-devel
%{_pkgconfigdir}/longomatch-addins.pc
%{_pkgconfigdir}/longomatch-core.pc
%{_pkgconfigdir}/longomatch-drawing.pc
%{_pkgconfigdir}/longomatch-drawing-cairo.pc
%{_pkgconfigdir}/longomatch-gui.pc
%{_pkgconfigdir}/longomatch-gui-helpers.pc
%{_pkgconfigdir}/longomatch-oxyplot.pc
%endif
