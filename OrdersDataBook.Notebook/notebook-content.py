# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "98133141-53c2-43e5-9f2c-537bd37100dc",
# META       "default_lakehouse_name": "LKH1",
# META       "default_lakehouse_workspace_id": "064c7ece-4d31-4d95-a5c8-9e12e3020c49",
# META       "known_lakehouses": [
# META         {
# META           "id": "98133141-53c2-43e5-9f2c-537bd37100dc"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/orders.csv")
# df now is a Spark DataFrame containing CSV data from "Files/orders.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df1 = df


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
