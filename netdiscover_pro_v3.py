#!/usr/bin/env python3

import scapy.all as scapy
import socket
import netifaces
import threading
import json
from queue import Queue
from rich.console import Console
from rich.table import Table

console = Console()

PORT_RANGE = range(1, 1025)
RISKY_PORTS = [21, 23, 445, 3389]

def get_network():
    iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
    ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
    ip_parts = ip.split(".")
    network = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"
    return network, iface

def arp_scan(network, iface):
    arp = scapy.ARP(pdst=network)
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = scapy.srp(packet, timeout=2, iface=iface, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "ttl": received.ttl
        })
    return devices

def port_worker(ip, queue, open_ports):
    while not queue.empty():
        port = queue.get()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            if sock.connect_ex((ip, port)) == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass
        queue.task_done()

def threaded_port_scan(ip):
    queue = Queue()
    open_ports = []

    for port in PORT_RANGE:
        queue.put(port)

    threads = []
    for _ in range(50):
        t = threading.Thread(target=port_worker, args=(ip, queue, open_ports))
        t.daemon = True
        t.start()
        threads.append(t)

    queue.join()
    return open_ports

def banner_grab(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = sock.recv(1024).decode(errors="ignore")
        sock.close()
        return banner.strip()
    except:
        return ""

def detect_camera(open_ports, ip):
    if 554 in open_ports:
        return "IP Camera (RTSP)"
    if 8080 in open_ports or 8000 in open_ports:
        banner = banner_grab(ip, 8080)
        if "camera" in banner.lower():
            return "Web Camera"
    return None

def detect_device_type(open_ports):
    if 445 in open_ports:
        return "Windows PC"
    if 22 in open_ports:
        return "Linux/Server"
    if 80 in open_ports or 443 in open_ports:
        return "Web Device"
    return "Unknown"

def detect_os(ttl):
    if ttl >= 120:
        return "Windows (Guess)"
    elif ttl >= 60:
        return "Linux/Unix (Guess)"
    else:
        return "Unknown"

def calculate_risk(open_ports):
    score = 0
    for port in open_ports:
        if port in RISKY_PORTS:
            score += 2
        else:
            score += 1
    return score

def main():
    console.print("[bold green]NetDiscover Pro v3 - Advanced Network Scanner[/bold green]\n")

    network, iface = get_network()
    console.print(f"Scanning Network: {network}\n")

    devices = arp_scan(network, iface)

    table = Table(title="Network Devices")
    table.add_column("IP")
    table.add_column("Open Ports")
    table.add_column("Device Type")
    table.add_column("OS Guess")
    table.add_column("Risk")
    table.add_column("Camera Detection")

    report_data = []

    for device in devices:
        ports = threaded_port_scan(device["ip"])
        device_type = detect_device_type(ports)
        os_guess = detect_os(device["ttl"])
        risk = calculate_risk(ports)
        camera = detect_camera(ports, device["ip"])

        table.add_row(
            device["ip"],
            str(len(ports)),
            device_type,
            os_guess,
            str(risk),
            camera if camera else "-"
        )

        report_data.append({
            "ip": device["ip"],
            "mac": device["mac"],
            "open_ports": ports,
            "device_type": device_type,
            "os_guess": os_guess,
            "risk_score": risk,
            "camera_detection": camera
        })

    console.print(table)
    console.print(f"\nTotal Devices Found: {len(devices)}")

    with open("scan_report.json", "w") as f:
        json.dump(report_data, f, indent=4)

    console.print("\nReport saved as scan_report.json")

if __name__ == "__main__":
    main()
