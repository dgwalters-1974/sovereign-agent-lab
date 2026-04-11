"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh"
QUERY_2_FINAL_ANSWER  = """The best match for your request is "The Albanach" 
with a capacity of 180 guests and vegan options available. The full address 
of this venue is "2 Hunter Square, Edinburgh"."""

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
The agent chose the Haymarket Vaults when the Albanach statuswas changed to 'full'.
I only needed to update VENUES within mcp_venue_server.py in order to trigger this
change in behaviour. This demonstrates that the client is isolated from the server
and that any other clients may connect to the same server and see the same source"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 10   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 50   # count in exercise4_mcp_client.py



# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP has the tools (& data) on a seperate server and provides a modular approach
to building a solution, without the need to import tools. It clearly involves more
setup and a more complex architecture but it allows for multiple agents to connect
to the same tool server and share the same data"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- Research Agent that can connect to MCP server and use tools
- MCP server with tools can be accessed
- Rasa agent used for connecting to MCP and performing structured workflows
- Memory store for storing past sessions and data
- Planning and execution agents for complex tasks
- An interface (voice or text) for the agent to interact with the user / provide feedback
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
Based on the work herein, the research should be performed by the LangGraph agent while
the call should be performed by the Rasa agent. This is because the LangGraph agent is
more flexible and likely can handle the changing behaviour of the venues (as they get
full closer to event time, bank holidays etc.), while the Rasa agent is more structured
and can handle the 'business' exchange in a more predictable way.
"""
