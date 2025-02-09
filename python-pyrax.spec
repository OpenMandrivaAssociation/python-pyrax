Name:		python-pyrax
Version:	1.10.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pyrax/pyrax-%{version}.tar.gz
Summary:	Python language bindings for OpenStack Clouds.
URL:		https://pypi.org/project/pyrax/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Python language bindings for OpenStack Clouds.

%prep
%autosetup -p1 -n pyrax-%{version}

%files
%{py_sitedir}/pyrax
%{py_sitedir}/pyrax-*.*-info
