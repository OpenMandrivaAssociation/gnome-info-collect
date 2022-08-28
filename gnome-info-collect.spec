Name:           gnome-info-collect
Version:        1.0.7
Release:        1
Summary:        A simple utility to collect system information
License:        GPL-3.0
URL:            https://gitlab.gnome.org/vstanek/gnome-info-collect
Source:         https://gitlab.gnome.org/vstanek/gnome-info-collect/-/archive/v1.0-7/gnome-info-collect-v1.0-7.tar.bz2

BuildRequires: meson
BuildRequires: gobject-introspection
BuildRequires: pkgconfig(gobject-introspection-1.0)
Requires: python
Requires: python-gobject3
Requires: python3dist(requests)
Requires: python3dist(pip)
Requires: gnome-online-accounts

BuildArch: noarch

%description
A GNOME system and user data collection tool.

The collected data is anonymous and is sent to a secure server.
The data will be used only for the purpose of enhancing usability and user experience of GNOME.
    
%prep
%autosetup %{name}-v1.0-7 -p1

%build
%meson

%install
%meson_install

%files
%license LICENSE
%{_bindir}/%{name}
