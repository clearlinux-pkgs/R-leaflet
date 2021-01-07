#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-leaflet
Version  : 2.0.4.1
Release  : 33
URL      : https://cran.r-project.org/src/contrib/leaflet_2.0.4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/leaflet_2.0.4.1.tar.gz
Summary  : Create Interactive Web Maps with the JavaScript 'Leaflet'
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GPL-3.0 MIT
Requires: R-RColorBrewer
Requires: R-base64enc
Requires: R-crosstalk
Requires: R-htmltools
Requires: R-htmlwidgets
Requires: R-leaflet.providers
Requires: R-magrittr
Requires: R-markdown
Requires: R-png
Requires: R-raster
Requires: R-scales
Requires: R-sp
Requires: R-viridis
BuildRequires : R-RColorBrewer
BuildRequires : R-base64enc
BuildRequires : R-crosstalk
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-leaflet.providers
BuildRequires : R-magrittr
BuildRequires : R-markdown
BuildRequires : R-png
BuildRequires : R-raster
BuildRequires : R-scales
BuildRequires : R-sp
BuildRequires : R-viridis
BuildRequires : buildreq-R

%description
JavaScript library and the 'htmlwidgets' package. These maps can be used
    directly from the R console, from 'RStudio', in Shiny applications and R Markdown
    documents.

%prep
%setup -q -c -n leaflet
cd %{_builddir}/leaflet

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610061563

