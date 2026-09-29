# Measuring Nutrients: Soil, Tissues, Sap, Cells, and Fluxes

Distilled from Chapters 6–17 of *Plant Mineral Nutrients: Methods and Protocols*. The wording is our own. Instrument brands appear only where the book names them as examples; equivalents work.

---

## §1 Multielement tissue analysis: ICP-OES and ICP-MS (Ch. 8)

**Why it matters:**
- Diagnoses crop nutrient status against species-specific thresholds.
- Checks food quality (essential elements, and toxic Cd, As, Hg).
- Supports biofortification breeding (Fe, Zn, Se, Mg), gene discovery (ionomics), nutrient-use-efficiency studies, and authenticity testing of organic produce.
- ICP techniques have largely replaced single-element atomic absorption (AAS). They cover about 0.1 to more than 50,000 µg/g in one run.

| | ICP-OES | ICP-MS |
|---|---|---|
| Sensitivity | Good for macronutrients and most micronutrients | Superior (sub-ppt); needed for Cd, Pb, Hg, **Ni, Mo** |
| Matrix tolerance and stability | Better | Lower; watch interferences such as ⁴⁰Ar¹⁶O⁺ on ⁵⁶Fe (use a collision/reaction cell) |
| Sample volume | ~5–10 mL | ~100 µL/min with a micronebulizer |
| Semi-quantitative screening | No | Yes (fast fingerprints) |

**Sample preparation:**
1. **Decontaminate:** rinse once in Tween-20 (1 g/L), then 3× in ultrapure water. Field dust and fertilizer residues inflate results.
   - **Hydroponic roots** need apoplast desorption: Tween rinse, 2× desorption solution (0.2 mM CaCl₂ + 12.5 µM H₃BO₃), then water. If Ca and B are analytes, desorb instead with 5 mM EDTA + 5 mM MES-Tris, pH 6.
2. **Freeze-dry** rather than oven-dry.
3. **Grind** in a mill with a **titanium** rotor (no trace-metal contamination).
4. Re-dry sample and CRM for 2 h at 60 °C before weighing.
5. Use 150–300 mg for representative subsampling. Micro-methods handle 2–20 mg.

**Labware:**
- Plastic or PTFE. Quartz for Se.
- Acid-bath clean: 10% HNO₃ for PTFE, 5% for glass, at least 2 h. Rinse 3× in ultrapure water and air-dry somewhere clean.
- Store all liquids in plastic.

**Digestion (HNO₃ + H₂O₂, typically 2:1):**
- **Open block** (cheap; leaf matrices only):
  1. 200–250 mg + 5 mL 35% HNO₃, reflux at 90–95 °C.
  2. Add 2.5 mL 69% HNO₃ and reflux 30 min.
  3. Add H₂O₂ in 1–1.5 mL aliquots until the reaction stops (normally ~3 mL, never more than 5 mL).
  4. Reduce volume to 5 mL, dilute to 50 mL (~7% HNO₃), then dilute 1:1 before analysis (3.5% HNO₃).
  - S and Fe are often underestimated with open digestion. Centrifuge or filter before analysis.
- **Closed microwave, macro** (100–300 mg): 5 mL 69% HNO₃ + 5 mL 15% H₂O₂; ramp to 1,400 W over 10 min and hold about 38 min; vent in a fume hood; dilute to 50 mL, then 1:1.
- **Closed microwave, micro** (2–20 mg): 250 µL HNO₃ + 125 µL 30% H₂O₂ at 140 °C for 80 min. Weigh vials before and after; correct results if more than 3–5% is lost.
- **Pressurized (N₂ at 40 bar, 230 °C):** mixed sample sizes, no cross-contamination.
- **Silica-rich material** (rice straw, grasses): add HF (HNO₃:HF about 2:1), then complex excess HF with H₃BO₃. HF is extremely hazardous; use specific training and calcium gluconate on hand.
- **Grain** underestimates Fe and S unless digested longer.

