def create_cmk(desc='Customer Master Key'):
    """Create a KMS Customer Master Key

    The created CMK is a Customer-managed key stored in AWS KMS.

    :param desc: key description
    :return Tuple(KeyId, KeyArn) where:
        KeyId: AWS globally-unique string ID
        KeyArn: Amazon Resource Name of the CMK
    :return Tuple(None, None) if error
    """

    # Create CMK
    kms_client = boto3.client('kms')
    try:
        response = kms_client.create_key(Description=desc)
    except ClientError as e:
        logging.error(e)
        return None, None

    # Return the key ID and ARN
    return response['KeyMetadata']['KeyId'], response['KeyMetadata']['Arn']
