docker exec -t docker-pyspark-1 \
pyspark --conf "spark.mongodb.read.connection.uri=mongodb://mongo:27017" \
              --conf "spark.mongodb.write.connection.uri=mongodb://mongo:27017" \
              --packages org.mongodb.spark:mongo-spark-connector_2.12:10.2.2
