#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-python_lsp_jsonrpc
Version  : 1.1.0
Release  : 22
URL      : https://files.pythonhosted.org/packages/cd/71/b5e98d6b2b76e3cf0cba9e5f5298eed44008f7651ff93bdf97b5a3584eea/python-lsp-jsonrpc-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/cd/71/b5e98d6b2b76e3cf0cba9e5f5298eed44008f7651ff93bdf97b5a3584eea/python-lsp-jsonrpc-1.1.0.tar.gz
Summary  : JSON RPC 2.0 server library
Group    : Development/Tools
License  : MIT
Requires: pypi-python_lsp_jsonrpc-license = %{version}-%{release}
Requires: pypi-python_lsp_jsonrpc-python = %{version}-%{release}
Requires: pypi-python_lsp_jsonrpc-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Python JSON RPC Server
A Python 3.8+ server implementation of the [JSON RPC 2.0](http://www.jsonrpc.org/specification) protocol. This library has been pulled out of the [Python LSP Server](https://github.com/python-lsp/python-lsp-server) project.

%package license
Summary: license components for the pypi-python_lsp_jsonrpc package.
Group: Default

%description license
license components for the pypi-python_lsp_jsonrpc package.


%package python
Summary: python components for the pypi-python_lsp_jsonrpc package.
Group: Default
Requires: pypi-python_lsp_jsonrpc-python3 = %{version}-%{release}

%description python
python components for the pypi-python_lsp_jsonrpc package.


%package python3
Summary: python3 components for the pypi-python_lsp_jsonrpc package.
Group: Default
Requires: python3-core
Provides: pypi(python_lsp_jsonrpc)
Requires: pypi(ujson)

%description python3
python3 components for the pypi-python_lsp_jsonrpc package.


%prep
%setup -q -n python-lsp-jsonrpc-1.1.0
cd %{_builddir}/python-lsp-jsonrpc-1.1.0
pushd ..
cp -a python-lsp-jsonrpc-1.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694188944
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-python_lsp_jsonrpc
cp %{_builddir}/python-lsp-jsonrpc-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-python_lsp_jsonrpc/c0a4218ed5c81a62f45a9cc14735457e71102cee || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-python_lsp_jsonrpc/c0a4218ed5c81a62f45a9cc14735457e71102cee

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
