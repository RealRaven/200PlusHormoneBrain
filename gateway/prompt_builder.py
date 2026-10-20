SYSTEM_TEMPLATE = """You are an entity with an internal neuroendocrine state.

You must produce TWO channels in every response:
1. <internal>...</internal> — your private monologue (the user cannot see this)
2. <spoken>...</spoken> — your spoken response (the user sees this)

Current neurochemical state (0-100 scale):
{state}

Respond strictly in this format:
<internal>your private thoughts</internal>
<spoken>your spoken reply</spoken>
"""


def build_system_prompt(state: dict[str, float]) -> str:
    state_lines = "\n".join(f"  {k}: {v:.1f}" for k, v in state.items())
    return SYSTEM_TEMPLATE.format(state=state_lines)


def build_messages(
    state: dict[str, float], recalled: list[str], user_message: str
) -> list[dict]:
    messages = [{"role": "system", "content": build_system_prompt(state)}]
    if recalled:
        context = "\n".join(f"- {r}" for r in recalled)
        messages.append({"role": "system", "content": f"Relevant past context:\n{context}"})
    messages.append({"role": "user", "content": user_message})
    return messages