**QA/QC run design:**
1. Tune the instrument.
2. External calibration with at least 8–10 standards covering at least 3 orders of magnitude.
3. Two wash cycles.
4. A **drift-control sample** (a matrix-matched CRM) every 10 samples; correct drift if RSD exceeds 5%.
5. At least **7 independently digested CRMs** (e.g., NIST 1515 apple leaves, NIST 1567a wheat flour). Accept only elements recovered within **±10%** of certified values.
6. At least **7 true blanks**: LOD = 3σ, LOQ = 10σ.
7. Internal standard (e.g., Er or Y) spiked into, or teed into, all samples.
8. Report µg/g DW. Values near the LOD aren't reproducible.
- Use ultrapure (sub-boiled) HNO₃ for trace work. Analytical grade may carry S and other backgrounds.

**Bioimaging with LA-ICP-MS:**
- A laser (5–500 µm spot) ablates the solid sample and carrier gas (He/Ar) sweeps it into the plasma.
- **Leaves:** rinse, tape flat to a slide, freeze-dry at least 12 h.
- **Grain:** freeze-dry, glue down, section with a vibrating-blade vibrotome for a smooth face.
- Typical leaf settings: 25–50 µm spot, 25–50 µm/s, 10–20 Hz, ~0.2 GW/cm². Tune on NIST SRM 612 glass.
- Use ¹³C as the internal standard. Quantification is matrix-dependent and hard; use pressed CRM pellets.
- Resolution depends on spot size, line spacing, scan speed and the ICP-MS cycle time (more elements means a slower cycle).

---

## §2 Anion analysis by HPLC, and anion influx (Ch. 7)

**Tissue content** (NO₃⁻, SO₄²⁻, phosphate, Cl⁻, NO₂⁻, malate in a single run):
1. 10–100 mg dry ground tissue + 1–2 mL water; heat at 80 °C for at least 30 min (2–4 h is better).
2. Centrifuge at 13,000 × g for 20 min. Freeze the supernatant overnight, thaw, and spin again (removes carbohydrate precipitate).
3. Filter through 0.2 µm and inject 0.1 mL.
- **Column and eluent:** an anion-exchange column (e.g., IonPac AS9-SC + guard) with carbonate/bicarbonate eluent (1×: 1.8 mM Na₂CO₃ / 1.7 mM NaHCO₃), a suppressor and a conductivity detector, at about 2 mL/min. Use helium-sparged ultrapure water.
- **Calibration:** 5-point standards, with a standard every 10 samples.
- **Troubleshooting:**
  - Dark extracts: clean up with XAD resin or PVP.
  - Off-scale peaks: dilute, or run twice.
  - Poor separation: clean the guard column first (200 mM Na₂CO₃/75 mM NaHCO₃), then both columns with acetonitrile/acidic NaCl, with the column order reversed.
  - Bunched peaks: lower the flow rate, but never below 1 mL/min.
- **Sulfate:malate ratio** diagnoses crop S status without absolute calibration.
- Alternatives: colorimetry, barium turbidimetry for sulfate, continuous-flow analyzers, capillary electrophoresis.

**Influx capacity:**
- Use the growth solution spiked with isotope: ³⁵SO₄²⁻, ³²P/³³P-phosphate, or ¹⁵NO₃⁻ at ~25% enrichment, measured by MS. ¹³N works but needs a cyclotron.
- Typical uptake concentrations: 2 mM NO₃⁻, 0.15 mM SO₄²⁻, 0.1 mM phosphate. Optionally buffer with 2.5 mM MES/Tris pH 5.5. Aerate; 20–25 °C.
- **Protocol:**
  1. Hang roots in the labelled solution (~50 mL per 100–200 mg root FW) for 10–20 min.
  2. Rinse 2 × 30 s in unlabelled solution.
  3. Blot, excise, weigh.
  4. For ³²P/³⁵S: extract in 0.1 M HCl at 100 °C for 30 min, then scintillation-count.
- Calibrate against the measured specific activity of the uptake solution. Longer labelling shows translocation to the shoot.

---

## §3 Large-scale ionomics (Ch. 17)

**What it is:** high-throughput ICP-MS profiling of about 20 elements across thousands of plants (mutants, natural accessions, mapping populations). It finds genes controlling the ionome, for example roles for suberin, sphingolipids, phloem transport and cytokinins, and natural variation in Na, Mo, Co, Cu and S.

