import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Headers provided by the user
headers = [
    "VM", "Powerstate", "Template", "SRM Placeholder", "Config status", "DNS Name",
    "Connection state", "Guest state", "Heartbeat", "Consolidation Needed", "PowerOn",
    "Suspend time", "Creation date", "Change Version", "CPUs", "Memory", "NICs",
    "Disks", "Total disk capacity MiB", "min Required EVC Mode Key", "Latency Sensitivity",
    "EnableUUID", "CBT", "Primary IP Address", "Network #1", "Network #2", "Network #3",
    "Network #4", "Network #5", "Network #6", "Network #7", "Network #8", "Num Monitors",
    "Video Ram KiB", "Resource pool", "Folder ID", "Folder", "vApp", "DAS protection",
    "FT State", "FT Role", "FT Latency", "FT Bandwidth", "FT Sec. Latency", "Provisioned MiB",
    "In Use MiB", "Unshared MiB", "HA Restart Priority", "HA Isolation Response",
    "HA VM Monitoring", "Cluster rule(s)", "Cluster rule name(s)", "Boot Required",
    "Boot delay", "Boot retry delay", "Boot retry enabled", "Boot BIOS setup",
    "Reboot PowerOff", "EFI Secure boot", "Firmware", "HW version", "HW upgrade status",
    "HW upgrade policy", "HW target", "Path", "Log directory", "Snapshot directory",
    "Suspend directory", "Annotation", "CitrixProvisioningSchemeId", "com.vrlcm.snapshot",
    "ent_patching_role", "ent_patching_role_stages", "Rubrik_LastBackup", "XdConfig",
    "ent-support-group", "ent-opco", "ent-app-name", "ent-apm-id", "ent-rubrick-backup-tier",
    "ent-owner", "ent-patch-schedule", "ent-env", "openshift-dall-om-001-prd-9zsg5",
    "ent-info-type", "ent-info-class", "Datacenter", "Cluster", "Host",
    "OS according to the configuration file", "OS according to the VMware Tools", "VM ID",
    "SMBIOS UUID", "VM UUID", "VI SDK Server type", "VI SDK API Version", "VI SDK Server",
    "VI SDK UUID"
]

# Value pools inspired by the provided content and typical VM attributes
powerstate_options = ["poweredOn", "poweredOff", "suspended"]
template_options = ["True", "False"]
srm_placeholder_options = ["Yes", "No"]
config_status_options = ["green", "yellow", "red"]
dns_name_options = [fake.domain_name() for _ in range(100)]
connection_state_options = ["connected", "disconnected", "inaccessible"]
guest_state_options = ["running", "notRunning", "unknown"]
heartbeat_options = ["green", "yellow", "red", "gray"]
consolidation_needed_options = ["True", "False"]
latency_sensitivity_options = ["High", "Medium", "Low"]
enableuuid_options = ["Yes", "No"]
cbt_options = ["Enabled", "Disabled"]
network_options = [f"Network-{i}" for i in range(1, 9)]
resource_pool_options = [fake.word() for _ in range(50)]
folder_options = [fake.word() for _ in range(50)]
ha_priority_options = ["High", "Medium", "Low"]
ha_isolation_response_options = ["Power Off", "Leave Powered On", "Shut Down"]
vapp_options = ["Yes", "No"]
datacenter_options = [fake.city() for _ in range(20)]
cluster_options = [fake.word() for _ in range(20)]
host_options = [fake.hostname() for _ in range(50)]
os_options = ["Windows", "Linux", "Ubuntu", "CentOS"]
firmware_options = ["BIOS", "EFI"]
hw_upgrade_status_options = ["Up-to-date", "Outdated"]
hw_upgrade_policy_options = ["Manual", "Automatic"]

