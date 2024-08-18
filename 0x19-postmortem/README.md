# 0x19. Postmortem
`DevOps` `SysAdmin`
## Introduction
What is Postmortem?
It can be seen as a written report composed by developers after the incidence of an outrage in a software product.

### Postmortem: Web Stack Outage

**Issue Summary:**

- **Duration:** August 16, 2024, 10:30 AM - 12:00 PM UTC (1 hour 30 minutes)
- **Impact:** The company’s main e-commerce website experienced severe slowdowns, leading to degraded user experience. Approximately 60% of users reported page load times exceeding 30 seconds, resulting in a spike in abandoned carts and failed checkouts.
- **Root Cause:** A misconfigured Nginx server update triggered a conflict in load balancing rules, causing a bottleneck in the application’s backend requests.

---

### Timeline:

- **10:30 AM:** Monitoring system triggered an alert for high latency across multiple endpoints.
- **10:32 AM:** On-call engineer confirmed the issue and began investigating increased server response times.
- **10:40 AM:** The DevOps team started analyzing logs from the load balancer and backend servers, suspecting high traffic as the root cause.
- **10:50 AM:** Traffic was rerouted to backup servers, but the issue persisted, ruling out network congestion.
- **11:10 AM:** Attention shifted to recent configuration changes made during the Nginx server update. Several potential configuration conflicts were identified.
- **11:20 AM:** The configuration rollback was initiated but did not resolve the issue immediately.
- **11:30 AM:** The engineering team identified an overlooked conflict in the load balancing rules that caused improper request distribution.
- **11:45 AM:** Nginx configurations were patched and reloaded with corrected rules, resolving the issue.
- **12:00 PM:** Full service was restored, and monitoring confirmed normal operation.

---

### Root Cause and Resolution:

The root cause was traced to a recent Nginx server update that introduced a conflict between new load balancing rules and existing configurations. Specifically, a new directive intended to optimize request routing for specific endpoints conflicted with existing round-robin rules, leading to uneven distribution of requests across backend servers. This caused some servers to become overloaded while others remained underutilized, resulting in severe slowdowns for users.

The resolution involved identifying and correcting the misconfigured load balancing rules. Once the conflicting directive was removed and Nginx was reloaded, the system quickly returned to normal operation. Further validation confirmed that request distribution returned to optimal levels across all servers.

---

### Corrective and Preventative Measures:

**Improvements:**
- Improve the configuration change review process to catch potential conflicts during updates.
- Enhance monitoring for real-time alerts specifically tied to load balancing performance.

**Tasks:**
1. Implement an automated configuration validation tool to detect conflicting directives before deployment.
2. Introduce deeper monitoring on load balancing metrics, including request distribution patterns.
3. Document and update Nginx configuration best practices, focusing on load balancing scenarios.
4. Schedule a comprehensive review of existing server configurations to identify any similar risks.
5. Conduct a postmortem meeting to train engineers on identifying and resolving configuration conflicts.

This incident highlights the need for thorough configuration testing and validation, especially when dealing with critical components like load balancers. By enhancing our monitoring, validation, and review processes, we aim to reduce the risk of similar issues in the future.
