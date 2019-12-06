for i in `ls ../../data/20191206-pdf/*/*.pdf`; do
  echo ${i}
  pdf2htmlEX --zoom 1.3 "${i}" "${i}".html;
done
