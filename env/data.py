
TICKETS = [
    {
        "ticket_id": "T1",
        "message": "Payment failed but money deducted",
        "customer_tier": "premium",
        "timestamp": "2026-03-01"
    },
    {
        "ticket_id": "T2",
        "message": "How to reset password?",
        "customer_tier": "free",
        "timestamp": "2026-03-02"
    },
    {
        "ticket_id": "T3",
        "message": "App crashes on checkout",
        "customer_tier": "premium",
        "timestamp": "2026-03-03"
    }
]

GROUND_TRUTH = [
    {
        "category": "billing",
        "priority": "high",
        "assigned_team": "payments"
    },
    {
        "category": "technical",
        "priority": "medium",
        "assigned_team": "tech"
    },
    {
        "category": "billing",
        "priority": "high",
        "assigned_team": "payments"
    }
]