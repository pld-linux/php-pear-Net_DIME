%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       DIME
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - implements DIME encoding
Summary(pl):	%{_pearname} - implementacja kodowania DIME
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	5e740eff36c049f4dcb348c6fb24da11
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an implementation of DIME as defined at
http://search.ietf.org/internet-drafts/draft-nielsen-dime-02.txt

%description -l pl
Dostarcza implementację DIME, jaka została zdefiniowana w dokumencie:
http://search.ietf.org/internet-drafts/draft-nielsen-dime-02.txt

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/test/*
%{php_pear_dir}/%{_class}/*.php
