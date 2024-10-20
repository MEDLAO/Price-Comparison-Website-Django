#!/bin/sh
set -x  # Enable debug mode to print each command


# Fetch AWS SSM parameters by path (/pcwd/), iterate over each parameter name
for param in $(aws ssm get-parameters-by-path --path /pcwd/ --with-decryption --query 'Parameters[*].Name' --output text); do

  # Remove the "/pcwd/" prefix from the parameter name to use it as the environment variable key
  key=$(echo $param | sed 's/\/pcwd\///');

  # Fetch the parameter value using its name, decrypting it if necessary
  value=$(aws ssm get-parameter --name "$param" --with-decryption --query 'Parameter.Value' --output text);

  # Check if the value is empty; if so, print an error and exit the script
  if [ -z "$value" ]; then
    echo "Error: Missing value for $key from AWS SSM"
    exit 1
  fi

  # Export the parameter as an environment variable using the key-value pair
  export $key="$value";
done

# Start Gunicorn after retrieving the environment variables
exec gunicorn pcwd.wsgi:application --bind 0.0.0.0:8000
