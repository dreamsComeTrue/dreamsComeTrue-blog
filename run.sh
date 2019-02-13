#!/usr/bin/env bash
docker network create kafka-network
docker-compose -f docker-compose.kafka.yml up -d
docker-compose -f docker-compose.kafka.yml logs -f kafka-server | grep "started"
docker-compose up -d

#docker run -v "$(pwd)":/app python-main-app