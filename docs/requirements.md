# SchemeAssist AI – Data Requirements

## Citizen Profile Information
The system requires a limited set of user-provided details to evaluate scheme
eligibility and personalize recommendations:
- Age of the applicant  
- Household annual income  
- Residential location (state and district)  
- Social classification for reservation based schemes  
- Gender

## Government Scheme Information
Each welfare scheme is represented using structured attributes that define
its scope and eligibility conditions:
- Official scheme title  
- Summary of benefits offered  
- Key eligibility conditions  
- Age based eligibility boundaries  
- Income thresholds for participation  
- Geographic applicability (central, state-specific, or local)  
- Demographic eligibility conditions, including category and gender  

## Data Sources
To maintain consistency in location-based filtering, the system aligns
administrative boundaries with official government references such as
the Local Government Directory (LGD).

## Data Usage and Integration Strategy
SchemeAssist AI uses a simple and practical data approach:
- Official reference data is used wherever it is available to ensure accuracy.
- When live data sources are not available, scheme eligibility is handled using predefined rules. 

