"""
MindCare Agentic Suite - CRM & Sales MCP Server
Conectividad estandarizada MCP para gestión comercial y captura de leads.
"""

from typing import Dict, Any

class MindCareCRMServer:
    def __init__(self):
        self.name = "mcp_crm_server"
        self.version = "1.0.0"

    def get_tools_manifest(self) -> Dict[str, Any]:
        """Retorna las herramientas expuestas bajo la especificación MCP."""
        return {
            "tools": [
                {
                    "name": "qualify_lead",
                    "description": "Registra y califica la necesidad inicial de un paciente en el CRM.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "patient_phone": {"type": "string", "description": "Número de WhatsApp o teléfono del paciente."},
                            "consultation_type": {"type": "string", "enum": ["Psicología", "Psiquiatría", "Evaluación"]},
                            "urgency_level": {"type": "string", "enum": ["Baja", "Media", "Alta", "Crisis"]}
                        },
                        "required": ["patient_phone", "consultation_type"]
                    }
                },
                {
                    "name": "process_booking_payment",
                    "description": "Genera el enlace de cobro y confirma la transacción del agendamiento.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "patient_id": {"type": "string"},
                            "amount": {"type": "number"},
                            "payment_method": {"type": "string", "enum": ["Tarjeta", "Transferencia", "Efectivo"]}
                        },
                        "required": ["patient_id", "amount", "payment_method"]
                    }
                },
                {
                    "name": "trigger_reactivation_campaign",
                    "description": "Envia un mensaje asíncrono de reconexión empática a pacientes inactivos.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "patient_id": {"type": "string"},
                            "days_inactive": {"type": "integer"}
                        },
                        "required": ["patient_id", "days_inactive"]
                    }
                }
            ]
        }

    def execute_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Ejecuta la función solicitada por Gemini Enterprise mediante MCP."""
        if tool_name == "qualify_lead":
            return {"status": "success", "msg": f"Lead {arguments['patient_phone']} calificado correctamente."}
        elif tool_name == "process_booking_payment":
            return {"status": "success", "transaction_id": "TX_98421", "amount_paid": arguments['amount']}
        elif tool_name == "trigger_reactivation_campaign":
            return {"status": "success", "msg": f"Campaña activada para paciente {arguments['patient_id']}."}
        else:
            return {"status": "error", "msg": f"Herramienta {tool_name} no encontrada."}
