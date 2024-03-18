FROM ubuntu


RUN apt update
RUN apt-get install vim python3 openjdk-8-jdk  net-tools dnsutils wget python3-pip -y

RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz && \
    tar -xvzf hadoop-3.3.6.tar.gz && mv hadoop-3.3.6 /opt && cd /opt && ln -s hadoop-3.3.6 hadoop && \
    rm -r /hadoop-3.3.6.tar.gz

RUN mkdir -p /opt/hdfs/namenode && mkdir -p /opt/hdfs/datanode

RUN pip3 install mrjob

COPY config/* /opt/hadoop-3.3.6/etc/hadoop/

ENV HADOOP_HOME=/opt/hadoop-3.3.6
ENV HADOOP_MAPRED_HOME=$HADOOP_HOME
ENV HADOOP_STREAMING_JAR=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar
ENV PATH=$PATH:$HADOOP_HOME
ENV PATH=$PATH:$HADOOP_HOME/bin
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
