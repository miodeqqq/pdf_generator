#!/bin/sh

clear; docker build . -t pdf_generator && docker-compose -f docker-compose.yml -p 'pdf_generator' up --remove-orphans