**Standardize everything:**
- Same soil batch, with the element mix sprayed in while mixing.
- Pre-wet trays for 24 h. Stratify 2 days at 4 °C.
- Bottom-water with 0.25× Hoagland + Fe-HBED twice a week (once when humidity is above 70%).
- Short days (10 h), about 90 µmol m⁻² s⁻¹. Harvest at 5 weeks.
- **Include control lines in every tray**; normalize to them.

**Harvest cleanly:**
- Gloves, plastic tweezers, scalpel. **No metal scissors.**
- Two leaves per plant. Rinse in deionized water, then place in acid-conditioned Pyrex tubes. Pre-digest new tubes 3× to cut Na and B leaching.

**Weight calculation:**
- For samples too small to weigh accurately (below ~3–5 mg on a 5-place balance), estimate dry weight from the summed concentrations of well-behaved elements, calibrated on 7–9 weighed "basis" samples.
- This assumes similar composition. Don't use it where groups differ systematically.

**Data:** a LIMS/workflow database tracks planting, harvest, drying, digestion and ICP stages. Store raw concentrations, then normalize to weight and controls. Public data is on the ionomics hub (ionomicshub.org).

---

## §4 Soil analysis by vis-NIR diffuse reflectance spectroscopy (Ch. 6)

**Principle:**
- Visible (400–780 nm) and NIR (780–2,500 nm) light is absorbed by bond vibrations (overtones and combinations of O–H, C–H, N–H, metal–OH) and by electronic transitions.
- The spectrum carries information on:
  - **Clay minerals:** 1,400 and 1,900 nm water bands; 2,200–2,500 nm metal-OH bands. Smectite has a strong 1,900 nm band.
  - **Fe oxides:** 400–660 nm and ~900 nm (haematite 880 nm, goethite 930 nm).
  - **Carbonates:** ~2,300 nm.
  - **Organic matter:** visible darkness, plus weak NIR bands.
  - **Water.**
- It is fast, non-destructive and chemical-free. One scan predicts several properties.
- **Nutrient salts don't absorb.** Predicting available nutrients relies on co-variation with properties that do absorb, so those models are weaker and need more samples.

**Workflow:**
1. **Sample prep:** air- or oven-dry and crush or sieve to less than 2 mm. Dry soil usually calibrates better than moist, because the water bands swamp neighbouring features. Standardized re-wetting can also work.
2. **Measure:**
   - Scan a large, representative area, or take replicate scans and **average** them (averaging repeated scans avoids false replicates).
   - Mix the sample without shaking (shaking stratifies particle sizes). Flatten the surface with a tool. Pack every sample the same way.
   - Clean cups and windows dry (no water or solvents).
   - Take white (Spectralon) and dark references **about every 10 min**. Control stray light.
   - Instrument: aim for 10 nm resolution or better, covering 400–2,500 nm. Use a post-dispersive design with a fibre probe for field use.
3. **Pre-treat spectra:**
   - Convert to absorbance, log(1/R) (or Kubelka–Munk).
   - Try derivatives with smoothing (Savitzky–Golay), SNV plus detrending, multiplicative scatter correction, or wavelets.
   - Test options on your calibration set; no single best exists. Don't over-process.
4. **Reference analyses:** a model can't be better than its lab reference data. Screen reference and spectral data for errors. Remove outliers **sparingly**.
5. **Calibrate:**
   - Methods: PLSR (most common), PCR or MLR, or data-mining methods (ANN, MARS, boosted trees, Cubist) for large, diverse libraries.
   - The calibration set must span the variation where the model will be used. Aim for 100–200 or more samples for regional or national libraries; 25 is the bare minimum at field or farm scale.
   - Select samples by spectra (e.g., Kennard–Stone) for even coverage.
6. **Validate:**
   - Use a truly **independent** validation set (sampled separately if possible); about 2/3 calibration and 1/3 validation is a common benchmark.
   - Keep all horizons of one profile, or all samples from one field or cluster, on the **same side** of the split, including in cross-validation.
   - Report **RMSE**, **bias** (mean error), **SDE** (standard deviation of error) and **RPD** (SD of the reference values / RMSE). Plot predicted vs measured and look for nonlinearity. Ask whether the error is good enough for the intended use.
