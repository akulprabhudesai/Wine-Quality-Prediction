from pyspark.sql import DataFrame
from pyspark import SparkContext, SQLContext
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql import SparkSession
from pyspark.ml.feature import Imputer
from pyspark.sql.functions import when
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler
from pyspark.mllib.util import MLUtils
from pyspark.mllib.evaluation import MulticlassMetrics
from pyspark.ml.classification import RandomForestClassifier
from pyspark.mllib.evaluation import MulticlassMetrics


spark = SparkSession.builder.master("local").appName("assignment2").config("spark.some.config.option","some-value").getOrCreate()

orignalData = spark.read.csv('TrainingDataset.csv',header='true', inferSchema='true', sep=';')

validationData = spark.read.csv('ValidationDataset.csv',header='true', inferSchema='true', sep=';')


featureColumns = [i for i in orignalData.columns if i != 'quality']
vectorass = VectorAssembler(inputCols=featureColumns, outputCol="Values")
transformation = vectorass.transform(orignalData)
transformation.cache()


feature = [i for i in validationData.columns if i != 'quality']
assemblerVal = VectorAssembler(inputCols=feature, outputCol="Values")
validationTransformation = assemblerVal.transform(validationData)


forest = RandomForestClassifier(labelCol="quality", featuresCol="Values", numTrees=100)
RFModel = forest.fit(transformation)


predictionData = RFModel.transform(validationTransformation)

print()
evaluation = MulticlassClassificationEvaluator(
    labelCol="quality", predictionCol="prediction", metricName="f1")
accuracy = evaluation.evaluate(predictionData)
print("Error Testing = %g" % (1.0 - accuracy))

print()

transformed_data = RFModel.transform(validationTransformation)
print(evaluation.getMetricName(), "Accuracy = " , evaluation.evaluate(transformed_data))
print()
