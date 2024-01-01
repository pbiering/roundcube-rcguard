#
# Fedora/Enterprise Linux spec file for Roundcube webmail plugin "rcguard"
#

# manual build
# rpmbuild -bb --undefine=_disable_source_fetch roundcubemail-plugin-rcguard.spec

%global roundcubedir %{_datadir}/roundcubemail
%global plug rcguard

Name: roundcubemail-plugin-rcguard
BuildArch: noarch
Version:   1.4.0
Release:   1
Summary:   CAPTCHA plugin for Roundcube webmail
License:   GPLv3+
URL:       https://github.com/pbiering/roundcube-rcguard/
Group:     Unspecified
Requires:  roundcubemail

Source0:        https://github.com/pbiering/roundcube-rcguard/archive/%{version}/roundcube-%{plug}-%{version}.tar.gz


%description
CAPTCHA plugin for Roundcube webmail, supporting
- Google reCAPTCHA: https://www.google.com/recaptcha
- hCaptcha: https://dashboard.hcaptcha.com/
- FriendlyCaptcha: https://friendlycaptcha.com/
- Cloudflare Turnstile: https://www.cloudflare.com/products/turnstile/


%prep
%setup -q -n roundcube-%{plug}-%{version}


%build
# Nothing


%install
install -d %{buildroot}%{roundcubedir}/plugins/%{plug}

%{__cp} -r * %{buildroot}%{roundcubedir}/plugins/%{plug}
%{__cp} config.inc.php.dist %{buildroot}%{roundcubedir}/plugins/%{plug}/config.inc.php


%files
%{roundcubedir}/plugins/%{plug}/SQL
%{roundcubedir}/plugins/%{plug}/lib
%{roundcubedir}/plugins/%{plug}/localization
%{roundcubedir}/plugins/%{plug}/skins
%{roundcubedir}/plugins/%{plug}/config.inc.php.dist
%{roundcubedir}/plugins/%{plug}/rcguard.php
%{roundcubedir}/plugins/%{plug}/composer.json

%config(noreplace) %{roundcubedir}/plugins/%{plug}/config.inc.php

%doc %{roundcubedir}/plugins/%{plug}/README.md


%changelog
* Mon Jan 01 2024 Peter Bieringer <pb@bieringer.de> - 1.4.0-1
- Initial release 1.4.0
