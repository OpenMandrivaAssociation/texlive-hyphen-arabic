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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Prevent hyphenation in Arabic.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-arabic:
arabic hyph-ar.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-arabic:
\addlanguage{arabic}{hyph-ar.tex}{}{0}{0}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-arabic:
['arabic'] = {
	loader = 'hyph-ar.tex',
	lefthyphenmin = 0,
	righthyphenmin = 0,
	synonyms = {  },
},
TL_HYPHEN_EOF
