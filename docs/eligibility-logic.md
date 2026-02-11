# Eligibility Evaluation Logic – SchemeAssist AI

## Purpose
This document explains how SchemeAssist AI evaluates user eligibility
for government schemes.

---

## Core Eligibility Factors
Eligibility evaluation is based on a combination of user profile
attributes and scheme-specific conditions. The primary factors include:

- Income
- Age
- Location
- Social category
- Gender (where applicable)

---

## Income-Based Evaluation
- The user’s annual family income is compared against the minimum
  and maximum income limits defined for each scheme.
- Schemes that fall within the user’s income range are considered eligible.
- Income is treated as a key factor in determining overall priority.

---

## Age-Based Evaluation
- User age is checked against scheme-specific age requirements.
- Schemes with age limits outside the user’s age range are excluded
  from recommendations.
- Age-based checks are applied before final ranking.

---

## Location-Based Evaluation
- The user’s state and district are matched with the scheme’s
  geographic applicability.
- Central schemes are considered applicable to all users.
- State or local schemes are considered only if the user’s location matches.

---

## Category and Gender Evaluation
- Social category is matched against category-specific scheme rules.
- Gender-based schemes are evaluated only when the user meets
  the specified gender requirement.
- These factors help refine eligibility and improve relevance.

---

## Eligibility Outcome
Based on the combined evaluation:
- Schemes may be classified as highly eligible, moderately eligible,
  or not eligible.
- Eligible schemes are passed to the scoring and ranking stage
  for further prioritization.
