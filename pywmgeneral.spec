Summary:	Python wrapper for wmgeneral functions
Summary(pl):	Wrapper dla funkcji wmgeneral
Name:		pywmgeneral
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://errl.info/pywmdockapps/downloads/current/%{name}-%{version}.tar.gz
# Source0-md5:	a393198a17f0c3f14920525cffc82669
URL:		http://errl.info/pywmdockapps/
BuildRequires:	/usr/bin/python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pywmgeneral is a library that makes it possible to write WindowMaker
dockapps in Python. Quite a bit of the code is taken from the old
wmgeneral.c and pywmgeneral just provides Python wrappers around these
functions. The library also contains a Python part above the wrappers
that ease up argument passing and return values. Also some other
usable methods are provided there.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
	--root=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO README
%{py_sitedir}/*
