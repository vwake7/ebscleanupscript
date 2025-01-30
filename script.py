import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')

def find_orphaned_volumes():
    volumes = ec2.describe_volumes(
        Filters=[
            {'Name': 'status', 'Values': ['available']}
        ]
    )
    orphaned_volumes = [v for v in volumes['Volumes'] 
                         if (datetime.now(tz=v['CreateTime'].tzinfo) - v['CreateTime']).days > 7]
    return orphaned_volumes

def create_snapshots(volumes):
    snapshots = []
    for volume in volumes:
        snapshot = ec2.create_snapshot(
            VolumeId=volume['VolumeId'],
            Description=f"Backup of orphaned volume {volume['VolumeId']} before deletion"
        )
        snapshots.append(snapshot['SnapshotId'])
    return snapshots

def delete_old_volumes(volumes):
    for volume in volumes:
        ec2.delete_volume(VolumeId=volume['VolumeId'])
        print(f"Deleted volume: {volume['VolumeId']}")

def tag_snapshots(snapshots):
    for snapshot_id in snapshots:
        ec2.create_tags(
            Resources=[snapshot_id],
            Tags=[{'Key': 'EBS-Janitor', 'Value': 'Automated-Cleanup'}]
        )

def main():
    orphaned_volumes = find_orphaned_volumes()
    if not orphaned_volumes:
        print("No orphaned volumes found.")
        return
    
    print(f"Found {len(orphaned_volumes)} orphaned volumes.")
    snapshots = create_snapshots(orphaned_volumes)
    print(f"Created {len(snapshots)} snapshots for backup.")
    tag_snapshots(snapshots)
    delete_old_volumes(orphaned_volumes)
    print("Cleanup complete.")

if __name__ == "__main__":
    main()
