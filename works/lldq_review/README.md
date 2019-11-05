# Pipeline

**Get dataset**

```shell
python get_dataset.py
```

**Sentiment analysis**

```shell
cd imdb_sentiment_analysis
for file in `ls lldq_imdb_review*.txt`; do
  java -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -props ../../../nlp/sentiment/sentiment_analysis.properties -file ${file};
done
cd -

cd youtube_sentiment_analysis
for file in `ls lldq_youtube_review*.txt`; do
  java -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -props ../../../nlp/sentiment/sentiment_analysis.properties -file ${file};
done
cd -
```

**Organize result**



