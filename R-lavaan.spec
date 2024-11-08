#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-lavaan
Version  : 0.6.19
Release  : 59
URL      : https://cran.r-project.org/src/contrib/lavaan_0.6-19.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lavaan_0.6-19.tar.gz
Summary  : Latent Variable Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-mnormt
Requires: R-numDeriv
Requires: R-pbivnorm
Requires: R-quadprog
BuildRequires : R-mnormt
BuildRequires : R-numDeriv
BuildRequires : R-pbivnorm
BuildRequires : R-quadprog
BuildRequires : buildreq-R

%description
factor analysis, structural equation modeling and latent growth curve models.

%prep
%setup -q -n lavaan
pushd ..
cp -a lavaan buildavx2
popd
pushd ..
cp -a lavaan buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727381851

%install
export SOURCE_DATE_EPOCH=1727381851
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lavaan/CITATION
/usr/lib64/R/library/lavaan/DESCRIPTION
/usr/lib64/R/library/lavaan/INDEX
/usr/lib64/R/library/lavaan/Meta/Rd.rds
/usr/lib64/R/library/lavaan/Meta/data.rds
/usr/lib64/R/library/lavaan/Meta/features.rds
/usr/lib64/R/library/lavaan/Meta/hsearch.rds
/usr/lib64/R/library/lavaan/Meta/links.rds
/usr/lib64/R/library/lavaan/Meta/nsInfo.rds
/usr/lib64/R/library/lavaan/Meta/package.rds
/usr/lib64/R/library/lavaan/NAMESPACE
/usr/lib64/R/library/lavaan/R/lavaan
/usr/lib64/R/library/lavaan/R/lavaan.rdb
/usr/lib64/R/library/lavaan/R/lavaan.rdx
/usr/lib64/R/library/lavaan/data/Rdata.rdb
/usr/lib64/R/library/lavaan/data/Rdata.rds
/usr/lib64/R/library/lavaan/data/Rdata.rdx
/usr/lib64/R/library/lavaan/help/AnIndex
/usr/lib64/R/library/lavaan/help/aliases.rds
/usr/lib64/R/library/lavaan/help/lavaan.rdb
/usr/lib64/R/library/lavaan/help/lavaan.rdx
/usr/lib64/R/library/lavaan/help/paths.rds
/usr/lib64/R/library/lavaan/html/00Index.html
/usr/lib64/R/library/lavaan/html/R.css
/usr/lib64/R/library/lavaan/understanding_lavaan_internals.R
