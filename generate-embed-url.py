import boto3
from botocore.exceptions import  ConnectionError, ClientError
import logging
import requests

def create_connection():
    try:
        print('CONNECTING')
        qs = boto3.client('quicksight', region_name=QSREGION) # TODO: Replace with the region in which your quicksight is configured
        return qs
    except  ConnectionError as e:
        print(e)
        logger.error("Error occured in connecting to qs: {}".format(e))
    except  Exception as e:
        print(e)
        logger.error("Unknown error occured: {}".format(e))

def getDashboardURL(dashboard_id, dashboard_namespace):
    
    qs = create_connection()
    print('Conn created')
    try:
        response = qs.get_dashboard_embed_url(
            AwsAccountId = AWS_ACCOUNT_ID, # TODO: Replace with your AWS Account ID
            DashboardId = dashboard_id, # TODO: Replace with your QuickSight Dashboard ID
            Namespace = "default", # TODO: Replace with your QuickSight Dashboard Namespace (if any)
            IdentityType = "QUICKSIGHT",
            UserArn = QUICKSIGHT_USER_ARN # TODO: Replace with your USER ARN which has access to QuickSight
        )
        return response['EmbedUrl']
    except ClientError as e:
        print(e)
        return "Error generating embeddedURL: " + str(e)
    except Exception as er:
        print(er)
