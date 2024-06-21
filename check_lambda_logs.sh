#!/bin/bash

LAMBDA_FUNCTIONS_FILE="lambda_functions.txt"

if [ ! -f "$LAMBDA_FUNCTIONS_FILE" ]; then
  echo "Arquivo $LAMBDA_FUNCTIONS_FILE não encontrado!"
  exit 1
fi

get_last_log_event() {
  local log_group_name=$1
  aws logs describe-log-streams --log-group-name "$log_group_name" --order-by LastEventTime --descending --limit 1 --query 'logStreams[0].lastEventTimestamp' --output text
}

while IFS= read -r function_name; do

  log_group_name="/aws/lambda/$function_name"

  last_log_event=$(get_last_log_event "$log_group_name")
  if [ "$last_log_event" == "None" ] || [ -z "$last_log_event" ]; then
    echo "No logs could be found for the group $log_group_name"
  else
    last_log_event_date=$(date -d @$((last_log_event / 1000)) +"%Y-%m-%d %H:%M:%S")
    echo "Last event on group $log_group_name: $last_log_event_date"
  fi

done < "$LAMBDA_FUNCTIONS_FILE"
