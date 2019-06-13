#!/bin/bash

docker build . -t log_thingie

docker run -it -p 8000:8000 log_thingie
