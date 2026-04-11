"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
The model correctly chose either the Haymarket Vaults or 
the Albanach as the correct answer for all three conditions. 
Unstructured 'PLAIN' input resulted in the model choosing 
the Haymarket Vaults which is in the 'middle' of the context, while
the structured 'XML' and 'SANDWICH' conditions resulted in the
model choosing the Albanach which is at the beginning of the context.
Intuitively, this is surprising to me as I would have expected the
model to gain a better 'overview' of the context and not process it
as linearly when the inputs were XML or SANDWICH, but it looks like 
that's what's happening.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
I think that the most likely distractor to cause a wrong answer
is the Holyrood Arms as it is most similar to the Haymarket Vaults
and is positioned directly before it in the context. This makes the 
'signal' less distinguishable from the 'noise' around it. Both entries 
have capacity of 160 and vegan options, both begin with a 'H', have 
2 words in their names etc:

The Holyrood Arms: capacity=160, vegan=yes, status=full
The Haymarket Vaults: capacity=160, vegan=yes, status=available

Inerestingly, the model used up more tokens to answer the question in
part B than part A - this suggests that the problem being solved is 
more complex in part B than part A. Which is kind of expected given the 
added near-miss distractors etc.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C showed since all of part A and all of part B selected answers
that were in the set of ACCEPTABLE answers, i.e. the Haymarket Vaults 
or the Albanach. It was necessary to use the smaller model to attempt
to see the effect of the near-miss distractors on the model's ability 
to select the correct answer.

"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the signal to noise ration is low or
when the signal is not easily distinguishable from the rest of the context.
In our experiments, it seems that the real distinction in behaviour is seen
between the large / small models with the larger model (A and B) choosing 
different answers based on context / presence of distractors, while the 
smaller model (C) didn't seem to respond to these changes (chose same option
in all three conditions).
Interestingly, the small model chose the Haymarket Vaults in all three conditions,
which is the option that is both in the middle of the context and the one
most likely to be confused by distractors (in particular, the Holyrood Arms).
This suggests that the smaller model has less primacy bias and / or is less
sensitive to context engineering.

"""
