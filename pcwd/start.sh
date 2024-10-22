#!/bin/sh
# Fetch and export environment variables from AWS SSM

export PROD_SECRET_KEY=$(aws ssm get-parameter --name /pcwd/PROD_SECRET_KEY --with-decryption --query 'Parameter.Value' --output text --region eu-west-3 --no-cli-pager)
echo "PROD_SECRET_KEY fetched: $PROD_SECRET_KEY"

export PROD_DB_NAME=$(aws ssm get-parameter --name /pcwd/PROD_DB_NAME --with-decryption --query 'Parameter.Value' --output text --region eu-west-3 --no-cli-pager)
echo "PROD_DB_NAME fetched: $PROD_DB_NAME"

export PROD_DB_USER=$(aws ssm get-parameter --name /pcwd/PROD_DB_USER --with-decryption --query 'Parameter.Value' --output text --region eu-west-3 --no-cli-pager)
echo "PROD_DB_USER fetched: $PROD_DB_USER"

export PROD_DB_PASSWORD=$(aws ssm get-parameter --name /pcwd/PROD_DB_PASSWORD --with-decryption --query 'Parameter.Value' --output text --region eu-west-3 --no-cli-pager)
echo "PROD_DB_PASSWORD fetched: $PROD_DB_PASSWORD"

export PROD_DB_HOST=$(aws ssm get-parameter --name /pcwd/PROD_DB_HOST --with-decryption --query 'Parameter.Value' --output text --region eu-west-3 --no-cli-pager)
echo "PROD_DB_HOST fetched: $PROD_DB_HOST"

export PROD_DB_PORT=$(aws ssm get-parameter --name /pcwd/PROD_DB_PORT --with-decryption --query 'Parameter.Value' --output text --region eu-west-3 --no-cli-pager)
echo "PROD_DB_PORT fetched: $PROD_DB_PORT"

export AWS_SES_EMAIL_HOST=$(aws ssm get-parameter --name /pcwd/AWS_SES_EMAIL_HOST --with-decryption --query 'Parameter.Value' --output text --region eu-west-3 --no-cli-pager)
echo "AWS_SES_EMAIL_HOST fetched: $AWS_SES_EMAIL_HOST"

export AWS_SES_SMTP_USER=$(aws ssm get-parameter --name /pcwd/AWS_SES_SMTP_USER --with-decryption --query 'Parameter.Value' --output text --region eu-west-3 --no-cli-pager)
echo "AWS_SES_SMTP_USER fetched: $AWS_SES_SMTP_USER"

export AWS_SES_SMTP_PASSWORD=$(aws ssm get-parameter --name /pcwd/AWS_SES_SMTP_PASSWORD --with-decryption --query 'Parameter.Value' --output text --region eu-west-3 --no-cli-pager)
echo "AWS_SES_SMTP_PASSWORD fetched: $AWS_SES_SMTP_PASSWORD"

export AWS_REDIS_ENDPOINT=$(aws ssm get-parameter --name /pcwd/AWS_REDIS_ENDPOINT --with-decryption --query 'Parameter.Value' --output text --region eu-west-3 --no-cli-pager)
echo "AWS_REDIS_ENDPOINT fetched: $AWS_REDIS_ENDPOINT"

export AWS_REDIS_PASSWORD=$(aws ssm get-parameter --name /pcwd/AWS_REDIS_PASSWORD --with-decryption --query 'Parameter.Value' --output text --region eu-west-3 --no-cli-pager)
echo "AWS_REDIS_PASSWORD fetched: $AWS_REDIS_PASSWORD"

export GOOGLE_API_CLIENT_ID=$(aws ssm get-parameter --name /pcwd/GOOGLE_API_CLIENT_ID --with-decryption --query 'Parameter.Value' --output text --region eu-west-3 --no-cli-pager)
echo "GOOGLE_API_CLIENT_ID fetched: $GOOGLE_API_CLIENT_ID"

export GOOGLE_API_SECRET=$(aws ssm get-parameter --name /pcwd/GOOGLE_API_SECRET --with-decryption --query 'Parameter.Value' --output text --region eu-west-3 --no-cli-pager)
echo "GOOGLE_API_SECRET fetched: $GOOGLE_API_SECRET"


# Start Gunicorn
exec gunicorn pcwd.wsgi:application --bind 0.0.0.0:8000