7. **Transfer:** calibrations are instrument-specific. To share them, use a common standard (e.g., washed and bleached quartz sand) and a common protocol.
- **Software:** vendor packages, or R (e.g., the `prospectr`, `pls` and `resemble` packages).

---

## §5 Element mapping with synchrotron X-ray fluorescence (Ch. 9)

**What it gives:**
- **µ-XRF:** quantitative 2-D maps of elements in situ, including in **fresh, hydrated** tissue.
- **XRF micro-tomography:** virtual cross-sections and 3-D distributions.
- **Complements:** LA-ICP-MS (destructive, bulk sensitivity), SEM-EDX (light elements, vacuum), NanoSIMS.

**Planning:**
- Pick a beamline and discuss it with its scientists early.
- Estimate beamtime from sample size, pixel size, dwell time and detector speed. Most experiments need 2–3 days; it is usually free via peer-reviewed proposals.
- Plan quarantine, transport, safety and **taking your samples home**.

**Incident energy:** set it above the absorption edges of all target elements. Example: Fe 7.11, Cu 8.98 and Zn 9.66 keV K-edges → ~10 keV. For heavy elements beyond range, use L-edges (e.g., Pb L₁ at 15.8 keV). Sometimes stay below an edge deliberately to avoid a dominant element.

**At the beamline:**
- Scan a reference standard daily.
- Bring a high-concentration test specimen to tune sensitivity.
- Know your target coordinates, and bring zoom-in images.
- Choose dwell time per pixel.
- Collect full spectra if possible, so elements can be extracted later.

**Sample preparation is decisive:**
- Artifacts scale with resolution: 1 µm of redistribution is irrelevant at 5 µm pixels but fatal at 100 nm.
- Freeze-drying can move mobile ions, so fresh or frozen-hydrated material is preferred.
- Keep hydrated samples from drying: seal between Ultralene films; you can map leaves still attached to the plant. Hutches get warm.
- For sections, snap-freeze. High-pressure freezing is best, for samples under 200 µm thick.
- Watch for **radiation damage** at high flux and long dwell.

---

## §6 Measuring ion fluxes

### Radiotracers for unidirectional influx (Ch. 10)
- **Why tracers:** they isolate **one-way** influx, needed for Km, Vmax, energetics and mechanism, especially when efflux is large and a net measurement would hide it.
- **Isotopes:**
  - ⁴²K (half-life ~12.4 h), ²⁴Na (~15 h), ¹³N (~10 min; needs a cyclotron).
  - ⁸⁶Rb (18.65 d) is common but an imperfect K analog, especially for translocation to the shoot.
  - ³²P, ³³P, ³⁵S, ⁴⁵Ca.
  - Stable isotopes (¹⁵N, ³⁴S) need mass spectrometry and are slower and less sensitive.
- **Protocol:**
  1. Measure the specific activity of the uptake solution.
  2. Pre-equilibrate 5–10 min.
  3. Label roots for **2–10 min**.
  4. **Desorb** in unlabelled solution (typically 5–10 min) to remove apoplastic tracer.
  5. Separate root and shoot. Spin roots briefly to remove surface water, weigh.
  6. Gamma- or scintillation-count.
  7. Flux = counts ÷ (specific activity × root mass × time).
- **Good practice:**
  - Use **intact** hydroponic plants where possible. Excised roots need hours of recovery (and sometimes sucrose), and they lose transpiration and partitioning information.
  - Keep labelling solutions identical to the growth solution, apart from the tracer, for steady-state work. Stripped-down "salt + CaSO₄" solutions change membrane potential and so change fluxes.
  - Use enough volume to avoid depletion (~200 mL for 5 min).
  - Measure under growth conditions, not on the open bench.
  - Bundle seedlings into one replicate if needed. Consider plant age and seed reserves.
