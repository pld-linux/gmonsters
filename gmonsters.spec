%define ver		0.3.0
%define RELEASE		1
%define rel		%{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}

Name: 		gmonsters
Summary: 	A little monster breeding for Gnome.
Version: 	%ver
Release: 	%rel
Copyright: 	GPL
Group: 		Amusments/Games
Source:		http://download.sourceforge.net/gmonsters/gmonsters-%{ver}.tar.bz2
BuildRoot: 	/var/tmp/%{name}-%{version}-root
URL: 		http://gmonsters.sourceforge.net/
Prefix:		/usr

%package devel
Summary: Development files for libgmonsters.
Group: Development/Libraries

%description
GMonsters is a monster training game similar in some aspects to the Monster
Rancher game on Playstation.  It features numerous species; many different
attacks; the ability to capture, train, and raise monsters; and more features
are to come.  It is fairly incomplete right now but it is stable and won't
(easily) crash.  Have fun!

%description devel
Files needed to develop libgmonsters-based games.
Requires: gmonsters = %ver

%prep

%setup -q -n gmonsters-%{ver}

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/%{prefix} datadir=$RPM_BUILD_ROOT/%{prefix}/share

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%{prefix}/bin/gmmain
%{prefix}/bin/gmnewuser
%{prefix}/bin/gmmanager
%{prefix}/bin/gmbattle
# Not finished...
#%{prefix}/bin/gmshop
%{prefix}/lib/*.so*
%{prefix}/share/gmspecies
%{prefix}/share/pixmaps/gmonsters
%{prefix}/share/gnome/apps/Games/*

%files devel
%defattr(-,root,root,0755)
%{prefix}/bin/gmonsters-config
%{prefix}/include/gmonsters
%{prefix}/lib/*a

%changelog
* Fri Sep 22 2000 Gregory Leblanc <gleblanc@cu-portland.edu>
- Added a requires gmonsters to gmonsters-devel

* Tue Sep 19 2000 Gregory Leblanc <gleblanc@cu-portland.edu>
- Moved removal of RPM_BUILD_ROOT to the install section
- changed revision to remove mdk stuff
- fixed name of package
