# Output Contract

Use this structure when a user needs a reusable or machine-readable result.

```json
{
  "insight": {
    "core_user": "",
    "main_pain": "",
    "main_desire": "",
    "click_barrier": "",
    "purchase_barrier": ""
  },
  "purchase_reasons": [
    {
      "reason": "",
      "evidence": [],
      "visual_proof": ""
    }
  ],
  "primary_hook": {
    "type": "pain|benefit|contrast|scene|emotion|value_bundle|trust|data",
    "copy": ""
  },
  "images": [
    {
      "index": 1,
      "role": "click image",
      "shopper_question": "",
      "objective": "",
      "headline": "",
      "supporting_points": [],
      "composition": "",
      "visual_proof": "",
      "required_evidence": [],
      "risk_note": ""
    }
  ],
  "evidence_gaps": [],
  "compliance_risks": [],
  "score": {
    "recognition": 0,
    "hook": 0,
    "purchase_reason": 0,
    "differentiation": 0,
    "visual_proof": 0,
    "hierarchy": 0,
    "trust_compliance": 0,
    "total": 0
  },
  "ab_tests": [
    {
      "variable": "",
      "version_a": "",
      "version_b": "",
      "primary_metric": ""
    }
  ]
}
```

## Natural-language default

When JSON is not requested, present:

1. diagnosis
2. top purchase reasons
3. primary hook
4. 5-image plan in a table
5. evidence gaps
6. score
7. A/B tests

Do not bury the recommendation under theory.
