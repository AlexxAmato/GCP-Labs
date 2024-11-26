import os
import subprocess

def run_command(command):
    """Runs a shell command and checks for errors."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        exit(1)

def update_and_upgrade():
    print("Updating and upgrading the system...")
    run_command("apt update && apt upgrade -y")

def install_dependencies():
    print("Installing dependencies...")
    dependencies = [
        "qemu-kvm", "libvirt-bin", "ubuntu-vm-builder", "bridge-utils",
        "tcpdump", "lib32z1", "lib32ncurses6", "libbz2-1.0:i386",
        "curl", "nano", "unzip", "genisoimage", "gawk", "jq",
        "apache2", "xterm", "gcc", "make", "git", "ccache",
        "software-properties-common", "libssl-dev", "libelf-dev",
        "linux-headers-$(uname -r)", "cgroup-tools", "ethtool"
    ]
    run_command(f"apt install -y {' '.join(dependencies)}")

def configure_network():
    print("Configuring the network...")
    # Adjust these configurations if necessary for your network
    netplan_config = """
    network:
      version: 2
      renderer: networkd
      ethernets:
        eth0:
          dhcp4: true
    """
    with open("/etc/netplan/01-netcfg.yaml", "w") as netplan_file:
        netplan_file.write(netplan_config)
    run_command("netplan apply")

def install_eve_ng():
    print("Installing EVE-NG...")
    # Add EVE-NG repository
    run_command("apt install -y wget")
    run_command("wget -O - http://www.eve-ng.net/focal.gpg | apt-key add -")
    run_command('echo "deb [trusted=yes] http://www.eve-ng.net/focal focal main" > /etc/apt/sources.list.d/eve-ng.list')
    run_command("apt update")

    # Install EVE-NG
    run_command("apt install -y eve-ng")

    # Post-install configuration
    print("Configuring EVE-NG...")
    run_command("eve-ng-cp")
    run_command("systemctl enable eve-ng")
    run_command("systemctl start eve-ng")

def setup_firewall():
    print("Setting up the firewall...")
    run_command("ufw allow 80/tcp")
    run_command("ufw allow 443/tcp")
    run_command("ufw allow 22/tcp")
    run_command("ufw --force enable")

def main():
    print("Starting EVE-NG installation...")
    update_and_upgrade()
    install_dependencies()
    configure_network()
    install_eve_ng()
    setup_firewall()
    print("EVE-NG installation completed successfully!")

if __name__ == "__main__":
    main()

