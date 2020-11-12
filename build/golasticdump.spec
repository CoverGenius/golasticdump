# SPEC file overview:
# https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/#con_rpm-spec-file-overview
# Fedora packaging guidelines:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/


Name: golasticdump
Version: 0.0.1
Release: 0%{?dist}
Summary: Elasticsearch dump tool
License: BSD
URL: https://www.covergenius.com
BuildRequires: golang >= 1.12
BuildArch: x86_64


%description
Backup tool


%prep
mkdir -p %{_topdir}/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp -rf %{_sourcedir}/* %{_topdir}/BUILD


%build
go build


%install
rm -rf %{buildroot}
%{__install} -D -m 0644 %{_topdir}/BUILD/golasticdump %{buildroot}/%{_sbindir}/golasticdump


%files
%defattr(755,root,root,755)
%{_sbindir}/golasticdump


%changelog
* Thu Nov 12 2020 Serghei Anicheev <serghei@covergenius.com>
- Initial
