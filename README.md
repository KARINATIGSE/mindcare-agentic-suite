# MindCare Agentic Suite

> **An Asynchronous Multi-Agent AI Suite for Mental Health Onboarding, Intake & Clinical Documentation**  
> *Built on Google Cloud (Gemini Enterprise, Vertex AI Agent Builder & Model Context Protocol - MCP)*

---

## Executive Overview
MindCare Agentic Suite is an enterprise-grade, asynchronous multi-agent ecosystem designed to eliminate administrative burnout for mental health specialists while driving 24/7 patient acquisition, intake, and retention.

By shifting heavy administrative workloads—such as clinical intake summaries, SOAP/DAP documentation, and multi-system data entry—into automated background tasks powered by **Gemini Enterprise** and **MCP**, therapists save up to **2.5 hours per day** to focus entirely on patient care.

---

## Architecture & Multi-Agent Specifications

### 1. Sales & Retention Lead Agent (`Agent 1`)
- **Role:** 24/7 Commercial Onboarding, Booking & Reactivation.
- **Capabilities:** Empathetic patient qualification, service breakdown, booking lock-in, and automated background recovery campaigns for inactive patients.
- **MCP Tool:** `mcp_crm_server.py`

### 2. Asynchronous Clinical Intake Agent (`Agent 2`)
- **Role:** Multimodal Pre-Session Triage & Executive Intake.
- **Capabilities:** Processes unstructured patient audio notes and texts in the background to generate a "1-Minute Executive Intake Summary" and emotional risk indicators for the clinician prior to session start.
- **MCP Tool:** `mcp_ehr_server.py`

### 3. PsychoSync MCP Documentation Agent (`Agent 3`)
- **Role:** Post-Session Clinical Documentation & EHR Synchronization.
- **Capabilities:** Converts 30-second post-session therapist voice notes into standardized SOAP/DAP clinical records, updating EHRs and CRMs autonomously with zero manual entry.
- **MCP Tool:** `mcp_scheduling_server.py`

---

## Repository Structure

```text
mindcare-agentic-suite/
├── config/
│   └── system_instructions.json      # Global Vertex AI Agent Configuration
├── mcp_servers/
│   ├── mcp_crm_server.py             # MCP Server for CRM & Sales Automation
│   ├── mcp_scheduling_server.py      # MCP Server for Medical Agenda & Booking
│   └── mcp_ehr_server.py             # MCP Server for Clinical Records (SOAP/DAP)
├── agents/
│   ├── agent_1_sales_onboarding/
│   ├── agent_2_clinical_intake/
│   └── agent_3_psychosync_doc/
└── docs/
    ├── architecture.md               # Complete System Sequence Diagrams
    └── security-and-compliance.md    # HIPAA, GDPR & LOPDP Privacy Frameworks
