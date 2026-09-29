# Networking fundamentals

Based on *Computer Networking Bible* (Worley, 2024), Part I. Where the book contains an error, the corrected fact is given and marked ✎.

## Core concepts

- **Networking:** exchanging data between nodes (computers, servers, phones, IoT) over copper, fiber or wireless media, using standard protocols that define how data is packaged, addressed and delivered.
- **Topology:** the physical or logical layout of a network.
- **Protocols:** the rules for formatting, sending and receiving data (TCP/IP, HTTP, FTP, SMTP).
- **IP addressing:** a unique identifier for each device (IPv4 or IPv6).
- **Network security:** protecting confidentiality, integrity and availability (the "CIA triad").
- **History:**
  - 1960s: ARPANET.
  - 1970s–80s: LANs and Ethernet.
  - 1990s: the World Wide Web, HTML and browsers.
  - 2000s: Wi-Fi and cellular, smartphones.
  - 2010s onward: IoT, cloud, edge, SDN.
- **Why it matters:** business (e-commerce, remote work, supply chains), education (online learning), healthcare (telemedicine, EHRs), entertainment (streaming, gaming), and AI/ML/blockchain, which all depend on moving large amounts of data.

## Models

### OSI reference model (ISO)
✎ Work began in the late 1970s and the model was published in 1984. The book says 1974.

| # | Layer | Function | Examples |
|---|---|---|---|
| 7 | Application | Network services to applications | HTTP, SMTP, DNS, FTP |
| 6 | Presentation | Encoding, encryption, compression | TLS (often placed here), JPEG |
| 5 | Session | Opening, maintaining and closing sessions | RPC, session control |
| 4 | Transport | End-to-end delivery, segmentation, flow control, reliability | TCP, UDP |
| 3 | Network | Logical addressing and routing | IP, ICMP, OSPF, BGP |
| 2 | Data link | Framing, MAC addressing, error detection, media access (LLC and MAC sublayers) | Ethernet, 802.11, switches, bridges |
| 1 | Physical | Bits on the medium: signalling, connectors, cables, radio | Cables, hubs, repeaters, transceivers |

Layers 1–3 (the "interface" layers) change slowly, so a network built today resembles one built ten years ago at those layers. Layers 4–7 have changed much more.

### TCP/IP model
Link (L1–2) → Internet (IP) → Transport (TCP/UDP) → Application (L5–7). TCP/IP splits data into packets, then addresses, routes and reassembles them. It is designed to survive device failures with minimal central management.

## Ethernet standards (IEEE 802.3)

Naming pattern: **speed + signalling + medium/distance**. For example, "100BASE-T" means 100 Mbps, baseband signalling, twisted pair. A trailing number means segment length in hundreds of meters (for example 10BASE5 = 500 m).

| Standard | Name | Medium | Speed | Notes |
|---|---|---|---|---|
| 10BASE2 | ThinNet | Thin coax | 10 Mbps | ~185–200 m. Obsolete. |
| 10BASE5 | ThickNet | Thick coax | 10 Mbps | 500 m. Obsolete. |
| 10BASE-T | — | UTP Cat3+ | 10 Mbps | Hubs: physical star, logical bus, collisions. Obsolete. The **5-4-3 rule** allowed at most 4 repeaters/hubs between stations. |
| 10BASE-F | — | Fiber | 10 Mbps | Obsolete. |
| 100BASE-T4 | — | Cat3, 4 pairs | 100 Mbps | Upgrade path for Cat3 cabling. Obsolete. |
| 100BASE-TX | Fast Ethernet | Cat5+, 2 pairs | 100 Mbps | Still common at the edge. |
| 100BASE-FX | Fast Ethernet over fiber | Multimode fiber | 100 Mbps | LED sources; distance limited by modal dispersion. |
| 1000BASE-T | Gigabit Ethernet | Cat5e+, all 4 pairs | 1 Gbps | Today's default for access ports. |
| 1000BASE-SX/LX | Gigabit over fiber | MMF / SMF | 1 Gbps | |
| 10GBASE-T | 10 Gigabit Ethernet | Cat6a (Cat6 up to ~55 m), 4 pairs | 10 Gbps | Full duplex only. Used for uplinks, backbones and servers. |

Duplex: **half duplex** sends one direction at a time (and suffers collisions); **full duplex** sends both directions at once. **Simplex** is one direction only.

## Wireless standards (IEEE 802.11 / Wi-Fi)

