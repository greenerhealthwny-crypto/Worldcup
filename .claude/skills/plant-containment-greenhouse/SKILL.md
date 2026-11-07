---
name: plant-containment-greenhouse
description: "Use whenever the user is working on plant biosafety or containment in research greenhouses, growth chambers, growth rooms or screenhouses, even if they don't name this skill. Covers assigning a biosafety level (BL1-P to BL4-P, BSL-3Ag) to experiments with transgenic/GE plants, plant pathogens, exotic or quarantined organisms, insects and mites, plant-made pharmaceuticals and Select Agents; designing physical and biological containment (screens, pollen filtration, negative pressure, vestibules, cages, flower bagging); greenhouse management practices (access, apparel, signage, transfer, devitalization and disposal, pest control, monitoring, records); SOPs, IBC biosafety reviews and APHIS inspection prep; loss-of-containment response; and designing, building or retrofitting containment greenhouses. Based on 'A Practical Guide to Containment: Plant Biosafety in Research Greenhouses' (Adair & Irwin, ISB/Virginia Tech, 2nd ed. 2008)."
---

# Plant Containment in Research Greenhouses

Practical containment guidance for greenhouses and plant growth facilities, distilled from *A Practical Guide to Containment: Plant Biosafety in Research Greenhouses* (Dann Adair and Ruth Irwin, Information Systems for Biotechnology, Virginia Tech, revised edition 2008). Page numbers below ("Guide p. N") refer to that edition.

The goal of all containment in this guide is **environmental protection**: stop propagules (pollen, seed, spores, microbes, insects) moving from inside the facility to a receptive environment outside. Worker protection matters only in rare plant cases.

## Before you answer: currency warning

The source is a 2008 snapshot of US rules. Regulations, agency programs, phone numbers and URLs it cites have changed since (for example, the guide itself warned that APHIS-BRS rules were about to change, and the NIH Guidelines have been revised since). So:

- Use this skill for **principles, practices, design features and checklists**. Those age well.
- For anything **regulatory** (which permit, who to notify, reporting deadlines, whether an experiment is exempt, current Select Agent list), state what the guide said, say it is from 2008, and tell the user to confirm with their IBC/Biosafety Officer and the current agency rules (USDA-APHIS, NIH Office of Science Policy, EPA, FDA, CDC/APHIS Select Agent Program, or their national authority outside the US). If web search is available, check the current rule before relying on it.
- Never present a containment level, exemption or permit decision as final. In the guide's model the PI proposes, the IBC verifies, and regulators decide case by case.

## Reference files (read the one you need)

| File | Use it for |
|---|---|
| `references/biosafety-levels.md` | Assigning BL1-P to BL4-P / BSL-3Ag, exemptions, the assignment criteria and Table 2, and a level-by-level practice matrix |
| `references/containment-strategies.md` | Routes of escape, physical containment (glazing, sealing, screens, pollen filters, air pressure, vestibules, cages, siting), biological containment and layering, plant/microbe/insect containment tactics |
| `references/management-practices.md` | Access, apparel, signage, labeling, storage, transfer, termination and disposal (temperatures and times), pest control, training, monitoring, loss of containment, records, inspections, security, SOPs |
| `references/facility-design.md` | Design team and construction phases, location, layout, security hardware, structure, glazing, floors and drains, doors, vestibules, screening, HVAC, pressurization and infiltration testing, benching, lighting, controls, piping, screenhouses, growth chambers, retrofit vs. rebuild |
| `references/oversight-and-roles.md` | NIH Guidelines Appendix P, US agencies (APHIS PPQ/BRS, EPA, FDA, CDC), international bodies, IBC/BSO/containment officer/PI/staff responsibilities (2008 snapshot) |
| `references/templates.md` | Biosafety review form outline (IBC), sample TMV quarantine guideline, APHIS-style facility inspection worksheet, minimum inspection questions, SOP topic list |

## How to run it

1. **Pin down the situation.** From the user's message, identify: the organisms (plant species, any pathogen, vector, microbe, insect), whether anything is genetically engineered and what the insert is, whether the organism is exotic/quarantined/Select Agent, the facility type (greenhouse, growth chamber, screenhouse), location and nearby crops or wild relatives, and what deliverable they want. If something essential is missing, ask for all of it in one short message. If they want you to go ahead, state your assumptions at the top.
2. **Pick the job type** and read the matching reference file(s):
   - *What level does this need?* → biosafety-levels.md (then containment-strategies.md for ways to layer down).
   - *How do I contain X?* → containment-strategies.md, plus the matrix in biosafety-levels.md.
   - *Write an SOP / training manual / disposal plan / breach plan* → management-practices.md + templates.md.
   - *Prepare for an IBC review or APHIS inspection* → templates.md + management-practices.md.
   - *Design, build or retrofit a facility* → facility-design.md + biosafety-levels.md matrix.
   - *Who is responsible / which agency* → oversight-and-roles.md (with the currency warning).
3. **Reason from risk, not from labels.** Work through: how the organism disseminates (wind, insects, water, people, animals), whether it can survive and find a host or mate outside, and what harm it could do. Name the most likely route of escape. The guide says human error (doors left open, unlabeled material thrown out in normal trash) causes more breaches than equipment failure, so always address people and procedures, not just hardware.
4. **Produce the deliverable** (see formats below). Match practices to the assigned level: the guide warns that procedures that look excessive for the real risk discourage compliance.
5. **Check against the quality rules** below, fix misses, then reply. End with at most one line offering a sensible next step (e.g., turn it into an SOP, an inspection checklist, or a room-by-room retrofit list).

## Output formats

- **Level assignment:** recommended level (and the "+ biological containment" alternative if one applies) → the criteria that drove it → what that level requires in practice (bullets by facility / practices / records) → what could move it up or down → who must approve it.
- **Containment plan:** organisms and escape routes → physical measures → biological measures → management practices → monitoring → termination/disposal → emergency response → responsibilities.
- **SOP:** purpose and scope → responsible person → materials/equipment → numbered steps → disposal and decontamination → what to do if something goes wrong → records kept → review date. Keep steps short and checkable.
- **Inspection prep / gap analysis:** a table of requirement → current state → gap → fix → owner, grouped by area (security and commingling, lab, growth chamber, greenhouse, records).
- **Design or retrofit brief:** required level → site and layout → envelope (structure, glazing, sealing) → floors and drains → doors and vestibules → screening and HVAC/pressure → controls, alarms and power → testing and commissioning → retrofit-vs-new cost check.

## Quality rules

- Tie every recommendation to the level and to a specific escape route or risk. No generic "follow best practices".
- Use the guide's numbers exactly when you give them (screen mesh sizes, sterilization temperatures and times, pressure differentials, infiltration rates) and say where they come from. Don't invent figures the guide doesn't give; say what the user needs to measure or confirm instead.
- In a room with mixed material, everything follows the **highest** level required by anything in the room.
- Recommend layering (physical + biological) where it genuinely lowers risk, and say that a lower level via layering still needs IBC/regulator agreement.
- Always include termination/disposal and a loss-of-containment response for BL2-P and above.
- Prefer the simple solution when two give the same result (the guide's quoted design advice).
- Flag anything regulatory as "per the 2008 guide; confirm current rule" and point to who decides.
- Don't overuse the biohazard symbol in signage; the guide reserves it for infectious agents that threaten people.
- If the user is outside the US, keep the principles but tell them to map the roles and permits to their national authority.
