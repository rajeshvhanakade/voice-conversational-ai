# app/agent/controller.py

import json
from tools import calculator, pdf_reader
from memory.short_term import add, get
from llm.ollama_client import query_llm


def agent_loop(user_input: str) -> str:
    # store user input
    add("user", user_input)

    # calculator tool
    if any(op in user_input.lower() for op in ["+", "plus", "-", "minus", "*", "times", "/", "divide"]):
        try:
            result = calculator.run(user_input)
            add("assistant", str(result))
            return str(result)
        except Exception:
            return "Invalid math expression"

    # normal LLM call
    prompt = f"Conversation history: {get()}\nUser: {user_input}\nAnswer:"
    response = query_llm(prompt)

    # try to parse tool JSON
    try:
        data = json.loads(response)
        if data.get("action") == "text":
            reply = data.get("input", "")
        else:
            reply = response
    except json.JSONDecodeError:
        reply = response

    add("assistant", reply)
    return reply