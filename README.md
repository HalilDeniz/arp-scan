# arp-scan

This is a very simple Python ARP scanner. It uses Python 3 and can be used to determine available devices on a network.

## Requirements

- Python 3.x
- Scapy library
- Colorama library

You can install the required libraries using pip:

```bash
pip install scapy colorama
```

## Usage

The script takes two arguments:
1. Your network interface (e.g., `ens33` or `eth0`)
2. The IP or IP address range you would like to scan (e.g., `192.168.10.15` or `192.168.10.0/24`)

### Example

To run the script, use the following command:

```bash
python arp-scan.py <interface> <ip_range>
```

For example:

```bash
python arp-scan.py ens33 192.168.217.0/24
```

### Expected Output

The output will display the scanning process and list the IP-MAC pairs of devices found on the network. The output may vary based on the devices connected to your network:

```
[*] Scanning...

[*] IP - MAC
192.168.217.1 - 00:50:56:c0:00:08
192.168.217.2 - 00:50:56:f7:37:a2
192.168.217.142 - 00:0c:29:76:96:d6
192.168.217.147 - 00:0c:29:bd:c1:63
192.168.217.254 - 00:50:56:e8:cd:79

[*] Scan Complete. Duration: 0:00:28.120490
```

## Notes

- Ensure you have the necessary permissions to run ARP scans on your network.
- This script is intended for educational purposes and should be used responsibly.

## Additional Resources

For more information on ARP discovery and to learn how to create your own ARP discovery tool in Python, please visit [this article](https://denizhalil.com/2024/11/18/arp-discovery-tool-python/).