- **CATE (compartmental analysis by tracer efflux):** load to steady state, then follow tracer release over time. The phases resolve surface, cell-wall and cytosolic pools, giving cytosolic concentrations and fluxes.
- **Safety:** needs a licence, shielding, dosimetry and a Geiger counter. ⁴²K and ²⁴Na are high-energy gamma emitters (millicurie quantities); plan waste disposal.

### MIFE: non-invasive microelectrode ion flux estimation (Ch. 11)
- **Principle:** ion-selective microelectrodes move slowly between two positions 20–30 µm from the tissue surface. The measured concentration gradient gives **net** flux via diffusion theory, with **µm and ~5 s resolution**, for up to three ions at once: H⁺, K⁺, Na⁺, Ca²⁺, Mg²⁺, NH₄⁺, Cl⁻, NO₃⁻. Similar systems are called SIET and SERIS.
- **Uses:** mapping flux profiles along the root (elongation vs mature zones); kinetics of responses to salinity, acidity/Al, oxidative stress, nutrient deficiency, pathogens; pharmacology of transporters and mutants.
- **Making electrodes:**
  1. Pull borosilicate blanks.
  2. Oven-dry at 220 °C and silanize with tributylchlorosilane (fume hood).
  3. Break back the tip to 2–3 µm.
  4. Backfill with electrolyte (e.g., K⁺: 200 mM KCl; Na⁺: 500 mM NaCl; Ca²⁺: 500 mM CaCl₂; H⁺: 15 mM NaCl + 40 mM KH₂PO₄).
  5. Front-fill 100–150 µm of commercial ionophore cocktail (liquid ion exchanger, LIX).
  6. Use within about 8–10 h.
- **Calibrate** with at least 3 standards. Accept slopes above 50 mV/decade (monovalent) or above 25 mV/decade (divalent), with r ≥ 0.999.
- **Measuring:**
  - Keep the solution simple, with target ions as low as physiologically sensible.
  - For H⁺, avoid alkaline pH and keep buffer minimal (pK at least 0.5 unit above pH).
  - Immobilize the root about 1 h beforehand. Roots 30–80 mm long are easiest; mount vertically for long apex recordings.
  - Record 10–15 min to steady state, then 1.5–2 min per position.
  - Revisit the first spot at the end to check stability.

---

## §7 Cytosolic ion concentrations

### Fluorescent dyes: Na⁺ with SBFI (Ch. 15)
- SBFI (sodium-binding benzofuran isophthalate) is a ratiometric dye. Load it as the AM-ester with Pluronic F-127 (mix the dye into the detergent droplet first), for 1 h at 22 °C in the dark. Wash, and allow 20 min for de-esterification.
- **Two-photon imaging** (rice cells): excite at **730 nm (Na⁺-bound) and 780 nm (free)**, emission ~515 nm. The 730/780 ratio rises with Na⁺ and plateaus near 150 mM.
- **Calibrate in situ:** permeabilize cells with gramicidin (2 µM) in 0–200 mM NaCl. Correct for autofluorescence using unloaded cells.
- **Cuvette method:** protoplasts (from etiolated seedlings) loaded with SBFI in a spectrofluorometer give population averages. The classic UV ratio is 340/380 nm.
- Limit illumination to acquisition time to avoid photobleaching.

### Ion-selective microelectrodes, intracellular (Ch. 16)
- **Multi-barrelled electrodes:** one barrel for membrane potential, one ion-selective barrel, and ideally a **pH barrel** to tell cytosol (pH ~7.3–7.5) from vacuole (acidic).
- **Sensor cocktail:** ionophore or exchanger + plasticizer + lipophilic additive + **PVC matrix**. The matrix is essential in plant cells; without it, turgor pushes the liquid membrane out. It raises resistance and slows the response.
  - Nitrate example: methyltridodecylammonium nitrate 3 mg, nitrocellulose 2.5 mg, PVC 11.5 mg, methyltriphenylphosphonium bromide 0.5 mg, nitrophenyl octyl ether 32.5 mg, dissolved in ~4 vol THF. About 70 electrodes per batch; keeps weeks at 4 °C.
