"""
MindCare Agentic Suite - Sales & Retention Lead Agent (Agent 1)
Orquestador Comercial de Conversión y Reactivación 24/7 sobre Vertex AI.
"""

from typing import Dict, Any

class SalesAndRetentionAgent:
    def __init__(self, crm_mcp, scheduling_mcp):
        self.agent_id = "agent_1_sales_onboarding"
        self.crm_mcp = crm_mcp
        self.scheduling_mcp = scheduling_mcp

    def handle_patient_inquiry(self, patient_phone: str, message: str) -> Dict[str, Any]:
        """Procesa consultas comerciales iniciales y califica al paciente."""
        lead_res = self.crm_mcp.execute_tool(
            "qualify_lead",
            {"patient_phone": patient_phone, "consultation_type": "Psicología", "urgency_level": "Media"}
        )
        
        slots_res = self.scheduling_mcp.execute_tool(
            "check_therapist_availability",
            {"preferred_date": "2026-08-15"}
        )
        
        return {
            "agent_response": "¡Hola! Gracias por comunicarte con MindCare. Hemos recibido tu consulta y tenemos citas disponibles este sábado.",
            "available_slots": slots_res.get("available_slots", []),
            "mcp_status": lead_res.get("status")
        }

    def execute_reactivation_flow(self, patient_id: str, days_inactive: int) -> Dict[str, Any]:
        """Flujo asíncrono en segundo plano para reactivar pacientes inactivos."""
        if days_inactive >= 14:
            return self.crm_mcp.execute_tool(
                "trigger_reactivation_campaign",
                {"patient_id": patient_id, "days_inactive": days_inactive}
            )
        return {"status": "skipped", "reason": "El paciente no cumple el criterio de inactividad."}
