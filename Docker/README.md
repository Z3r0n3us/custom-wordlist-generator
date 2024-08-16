# Docker Setup for Custom Wordlist Generator

This directory contains the Docker setup for the Custom Wordlist Generator tool.

## Building the Docker Image

1. Navigate to this directory:
   ```bash
   cd docker

2. Build the Docker image:
   ```bash
   docker build -t wordlist-generator .

## Running the Docker Container

3. To run the container and see the help options:
   ```bash
   docker run --rm wordlist-generator --help

## Example:
To generate a wordlist:
docker run --rm wordlist-generator --words admin root password --output my_wordlist.txt

