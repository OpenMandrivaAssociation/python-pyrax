Name:		python-pyrax
Version:	1.10.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/p/pyrax/pyrax-%{version}.tar.gz
Summary:	Python language bindings for OpenStack Clouds.
URL:		https://pypi.org/project/pyrax/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

%patchlist
pyrax-relax-novaclient-dep.patch

%description
Python language bindings for OpenStack Clouds.

%files
%{py_sitedir}/pyrax
%{py_sitedir}/pyrax-*.*-info