# Generate a specified number of rows of data
def generate_vm_data(num_rows=100):
    rows = []
    for _ in range(num_rows):
        row = {
            "VM": fake.hostname(),
            "Powerstate": random.choice(powerstate_options),
            "Template": random.choice(template_options),
            "SRM Placeholder": random.choice(srm_placeholder_options),
            "Config status": random.choice(config_status_options),
            "DNS Name": random.choice(dns_name_options),
            "Connection state": random.choice(connection_state_options),
            "Guest state": random.choice(guest_state_options),
            "Heartbeat": random.choice(heartbeat_options),
            "Consolidation Needed": random.choice(consolidation_needed_options),
            "PowerOn": fake.date_time_this_year(),
            "Suspend time": fake.date_time_this_year(),
            "Creation date": fake.date_this_decade(),
            "Change Version": fake.iso8601(),
            "CPUs": random.randint(1, 16),
            "Memory": random.randint(1024, 65536),  # Memory in MB
            "NICs": random.randint(1, 4),
            "Disks": random.randint(1, 8),
            "Total disk capacity MiB": random.randint(1024, 1048576),
            "min Required EVC Mode Key": random.choice(["Intel", "AMD", "None"]),
            "Latency Sensitivity": random.choice(latency_sensitivity_options),
            "EnableUUID": random.choice(enableuuid_options),
            "CBT": random.choice(cbt_options),
            "Primary IP Address": fake.ipv4(),
            "Network #1": random.choice(network_options),
            "Network #2": random.choice(network_options),
            "Network #3": random.choice(network_options),
            "Network #4": random.choice(network_options),
            "Network #5": random.choice(network_options),
            "Network #6": random.choice(network_options),
            "Network #7": random.choice(network_options),
            "Network #8": random.choice(network_options),
            "Num Monitors": random.randint(1, 3),
            "Video Ram KiB": random.randint(1024, 8192),
            "Resource pool": random.choice(resource_pool_options),
            "Folder ID": fake.uuid4(),
            "Folder": random.choice(folder_options),
            "vApp": random.choice(vapp_options),
            "DAS protection": random.choice(["Enabled", "Disabled"]),
            "FT State": random.choice(["Enabled", "Disabled"]),
            "FT Role": random.choice(["Primary", "Secondary"]),
            "FT Latency": round(random.uniform(0.1, 10.0), 2),
            "FT Bandwidth": round(random.uniform(10.0, 1000.0), 2),
            "FT Sec. Latency": round(random.uniform(0.01, 5.0), 2),
            "Provisioned MiB": random.randint(1024, 1048576),
            "In Use MiB": random.randint(1024, 1048576),
            "Unshared MiB": random.randint(1024, 1048576),
            "HA Restart Priority": random.choice(ha_priority_options),
            "HA Isolation Response": random.choice(ha_isolation_response_options),
            "HA VM Monitoring": random.choice(["Enabled", "Disabled"]),
            "Cluster rule(s)": fake.word(),
            "Cluster rule name(s)": fake.word(),
            "Boot Required": random.choice(["Yes", "No"]),
            "Boot delay": random.randint(0, 60),
            "Boot retry delay": random.randint(0, 60),
            "Boot retry enabled": random.choice(["Yes", "No"]),
            "Boot BIOS setup": random.choice(["Enabled", "Disabled"]),
            "Reboot PowerOff": random.choice(["Yes", "No"]),
            "EFI Secure boot": random.choice(["Enabled", "Disabled"]),
            "Firmware": random.choice(firmware_options),
            "HW version": random.randint(1, 15),
            "HW upgrade status": random.choice(hw_upgrade_status_options),
            "HW upgrade policy": random.choice(hw_upgrade_policy_options),
            "HW target": fake.word(),
            "Path": fake.file_path(),
            "Log directory": fake.file_path(),
            "Snapshot directory": fake.file_path(),
            "Suspend directory": fake.file_path(),
            "Annotation": fake.sentence(),
            "CitrixProvisioningSchemeId": fake.uuid4(),
            "com.vrlcm.snapshot": random.choice(["Enabled", "Disabled"]),
            "ent_patching_role": fake.word(),
            "ent_patching_role_stages": fake.word(),
            "Rubrik_LastBackup": fake.date_time_this_year(),
            "XdConfig": fake.word(),
            "ent-support-group": fake.word(),
            "ent-opco": fake.word(),
            "ent-app-name": fake.word(),
            "ent-apm-id": fake.word(),
            "ent-rubrick-backup-tier": fake.word(),
            "ent-owner": fake.name(),
            "ent-patch-schedule": fake.word(),
            "ent-env": fake.word(),
            "openshift-dall-om-001-prd-9zsg5": fake.word(),
            "ent-info-type": fake.word(),
            "ent-info-class": fake.word(),
            "Datacenter": random.choice(datacenter_options),
            "Cluster": random.choice(cluster_options),
            "Host": random.choice(host_options),
            "OS according to the configuration file": random.choice(os_options),
            "OS according to the VMware Tools": random.choice(os_options),
            "VM ID": fake.uuid4(),
            "SMBIOS UUID": fake.uuid4(),
            "VM UUID": fake.uuid4(),
            "VI SDK Server type": random.choice(["vCenter", "ESXi"]),
            "VI SDK API Version": f"{random.randint(6, 7)}.0",
            "VI SDK Server": fake.hostname(),
            "VI SDK UUID": fake.uuid4()
        }
        rows.append(row)

    return pd.DataFrame(rows, columns=headers)

# Example usage: Generate 100 rows and save to CSV
example_df = generate_vm_data(10000)
output_path = "./rvtools_generated_data.csv"
example_df.to_csv(output_path, index=False)
output_path
