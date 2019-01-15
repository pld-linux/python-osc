#
#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module		pythonosc
%define		egg_name	python_osc
%define		pypi_name	python-osc
Summary:	Open Sound Control server and client implementations in pure Python
Name:		python-osc
Version:	1.7.0
Release:	1
License:	public domain
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	d2d72048be1c98c226e55a62e284b976
URL:		https://github.com/attwad/python-osc
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open Sound Control server and client implementations in pure Python.

%package -n python3-osc
Summary:	Open Sound Control server and client implementations in pure Python
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-osc
Open Sound Control server and client implementations in pure Python.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-osc
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
