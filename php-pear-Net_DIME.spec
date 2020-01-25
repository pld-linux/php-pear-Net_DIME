%define		_class		Net
%define		_subclass	DIME
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - implements DIME encoding
Summary(pl.UTF-8):	%{_pearname} - implementacja kodowania DIME
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	2
Epoch:		0
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	530e0b358acb976eabe66d8a8e9b10ba
URL:		http://pear.php.net/package/Net_DIME/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Net_DIME-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an implementation of DIME as defined at
http://search.ietf.org/internet-drafts/draft-nielsen-dime-02.txt

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Dostarcza implementację DIME, jaka została zdefiniowana w dokumencie:
http://search.ietf.org/internet-drafts/draft-nielsen-dime-02.txt

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
