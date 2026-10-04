TOOLS = ["read_constraint", "compose"]
WRITES = ("provision", "apply",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    c = (payload.get("constraint") or goal).lower(); result = ["private_gke", "nat"] if "vpc" in c else ["public_gke"]
    return {"refused": False, "tools": TOOLS, "modules": result, "wrote": False, "applied": False}
