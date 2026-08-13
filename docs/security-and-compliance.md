# Security, Privacy & Regulatory Compliance Protocol

## Overview

MindCare Agentic Suite is engineered specifically for mental health institutions and practices, prioritizing maximum security for protected health information (PHI) and clinical records.

## Core Compliance Frameworks

### 1. HIPAA & LOPDP Alignment
- **Data Minimization:** Agents only access data explicitly required for tool execution via scope-bounded MCP interfaces.
- **Encryption at Rest & in Transit:** All communications between agents and MCP servers use TLS 1.3 encryption. Database records are encrypted using AES-256 via GCP Cloud KMS.
- **Zero Retention Model:** Gemini Enterprise API calls do NOT use patient input data or audio transcripts for training base models.

### 2. Multi-Agent Security Boundaries
- **Server Isolation:** Each MCP server (`mcp_crm_server`, `mcp_scheduling_server`, `mcp_ehr_server`) runs in an isolated runtime context with granular key authentication.
- **Role-Based Access Control (RBAC):** `agent_1_sales_onboarding` is strictly restricted from accessing `mcp_ehr_server` (clinical records), preventing unauthorized exposure of therapeutic histories.

### 3. Critical Risk Escrow
- Automatic Red Flag detection during intake triggers immediate escalation to human clinical directors, bypassing automated workflows when crisis markers are identified.
