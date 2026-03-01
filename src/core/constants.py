from enum import Enum
from typing import Dict, Any

class RiskBucket(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class CommunicationChannel(str, Enum):
    SMS = "sms"
    EMAIL = "email"
    WHATSAPP = "whatsapp"
    PHONE = "phone"
    LETTER = "letter"

class CommunicationStatus(str, Enum):
    PENDING = "pending"
    SENT = "sent"
    DELIVERED = "delivered"
    READ = "read"
    FAILED = "failed"
    BLOCKED = "blocked"

class PaymentStatus(str, Enum):
    PAID = "paid"
    PARTIAL = "partial"
    MISSED = "missed"
    PENDING = "pending"
    DEFAULTED = "defaulted"

class WorkflowStep(str, Enum):
    FETCH_DATA = "fetch_data"
    CLASSIFY_RISK = "classify_risk"
    ANALYZE_INCOME = "analyze_income"
    GENERATE_PLAN = "generate_plan"
    CREATE_SCRIPT = "create_script"
    SEND_COMMUNICATION = "send_communication"
    ESCALATE_LEGAL = "escalate_legal"
    LOG_COMPLETION = "log_completion"

# Risk weights for scoring
RISK_WEIGHTS: Dict[str, float] = {
    "delinquency_days": 0.3,
    "payment_history": 0.25,
    "debt_amount": 0.15,
    "income_stability": 0.2,
    "communication_response": 0.1
}

# Default payment plans by risk bucket
DEFAULT_PAYMENT_PLANS: Dict[str, Dict[str, Any]] = {
    "low": {
        "max_months": 3,
        "min_down_payment": 0.1,
        "interest_rate": 0.0
    },
    "medium": {
        "max_months": 6,
        "min_down_payment": 0.2,
        "interest_rate": 0.05
    },
    "high": {
        "max_months": 9,
        "min_down_payment": 0.3,
        "interest_rate": 0.08
    },
    "critical": {
        "max_months": 12,
        "min_down_payment": 0.4,
        "interest_rate": 0.12
    }
}

# Communication templates by channel
COMMUNICATION_TEMPLATES: Dict[str, str] = {
    "sms": """
    Hi {borrower_name}, this is {agent_name} from Collections. 
    We have a personalized payment plan for you: {plan_summary}
    Reply YES to learn more or call {contact_number}
    """,
    "email": """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            .container {{ max-width: 600px; margin: 0 auto; }}
            .header {{ background-color: #f8f9fa; padding: 20px; }}
            .content {{ padding: 20px; }}
            .plan-details {{ background-color: #e9ecef; padding: 15px; border-radius: 5px; }}
            .button {{ background-color: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>Personalized Payment Plan</h2>
            </div>
            <div class="content">
                <p>Dear {borrower_name},</p>
                <p>We understand financial situations can be challenging. Based on your profile, we've created a personalized payment plan:</p>
                <div class="plan-details">
                    <h3>Your Plan:</h3>
                    <p>{plan_detailed}</p>
                    <p>Monthly Payment: ${monthly_payment}</p>
                    <p>Duration: {duration_months} months</p>
                    <p>First Payment: {first_payment_date}</p>
                </div>
                <p>To accept this plan, click the button below:</p>
                <a href="{acceptance_link}" class="button">Accept Payment Plan</a>
                <p>Or contact us at {contact_number}</p>
            </div>
        </div>
    </body>
    </html>
    """,
    "whatsapp": """
    *Personalized Payment Plan from Collections Team*
    
    Hi {borrower_name},
    
    We've analyzed your situation and created a payment plan just for you:
    
    *Plan Details:*
    {plan_bullets}
    
    *Next Steps:*
    1. Reply with ACCEPT to confirm
    2. Or call us at {contact_number} to discuss options
    
    We're here to help you get back on track.
    """
}

# Error messages
ERROR_MESSAGES = {
    "borrower_not_found": "Borrower with ID {borrower_id} not found",
    "cache_error": "Cache operation failed: {error}",
    "database_error": "Database operation failed: {error}",
    "llm_error": "LLM processing failed: {error}",
    "validation_error": "Validation failed: {error}",
    "workflow_error": "Workflow execution failed at step {step}: {error}",
    "rate_limit": "Rate limit exceeded. Try again in {seconds} seconds"
}
