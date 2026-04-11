"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Bot loaded. Type a message and press enter (use '/stop' to exit): 
Your input ->  calling to confirm a booking                       
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                         
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit                                       
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, 
£200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
Your input ->                  """

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Bot loaded. Type a message and press enter (use '/stop' to exit): 
Your input ->  calling to confirm a booking                       
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                         
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan 
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £500 deposit                                       
I need to check one thing with the organiser before I can confirm. 
The issue is: a deposit of £500 exceeds the organiser's authorised 
limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
Your input ->    """

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Bot loaded. Type a message and press enter (use '/stop' to exit): 
Your input ->  calling to confirm a booking                       
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?          
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, 
please contact the event organiser directly.
Would you like to continue with confirm booking?
Your input ->"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
I think that upon receiving the out of scope message, CALM
triggers the handle_out_of_scope flow and returns the associated
message to the user.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
In exercise 2 scenario 3, the LangGraph agent admitted defeat ('I
cannot perform this task...') after 'inventing' a function that didn't
exist and call it. Here the workflow is more measured and the agent 
informs the user of its limitations and the need to escelate if the 
user needs help with parking / something else. The communication is 
clearer here."""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ['exercise3_rasa/actions/actions.py']

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I tested it by changing the if statement in actions.py line 121
to 'if True:' to force the escalation. I then restarted the server
and went through the conversation again.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
The LLM now handles the elements of the interaction that have nuance
so we are leveraging the LLM's ability to interpret natural language 
and to extract the data from the user's message. We gain a more flexible
and wide reaching interpretation of the input. When the model needs to
make a decision that is more discrete / black and white, we revert
to using the cold hard logic of Python as this is sufficient. We use
both approaches (LLM and Python) when it suits their strengths. The downside
of this combined approach is the usual risk of hallucination or relinquishing
control to the LLM.

Think about:
- What does the LLM handle now that Python handled before?
- What does Python STILL handle, and why (hint: business rules)?
- Is there anything you trusted more in the old approach?
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
In return for the Rasa CALM setup costs, we get a more tightly defined
and rigid workflow that doesn't have the LangGraph flexibility. In the 
context of managing a booking such as this one, this is a good thing 
as it forces the agent to stick to the script and lessens the risk of 
hallucination or of looping indefinitely. There are circumstances where
the creativity of LangGraph might be a benefit such as when it needs
to improvise a response to a situation it hasn't been trained on but
for this use case, I think the additional costs are worth it to keep
the process on rails.

Be specific. What can the Rasa CALM agent NOT do that LangGraph could?
Is that a feature or a limitation for the confirmation use case?
Think about: can the CALM agent improvise a response it wasn't trained on?
Can it call a tool that wasn't defined in flows.yml?
"""
