---
name: computer-networking
description: Apply the teachings of "Computer Networking Bible" (Rick C. Worley, 2024) — networking fundamentals (OSI/TCP-IP, Ethernet and Wi-Fi standards, devices, topologies, IP addressing/subnetting, DNS, DHCP, NAT, VPN, core protocols) and the practice of designing, planning, implementing, securing, optimizing, scaling, automating and monitoring networks, including cloud, SDN/NFV, virtualization and IoT. Use when the user asks to explain a networking concept, design or document a network (home, small office, campus, branch, data center, cloud/hybrid, IoT), plan IP addressing/VLANs, choose hardware or wireless standards, write router/switch configurations, troubleshoot connectivity or performance, harden network security, plan redundancy/disaster recovery, or automate network operations.
---

# Computer Networking

A working guide distilled from *Computer Networking Bible: The Complete Crash Course to Effectively Design, Implement and Manage Networks* by Rick C. Worley (2024). The book has three goals: teach the **fundamentals**, survey **emerging technologies** (cloud, SDN, IoT, automation), and build the **practical skill** to design, implement and manage networks with a focus on **security, performance and scalability**.

## Core principles

1. **Requirements before technology.** Start from users, applications, information flows, growth, security/compliance and budget. State requirements in business language (for example, "remote staff can give customers real-time information") before choosing protocols and boxes.
2. **Think in layers.** Use the OSI (7 layers) and TCP/IP (4 layers) models to reason about where a function lives and where a fault sits. Layers 1–3 (physical, data link, network) are stable over time. Hubs work at L1, switches and bridges at L2, routers at L3, and gateways at L4–L7.
3. **Hierarchical, modular design.** Build core / distribution / access for campuses and spine-leaf for data centers. Modules can grow or be replaced without redesigning the whole network.
4. **Remove single points of failure.** Use redundant links, devices, power and paths; link aggregation (LACP/EtherChannel); first-hop redundancy (HSRP/VRRP); and clustered or HA services. Test failover.
5. **Defense in depth, least privilege.** Layer the controls:
   - perimeter firewall / NGFW and IDS/IPS;
   - segmentation (VLANs, subnets, ACLs, micro-segmentation);
   - strong authentication (RADIUS/TACACS+, 802.1X, MFA, RBAC);
   - encryption in transit and at rest (IPsec, TLS, WPA3);
   - endpoint security;
   - monitoring (SIEM) and a tested incident-response plan.
6. **Measure, then optimize.** "What you can't see can't be optimized." Baseline bandwidth, latency, jitter, packet loss and availability. Find the bottleneck, fix the root cause (QoS, protocol tuning, upgrades, load balancing), then re-measure.
7. **Plan for growth.** Do capacity planning with trend data. Use a hierarchical, summarizable IP plan with VLSM. Use scalable protocols (OSPF/EIGRP/BGP, VLANs, STP/RSTP), and consider cloud, hybrid and edge.
8. **Document and control change.** Keep up-to-date diagrams, inventory, the IP/VLAN plan, configurations under version control (Git), SOPs, and a knowledge base. Run formal change management with a risk assessment, testing and a rollback plan.
9. **Automate the repetitive.** Configuration, backups, compliance checks, provisioning and patching with Ansible, Netmiko, NAPALM, NSO, or controllers and APIs. Automation cuts errors and frees people for design. When everyone has the same tools, good architecture is what differentiates.
10. **Be ready for failure.** High availability, backups (full/incremental/differential with RTO/RPO targets), and a business continuity / disaster recovery (BC/DR) plan that is tested regularly.
11. **Keep learning.** The field changes fast (Wi-Fi 7, 5G/6G, SDN, edge, AI-driven operations). Keep current and verify vendor specifics.

## How to use this skill

| User wants… | Go to |
|---|---|
| Explain a concept (OSI, TCP vs UDP, subnetting, DNS, DHCP, NAT, VPN, topologies, device roles, Ethernet/Wi-Fi standards) | `references/fundamentals.md` |
| Design or plan a network, choose architecture or hardware, IP/VLAN plan | `references/design-and-operations.md` §1–§3 |
| Router or switch configuration (Cisco IOS style) | `references/design-and-operations.md` §4 |
| Troubleshooting or performance tuning | `references/design-and-operations.md` §5–§6 |
| Security hardening, firewalls/IDS, wireless security, access control, crypto | `references/design-and-operations.md` §7 |
| Scalability, HA, DR/BC | `references/design-and-operations.md` §8 |
| Virtualization, cloud, SDN/NFV, IoT, automation, monitoring/analytics | `references/design-and-operations.md` §9–§12 |

**Workflow for design requests:**
1. Gather requirements (users and growth, locations, applications and their bandwidth/latency needs, security/compliance, budget, existing kit).
2. Propose an architecture and topology with redundancy.
3. Produce an IP/VLAN plan, the device list and the security zones.
4. Add management and monitoring, a documentation and change process, and the DR approach.
5. List assumptions and the next steps (site survey, pilot, test).

**Workflow for troubleshooting:** Work bottom-up through the layers:
1. Physical: cables, link lights.
2. Data link: VLAN, duplex, STP.
3. Network: IP, mask, gateway, routes.
4. Transport and application: ports, firewall/ACL, DNS.

Use `ipconfig /all`, `ip addr`, `ping`, `traceroute`/`tracert`, `nslookup`/`dig`, and `show` commands. Change one thing at a time and record what you did.

## Output style

- Give concrete deliverables: topology descriptions or diagrams, addressing tables, configuration snippets, checklists.
- Mark vendor-specific commands as Cisco IOS examples and note that syntax differs by platform and version.
- **Safety:** Recommend testing in a lab or maintenance window with backups and a rollback plan. Never suggest disabling security controls as a "fix." Keep security guidance defensive.
- **Accuracy:** The book (2024) has some errors. `references/fundamentals.md` notes the corrections; prefer the corrected facts, and check current standards and vendor documentation for specifics.
