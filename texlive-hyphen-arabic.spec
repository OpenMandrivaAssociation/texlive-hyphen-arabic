%global tl_name hyphen-arabic
%global tl_revision 74115

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	(No) Arabic hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-arabic
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-arabic.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Prevent hyphenation in Arabic.

