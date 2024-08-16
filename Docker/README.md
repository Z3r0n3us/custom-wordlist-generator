# Docker Setup for Custom Wordlist Generator

This directory contains the Docker setup for the Custom Wordlist Generator tool.

## Building the Docker Image

1. Navigate to this directory:
   ```bash
   cd docker

Build the Docker image:
'''docker build -t wordlist-generator .
'''

Running the Docker Container

To run the container and see the help options:
'''docker run --rm wordlist-generator --help
'''

To generate a wordlist:
'''docker run --rm wordlist-generator --words admin root password --output my_wordlist.txt
'''
