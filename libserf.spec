%global scons scons-3
%global scons_pkg python3-scons

Name:           libserf
Version:        1.3.9
Release:        17
Summary:        High-Performance Asynchronous HTTP Client Library
License:        ASL 2.0
URL:            https://serf.apache.org/
Source0:        https://archive.apache.org/dist/serf/serf-%{version}.tar.bz2
BuildRequires:  gcc, %{scons_pkg}, pkgconfig, zlib-devel
BuildRequires:  apr-devel, apr-util-devel, krb5-devel, openssl-devel

Patch0:         %{name}-norpath.patch
Patch1:         %{name}-python3.patch
Patch2:         backport-%{name}-1.3.9-errgetfunc.patch
Patch3:         0001-fix-CC-compiler-error.patch
%description
The serf library is a C-based HTTP client library built upon the Apache 
Portable Runtime (APR) library. It multiplexes connections, running the
read/write communication asynchronously. Memory copies and transformations are
kept to a minimum to provide high performance operation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release} apr-devel%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%package_help

%prep
%autosetup -n serf-%{version} -p1 

sed -i '/SHLIBVERSION/s/MAJOR/0/' SConstruct

%build
%{scons} \
      CFLAGS="%{optflags}" LINKFLAGS="%{__global_ldflags}" \
      PREFIX=%{_prefix} LIBDIR=%{_libdir} \
      GSSAPI=%{_prefix} %{?_smp_mflags}


%install
%{scons} install --install-sandbox=%{buildroot}

%delete_la_and_a

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%{scons} %{?_smp_mflags} check || true

%ldconfig_scriptlets

%files
%defattr(-,root,root)
%license LICENSE NOTICE
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/serf-1/
%{_libdir}/*.so
%{_libdir}/pkgconfig/serf*.pc

%files help
%defattr(-,root,root)
%doc README CHANGES design-guide.txt

%changelog
* Mon Apr 24 2023 sjxur <sjxur@isoftstone.com> - 1.3.9-17
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix CC compiler error

* Wed Feb 01 2023 gaihuiying <eaglegai@163.com> - 1.3.9-16
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix build with openssl 3.0

* Sat Oct 22 2022 gaihuiying <eaglegai@163.com> - 1.3.9-15
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:modify description about libserf

* Thu Apr 28 2022 xinghe <xinghe2@h-partners.com> - 1.3.9-14
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:rebuild package

* Mon Jul 19 2021 lijingyuan <lijingyuan3@huawei.com> - 1.3.9-13
- Type:requirement
- ID:NA
- SUG:NA
- DESC:cancel gdb in buildrequires

* Fri Mar 20 2020 songnannan <songnannan2@huawei.com> - 1.3.9-12
- add gdb in buildrequires

* Mon Sep 16 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.3.9-11
- Package init
