Summary:	Python wrapper for wmgeneral functions
Summary(pl.UTF-8):	Pythonowy wrapper dla funkcji wmgeneral
Name:		pywmgeneral
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://errl.info/pywmdockapps/downloads/current/%{name}-%{version}.tar.gz
# Source0-md5:	a393198a17f0c3f14920525cffc82669
URL:		http://errl.info/pywmdockapps/
BuildRequires:	/usr/bin/python
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pywmgeneral is a library that makes it possible to write WindowMaker
dockapps in Python. Quite a bit of the code is taken from the old
wmgeneral.c and pywmgeneral just provides Python wrappers around these
functions. The library also contains a Python part above the wrappers
that ease up argument passing and return values. Also some other
usable methods are provided there.

%description -l pl.UTF-8
Pywmgeneral to biblioteka umożliwiająca pisanie dokletów WindowMakera
w Pythonie. Spora część kodu pochodzi ze starego wmgeneral.c, a
pywmgeneral po prostu dostarcza wrappery Pythona dla tych funkcji. Ta
biblioteka zawiera także część pythonową ponad tymi wrapperami,
ułatwiającą przekazywanie parametrów i zwracanych wartości. Dodanych
jest także trochę użytecznych metod.

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
%{py_sitedir}/*.py*
%attr(755,root,root) %{py_sitedir}/*.so
