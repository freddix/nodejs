Summary:	Evented I/O for V8 javascript
Name:		nodejs
Version:	0.10.29
Release:	1
License:	MIT
Group:		Applications
Source0:	http://nodejs.org/dist/v%{version}/node-v%{version}.tar.gz
# Source0-md5:	e14ea9f46f9beecdf4e9423fb626c70b
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	pkg-config
BuildRequires:	python
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Node.js is a software platform that is used to build scalable network
(especially server-side) applications. Node.js utilizes JavaScript as
its scripting language, and achieves high throughput via non-blocking
I/O and a single-threaded event loop.

%prep
%setup -qn node-v%{version}

grep -r '#!.*env python' -l . | xargs %{__sed} -i -e '1 s,#!.*env python,#!%{__python},'

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
./configure \
	--prefix=%{_prefix}	\
	--shared-openssl	\
	--shared-zlib		\
	--without-dtrace	\
	--without-npm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	LIBDIR=%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog CONTRIBUTING.md LICENSE README.md
%attr(755,root,root) %{_bindir}/node
%{_includedir}/node
%{_mandir}/man1/node.1*

