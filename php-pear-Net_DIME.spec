%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       DIME
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - implements DIME encoding
Summary(pl):	%{_class}_%{_subclass} - implementacja kodowania DIME
Name:		php-pear-%{_pearname}
Version:	0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Patch0:		%{name}-class_name.patch
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an implementation of DIME as defined at
http://search.ietf.org/internet-drafts/draft-nielsen-dime-02.txt

%description -l pl
Dostarcza implementacjê DIME, jaka zosta³a zdefiniowana w dokumencie:
http://search.ietf.org/internet-drafts/draft-nielsen-dime-02.txt

%prep
%setup -q -c
%patch0 -p1

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
