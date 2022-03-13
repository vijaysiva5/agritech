import sys
import logging

# Local directory paths and file names
PROVISION_FILE_NAME = "provisioning-data.json"
THING_CREATION_FILE_NAME = "thing-creation.json"
POLICY_FILE_NAME = "general_policy.json"
PROVISIONING_TEMPLATE = 'provisioning-template.json'

PATH_TO_PROVISION= '../secure/provision/'+PROVISION_FILE_NAME
PATH_TO_THING_CREATION= '../secure/provision/'+THING_CREATION_FILE_NAME
PATH_TO_POLICY = '../secure/policy/'+POLICY_FILE_NAME
PATH_TO_PROVISIONING_TEMPLATE = '../secure/provision/' + PROVISIONING_TEMPLATE

# AWS IoT Core Region
IOT_CORE_REGION = "us-east-1"

# AWS IoT Core - Parameters used for creating thing(s) and thing type
THING_TYPE_NAME = "SmartFarm"
THING_NAME_PREFIX = "Sensor"
THING_GROUP_PREFIX = "Sub-Farm"
THING_COUNT = 25

# AWS IoT Core - Parameters used for the MQTT Connection
MQTT_ENDPOINT = "a1u3xldc4v4kx2-ats.iot.us-east-1.amazonaws.com"
PATH_TO_ROOT_CA = "../secure/ca/AmazonRootCA1.pem"
MQTT_PORT = 8883
MQTT_TOPIC = "iot/SensorFeed"

# AWS IoT Core - Parameter used for creating certificates(s)
SET_CERT_UNIQUE = True


# AWS S3 - Paremeters used to set up a  S3 bucket 
S3_REGION = "us-east-1"
S3_BUCKET= 'sf-iot'
ROLE_ARN = "arn:aws:iam::555122611600:role/SF_IOT_Role"
BUCKET_NAME = "sf-iot-config"

# AWS Kinesis - Setup parameters

KINESIS_DATA_STREAM = "Sensor_data_stream"

kinesis_handle = boto3.client('kinesis', region_name = "us-east-1")

OBJ_PROVISION_FILE= PROVISION_FILE_NAME

# Logger Settings
logger_aws_iot_core = logging.getLogger('example_logger')
logger_aws_iot_core.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler_aws_iot_core = logging.StreamHandler(sys.stdout)
log_format_aws_iot_core = logging.Formatter('%(asctime)s - %(levelname)s - AWS-IOT-CORE - %(message)s',datefmt='%H:%M:%S')
log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
handler_aws_iot_core.setFormatter(log_format_aws_iot_core)
handler.setFormatter(log_format)
logger_aws_iot_core.addHandler(handler_aws_iot_core)