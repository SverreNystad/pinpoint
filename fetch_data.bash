#!/bin/bash
curl -L -o ./data/google-street-view.zip \
  https://www.kaggle.com/api/v1/datasets/download/paulchambaz/google-street-view

# Unzip into ./data and overwrite existing files if needed
unzip -o ./data/google-street-view.zip -d ./data

# (Optional) Remove the zip file after extraction
rm ./data/google-street-view.zip