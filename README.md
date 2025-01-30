# EBS Janitor - Automated Cleanup Script

## Overview
The **EBS Janitor** script automates the detection, backup, and deletion of orphaned EBS volumes in AWS. It helps reduce unnecessary storage costs by ensuring that unattached volumes older than seven days are identified, snapshotted for backup, and then deleted.

## Features
- **Find Orphaned Volumes**: Identifies unattached EBS volumes older than seven days.
- **Snapshot Creation**: Creates a backup snapshot before deleting volumes.
- **Tagging for Compliance**: Tags snapshots for tracking.
- **Automated Cleanup**: Deletes old volumes to free up storage.

## Prerequisites
- Python 3.x
- Boto3 (AWS SDK for Python)
- AWS CLI configured with appropriate permissions

## Installation
1. Clone the repository or download the script.
2. Install required dependencies:
   ```sh
   pip install boto3
   ```
3. Configure AWS credentials:
   ```sh
   aws configure
   ```

## Usage
Run the script using:
```sh
python ebs_cleanup_script.py
```

## AWS Permissions Required
Ensure the following AWS IAM permissions are granted:
- `ec2:DescribeVolumes`
- `ec2:CreateSnapshot`
- `ec2:DeleteVolume`
- `ec2:CreateTags`

## Notes
- The script will only delete volumes that have been unattached for more than seven days.
- Snapshots created will be tagged for tracking.

## License
This project is licensed under the MIT License.

## Contribution
Feel free to open issues or submit pull requests for improvements!
