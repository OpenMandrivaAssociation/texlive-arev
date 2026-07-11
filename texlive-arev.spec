%global tl_name arev
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Fonts and LaTeX support files for Arev Sans
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/arev
License:	lppl1.3a
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arev.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arev.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arev.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package arev provides type 1 and virtual fonts, together with LaTeX
packages for using Arev Sans in both text and mathematics. Arev Sans is
a derivative of Bitstream Vera Sans created by Tavmjong Bah, adding
support for Greek and Cyrillic characters. Bah also added a few variant
letters that are more appropriate for mathematics. The primary purpose
for using Arev Sans in LaTeX is presentations, particularly when using a
computer projector. In such a context, Arev Sans is quite readable, with
large x-height, "open letters", wide spacing, and thick stems. The style
is very similar to the SliTeX font lcmss, but heavier. Arev is one of a
very small number of sans-font mathematics support packages. Others are
cmbright, hvmath and kerkis.

