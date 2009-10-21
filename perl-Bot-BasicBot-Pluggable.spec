%define realname   Bot-BasicBot-Pluggable

Name:		perl-%{realname}
Version:    0.50
Release:    %mkrel 1
License:	Artistic or GPL
Group:		Development/Perl
Summary:    Extension to the simple irc bot base class allowing for pluggable modules
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Bot/Bot-BasicBot-Pluggable-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Feed)
BuildRequires:	perl(POE)
BuildRequires:	perl(Bot::BasicBot)
BuildRequires:  perl(URI::Find::Simple)
BuildRequires:  perl(URI::Title)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBD::SQLite)
	
BuildArch: noarch

%description
Extension to the simple irc bot base class allowing for pluggable modules.

%prep
%setup -q -n Bot-BasicBot-Pluggable-%{version} 
# (misc) done because packaging DBM::Deep is too long for the moment
rm -f lib/Bot/BasicBot/Pluggable/Store/Deep.pm
rm -f t/03store_deep.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/*
%{_mandir}/man1/*
