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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/source/fonts
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/arev
%dir %{_datadir}/texmf-dist/fonts/afm/public
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/fonts/vf/public
%dir %{_datadir}/texmf-dist/source/fonts/arev
%dir %{_datadir}/texmf-dist/tex/latex/arev
%dir %{_datadir}/texmf-dist/fonts/afm/public/arev
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/arev
%dir %{_datadir}/texmf-dist/fonts/map/dvips/arev
%dir %{_datadir}/texmf-dist/fonts/tfm/public/arev
%dir %{_datadir}/texmf-dist/fonts/type1/public/arev
%dir %{_datadir}/texmf-dist/fonts/vf/public/arev
%doc %{_datadir}/texmf-dist/doc/fonts/arev/ArevSansLicense.txt
%doc %{_datadir}/texmf-dist/doc/fonts/arev/BitstreamVeraLicense.txt
%doc %{_datadir}/texmf-dist/doc/fonts/arev/ChangeLog
%doc %{_datadir}/texmf-dist/doc/fonts/arev/GPLv2.txt
%doc %{_datadir}/texmf-dist/doc/fonts/arev/LPPLv1-3a.txt
%doc %{_datadir}/texmf-dist/doc/fonts/arev/Makefile
%doc %{_datadir}/texmf-dist/doc/fonts/arev/README
%doc %{_datadir}/texmf-dist/doc/fonts/arev/arevdoc.lyx
%doc %{_datadir}/texmf-dist/doc/fonts/arev/arevdoc.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/arev/arevdoc.tex
%doc %{_datadir}/texmf-dist/doc/fonts/arev/fontsample.tex
%doc %{_datadir}/texmf-dist/doc/fonts/arev/mathtesty.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/arev/mathtesty.tex
%doc %{_datadir}/texmf-dist/doc/fonts/arev/prosper-arev.tex
%doc %{_datadir}/texmf-dist/doc/fonts/arev/prosper-cmbright.tex
%doc %{_datadir}/texmf-dist/doc/fonts/arev/prosper-cmss.tex
%doc %{_datadir}/texmf-dist/doc/fonts/arev/prosper-header.tex
%doc %{_datadir}/texmf-dist/doc/fonts/arev/prosper-helvetica.tex
%doc %{_datadir}/texmf-dist/doc/fonts/arev/prosper-kerkis.tex
%doc %{_datadir}/texmf-dist/doc/fonts/arev/prosper-lcmss.tex
%doc %{_datadir}/texmf-dist/doc/fonts/arev/prosper-text.tex
%{_datadir}/texmf-dist/fonts/afm/public/arev/ArevSans-Bold.afm
%{_datadir}/texmf-dist/fonts/afm/public/arev/ArevSans-BoldOblique.afm
%{_datadir}/texmf-dist/fonts/afm/public/arev/ArevSans-Oblique.afm
%{_datadir}/texmf-dist/fonts/afm/public/arev/ArevSans-Roman.afm
%{_datadir}/texmf-dist/fonts/enc/dvips/arev/arevoml.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arev/arevoms.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arev/arevot1.enc
%{_datadir}/texmf-dist/fonts/map/dvips/arev/arev.map
%{_datadir}/texmf-dist/fonts/tfm/public/arev/ArevSans-Bold.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/ArevSans-BoldOblique.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/ArevSans-Oblique.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/ArevSans-Roman.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/favb8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/favb8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/favbi8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/favbi8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/favmb7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/favmbi7m.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/favmr7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/favmr7y.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/favmri7m.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/favr8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/favr8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/favri8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/favri8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/zavmb7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/zavmbi7m.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/zavmr7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/zavmr7y.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arev/zavmri7m.tfm
%{_datadir}/texmf-dist/fonts/type1/public/arev/ArevSans-Bold.pfb
%{_datadir}/texmf-dist/fonts/type1/public/arev/ArevSans-BoldOblique.pfb
%{_datadir}/texmf-dist/fonts/type1/public/arev/ArevSans-Oblique.pfb
%{_datadir}/texmf-dist/fonts/type1/public/arev/ArevSans-Roman.pfb
%{_datadir}/texmf-dist/fonts/vf/public/arev/favb8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/arev/favbi8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/arev/favr8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/arev/favri8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/arev/zavmb7t.vf
%{_datadir}/texmf-dist/fonts/vf/public/arev/zavmbi7m.vf
%{_datadir}/texmf-dist/fonts/vf/public/arev/zavmr7t.vf
%{_datadir}/texmf-dist/fonts/vf/public/arev/zavmr7y.vf
%{_datadir}/texmf-dist/fonts/vf/public/arev/zavmri7m.vf
%doc %{_datadir}/texmf-dist/source/fonts/arev/TODO.txt
%doc %{_datadir}/texmf-dist/source/fonts/arev/afmtoglyphlist
%doc %{_datadir}/texmf-dist/source/fonts/arev/arevfontinst.tex
%doc %{_datadir}/texmf-dist/source/fonts/arev/arevoml.etx
%doc %{_datadir}/texmf-dist/source/fonts/arev/arevoms.etx
%doc %{_datadir}/texmf-dist/source/fonts/arev/arevot1.etx
%doc %{_datadir}/texmf-dist/source/fonts/arev/convert-ff
%doc %{_datadir}/texmf-dist/source/fonts/arev/createkerndata
%doc %{_datadir}/texmf-dist/source/fonts/arev/enctofontpos
%doc %{_datadir}/texmf-dist/source/fonts/arev/fixkernaccents.tex
%doc %{_datadir}/texmf-dist/source/fonts/arev/fixweierstrass.mtx
%doc %{_datadir}/texmf-dist/source/fonts/arev/fonttokernsfd.ff
%doc %{_datadir}/texmf-dist/source/fonts/arev/fonttopfb.ff
%doc %{_datadir}/texmf-dist/source/fonts/arev/glyphlistoml.tex
%doc %{_datadir}/texmf-dist/source/fonts/arev/glyphlistoms.tex
%doc %{_datadir}/texmf-dist/source/fonts/arev/glyphlistot1.tex
%doc %{_datadir}/texmf-dist/source/fonts/arev/makefontfiles
%doc %{_datadir}/texmf-dist/source/fonts/arev/resetdotlessi.mtx
%doc %{_datadir}/texmf-dist/source/fonts/arev/sfdtokernaccent
%doc %{_datadir}/texmf-dist/source/fonts/arev/unsetomssymbols.mtx
%doc %{_datadir}/texmf-dist/source/fonts/arev/unsetot1symbols.mtx
%{_datadir}/texmf-dist/tex/latex/arev/ams-mdbch.sty
%{_datadir}/texmf-dist/tex/latex/arev/arev.sty
%{_datadir}/texmf-dist/tex/latex/arev/arevmath.sty
%{_datadir}/texmf-dist/tex/latex/arev/arevsymbols.tex
%{_datadir}/texmf-dist/tex/latex/arev/arevtext.sty
%{_datadir}/texmf-dist/tex/latex/arev/omlzavm.fd
%{_datadir}/texmf-dist/tex/latex/arev/omszavm.fd
%{_datadir}/texmf-dist/tex/latex/arev/ot1zavm.fd
%{_datadir}/texmf-dist/tex/latex/arev/t1fav.fd
%{_datadir}/texmf-dist/tex/latex/arev/uzavm.fd
