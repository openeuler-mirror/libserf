%global scons scons-3
%global scons_pkg python3-scons

Name:           libserf
Version:        1.3.9
Release:        13
Summary:        High-Performance Asynchronous HTTP Client Library
License:        ASL 2.0
URL:            https://serf.apache.org/
Source0:        https://archive.apache.org/dist/serf/serf-%{version}.tar.bz2
BuildRequires:  gcc, %{scons_pkg}, pkgconfig, zlib-devel gdb
BuildRequires:  apr-devel, apr-util-devel, krb5-devel, openssl-devel

Patch0:         %{name}-norpath.patch
Patch1:         %{name}-python3.patch

%description
The serf library is a high performance C-based HTTP client library built upon
the Apache Portable Runtime (APR) library. It is permissively licensed under
the Apache License, v2.

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
* Mon May 18 2020 wangchen <wangchen137@huawei.com> - 1.3.9-13
- rebuild for libserf

* Fri Mon 20 2020 songnannan <songnannan2@huawei.com> - 1.3.9-12
- add gdb in buildrequires

* Mon Sep 16 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.3.9-11
- Package init
