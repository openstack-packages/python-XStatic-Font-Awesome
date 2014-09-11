%global pypi_name XStatic-Font-Awesome

%{!?__python2:%global __python2 %{__python}}

Name:           python-%{pypi_name}
Version:        4.1.0.0
Release:        1%{?dist}
Summary:        Font-Awesome (XStatic packaging standard)

# font awesome is licensed under SIL 1.1.
# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses_4
# short name: OFL
# Code is distributed under MIT
License:        OFL and MIT
URL:            https://fortawesome.github.io/Font-Awesome/
Source0:        https://pypi.python.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  web-assets-devel
BuildRequires:  fontawesome-fonts

Requires: python-XStatic
Requires: web-assets-filesystem
Requires: fontawesome-fonts-web
Requires: fontawesome-fonts


%description
Font Awesome icons packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code
except some metadata nor has any extra requirements.


%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

# use fontawesome-fonts directly
rm -f %{buildroot}/%{python2_sitelib}/xstatic/pkg/font_awesome/data/fonts/*
ln -s %{_datadir}/fonts/fontawesome/*  %{buildroot}/%{python2_sitelib}/xstatic/pkg/font_awesome/data/fonts/

# use fontawesome-fonts-web for css, scss,
for dir in css less scss ; do  
rm -rf %{buildroot}/%{python2_sitelib}/xstatic/pkg/font_awesome/data/$dir
ln -s %{_datadir}/font-awesome-web/$dir %{buildroot}/%{python2_sitelib}/xstatic/pkg/font_awesome/data/$dir
done



%files
%doc README.txt
%{python2_sitelib}/xstatic/pkg/font_awesome
%{python2_sitelib}/XStatic_Font_Awesome-%{version}-py%{python_version}.egg-info
%{python2_sitelib}/XStatic_Font_Awesome-%{version}-py%{python_version}-nspkg.pth

%changelog
* Wed Sep 10 2014 Matthias Runge <mrunge@redhat.com> - 4.1.0.0-1
- Initial package.
