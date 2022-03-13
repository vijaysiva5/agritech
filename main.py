from config import *
from auto_provision import *
from sys import exit

if __name__ == "__main__":

    # Step 1 : Reset/Delete all the existing things, certificates and policies registered in AWS IoT Core
    aws_iot_core_reset()

    # Step 2 : Reset/Delete all the existing buckets and their contents in AWS S3
    aws_s3_reset()

    # Step 3 : Create a provision file
    create_provision_file()

    # Step 4 : Configure the s3 bucket 
    aws_s3_config()

    # Step 5 : Create things in the Iot Core registry
    status = aws_iot_core_create_bulk_things()
    print(status)
    if not status: exit

    # Step 6 : Create certificates in the Iot Core registry
    aws_iot_core_create_certificates()

    # Step 7 : Create policy
    aws_iot_core_create_policy()

    # Step 8 : Attach everything
    aws_iot_core_attach_certificates()

    #Step 9 : Create IOT_Data table
    create_IOT_data_table()

    #Step 10: Create IOT_Relation table
    create_IOT_relation_table()

    #Step 11: Create Weather API feed table
    create_Weather_api_table()