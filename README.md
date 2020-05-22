## Requirements

- python3.7
- docker
- docker-compose

## Setup

`make install`

## Other commands

`inv -l`

**Note**: You need to activate the venv in order to run the `inv` commands


## Use cases

- Upload to S3
- Download from S3
- Read/Write from RDS
- Use NLP models


aws setup:

- elasticache redis cluster
    + t2.micro
    + figure out VPC and subnet (using default VPC for now)
    ```
    redis-cli -c -h airflow-redis.ekda3y.ng.0001.use1.cache.amazonaws.com -p 6379
    ```
- postgres db
    + user: airflow
    + pwd: airflow123
    + using default VPC
- remove extra stuff from `entrypoint.sh`
