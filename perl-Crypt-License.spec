#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	License
Summary:	Crypt::License - Perl extension to examine a license file
Summary(pl):	Crypt::License - rozszerzenie Perla do kontrolowania pliku licencji
Name:		perl-Crypt-License
Version:	2.02
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2ef372c947502f94f7c42edef567104d
# perl-modules or perl-Filter
%{!?_without_tests:BuildRequires:	perl(Filter::Util::Call) >= 1.04}
%{!?_without_tests:BuildRequires:	perl-Crypt-CapnMidNite >= 1.00}
%{!?_without_tests:BuildRequires:	perl-Crypt-C_LockTite >= 1.00}
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
Ten zestaw modu��w udost�pnia narz�dzia do skutecznego ukrycia kodu
�r�d�owego w Perlu i pozwalania na dekodowanie oraz wykonywanie go w
zale�no�ci od hosta, u�ytkownika, daty wyga�ni�cia i innych
parametr�w. Co wi�cej, wykonywanie mo�na ograniczy� na podstawie
klucza globalnego dla systemu lub unikalnego dla ka�dego u�ytkownika.

Ponadto pakiet zawiera zbi�r narz�dzi daj�cych powiadomienia poczt�
elektroniczn� o wygasaniu licencji oraz niebezpo�rednie u�ywanie
zaszyfrowanych modu��w przez inne standardowe modu�y, kt�re mog�
istnie� w systemie, jak wywo�ania z podproces�w przez
Apache-AuthCookie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

# bleh, won't succeed in timezone other than author's
#%{!?_without_tests:%{__make} test}

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
