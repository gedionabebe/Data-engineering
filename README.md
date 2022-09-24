# Data-engineering
## Data engineering and warehousing using Airflow, DBT and Redash

<!-- Table of contents -->
- [About](#about)
- [Objectives](#objectives)
- [Data](#data)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Contrbutors](#contrbutors)


## About
This project will create a scalable data warehouse that will host the vehicle trajectory data extracted by
analysing footage taken by swarm drones and static roadside cameras.

## Objectives
After joining an AI startup that deploys sensors to businesses, collects data from all activities
in a business - people’s interaction, traffic flows, smart appliances installed in a company, the
objective is to help organisations obtain critical intelligence based on public and private data
they collect and organise.

The following are our subtasks:
- Create a DAG in Airflow to load the data into our database.
- Connect DBT with our database and write transformers for it.
- Connect a reporting environment and create a dashboard out of our data.

## Data
The Data used for this project is from open source dataset called PNeuma which is an open large-scale dataset of naturalistic trajectories of half a million vehicles that have been collected by a one-of-a-kind experiment by a swarm of drones in the congested downtown area of Athens, Greece.

## Repository Structure
  Structure of the repository:
 
        ├── airflow  (airflow scripts containing the dags)
        ├── screenshots  (Important screenshots)
        ├── dbt_dir  (dbt configrations and models)
        ├── airflow/data    (contains data)
        ├── redash  (contains the redash configuration)
        ├── README.md (contains the project description)
        ├── requirements.txt (contains the required packages)
        
        

## Requirements
The project requires the following:
python3
Pip3
docker
docker-compose

## Contrbutors
- Gedion Abebe




