# 0x09. Web Infrastructure Design

### Developer Team
- Nuelo


## Project Overview
This project involves designing and understanding various web infrastructure components and configurations. You will work on designing simple, distributed, secured, and scalable web infrastructures, and learn about concepts like DNS, monitoring, load balancing, and server roles.

## Concepts Covered
- DNS
- Monitoring
- Web Server
- Network Basics
- Load Balancer
- Server
- Database
- HTTPS
- Firewalls

## Learning Objectives
By the end of this project, you should be able to:
- Draw a web stack diagram based on your sysadmin/devops track projects.
- Explain the roles and operations of each component.
- Describe system redundancy and mitigate single points of failure (SPOF).
- Understand key acronyms like LAMP, SPOF, and QPS

## Tasks Overview

### 0. Simple Web Stack
**Objective**: Design a one-server web infrastructure.
- **Components**: 1 server, 1 web server (Nginx), 1 application server, 1 database (MySQL), and 1 domain name (foobar.com) pointing to IP `8.8.8.8`.
- **Concepts**: Explain server roles, DNS, web server, application server, database, communication protocols, and infrastructure issues like SPOF and scalability.

### 1. Distributed Web Infrastructure
**Objective**: Design a three-server infrastructure with a load balancer.
- **Components**: 2 additional servers, 1 load balancer (HAProxy), 1 web server (Nginx), 1 application server, 1 database (MySQL).
- **Concepts**: Load balancing algorithms, Active-Active vs Active-Passive setup, database primary-replica cluster, and infrastructure issues like SPOF, security, and monitoring.

### 2. Secured and Monitored Web Infrastructure
**Objective**: Design a three-server infrastructure with security and monitoring.
- **Components**: 3 firewalls, 1 SSL certificate, 3 monitoring clients.
- **Concepts**: Role of firewalls, HTTPS encryption, monitoring, data collection methods, and infrastructure issues like SSL termination, single write-capable MySQL server, and server component separation.

### 3. Scale Up
**Objective**: Scale the infrastructure by adding more servers and components.
- **Components**: 1 additional server, 1 load balancer (HAProxy) cluster, separate servers for web server, application server, and database.
- **Concepts**: Explain the need for each additional component and how it improves scalability and performance.

**ALX Program** - System Engineering / DevOps Track
© 2024 ALX, All rights reserved.