---
name: plant-mineral-nutrition
description: Apply the teachings of "Plant Mineral Nutrients: Methods and Protocols" (Frans J.M. Maathuis, ed., Methods in Molecular Biology vol. 953, Humana/Springer 2013) — the roles, uptake, transport and functions of the essential plant nutrients (N, K, Ca, Mg, P, S, Cl, Fe, B, Mn, Zn, Cu, Ni, Mo), and the laboratory methods used to study them: growing plants in soil, hydroponics and on agar (nutrient-solution recipes, seed sterilization, growth conditions), mycorrhizal and rhizobial symbioses, plant cell suspension cultures, vis-NIR soil spectroscopy, anion (HPLC) and multielement (ICP-OES/ICP-MS, LA-ICP-MS) tissue analysis, synchrotron XRF element mapping, radiotracer and MIFE ion-flux measurements, phloem and xylem sap sampling, single-cell sampling, cytosolic ion dyes and ion-selective microelectrodes, ionomics, and image-based phenotyping of nutrient use efficiency. Use when the user asks what a nutrient does in a plant, diagnoses deficiency or toxicity, designs a hydroponic or nutrient-solution recipe, plans a plant-nutrition experiment, chooses or troubleshoots an analytical method, or interprets tissue, sap or flux data.
---

# Plant Mineral Nutrition (Maathuis, ed.)

A working guide distilled from *Plant Mineral Nutrients: Methods and Protocols*, edited by Frans J.M. Maathuis (Methods in Molecular Biology, vol. 953, Humana Press/Springer, 2013). The book has 18 chapters by different research groups:
- Chapter 1 reviews what each essential nutrient does.
- Chapters 2–5 cover how to grow plants, symbioses and cell cultures.
- Chapters 6–18 are bench protocols for measuring nutrients in soil, tissues, sap, single cells and whole plants.

**The book's premise:** people eat plants directly or indirectly, fertilizer is expensive and polluting, and populations are growing. So we need to understand how plants acquire, move, store and use minerals, both to grow crops with fewer inputs and to make food more nutritious (biofortification).

## Core principles

1. **Essential means the plant can't complete its life cycle without it.**
   - Besides C, H and O (from CO₂ and water), plants need 14 mineral elements.
   - Six macronutrients: N, K, Ca, Mg, P, S.
   - Eight micronutrients: Cl, Fe, B, Mn, Zn, Cu, Ni, Mo.
   - Na, Si and Co are "beneficial" for some species or symbionts.
   - About 95% of dry matter is C, H and O; minerals make up the remaining ~5%.
2. **Plants take up nutrients as ions from the soil solution, through specific transport proteins.** Common patterns:
   - Uptake systems have two affinity ranges: high-affinity (µM range, often inducible by deficiency) and low-affinity (mM range).
   - Anions (NO₃⁻, H₂PO₄⁻, SO₄²⁻) and most micronutrients need energy: they are co-transported with H⁺.
   - Cations (K⁺, NH₄⁺, Ca²⁺, Mg²⁺) mostly enter passively through channels, driven by the negative membrane potential.
3. **Availability in soil is low and patchy, so plants adapt.** Strategies:
   - Proliferating lateral roots or cluster roots in rich patches.
   - Exuding acids, chelators or phytosiderophores to release nutrients.
   - Partnering with mycorrhizal fungi (more than 90% of species) and N-fixing rhizobia.
   - Storing surpluses in the vacuole, the cell's "well-buffered larder" for K⁺, NO₃⁻, SO₄²⁻, Ca²⁺ and phosphate.
4. **Nutrients interact.**
   - NO₃⁻ moving from root to shoot needs K⁺ as a counter-ion.
   - NH₄⁺ and amino acids suppress NO₃⁻ uptake.
   - Ca, K and Mg compete with each other.
   - P deficiency shifts membranes toward sulfolipids.
   - Heavy-metal stress raises sulfate demand (for phytochelatins).
   - Ni is taken up through Fe transporters.
   Design experiments and diagnoses with the whole system in mind.
5. **Mobility decides where symptoms appear.**
   - Mobile nutrients (N, P, K, Mg, Cl) are moved out of old leaves, so deficiency shows on **older** leaves first.
   - Immobile nutrients (Ca, B, Fe, Cu, Mn; S and Zn intermediate) show deficiency on **young** tissue, tips and fruits.
   - Ca moves only with the transpiration stream. That is why blossom-end rot, bitter pit and blackheart appear even in Ca-rich soils when humidity is high or water supply is erratic.
6. **Control the growing conditions or the data mean nothing.**
   - Use defined media (hydroponics, agar) and deionized water.
   - Stratify seeds for uniform germination, and use uniform seedlings.
   - Keep light, photoperiod, temperature and humidity constant.
   - Grow mutants and wild type in the same container.
   - Change solutions on a schedule and monitor pH.
7. **Contamination is the enemy of element analysis.** Rinse off dust and soil. Desorb root apoplast ions. Use plastic or PTFE labware, titanium mills and plastic tweezers, never metal scissors. Clean labware in acid baths. Run blanks and certified reference materials (CRMs) with every batch.
8. **Validate every measurement.**
   - Use calibration curves spanning at least 3 orders of magnitude.
   - Check drift with a control every 10 samples.
   - Accept an element only when CRM recovery is within ±10% of the certified value.
   - Calculate the limit of detection (LOD = 3σ) and limit of quantification (LOQ = 10σ) from at least 7 blanks.
   - Use independent validation sets for spectroscopic models.
   - Calibrate electrodes at the temperature you measure at.
