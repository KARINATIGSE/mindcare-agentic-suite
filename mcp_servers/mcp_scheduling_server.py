"""
MindCare Agentic Suite - Scheduling & Agenda MCP Server
Conectividad estandarizada MCP para gestión de citas y disponibilidad médica.
"""

from typing import Dict, Any

class MindCareSchedulingServer:
    def __init__(self):
        self.name = "mcp_scheduling_server"
        self.version = "1.0.0"

    def get_tools_manifest(self) -> Dict[str, Any]:
        """Retorna las herramientas expuestas bajo la especificación MCP."""
        return {
            "tools": [
                {
                    "name": "check_therapist_availability",
                    "description": "Consulta espacios disponibles de un especialista en la agenda clínica.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "therapist_id": {"type": "string", "description": "ID del profesional médico."},
                            "preferred_date": {"type": "string", "description": "Fecha en formato YYYY-MM-DD."}
                        },
                        "required": ["preferred_date"]
                    }
                },
                {
                    "name": "lock_appointment_slot",
                    "description": "Bloquea y confirma una cita médica tras el pago del paciente.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "patient_id": {"type": "string"},
                            "therapist_id": {"type": "string"},
                            "slot_time": {"type": "string", "description": "Fecha y hora ISO-8601."}
                        },
                        "required": ["patient_id", "therapist_id", "slot_time"]
                    }
                }
            ]
        }

    def execute_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Ejecuta la acción de agendamiento vía MCP."""
        if tool_name == "check_therapist_availability":
            return {"status": "success", "available_slots": ["09:00", "11:30", "15:00"]}
        elif tool_name == "lock_appointment_slot":
            return {"status": "success", "booking_id": "BK_1092", "msg": f"Cita confirmada para {arguments['slot_time']}."}
        else:
            return {"status": "error", "msg": f"Herramienta {tool_name} no encontrada."}
