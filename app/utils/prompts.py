EVAL_PROMPT = """
Evaluate the following candidate answer.

Return ONLY valid JSON:
{
  "score": <1-5>,
  "summary": "<one sentence summary>",
  "improvement": "<one improvement suggestion>"
}

Candidate Answer:
"{answer}"
"""