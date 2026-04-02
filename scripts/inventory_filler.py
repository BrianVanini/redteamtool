import os

def get_live_ips(subnet):
    # Quick ping sweep to see who is alive
    print(f"[*] Scanning {subnet} for active Blue Team targets...")
    live_hosts = os.popen(f"fping -ag {subnet} 2>/dev/null").read().splitlines()
    return live_hosts

def write_inventory(ips):
    with open("inventory.ini", "w") as f:
        f.write("[blue_team]\n")
        for ip in ips:
            f.write(f"{ip}\n")
        f.write("\n[blue_team:vars]\n")
        f.write("ansible_user=ubuntu\n")
        f.write("ansible_ssh_common_args='-o StrictHostKeyChecking=no'\n")

if __name__ == "__main__":
    targets = get_live_ips("10.10.10.45,/24") # Adjust to your competition subnet
    write_inventory(targets)
    print(f"[+] Created inventory.ini with {len(targets)} hosts.")