%install
export SOURCE_DATE_EPOCH=1610061563
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library leaflet
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library leaflet
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library leaflet
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc leaflet || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/leaflet/DESCRIPTION
/usr/lib64/R/library/leaflet/INDEX
/usr/lib64/R/library/leaflet/Meta/Rd.rds
/usr/lib64/R/library/leaflet/Meta/data.rds
/usr/lib64/R/library/leaflet/Meta/features.rds
/usr/lib64/R/library/leaflet/Meta/hsearch.rds
/usr/lib64/R/library/leaflet/Meta/links.rds
/usr/lib64/R/library/leaflet/Meta/nsInfo.rds
/usr/lib64/R/library/leaflet/Meta/package.rds
/usr/lib64/R/library/leaflet/NAMESPACE
/usr/lib64/R/library/leaflet/NEWS
/usr/lib64/R/library/leaflet/R/leaflet
/usr/lib64/R/library/leaflet/R/leaflet.rdb
/usr/lib64/R/library/leaflet/R/leaflet.rdx
/usr/lib64/R/library/leaflet/data/Rdata.rdb
/usr/lib64/R/library/leaflet/data/Rdata.rds
/usr/lib64/R/library/leaflet/data/Rdata.rdx
/usr/lib64/R/library/leaflet/help/AnIndex
/usr/lib64/R/library/leaflet/help/aliases.rds
/usr/lib64/R/library/leaflet/help/leaflet.rdb
/usr/lib64/R/library/leaflet/help/leaflet.rdx
/usr/lib64/R/library/leaflet/help/paths.rds
/usr/lib64/R/library/leaflet/html/00Index.html
/usr/lib64/R/library/leaflet/html/R.css
/usr/lib64/R/library/leaflet/htmlwidgets/leaflet.js
/usr/lib64/R/library/leaflet/htmlwidgets/leaflet.yaml
/usr/lib64/R/library/leaflet/htmlwidgets/lib/jquery/jquery.min.js
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/images/cancel.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/images/cancel_@2X.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/images/check.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/images/check_@2X.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/images/focus.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/images/focus_@2X.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/images/rulers.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/images/rulers_@2X.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/images/start.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/images/start_@2X.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/images/trash.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/images/trash_@2X.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/leaflet-measure.css
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-measure/leaflet-measure.min.js
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-omnivore/LICENSE
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-omnivore/index.js
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-omnivore/leaflet-omnivore.min.js
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet-omnivore/package.json
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet/images/layers-2x.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet/images/layers.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet/images/marker-icon-2x.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet/images/marker-icon.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet/images/marker-shadow.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet/leaflet.css
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leaflet/leaflet.js
/usr/lib64/R/library/leaflet/htmlwidgets/lib/leafletfix/leafletfix.css
/usr/lib64/R/library/leaflet/htmlwidgets/lib/rstudio_leaflet/images/1px.png
/usr/lib64/R/library/leaflet/htmlwidgets/lib/rstudio_leaflet/rstudio_leaflet.css
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet-MiniMap/Control.MiniMap.css
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet-MiniMap/Control.MiniMap.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet-MiniMap/Control.MiniMap.min.css
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet-MiniMap/Control.MiniMap.min.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet-MiniMap/Minimap-binding.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet-MiniMap/images/toggle.png
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet-MiniMap/images/toggle.svg
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.EasyButton/EasyButton-binding.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.EasyButton/LICENSE
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.EasyButton/easy-button.css
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.EasyButton/easy-button.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.Graticule/Graticule-binding.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.Graticule/L.Graticule.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.Graticule/Leaflet.Graticule.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.SimpleGraticule/L.SimpleGraticule.css
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.SimpleGraticule/L.SimpleGraticule.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.SimpleGraticule/SimpleGraticule-binding.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.Terminator/L.Terminator.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.Terminator/Terminator-binding.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/bootstrap-theme.min.css
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/bootstrap.min.css
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/bootstrap.min.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/font-awesome.min.css
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/fonts/FontAwesome.otf
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/fonts/fontawesome-webfont.eot
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/fonts/fontawesome-webfont.svg
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/fonts/fontawesome-webfont.ttf
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/fonts/fontawesome-webfont.woff
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/fonts/glyphicons-halflings-regular.eot
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/fonts/glyphicons-halflings-regular.svg
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/fonts/glyphicons-halflings-regular.ttf
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/fonts/glyphicons-halflings-regular.woff
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/fonts/ionicons.eot
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/fonts/ionicons.svg
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/fonts/ionicons.ttf
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/fonts/ionicons.woff
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/images/markers-matte.png
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/images/markers-matte@2x.png
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/images/markers-plain.png
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/images/markers-shadow.png
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/images/markers-shadow@2x.png
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/images/markers-soft.png
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/images/markers-soft@2x.png
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/ionicons.min.css
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/leaflet.awesome-markers.css
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/leaflet.awesome-markers.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.awesome-markers/leaflet.awesome-markers.min.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.markercluster/MIT-LICENCE.txt
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.markercluster/MarkerCluster.Default.css
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.markercluster/MarkerCluster.css
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.markercluster/leaflet.markercluster.freezable.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.markercluster/leaflet.markercluster.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.markercluster/leaflet.markercluster.layersupport.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Leaflet.markercluster/package.json
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Proj4Leaflet/proj4.min.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/Proj4Leaflet/proj4leaflet.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/leaflet-locationfilter/img/filter-icon.png
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/leaflet-locationfilter/img/move-handle.png
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/leaflet-locationfilter/img/resize-handle.png
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/leaflet-locationfilter/locationfilter-bindings.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/leaflet-locationfilter/locationfilter.css
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/leaflet-locationfilter/locationfilter.js
/usr/lib64/R/library/leaflet/htmlwidgets/plugins/leaflet-providers-plugin/leaflet-providers-plugin.js
/usr/lib64/R/library/leaflet/legacy/examples/choropleth/DESCRIPTION
/usr/lib64/R/library/leaflet/legacy/examples/choropleth/Rplots.pdf
/usr/lib64/R/library/leaflet/legacy/examples/choropleth/global.R
/usr/lib64/R/library/leaflet/legacy/examples/choropleth/server.R
/usr/lib64/R/library/leaflet/legacy/examples/choropleth/shinyapps/jcheng/choropleth3.dcf
/usr/lib64/R/library/leaflet/legacy/examples/choropleth/ui.R
/usr/lib64/R/library/leaflet/legacy/examples/geojson/server.R
/usr/lib64/R/library/leaflet/legacy/examples/geojson/ui.R
/usr/lib64/R/library/leaflet/legacy/examples/population/server.R
/usr/lib64/R/library/leaflet/legacy/examples/population/ui.R
/usr/lib64/R/library/leaflet/legacy/examples/population/www/styles.css
/usr/lib64/R/library/leaflet/legacy/www/binding.js
/usr/lib64/R/library/leaflet/legacy/www/images/layers-2x.png
/usr/lib64/R/library/leaflet/legacy/www/images/layers.png
/usr/lib64/R/library/leaflet/legacy/www/images/marker-icon-2x.png
/usr/lib64/R/library/leaflet/legacy/www/images/marker-icon.png
/usr/lib64/R/library/leaflet/legacy/www/images/marker-shadow.png
/usr/lib64/R/library/leaflet/legacy/www/leaflet-src.js
/usr/lib64/R/library/leaflet/legacy/www/leaflet.css
/usr/lib64/R/library/leaflet/legacy/www/leaflet.js
/usr/lib64/R/library/leaflet/tests/testthat.R
/usr/lib64/R/library/leaflet/tests/testthat/test-colors.R
/usr/lib64/R/library/leaflet/tests/testthat/test-evalFormula.R
/usr/lib64/R/library/leaflet/tests/testthat/test-icon.R
/usr/lib64/R/library/leaflet/tests/testthat/test-legend.R
/usr/lib64/R/library/leaflet/tests/testthat/test-measure.R
/usr/lib64/R/library/leaflet/tests/testthat/test-normalize-2.R
/usr/lib64/R/library/leaflet/tests/testthat/test-normalize.R
/usr/lib64/R/library/leaflet/tests/testthat/test-remote.R
