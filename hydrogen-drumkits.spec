Summary:	Hydrogen drumkits
Summary(pl):	Zestawy perkusyjne dla Hydrogena
Name:		hydrogen-drumkits
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/hydrogen/3355606.tar.gz
# Source0-md5:	1980647fa79029fa1dd1eb4f5ad14d65
Source1:	http://dl.sourceforge.net/hydrogen/DrumkitPack1.tar.gz
# Source1-md5:	8ddc8e3f5d02f5e2f12533db45e77c55
Source2:	http://dl.sourceforge.net/hydrogen/DrumkitPack2.tar.gz
# Source2-md5:	535b873aead13de2105cc2a5609ec977
Source3:	http://dl.sourceforge.net/hydrogen/EasternHop-1.tar.gz
# Source3-md5:	def807440c5a5e01e22f2b7a52a872df
Source4:	http://dl.sourceforge.net/hydrogen/TD-7.tar.gz
# Source4-md5:	2ccaed2a392a97143f31f52488fdde74
URL:		http://hydrogen.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hydrogen drumkits.

%description -l pl
Zestawy perkusyjne dla Hydrogena.

%package 3355606
Summary:	Hydrogen drumkit 3355606
Summary(pl):	Zestaw perkusyjny 3355606 dla Hydrogena
Group:          Applications/Sound
Requires:	libhydrogen

%description 3355606
Hydrogen drumkit 3355606.

%description 3355606 -l pl
Zestaw perkusyjny 3355606 dla Hydrogena.

%package DrumkitPack1
Summary:	Hydrogen drumkit DrumkitPack1
Summary(pl):	Zestaw perkusyjny DrumkitPack1 dla Hydrogena
Group:          Applications/Sound
Requires:	libhydrogen

%description DrumkitPack1
Hydrogen drumkit DrumkitPack1.

%description DrumkitPack1 -l pl
Zestaw perkusyjny DrumkitPack1 dla Hydrogena.

%package DrumkitPack2
Summary:	Hydrogen drumkit DrumkitPack2
Summary(pl):	Zestaw perkusyjny DrumkitPack2 dla Hydrogena
Group:          Applications/Sound
Requires:	libhydrogen

%description DrumkitPack2
Hydrogen drumkit DrumkitPack2.

%description DrumkitPack2 -l pl
Zestaw perkusyjny DrumkitPack2 dla Hydrogena.

%package EasternHop-1
Summary:	Hydrogen drumkit EasternHop-1
Summary(pl):	Zestaw perkusyjny EasternHop-1 dla Hydrogena
Group:          Applications/Sound
Requires:	libhydrogen

%description EasternHop-1
Hydrogen drumkit EasternHop-1.

%description EasternHop-1 -l pl
Zestaw perkusyjny EasternHop-1 dla Hydrogena.

%package TD-7
Summary:	Hydrogen drumkit TD-7
Summary(pl):	Zestaw perkusyjny TD-7 dla Hydrogena
Group:          Applications/Sound
Requires:	libhydrogen

%description TD-7
Hydrogen drumkit TD-7.

%description TD-7 -l pl
Zestaw perkusyjny TD-7 dla Hydrogena.

%prep
%setup -c -a1 -a2 -a3 -a4

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/demo_songs

for dir in 3355606 DrumkitPack1 DrumkitPack2 EasternHop-1 TD-7
do
install -c $dir/*.h2drumkit \
    $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
install -c $dir/*.h2song \
    $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/demo_songs
done

%clean
rm -rf $RPM_BUILD_ROOT

%files 3355606
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/3355606kit.h2drumkit
%{_datadir}/hydrogen/data/demo_songs/3355606demo.h2song

%files DrumkitPack1
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/HipHop*.h2drumkit
%{_datadir}/hydrogen/data/demo_songs/HipHop*.h2song

%files DrumkitPack2
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/Synthie-*.h2drumkit
%{_datadir}/hydrogen/data/drumkits/Techno-1.h2drumkit
%{_datadir}/hydrogen/data/drumkits/TR808909.h2drumkit
%{_datadir}/hydrogen/data/demo_songs/Synthie-1.demo1.h2song
%{_datadir}/hydrogen/data/demo_songs/Techno-1*.h2song
%{_datadir}/hydrogen/data/demo_songs/TR808909demo1.h2song

%files EasternHop-1
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/EasternHop-1.h2drumkit
%{_datadir}/hydrogen/data/demo_songs/EasternHop-1*.h2song

%files TD-7
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/TD-7kit.h2drumkit
%{_datadir}/hydrogen/data/demo_songs/TD7.h2song
