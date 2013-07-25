%define upstream_name    Bot-BasicBot-Pluggable
%define upstream_version 0.98

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.98
Release:	1

Summary:	Extension to the simple irc bot base class allowing for pluggable modules
License:	Artistic or GPL+
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Bot/Bot-BasicBot-Pluggable-0.98.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Bot::BasicBot)
BuildRequires:	perl(Config::Find)
BuildRequires:	perl(Crypt::SaltedHash)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBI)
BuildRequires:	perl(DBM::Deep)
BuildRequires:	perl(Log::Log4perl)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Getopt)
BuildRequires:	perl(MooseX::ConfigFromFile)
BuildRequires:	perl(MooseX::SimpleConfig)
BuildRequires:	perl(POE)
BuildRequires:	perl(Text::Unidecode)
BuildRequires:	perl(URI::Find::Simple)
BuildRequires:	perl(URI::Title)
BuildRequires:	perl(XML::Feed)
BuildRequires:	perl(YAML::XS)
	
BuildArch:	noarch

%description
Extension to the simple irc bot base class allowing for pluggable modules.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Sun May 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.920.0-1mdv2011.0
+ Revision: 672602
- update to new version 0.92

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.910.0-2
+ Revision: 654230
- rebuild for updated spec-helper

* Wed Dec 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.910.0-1mdv2011.0
+ Revision: 616308
- new version

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.900.0-1mdv2011.0
+ Revision: 595075
- update to new version 0.90

* Thu Sep 02 2010 Jérôme Quelin <jquelin@mandriva.org> 0.880.0-1mdv2011.0
+ Revision: 575393
- update to 0.88

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.870.0-1mdv2011.0
+ Revision: 552371
- update to 0.87

* Mon Mar 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.860.0-1mdv2010.1
+ Revision: 528757
- update to 0.86

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.850.0-1mdv2010.1
+ Revision: 505676
- update to 0.85

* Mon Dec 14 2009 Jérôme Quelin <jquelin@mandriva.org> 0.840.0-1mdv2010.1
+ Revision: 478527
- adding missing buildrequires:
- update to 0.84

* Tue Nov 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.830.0-1mdv2010.1
+ Revision: 466967
- update buildrequires:
- adding missing buildrequires:
- adding missing buildrequires:
- adding missing buildrequires:
- update to 0.83

* Wed Oct 21 2009 Michael Scherer <misc@mandriva.org> 0.50-1mdv2010.1
+ Revision: 458555
- add missing Requires
- import perl-Bot-BasicBot-Pluggable

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Sep 24 2007 Michael Scherer <misc@mandriva.org> 0.50-1mdv2008.0
- First Mandriva package

