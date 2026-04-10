import socket
import struct


def send_wol(mac_address: str) -> bool:
    """Send a Wake-on-LAN magic packet to the given MAC address."""
    if not mac_address:
        raise ValueError("MAC address is required")

    # Normalize MAC address to 12 hex digits
    mac_address = mac_address.replace("-", "").replace(":", "").lower()
    if len(mac_address) != 12 or not all(c in "0123456789abcdef" for c in mac_address):
        raise ValueError("Invalid MAC address format")

    try:
        mac_bytes = bytes.fromhex(mac_address)
        packet = b"\xff" * 6 + mac_bytes * 16

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(packet, ("255.255.255.255", 9))

        return True
    except Exception as exc:
        raise RuntimeError(f"Failed to send Wake-on-LAN packet: {exc}") from exc