- **Steps:**
  1. Silanize only the ion-selective barrel (heat lamp, 140 °C; toxic vapour, fume hood).
  2. Backfill the cocktail and let the THF evaporate for about 48 h.
  3. Backfill the salt solution (no bubbles).
  4. Condition at least 30 min in 0.1 M of the target ion.
  5. Calibrate. Slope about 58 mV/decade for monovalent ions at 20 °C, with low detection limit and good selectivity.
- **Calibrate at the measurement temperature:** the slope is about 55 mV/decade at 4 °C.
- Use Ca²⁺ and H⁺ buffers for calibrations in the low range.
- Unfilled silanized electrodes store for years over silica gel in the dark.

---

## §8 Long-distance transport: phloem and xylem sap

### Phloem sap (Ch. 12)
- **Why:** the phloem redistributes minerals as well as sugars, and it carries signals (flowering and tuberization signals, systemic resistance, silencing, nutrient-allocation signals). It is often neglected because sieve elements seal quickly when wounded (P-protein and callose).
- **Choose a method:**
  - **Spontaneous exudation** (cucurbits, *Ricinus*, *Brassica*, *Yucca*, some trees):
    1. Cut or puncture the phloem.
    2. **Blot away the first drop** (contamination from injured cells).
    3. Collect into tubes on ice or liquid N₂, or straight into Trizol or protein buffer.
    - Large volumes (mL from pumpkin).
  - **EDTA-facilitated exudation:**
    1. Cut petioles under water.
    2. Stand them in an EDTA (or BAPTA) collection solution; the chelator stops Ca-triggered sealing.
    3. Block transpiration (high humidity or darkness), or the solution gets drawn into the xylem.
    - Easy, but **dilution is unknown**, so it isn't quantitative. Artifacts grow with time; keep exudation to a few hours at most. Remove or dialyze EDTA before downstream work.
  - **Insect stylectomy:**
    1. Let aphids or planthoppers feed.
    2. Sever the stylet by laser or radio-frequency microcautery.
    3. Collect pure sap under oil: nL volumes, at 0.5–2 nL/min, lasting minutes to hours.
    - Highest purity. Works best in grasses; laborious and unpredictable. Cut soon after feeding starts to limit saliva effects.
  - Other methods: microcapillaries on sieve elements visualized with carboxyfluorescein, laser microdissection, fluorescence-activated cell sorting.
- **Control variables:** well-watered plants in high humidity, the same time of day (strong diurnal variation), the same organ age and position, and known stress status.
- **Check purity:**
  - High sucrose with no glucose or fructose.
  - No photosynthesis proteins or RNAs (e.g., RbcS).
  - Actin and profilin present, tubulin absent.

### Xylem sap (Ch. 13)
- Xylem sap is the bulk transpiration-stream cargo from roots to shoots: minerals, root metabolites, signals. To turn **concentration** into **flux**, you also need **volume flow** (transpiration).
- **Methods:**
  1. **Root-pressure exudate:**
     - Water the plant first, then cut the shoot at the base, remove 1–2 cm of bark, rinse, and fit silicone tubing.
     - Discard the first microlitres, then collect on ice.
     - Best with wide vessels (e.g., grapevine in spring). Not for stressed plants.
     - Collect only as long as needed: phloem recycling stops, and root energy for xylem loading runs down.
  2. **Scholander–Hammel pressure chamber:**
     - Use a twig 0.5–1 cm in diameter, sealed with its cut end protruding 2–3 cm, with bark removed near the cut.
     - Pressurize slowly with N₂ and collect the sap that emerges.
     - **Safety:** wear safety glasses and keep your head clear of the lid. Never exceed the vessel's rated pressure (~3 MPa in the book's example). Tighten the fittings. Wipe wet twigs; moisture can make the bark slip and the twig can shoot out. Extra caution with drought- or salt-stressed plants, which need high pressures.
  3. **Passioura root-pressurizing vessel:** pressurize the whole root system so xylem sap flows at rates matching transpiration. Gives more representative concentrations.
  4. **Vacuum extraction** (hand or battery pump) from cut stem segments.
- Aliquot samples. Allow at most 2 freeze–thaw cycles (amino acids degrade).

---

## §9 Single-cell sampling and analysis (Ch. 14)

