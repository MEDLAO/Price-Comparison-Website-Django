import boto3
from botocore.exceptions import ClientError
import os


def get_ssm_parameter(name, with_decryption=True):
    """Fetch a parameter from AWS SSM Parameter Store."""
    ssm = boto3.client('ssm', region_name='eu-west-3')
    try:
        parameter = ssm.get_parameter(Name=name, WithDecryption=with_decryption)
        return parameter['Parameter']['Value']
    except ClientError as e:
        print(f"Error fetching {name} from SSM: {e}")
        return None


def get_env_or_ssm(var_name, ssm_param_name=None, default=None):
    """Fetch from environment variable or AWS SSM if not found in env."""
    value = os.getenv(var_name)
    if value:
        print(f"Using environment variable for {var_name}")
        return value or default
    else:
        print(f"Environment variable {var_name} not set. Fetching from SSM for {ssm_param_name}")
        value = get_ssm_parameter(ssm_param_name)
        return value or default
