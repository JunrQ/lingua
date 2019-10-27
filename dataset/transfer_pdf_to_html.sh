for i in `ls ../data/pdf/*/*.pdf`; do
  echo ${i}
  pdf2htmlEX --zoom 1.3 "${i}" "${i}".html;
done
