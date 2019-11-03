# Sentiment Analysis

## Stanford nlp

[Stanford nlp](https://stanfordnlp.github.io/CoreNLP/index.html)

### Setup

Download stanford corenlp and set `CLASSPATH` for *Java* using following command:

```shell
# nlp_path="/Users/junr/Documents/work/stanford-corenlp-full-2018-10-05"
nlp_path=YOUR_DOWNLOAD_PATH_OF_CORENLP
for file in `find ${nlp_path} -name "*.jar"`; do
  export CLASSPATH=${CLASSPATH}:${file};
done
```

### Do sentiment analysis

```shell
java -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -props sentiment_analysis.properties -file test_text.txt
```