| Standard | Wi-Fi name | Year | Band | Max rate (theoretical) |
|---|---|---|---|---|
| 802.11 | — | 1997 | 2.4 GHz | 2 Mbps ✎ (the book states 54 Mbps in one place) |
| 802.11b | (Wi-Fi 1) | 1999 | 2.4 GHz | 11 Mbps. Popularized Wi-Fi. |
| 802.11a | (Wi-Fi 2) | 1999 | 5 GHz | 54 Mbps. Less interference, shorter range. |
| 802.11g | (Wi-Fi 3) | 2003 | 2.4 GHz | 54 Mbps |
| 802.11n | Wi-Fi 4 | 2009 | 2.4 / 5 GHz | 600 Mbps (MIMO, channel bonding) |
| 802.11ac | Wi-Fi 5 | 2013–14 | 5 GHz | ~1.3 Gbps (wave 1) to ~3.5–6.9 Gbps (wave 2); MU-MIMO (downlink) |
| 802.11ax | Wi-Fi 6 / 6E | 2019 / 2020 | 2.4 / 5 (/6 GHz for 6E) | ~9.6 Gbps; OFDMA, uplink+downlink MU-MIMO, better dense-area efficiency |
| 802.11be | Wi-Fi 7 | 2024 | 2.4 / 5 / 6 GHz | ~46 Gbps theoretical ✎ (the book cites a target of 9.6 Gbps, which is Wi-Fi 6's figure); 320 MHz channels, multi-link operation (MLO), 4K-QAM, lower latency |

**Other wireless technologies:**
- **Bluetooth / BLE:** 2.4 GHz, short range, peripherals and wearables. BLE is low power, about 1 Mbps.
- **Zigbee:** IEEE 802.15.4, 2.4 GHz, low power and low data rate, mesh; home and industrial automation.
- **LoRaWAN:** sub-GHz, low-power wide-area network, kilometers of range, small payloads (agriculture, smart city).
- **NFC:** a few centimeters; payments, access control, pairing.
- **5G:** high rates, low latency, massive IoT, network slicing. **6G** is in research (immersive XR, haptics).

**WLAN building blocks:**
- Station (STA) and access point (AP).
- BSS (one AP plus its clients); IBSS (ad hoc, no AP); ESS (several BSSs sharing an SSID).
- Distribution system (wired or wireless links between APs).
- Wireless LAN controller.

## Network devices

| Device | Layer | Function | Collision / broadcast domains |
|---|---|---|---|
| Repeater / hub | L1 | Regenerates the signal; hub repeats to all ports (active hubs are powered, passive hubs are not; "intelligent" hubs are manageable) | One shared collision domain |
| Bridge | L2 | Learns MACs per segment, filters and forwards frames; transparent bridging | Separates collision domains |
| Switch | L2 (L3 switches also route) | Multiport bridge; MAC address table; dedicated bandwidth per port; buffering; error checking; VLANs | One collision domain per port; one broadcast domain per VLAN |
| Router | L3 | Forwards packets between networks using routing tables; runs routing protocols (OSPF, EIGRP, BGP); usually also NAT, ACLs and DHCP | Separates broadcast domains |
| Gateway | L4–7 | Converts between protocols and data formats (for example SNA↔TCP/IP); often adds security features | — |
| Firewall | L3–7 | Filters traffic by policy (see design-and-operations §7) | — |
| Modem | L1/2 | Modulates/demodulates over phone, cable, fiber or satellite for WAN access | — |
| NIC | L1/2 | The host's interface, with a burned-in MAC address | — |
| Access point / WLC | L2 | Wireless access; the controller centralizes AP management | — |

**Choosing hardware** (book's criteria):
- performance (throughput, CPU, memory);
- scalability (ports, modularity, stacking);
- compatibility (standards, media, existing kit);
- security features (ACLs, VPN, firewall, encryption);
- manageability (CLI, GUI, SNMP, API);
- total cost of ownership (purchase, licenses, support, operating cost).

## Topologies

| Topology | Description | Strengths | Weaknesses |
|---|---|---|---|
| Point-to-point | Two nodes, one link | Simple, dedicated | Doesn't scale |
| Bus | Shared backbone cable with terminators; CSMA/CD | Cheap, simple | The cable is a single point of failure; collisions |
| Star | All nodes connect to a central hub or switch | Easy to add hosts, isolates faults | The central device is a single point of failure |
| Ring | Each node links to two neighbors | Predictable | One break can take down the ring (dual rings mitigate this) |
| Mesh (full or partial) | Many or all nodes interconnected; full mesh needs n(n−1)/2 links | Highly resilient | Costly cabling and ports |
| Tree / hierarchical | Extended star in tiers (core / distribution / access) | Scalable, the most common LAN design | Upper-tier failures isolate branches |
| Daisy chain | Linear chain of nodes | Simple | Each link is a single point of failure |
| Hybrid | A mix (the Internet is the largest example; WANs often dual-ring, LANs star) | Flexible | Inherits the weaknesses of its parts |

## IP addressing and subnetting

- **IPv4:** 32-bit dotted decimal (for example 192.0.2.15). The **network portion** identifies the network and the **host portion** identifies the device. In a subnet, the first address is the **network address** and the last is the **broadcast address**; usable hosts = 2^(host bits) − 2.
- **IPv6:** 128-bit hexadecimal, for example `2001:db8::1`. It has a vast address space, no broadcast (it uses multicast), and SLAAC and DHCPv6 for configuration.
- **Subnet mask / CIDR:** Separates network from host bits, for example /24 = 255.255.255.0. Routers AND the destination address with the mask to decide where to forward. Subnetting shrinks broadcast domains, improves efficiency and security, and makes large address blocks manageable.
  - Worked example: 192.0.2.0/24 has hosts .1–.254 and broadcast .255. Split into /26 blocks: .0, .64, .128, .192, each with 62 hosts.
- **VLSM:** Use different mask lengths for different segment sizes (for example /30 or /31 for point-to-point links, /24 for user VLANs).
- **Private ranges (RFC 1918):** 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16. Use these inside and NAT to public addresses.
- **Classful legacy:** Class A /8, B /16, C /24. Modern networks use classless CIDR.

## Core services and protocols

- **DNS:** A distributed, hierarchical database mapping names to IP addresses (A/AAAA records) and back (PTR). Each server holds only part of the namespace and refers or forwards for the rest. Other record types: MX (mail), CNAME, SRV (service location, used by Active Directory — ✎ the book calls it "SVC"), TXT, NS, SOA.
- **DHCP:** Automatically hands out IP address, mask, default gateway, DNS servers and lease time (Discover → Offer → Request → Acknowledge). Avoids manual errors and duplicate addresses. Use reservations (by MAC address) for devices that need a fixed address. Use DHCP relay (ip helper-address) when the server is on another subnet.
- **NAT:** Translates private to public addresses.
  - Static NAT: one-to-one, fixed.
  - Dynamic NAT: drawn from a pool.
  - PAT / NAT overload: many hosts share one public IP, distinguished by port. This is the typical home or office setup.
- **VPN:** An encrypted tunnel over the internet.
  - **Remote access** (client to site): checks the user and the device's security posture.
  - **Site-to-site** (links branch offices).
  - Technologies: IPsec, SSL/TLS VPNs, WireGuard.
- **FTP (TCP 20/21):** Separate control and data channels; credentials sent in clear text, so avoid it. Prefer **SFTP** (over SSH, port 22) or **FTPS** (FTP plus TLS), or managed cloud storage and transfer services.
- **HTTP / HTTPS (80/443):** Request (method, URL, version, headers, optional body) and response (status code, headers, body). HTTPS adds TLS.
- **SMTP (25; 587 for client submission):** Sends and relays mail between servers; the MTA uses DNS MX records to find the recipient's server. **IMAP (143/993)** and **POP3 (110/995)** retrieve mail.
- **TCP:** Connection-oriented (three-way handshake), reliable, ordered, with flow and congestion control and retransmission (RFC 793, now RFC 9293). Used for web, mail, file transfer.
- **UDP:** Connectionless, low overhead, checksum only, no delivery guarantee. Used for DNS queries, VoIP/video, streaming, gaming, DHCP.
- **Other:** ICMP (ping, traceroute), ARP (IP to MAC), NTP (time), SNMP (monitoring), SSH (secure management; do not use Telnet), Syslog, NetFlow/sFlow/IPFIX.

## Wireless design essentials

- **Site survey:** Pre-deployment (floor plans, walkthrough, interviews with IT and users; passive or active survey software; predictive modelling) and post-deployment validation. Define the coverage boundary and the required signal strength (RSSI) and signal-to-noise ratio (SNR) for the applications (voice needs stricter numbers than data).
- **Design factors:** coverage, interference, security, capacity, scalability, reliability.
  - Interference: other WLANs, microwave ovens, Bluetooth; plan channels (non-overlapping 1/6/11 at 2.4 GHz); directional antennas.
  - Capacity: plan for user and device density and per-application bandwidth; use QoS.
  - Reliability: redundant hardware, failover and load balancing.
- **AP and controller configuration:**
  - Management IP and VLAN; SSIDs mapped to VLANs; WPA3 (or WPA2-AES).
  - Transmit power, channel width and channel plan.
  - Roaming (802.11r/k/v).
  - QoS/WMM for voice and video.
  - SNMP, syslog and NetFlow; keep firmware current.

## Corrections to the book (✎)

- The OSI model was published in 1984, not 1974.
- Original 802.11 = 2 Mbps, not 54 Mbps.
- Wi-Fi 7's theoretical peak is about 46 Gbps (9.6 Gbps is Wi-Fi 6).
- 10GBASE-T uses Cat6a (Cat6 only to about 55 m); "Cat5 or better" is not sufficient.
- The DNS service record type is **SRV**.
- **Hypervisors:** Type 1 runs directly on hardware (bare metal); Type 2 runs on top of a host operating system (the book's wording is garbled). The book's advice to use Type 1 for production, and that Type 1 costs more, still stands.
- Some product details (for example, specific vendor tools) change quickly; verify them against current documentation.
