#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Evol
Summary:	Math::Evol - Evolution search optimisation
Summary(pl):	Math::Evol - optymalizacja przez poszukiwanie ewolucyjne
Name:		perl-Math-Evol
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a844341b8c32e70cbbb39ca9f66e8bdf
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the evolution search strategy. Derivatives of
the objective function are not required. Constraints can be
incorporated. The caller must supply initial values for the variables
and for the initial step sizes.

%description -l pl
Ten modu³ jest implementacj± algorytmu poszukiwania ewolycyjnego.
Pochodne optymalizowanej funkcji nie s± potrzebne. Mo¿na na³o¿yæ
ograniczenia. Wo³aj±cy musi podaæ warto¶ci pocz±tkowe zmiennych oraz
pocz±tkowe rozmiary kroków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Math/Evol.pm
%{_mandir}/man[13]/*
