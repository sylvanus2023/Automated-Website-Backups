import boto3

def find_buckets_with_tag(tag_key, tag_value):
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()

    matching_buckets = []

    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        try:
            tags = s3.get_bucket_tagging(Bucket=bucket_name)
            for tag in tags['TagSet']:
                if tag['Key'] == tag_key and tag['Value'] == tag_value:
                    matching_buckets.append(bucket_name)
        except s3.exceptions.NoSuchTagSet:
            # Bucket has no tags
            continue

    return matching_buckets

def delete_non_empty_bucket(bucket_name):
    s3 = boto3.client('s3')
    # Delete all objects
    objects = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in objects:
        for obj in objects['Contents']:
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
    
    # Delete all object versions (if versioning is enabled)
    versions = s3.list_object_versions(Bucket=bucket_name)
    if 'Versions' in versions:
        for version in versions['Versions']:
            s3.delete_object(Bucket=bucket_name, Key=version['Key'], VersionId=version['VersionId'])
    
    if 'DeleteMarkers' in versions:
        for marker in versions['DeleteMarkers']:
            s3.delete_object(Bucket=bucket_name, Key=marker['Key'], VersionId=marker['VersionId'])
    
    # Delete the bucket
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} has been deleted.")

if __name__ == "__main__":
    tag_key = "Name"
    tag_value = "careunlocked-backups"
    buckets = find_buckets_with_tag(tag_key, tag_value)
    if buckets:
        print(f"Buckets with tag {tag_key}={tag_value}: {buckets}")
        delete_confirmation = input("Do you want to delete these buckets? (yes/no): ")
        if delete_confirmation.lower() == "yes":
            for bucket in buckets:
                try:
                    delete_non_empty_bucket(bucket)
                except Exception as e:
                    print(f"Error deleting bucket {bucket}: {e}")
        else:
            print("Buckets not deleted")
    else:
        print(f"No buckets found with tag {tag_key}={tag_value}")
