%define upstream_name    Catalyst-Plugin-CustomErrorMessage
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	6

Summary:	Catalyst plugin to have more "cute" error message
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Catalyst-Plugin-CustomErrorMessage
Source0:	https://cpan.metacpan.org/authors/id/J/JK/JKUTEJ/Catalyst-Plugin-CustomErrorMessage-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Class::Data::Inheritable)
BuildArch:	noarch

%description
You can use this module if you want to get rid of:

        (en) Please come back later
        (fr) SVP veuillez revenir plus tard
        (de) Bitte versuchen sie es spaeter nocheinmal
        (at) Konnten's bitt'schoen spaeter nochmal reinschauen
        (no) Vennligst prov igjen senere
        (dk) Venligst prov igen senere
        (pl) Prosze sprobowac pozniej

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 654260
- rebuild for updated spec-helper

* Sat Jan 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 627247
- import perl-Catalyst-Plugin-CustomErrorMessage

