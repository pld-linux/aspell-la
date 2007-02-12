Summary:	Latin dictionary for aspell
Summary(pl.UTF-8):   Słownik łaciński dla aspella
Name:		aspell-la
Version:	20020503
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/la/aspell6-la-%{version}-%{subv}.tar.bz2
# Source0-md5:	d42c679b95ba9b094aaa65f118834bf6
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Latin dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik łaciński (lista słów) dla aspella.

%prep
%setup -q -n aspell6-la-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
