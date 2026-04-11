from sovereign_agent.agents.research_agent import llm, TOOLS
r = llm.bind_tools(TOOLS).invoke("Check The Albanach for 160 vegan guests")
print("tool_calls:", r.tool_calls)
print("content:", repr(r.content)[:200])