- **Why:** nutrients are compartmentalized between organs, tissues (epidermis vs mesophyll vs bundle sheath), cell types and organelles. That partitioning is how plants store and remobilize nutrients and build turgor. Bulk tissue analysis averages it away.
- **Sampling:**
  - Pull glass microcapillaries and break or forge the tips to a few µm. **Silanize** capillaries used under liquid (e.g., root cells), so medium doesn't enter by capillarity and dilute the sample.
  - Backfill with silicone oil or paraffin (50–100× the sample volume).
  - Puncture the cell. Turgor pushes the sap in, so the sample is mostly **vacuolar**.
  - Pipette picolitre volumes with constriction pipettes under paraffin oil on slides (to prevent evaporation).
  - A cell pressure probe can measure turgor at the same time.
- **Analyses on picolitre droplets:**
  - **Picolitre osmometry:** osmolality by freezing-point.
  - **EDX** (energy-dispersive X-ray, in an SEM): Na, K, P, S, Cl, Ca in dried droplets against standards. You need quantitative EDX software, not imaging-only.
  - **Microfluorometry:** NO₃⁻, other anions, amino acids, sugars by enzyme-coupled fluorescence. Use ImageJ on 8-bit images if you lack a photometer.
- **Pitfalls:** evaporation, dilution, mixing with incoming fluid in silanized narrow tips, cross-contamination between cells.

---

## §10 Choosing a method

| Question | Method(s) | Key limitation |
|---|---|---|
| Is this crop deficient? What's the element profile? | ICP-OES (macro- and most micronutrients); ICP-MS for Ni, Mo, Cd, Pb | Needs digestion, CRMs, clean prep |
| NO₃⁻, SO₄²⁻, PO₄³⁻, malate pools | HPLC/IC (Ch. 7); colorimetry | Water-extractable pools only |
| Quick soil clay, organic C, texture for many samples | vis-NIR + calibration (Ch. 6) | Needs a local calibration library; weak for available nutrients |
| Where in the leaf or grain is Zn/Fe? | LA-ICP-MS (dry); synchrotron µ-XRF (hydrated, µm–nm) | Quantification (LA); beamtime (XRF) |
| Uptake kinetics (Km, Vmax), unidirectional flux | Radiotracers / stable isotopes (Ch. 7, 10) | Radiation safety; short half-lives |
| Real-time net flux, spatial profile, stress response | MIFE (Ch. 11) | Net flux only; needs simple media |
| Cytosolic [Na⁺], [NO₃⁻], [K⁺] | SBFI dye (Ch. 15); ion-selective microelectrodes (Ch. 16) | Calibration in situ; compartment identity |
| Vacuolar content of specific cell types | Single-cell sampling + EDX / microfluorometry (Ch. 14) | Picolitre handling skill |
| What the xylem or phloem carries | Xylem sap (Ch. 13); phloem sap (Ch. 12) | Artifacts: dilution (EDTA), contamination, decapitation |
| Which genes control element accumulation? | Ionomics (Ch. 17) | Needs standardized, high-throughput pipeline |
| Genotype differences in nutrient use efficiency over time | Image-based phenotyping (Ch. 18) | Imaging setup; colour calibration |

---

## §11 Lab-safety checklist for these protocols

- **Acids:** hot concentrated HNO₃ with H₂O₂ reacts vigorously; add peroxide in small aliquots. Vent microwave vessels in a fume hood after cooling. **HF** needs specific training, PPE and calcium gluconate gel.
- **Chlorine gas** (bleach + HCl seed sterilization): fume hood only; sealed box.
- **Silanizing agents** (dimethyldichlorosilane, tributylchlorosilane): toxic vapour; fume hood; small volumes.
- **Radioisotopes:** licensed users, shielding, dosimeters, contamination surveys, designated waste streams.
- **Pressure chambers:** eye protection; stay below the vessel's rated pressure; position yourself away from the lid.
- **Cryogens:** liquid N₂ burns and asphyxiation.
- **Biological:** autoclave transgenic plant waste and bacterial cultures; hypochlorite-treat bacterial suspensions.
- **Lasers and synchrotron:** follow facility interlocks and training.
