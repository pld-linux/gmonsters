Summary:	A little monster breeding for Gnome
Summary(pl):	Hodowanie potworów dla GNOME
Name:		gmonsters
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	0dd20019a37b8ef1431a5083e05ab5db
Patch0:		%{name}-desktop.patch
URL:		http://gmonsters.sourceforge.net/
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	%{name}-devel
Obsoletes:	%{name}-static

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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gmonsters
%{_datadir}/gmonsters
%{_pixmapsdir}/*.png
%{_applnkdir}/Games/Strategy/*
