Summary:	A little monster breeding for Gnome
Name:		gmonsters
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://download.sourceforge.net/gmonsters/%{name}-%{version}.tar.bz2
URL:		http://gmonsters.sourceforge.net/
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GMonsters is a monster training game similar in some aspects to the
Monster Rancher game on Playstation. It features numerous species;
many different attacks; the ability to capture, train, and raise
monsters; and more features are to come. It is fairly incomplete right
now but it is stable and won't (easily) crash. Have fun!

%package devel
Summary:	Development files for libgmonsters
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Files needed to develop libgmonsters-based games.

%package static
Summary:	Static libgmonsters
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libgmonsters.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GMdir=%{_applnkdir}/Games/GMonsters

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gmmain
%attr(755,root,root) %{_bindir}/gmnewuser
%attr(755,root,root) %{_bindir}/gmmanager
%attr(755,root,root) %{_bindir}/gmbattle
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man?/*
%{_datadir}/gmspecies
%{_pixmapsdir}/gmonsters
%{_applnkdir}/Games/GMonsters

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gmonsters-config
%{_includedir}/gmonsters
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/*a
