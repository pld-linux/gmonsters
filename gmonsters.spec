Summary:	A little monster breeding for Gnome
Summary(pl):	Hodowanie potworów dla GNOME
Name:		gmonsters
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.sourceforge.net/gmonsters/%{name}-%{version}.tar.bz2
Patch0:		%{name}-desktop.patch
URL:		http://gmonsters.sourceforge.net/
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	%{name}-devel
Obsoletes:	%{name}-static

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_datadir	%{_prefix}/share

%description
GMonsters is a monster training game similar in some aspects to the
Monster Rancher game on Playstation. It features numerous species;
many different attacks; the ability to capture, train, and raise
monsters; and more features are to come. It is fairly incomplete right
now but it is stable and won't (easily) crash. Have fun!

%description -l pl
GMonsters to gra w tresowanie potworów podobna pod niektórymi
wzglêdami do Monster Rancher z Playstation. Ma wiele gatunków; wiele
ró¿nych rodzajów ataków; mo¿liwo¶æ ³apania, tresowania, hodowli
potworów; wiele innych w przysz³o¶ci. Jest jeszcze nie dokoñczona, ale
stabilna. Mi³ej zabawy.

%prep
%setup -q
%patch -p1

%build
%configure2_13
sed 's:@prefix@:%{_prefix}:g' < src/filedirs.h.in > src/filedirs.h
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomemenudir=%{_applnkdir}/Games/Strategy

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gmonsters
%{_datadir}/gnome/help/gmonsters
%{_datadir}/gmonsters
%{_pixmapsdir}/*.png
%{_applnkdir}/Games/Strategy/*
