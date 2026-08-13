# MindCare Agentic Suite - Architecture & Sequence Diagrams

## System Overview

MindCare Agentic Suite operates as an asynchronous multi-agent system deployed on Google Cloud Platform, leveraging Gemini Enterprise and Vertex AI Agent Builder. Communication between autonomous agents and clinical databases is fully decoupled using the Model Context Protocol (MCP).
## Agent Workflows

### 1. Sales & Onboarding Lead (`agent_1_sales_onboarding.py`)
- **Trigger:** Inbound WhatsApp or Web form inquiry.
- **Actions:**
  1. Calls `mcp_crm_server.qualify_lead`.
  2. Queries `mcp_scheduling_server.check_therapist_availability`.
  3. Returns real-time slot selection to patient.
  4. Triggers background reactivation flows for inactive patients (>14 days).

### 2. Asynchronous Clinical Intake (`agent_2_clinical_intake.py`)
- **Trigger:** Pre-session voice note or unstructured patient text.
- **Actions:**
  1. Multimodal processing via Gemini Enterprise.
  2. Triage rating (Anxiety, Depression, Critical Risk Flag).
  3. Generates "1-Minute Executive Intake Summary" stored for therapist review prior to consultation.

### 3. PsychoSync MCP Documentation (`agent_3_psychosync_doc.py`)
- **Trigger:** Post-session therapist voice dictation.
- **Actions:**
  1. Formats unstructured speech into SOAP (Subjective, Objective, Assessment, Plan) structure.
  2. Calls `mcp_ehr_server.save_soap_note` to update history without manual data entry.
