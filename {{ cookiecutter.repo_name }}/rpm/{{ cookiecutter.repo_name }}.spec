%define vendor_prefix {{ cookiecutter.vendor_prefix }}
%define _prefix /opt/%{vendor_prefix}/%{name}

Name:           {{ cookiecutter.repo_name }}
Version:        {{ cookiecutter.package_version }}
Release:        1%{?dist}
Summary:        {{ cookiecutter.description }}

Group:          Applications/System
License:        Apache
#URL:            {{ cookiecutter.package_url }}
Source0:        https://pypi.python.org/packages/source/{{ cookiecutter.repo_name | first }}/{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}-{{ cookiecutter.package_version }}.tar.gz
Source1:        link_console_scripts.py

BuildRequires:  python-pip
BuildRequires:  python-virtualenv
#Requires:

Prefix:         %{_prefix}

%description
{{ cookiecutter.description }}


%prep
%setup -q


%build


%install
rm -rf %{buildroot}
virtualenv %{buildroot}/%{name}
source %{buildroot}/%{name}/bin/activate
python setup.py install
python -c 'import argparse' 1>/dev/null 2>&1 || pip install argparse
deactivate
virtualenv --relocatable %{buildroot}/%{name}
mkdir -p %{buildroot}/opt/%{vendor_prefix}
mv %{buildroot}/%{name} %{buildroot}/opt/%{vendor_prefix}
cp %{SOURCE1} %{buildroot}/%{_bindir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
/opt/%{vendor_prefix}/*


%post
%{_bindir}/python %{_bindir}/link_console_scripts.py install -v %{name}


%preun
%{_bindir}/python %{_bindir}/link_console_scripts.py uninstall -v %{name}


%changelog
