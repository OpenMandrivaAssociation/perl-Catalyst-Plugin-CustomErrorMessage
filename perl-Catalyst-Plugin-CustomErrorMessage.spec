%define upstream_name    Catalyst-Plugin-CustomErrorMessage
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Catalyst plugin to have more "cute" error message
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Catalyst)
BuildRequires: perl(Class::Data::Inheritable)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


