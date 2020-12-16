# Data Engineering Project 2

## Create model

Run create\_model.py to get the model_file

## Build and run the container

Building the docker file:
```
docker build -t data-eng-proj2 .	
```

This will run the unit tests & the integration test.

To run the service, run the following command:  
```
docker run -p 5000:5000 data-eng-proj2
```

This will run website on port 5000

Go to [http://localhost:5000](http://localhost:5000) and start playing with the application!

If you want to monitor this application with Prometheus, open port 8010:
```
docker run -p 5000:5000 -p 8010:8010 data-eng-proj2
```

## Tests
Running the unit tests:
```
python test.py
```

Running the stress tests:
```
python stress_test.py
```

## Link to Trello
[https://trello.com/b/GBY14s2p/engineeringproject](https://trello.com/b/GBY14s2p/engineeringproject)