9. **Pick the method for the question and the scale:**
   - Whole tissue: ICP-OES/ICP-MS, HPLC.
   - Distribution in tissue: LA-ICP-MS, synchrotron µ-XRF.
   - Single cells or vacuoles: picolitre sampling with EDX analysis.
   - Cytosol: ion-selective dyes and microelectrodes.
   - Fluxes: radiotracers for unidirectional flux, MIFE for net flux in real time.
   - Long-distance transport: xylem and phloem sap.
   - Genes: ionomics.
   - Whole-plant nutrient use efficiency: image-based phenotyping.
10. **Every sampling method has artifacts.** Know them:
    - Excised roots have wound responses.
    - EDTA-exudation dilutes phloem sap to an unknown extent.
    - Decapitated plants lose phloem recycling.
    - Freeze-drying redistributes mobile ions.
    - Rb⁺ is an imperfect stand-in for K⁺.
    - Parafilm releases toxic compounds.

## How to use this skill

| User wants… | Go to |
|---|---|
| What a nutrient does, how it's taken up and moved, and signs of deficiency or toxicity | `references/nutrients.md` |
| Typical tissue concentrations, symptom-diagnosis key | `references/nutrients.md` §Quick reference |
| Growing plants in soil, hydroponics or on agar; nutrient-solution recipes; seed sterilization; growth conditions for Arabidopsis, barley, rice and Thlaspi | `references/growth-and-culture.md` §1–§4 |
| Mycorrhizal inoculation, root organ culture, rhizobial nodulation assays, cell suspension cultures and protoplasts | `references/growth-and-culture.md` §5–§7 |
| Pot field capacity, image-based phenotyping, nutrient use efficiency | `references/growth-and-culture.md` §8 |
| Tissue element analysis (ICP-OES/MS, digestion, QA/QC), anion HPLC, ionomics | `references/analysis-methods.md` §1–§3 |
| Soil vis-NIR spectroscopy and calibration | `references/analysis-methods.md` §4 |
| Element imaging (LA-ICP-MS, synchrotron XRF) | `references/analysis-methods.md` §5 |
| Ion fluxes (radiotracers, ¹⁵N, MIFE), cytosolic ions (dyes, ion-selective microelectrodes) | `references/analysis-methods.md` §6–§7 |
| Phloem and xylem sap, single-cell sampling | `references/analysis-methods.md` §8–§9 |
| Choosing a method, lab safety | `references/analysis-methods.md` §10–§11 |

**Workflow for a plant-nutrition problem or experiment:**
1. **Define the question and scale:** field diagnosis, a controlled experiment, or a mechanism in a tissue, cell or transporter. Decide which nutrient or nutrients, and whether you care about deficiency, toxicity or efficiency.
2. **Choose the growth system:** soil or peat mix (realistic), hydroponics (precise control of supply, roots accessible), or agar plates (sterile, root phenotyping). Set nutrient levels deliberately: omit or lower the target nutrient and substitute counter-ions, such as KCl for KNO₃ in low-N treatments.
3. **Standardize:** seed lot and size, sterilization, stratification, light (µmol m⁻² s⁻¹), photoperiod, temperature, humidity, solution pH and renewal, and randomized positions.
4. **Measure with the right method** (§10 of the analysis file), with blanks, CRMs and standards, replicate plants (not replicate scans), and a record of fresh and dry weights.
5. **Interpret mechanistically:** uptake vs translocation vs storage (vacuole) vs use. Check against reference ranges and against interacting nutrients. Report concentration on a dry-weight basis with units.

## Output style

- Explain the physiology briefly (form taken up, transporter family, where it goes, what it does), then give concrete protocol steps, recipes and numbers with units: mM or µM in solution; µg/g, % DW or µmol/g DW in tissue; µmol m⁻² s⁻¹ for light.
- For recipes, give stock concentration, volume of stock per litre, and final concentration, as the book does. State the pH target and how to adjust it (KOH if you need a Na-free solution).
- Flag assumptions and species differences (Arabidopsis ≠ cereals ≠ rice). These are research protocols; tell users to adapt them to local facilities.
- **Safety:** Flag hazards whenever a protocol involves them: radioisotopes (licensing, shielding, dosimetry), HF and hot concentrated HNO₃/H₂O₂ digestions, chlorine-gas seed sterilization (fume hood), silanizing agents (toxic vapour), pressure vessels (Scholander bombs can eject the lid; stay below the vessel's rated pressure, ~3 MPa in the book's example; wear safety glasses), liquid nitrogen, and transgenic or biological waste (autoclave).
- **Corrections to the source**, applied throughout this skill:
  - Ch. 1 lists Co instead of B among micronutrients. B is essential; Co is needed by N-fixing symbionts, not by plants directly.
  - Ch. 1 gives soil-solution phosphate as "~0.1–1 mM". Typical values are about 0.1–10 **µM**.
  - Ch. 1 gives the high-affinity Sultr sulfate transporters a Km of "~10 mM". It is about 10 **µM**.
  - Ch. 1 names "ribulose-1,6-bisphosphate carboxylase". It is **ribulose-1,5-bisphosphate** (Rubisco).
  - Ch. 1 gives apatite as "CaHPO₄". Apatite is Ca₅(PO₄)₃(F,Cl,OH); CaHPO₄ is dicalcium phosphate.
  - Ch. 1 gives magnesite as "MgO". Magnesite is MgCO₃.
  - Ch. 18's "(WW − DW)/DW" is **gravimetric** water content. Multiply by bulk density to get volumetric.
