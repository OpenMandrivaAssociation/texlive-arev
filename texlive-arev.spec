Name:		texlive-arev
Version:	15878
Release:	1
Summary:	Fonts and LaTeX support files for Arev Sans
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/arev
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arev.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arev.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arev.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package arev provides type 1 and virtual fonts, together
with LaTeX packages for using Arev Sans in both text and
mathematics. Arev Sans is a derivative of Bitstream Vera Sans
created by Tavmjong Bah, adding support for Greek and Cyrillic
characters. Bah also added a few variant letters that are more
appropriate for mathematics. The primary purpose for using Arev
Sans in LaTeX is presentations, particularly when using a
computer projector. In such a context, Arev Sans is quite
readable, with large x-height, "open letters", wide spacing,
and thick stems. The style is very similar to the SliTeX font
lcmss, but heavier. Arev is one of a very small number of sans-
font mathematics support packages. Others are cmbright, hvmath
and kerkis.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/arev/ArevSans-Bold.afm
%{_texmfdistdir}/fonts/afm/public/arev/ArevSans-BoldOblique.afm
%{_texmfdistdir}/fonts/afm/public/arev/ArevSans-Oblique.afm
%{_texmfdistdir}/fonts/afm/public/arev/ArevSans-Roman.afm
%{_texmfdistdir}/fonts/enc/dvips/arev/arevoml.enc
%{_texmfdistdir}/fonts/enc/dvips/arev/arevoms.enc
%{_texmfdistdir}/fonts/enc/dvips/arev/arevot1.enc
%{_texmfdistdir}/fonts/map/dvips/arev/arev.map
%{_texmfdistdir}/fonts/tfm/public/arev/ArevSans-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/ArevSans-BoldOblique.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/ArevSans-Oblique.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/ArevSans-Roman.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/favb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/favb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/favbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/favbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/favmb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/favmbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/favmr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/favmr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/favmri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/favr8r.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/favr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/favri8r.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/favri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/zavmb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/zavmbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/zavmr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/zavmr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/arev/zavmri7m.tfm
%{_texmfdistdir}/fonts/type1/public/arev/ArevSans-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/arev/ArevSans-BoldOblique.pfb
%{_texmfdistdir}/fonts/type1/public/arev/ArevSans-Oblique.pfb
%{_texmfdistdir}/fonts/type1/public/arev/ArevSans-Roman.pfb
%{_texmfdistdir}/fonts/vf/public/arev/favb8t.vf
%{_texmfdistdir}/fonts/vf/public/arev/favbi8t.vf
%{_texmfdistdir}/fonts/vf/public/arev/favr8t.vf
%{_texmfdistdir}/fonts/vf/public/arev/favri8t.vf
%{_texmfdistdir}/fonts/vf/public/arev/zavmb7t.vf
%{_texmfdistdir}/fonts/vf/public/arev/zavmbi7m.vf
%{_texmfdistdir}/fonts/vf/public/arev/zavmr7t.vf
%{_texmfdistdir}/fonts/vf/public/arev/zavmr7y.vf
%{_texmfdistdir}/fonts/vf/public/arev/zavmri7m.vf
%{_texmfdistdir}/tex/latex/arev/ams-mdbch.sty
%{_texmfdistdir}/tex/latex/arev/arev.sty
%{_texmfdistdir}/tex/latex/arev/arevmath.sty
%{_texmfdistdir}/tex/latex/arev/arevsymbols.tex
%{_texmfdistdir}/tex/latex/arev/arevtext.sty
%{_texmfdistdir}/tex/latex/arev/omlzavm.fd
%{_texmfdistdir}/tex/latex/arev/omszavm.fd
%{_texmfdistdir}/tex/latex/arev/ot1zavm.fd
%{_texmfdistdir}/tex/latex/arev/t1fav.fd
%{_texmfdistdir}/tex/latex/arev/uzavm.fd
%doc %{_texmfdistdir}/doc/fonts/arev/ArevSansLicense.txt
%doc %{_texmfdistdir}/doc/fonts/arev/BitstreamVeraLicense.txt
%doc %{_texmfdistdir}/doc/fonts/arev/ChangeLog
%doc %{_texmfdistdir}/doc/fonts/arev/GPLv2.txt
%doc %{_texmfdistdir}/doc/fonts/arev/LPPLv1-3a.txt
%doc %{_texmfdistdir}/doc/fonts/arev/Makefile
%doc %{_texmfdistdir}/doc/fonts/arev/README
%doc %{_texmfdistdir}/doc/fonts/arev/arevdoc.lyx
%doc %{_texmfdistdir}/doc/fonts/arev/arevdoc.pdf
%doc %{_texmfdistdir}/doc/fonts/arev/arevdoc.tex
%doc %{_texmfdistdir}/doc/fonts/arev/fontsample.tex
%doc %{_texmfdistdir}/doc/fonts/arev/mathtesty.pdf
%doc %{_texmfdistdir}/doc/fonts/arev/mathtesty.tex
%doc %{_texmfdistdir}/doc/fonts/arev/prosper-arev.tex
%doc %{_texmfdistdir}/doc/fonts/arev/prosper-cmbright.tex
%doc %{_texmfdistdir}/doc/fonts/arev/prosper-cmss.tex
%doc %{_texmfdistdir}/doc/fonts/arev/prosper-header.tex
%doc %{_texmfdistdir}/doc/fonts/arev/prosper-helvetica.tex
%doc %{_texmfdistdir}/doc/fonts/arev/prosper-kerkis.tex
%doc %{_texmfdistdir}/doc/fonts/arev/prosper-lcmss.tex
%doc %{_texmfdistdir}/doc/fonts/arev/prosper-text.tex
#- source
%doc %{_texmfdistdir}/source/fonts/arev/TODO.txt
%doc %{_texmfdistdir}/source/fonts/arev/afmtoglyphlist
%doc %{_texmfdistdir}/source/fonts/arev/arevfontinst.tex
%doc %{_texmfdistdir}/source/fonts/arev/arevoml.etx
%doc %{_texmfdistdir}/source/fonts/arev/arevoms.etx
%doc %{_texmfdistdir}/source/fonts/arev/arevot1.etx
%doc %{_texmfdistdir}/source/fonts/arev/convert-ff
%doc %{_texmfdistdir}/source/fonts/arev/createkerndata
%doc %{_texmfdistdir}/source/fonts/arev/enctofontpos
%doc %{_texmfdistdir}/source/fonts/arev/fixkernaccents.tex
%doc %{_texmfdistdir}/source/fonts/arev/fixweierstrass.mtx
%doc %{_texmfdistdir}/source/fonts/arev/fonttokernsfd.ff
%doc %{_texmfdistdir}/source/fonts/arev/fonttopfb.ff
%doc %{_texmfdistdir}/source/fonts/arev/glyphlistoml.tex
%doc %{_texmfdistdir}/source/fonts/arev/glyphlistoms.tex
%doc %{_texmfdistdir}/source/fonts/arev/glyphlistot1.tex
%doc %{_texmfdistdir}/source/fonts/arev/makefontfiles
%doc %{_texmfdistdir}/source/fonts/arev/resetdotlessi.mtx
%doc %{_texmfdistdir}/source/fonts/arev/sfdtokernaccent
%doc %{_texmfdistdir}/source/fonts/arev/unsetomssymbols.mtx
%doc %{_texmfdistdir}/source/fonts/arev/unsetot1symbols.mtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
