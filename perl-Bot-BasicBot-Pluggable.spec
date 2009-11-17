%define upstream_name    Bot-BasicBot-Pluggable
%define upstream_version 0.83

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Extension to the simple irc bot base class allowing for pluggable modules
License:	Artistic or GPL+
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Bot/Bot-BasicBot-Pluggable-%{upstream_version}.tar.gz

BuildRequires:	perl(Bot::BasicBot)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:	perl(POE)
BuildRequires:  perl(URI::Find::Simple)
BuildRequires:  perl(URI::Title)
BuildRequires:	perl(XML::Feed)
	
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Extension to the simple irc bot base class allowing for pluggable modules.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
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
