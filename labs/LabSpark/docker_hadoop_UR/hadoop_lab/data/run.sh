#!/bin/bash
python $1 -r hadoop --file input/NASDAQsample hdfs://$2
