#!/bin/bash
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
HOSPINC=$(echo $DATA | jq '.[0].hospitalizedIncrease')
DEATHINC=$(echo $DATA | jq '.[0].deathIncrease')
HOSPCURR=$(echo $DATA | jq '.[0].hospitalizedCurrently')

echo "On $TODAY, $HOSPINC amount of people entered a hospital, $DEATHINC amount of people died, and $HOSPCURR amount of people are currently hospitalized"
