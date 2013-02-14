# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 

Name:       intltool
Summary:    Utility for internationalizing various kinds of data files
Version:    0.41.0
Release:    1
Group:      Development/Tools
License:    GPLv2 with exceptions
URL:        http://www.gnome.org
Source0:    http://download.gnome.org/sources/intltool/0.41/%{name}-%{version}.tar.gz
Source1001: packaging/intltool.manifest 
Patch0:     schemas-merge.patch
Requires:   patch
Requires:   automake
Requires:   gettext-tools
Requires:   perl(XML::Parser)
BuildRequires:  perl(XML::Parser)
BuildRequires:  gettext-tools


%description
This tool automatically extracts translatable strings from oaf, glade,
bonobo ui, nautilus theme, .desktop, and other data files and puts
them in the po files.




%prep
%setup -q -n %{name}-%{version}

# schemas-merge.patch
%patch0 -p1

%build
cp %{SOURCE1001} .

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install







%files
%manifest intltool.manifest
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%doc %{_mandir}/man*/*
%{_bindir}/*
%{_datadir}/intltool
%{_datadir}/aclocal/*

