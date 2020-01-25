#
# Conditional build:
%bcond_with	tests	# Do not perform "make test"
			# won't succeed in timezone other than author's
#
%define		pdir	Crypt
%define		pnam	License
Summary:	Crypt::License - Perl extension to examine a license file
Summary(pl.UTF-8):	Crypt::License - rozszerzenie Perla do kontrolowania pliku licencji
Name:		perl-Crypt-License
Version:	2.04
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	736ac14322df92b75048587726985479
URL:		http://search.cpan.org/dist/Crypt-License/
# perl-modules or perl-Filter
%if %{with tests}
BuildRequires:	perl(Filter::Util::Call) >= 1.04
BuildRequires:	perl-Crypt-CapnMidNite >= 1.00
BuildRequires:	perl-Crypt-C_LockTite >= 1.00
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Crypt-CapnMidNite >= 1.00
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(Filter::Util::Call)'

%description
This module set provides tools to effectively obfuscate Perl source
code and allow it to be decoded and executed based on host server,
user, expiration date and other parameters. Further, decoding and
execution can be set for a system wide key as well as a unique user
key.

In addition, there are a set of utilities that provide email
notification of License expiration and indirect use of the encrypted
modules by other standard modules that may reside on the system. i.e.
sub-process calls by Apache-AuthCookie while not in user space.

%description -l pl.UTF-8
Ten zestaw modułów udostępnia narzędzia do skutecznego ukrycia kodu
źródłowego w Perlu i pozwalania na dekodowanie oraz wykonywanie go w
zależności od hosta, użytkownika, daty wygaśnięcia i innych
parametrów. Co więcej, wykonywanie można ograniczyć na podstawie
klucza globalnego dla systemu lub unikalnego dla każdego użytkownika.

Ponadto pakiet zawiera zbiór narzędzi dających powiadomienia pocztą
elektroniczną o wygasaniu licencji oraz niebezpośrednie używanie
zaszyfrowanych modułów przez inne standardowe moduły, które mogą
istnieć w systemie, jak wywołania z podprocesów przez
Apache-AuthCookie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

# bleh, won't succeed in timezone other than author's
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install License.{template,txt} *.pl \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/Crypt/License.pm
%{perl_vendorlib}/Crypt/License
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/License.*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
