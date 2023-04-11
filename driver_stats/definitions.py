# Importing dependencies
from datetime import timedelta
import pandas as pd
from feast import (
    Entity, 
    Feature, 
    FeatureView, 
    FileSource,  
    Field
)
import os
from feast.types import Float32, Int64

# Getting the current working directory
dir = os.getcwd()

# Declaring an entity for the dataset
driver = Entity(
    name="driver", 
    join_keys=["driver_id"]
    )

# Declaring the source for the first feature file
file_source1 = FileSource(
    name="driver_stats_source1",
    path=os.path.join(dir, "data", "driver_stats_1.parquet"),
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created"
)

# Defining the features for the first feature view
driver_stats_fv1 = FeatureView(
    name="driver_stats_fv1",
    ttl=timedelta(days=2),
    entities=[driver],
    schema=[
        Field(name="conv_rate", dtype=Float32)    
        ],    
    source=file_source1
)


# Declaring the source for the second feature file
file_source2 = FileSource(
    name="driver_stats_source2",
    path=os.path.join(dir, "data", "driver_stats_2.parquet"),
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created"
)

# Defining the features for the second feature view
driver_stats_fv2 = FeatureView(
    name="driver_stats_fv2",
    ttl=timedelta(days=2),
    entities=[driver],
    schema=[
        Field(name="acc_rate", dtype=Float32),
        Field(name="avg_daily_trips", dtype=Int64)        
        ],    
    source=file_source2
)
