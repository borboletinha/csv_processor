# CSV Deals Processor Script

## TOC
1. [Description](#description)
   - [Principle of operation](#principle-of-operation)
   - [Project structure](#project-structure)
   - [URL structure](#url-structure)
   - [Tests absence](#tests-absence)
2. [Installation](#installation)
   - [Docker-compose deploy](#docker-compose-deploy)

## Description

A script that processes standardized csv-files containing gemstones purchase data:
```csv
customer,item,total,quantity,date
```

### Principle of operation

1. Uploading a standardized csv-file is done via the ```/api/upload-file/``` endpoint with a POST-request;


2. The uploaded file is parsed. The processed file data creates instances of the ```Deals``` model: a single line of the file is an instance;


3. Processed data is received via the ```/api/get-processed-data/``` endpoint with a GET-request.

* What data is displayed:
  * Top 5 customers with the most spending for the entire period. 
  * Each customer is described by the following fields:
    * ```username``` - customer login; 
    * ```spent_money``` - the amount of funds spent by the customer for the entire period;
    * ```gems``` - a list of gemstones that have been bought by at least two of these five customers, and this customer is one of the customers.


* The example output:
```json
{
  "response": [
    {
      "username": "example_username",
      "spent_money": 10000,
      "gems": [
        "Opal",
        "Quartz"
      ]
    }
  ]
}
```

### Project structure
```
├── deals
│ ├── deals_core
│ │ ├── .env
│ │ ├── settings.py  
│ │ ├── urls.py  
│ │ └── wsgi.py
│ ├── migrations  
│ │ └── 0001_initial.py   
│ ├── admin.py  
│ ├── api_urls.py  
│ ├── apps.py  
│ ├── models.py  
│ ├── serializers.py  
│ ├── utils.py  
│ ├── views.py  
│ ├── deals_core  
├── scripts  
│ └── docker-entrypoint.sh  
├── docker-compose.yml  
├── Dockerfile  
├── manage.py  
├── README.md  
├── requirements.txt
├── db.sqlite3                            # prepopulated database
└── deals.csv                             # example csv-file
```

### URL structure
```
├── api/  
│ ├── upload-file/  
│ └── get-processed-data/  
└── admin/
```

### Tests absence

Please note that there are no tests in this project, since their writing was not included in the Scope of Work.

## Installation

### Docker-compose deploy

1. Create an image.
While in the directory where the Dockerfile and the docker-compose files are located, run the following command in the terminal:

  ``` bash
docker-compose build
```

2. Run the image.
In the terminal, run the command:

  ``` bash
docker-compose up
```

**N.B.** Please note that it is also possible to launch a project with a single command in the terminal:
  ``` bash
docker-compose up --build
```