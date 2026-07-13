from agent.models.state import AgentState


class PlannerNode:
    """
    Decides whether the agent should use the Knowledge Base.
    """

    KB_KEYWORDS = {
        "authentication": [
            "auth", "authentication", "login",
            "credential", "401", "unauthorized",
            "token", "api key"
        ],

        "network": [
            "network", "timeout", "connection",
            "dns", "firewall", "vpc",
            "connectivity", "unreachable"
        ],

        "data_permissions": [
            "permission", "403", "forbidden",
            "acl", "policy", "role",
            "access denied"
        ],

        "deployment_config": [
            "config", "configuration",
            "deploy", "deployment",
            "yaml", "environment variable",
            "env variable"
        ],

        "database_timeout": [
            "database", "db",
            "query timeout",
            "deadlock",
            "connection pool",
            "slow query"
        ],

        "rate_limiting": [
            "429",
            "rate limit",
            "quota",
            "throttle",
            "too many requests"
        ],

        "ssl_certificate": [
            "ssl",
            "tls",
            "certificate",
            "handshake"
        ],

        "disk_space": [
            "disk",
            "disk full",
            "storage",
            "no space left"
        ]
    }

    FAILURE_KEYWORDS = [
        "error",
        "failed",
        "failure",
        "crash",
        "down",
        "cannot",
        "unable",
        "not working"
    ]

    def run(self, state: AgentState) -> AgentState:

        ticket = state.ticket.lower()

        state.should_search_kb = False
        state.planner_reason = (
            "No KB lookup required."
        )

        # 1. Check KB category keywords
        for category, keywords in self.KB_KEYWORDS.items():

            if any(keyword in ticket for keyword in keywords):

                state.should_search_kb = True

                state.planner_reason = (
                    f"Detected {category.replace('_',' ')} related keywords."
                )

                return state

        # 2. Generic troubleshooting
        if any(word in ticket for word in self.FAILURE_KEYWORDS):

            state.should_search_kb = True

            state.planner_reason = (
                "General failure symptoms detected."
            )

        return state