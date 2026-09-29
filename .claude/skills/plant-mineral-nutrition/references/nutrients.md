# The Essential Nutrients: Roles, Uptake, and Functions

Distilled mainly from Chapter 1 (Maathuis & Diatloff), with supporting points from Chapters 7, 8, 10 and 11. The wording is our own. Molecular details come mostly from Arabidopsis and rice. The corrections noted in `SKILL.md` are applied.

## Shared patterns (apply to most nutrients)

- **Two affinity ranges of uptake:**
  - High-affinity transport system (HATS): µM Km, active, often *induced* by deficiency.
  - Low-affinity transport system (LATS): mM Km, often channel-mediated.
- **Energization:**
  - Anions are co-transported with H⁺ (the plasma-membrane H⁺-ATPase builds the proton gradient).
  - Cations mostly move passively down the electrical gradient (the cell interior is strongly negative).
  - Charge balance: cation uptake exceeds anion uptake when NH₄⁺ is the N source, and vice versa with NO₃⁻. The difference is balanced by H⁺ release and organic-acid synthesis. That's why NH₄⁺ nutrition acidifies the rhizosphere and NO₃⁻ nutrition alkalinizes it.
- **Adaptations to scarcity:** lateral-root proliferation in rich patches, cluster roots, exudation of acids and chelators, mycorrhizae, and a vacuolar storage pool that buffers the cytoplasm.
- **Relative amounts in a typical plant** (book's Table 1, with N = 100): K 50, Ca 25, Mg 10, P 8, S 5; Cl 0.05, Fe 0.03, B 0.03, Mn 0.02, Zn 0.007, Cu 0.002, Ni 0.0004, Mo 0.0001.

---

## Nitrogen (N): ~1.5% of dry weight
- **Forms taken up:** NO₃⁻ and NH₄⁺, plus amino acids and peptides.
  - Low pH and waterlogged (reducing) soils favor NH₄⁺. Paddy rice takes mostly NH₄⁺.
  - Aerobic, higher-pH soils favor NO₃⁻ (wheat, barley).
  - Most plants grow best on a **mix** of the two.
  - In soil, NO₃⁻ is highly mobile and NH₄⁺ less so. Both reach roots by mass flow and diffusion.
- **Transporters:**
  - NO₃⁻: NRT1 (mostly low-affinity) and NRT2 (high-affinity) families, both H⁺-coupled. The high-affinity system has a constitutive part and a nitrate-inducible part.
  - NH₄⁺: AMT family. Rice roots have many AMTs, regulated by phosphorylation.
  - Peptides and amino acids: POT/PTR (NPF) transporters.
  - Glutamine and NH₄⁺ feed back to inhibit NO₃⁻ uptake.
- **Assimilation:**
  - NO₃⁻ → NO₂⁻ via nitrate reductase (cytosol, needs **Mo**), then NO₂⁻ → NH₄⁺ via nitrite reductase (plastid). This costs about 15 ATP equivalents.
  - NH₄⁺ is cheaper to use but **toxic**: it dissipates membrane gradients. It is assimilated quickly into glutamine.
  - NO₃⁻ can be stored safely in vacuoles and contributes to turgor.
- **Functions:** amino acids and proteins (~85% of plant N), nucleic acids (~5%), chlorophyll, coenzymes, polyamines, secondary metabolites, signals.
- **Interactions:** C:N balance (CO₂ fixation and N reduction are coordinated); K⁺ is the counter-ion for NO₃⁻ moving in the xylem, so good K supply supports N nutrition.
- **Legumes:** rhizobia in nodules fix N₂ in a low-O₂ environment, in exchange for plant sugars. Nitrate in the medium suppresses nodulation.
- **Deficiency:** general chlorosis of older leaves; red or purple stems (anthocyanin) in Medicago and other species.

## Potassium (K): ~1% of dry weight
- **Soil pools:** mineral K (feldspars, micas), fixed K between illite and vermiculite layers, exchangeable K, and solution K (0.1–1 mM, very mobile). True deficiency is uncommon, but potash is widely applied to get optimal yields.
- **Uptake:**
  - Low-affinity: the **AKT1** inward-rectifying channel. It can also work in the high-affinity range when the membrane is strongly hyperpolarized. It is activated under low K by a Ca²⁺ signal via the CBL1/9 sensors and the CIPK23 kinase.
  - High-affinity: **HAK/KUP** transporters (HAK5 in Arabidopsis), strongly induced by K starvation.
  - Loading into the xylem: **SKOR** channels.
  - K cycles between root and shoot. This supports homeostasis and provides the counter-ion for NO₃⁻.
- **Vacuole:** the main K store (turgor). Loaded by NHX/CHX K⁺/H⁺ exchangers, released through TPC1/TPK1 channels. Under prolonged starvation, vacuolar K can fall below cytosolic K, and HAK/KUP transporters on the tonoplast take over.
- **Functions:**
  - Activates many enzymes (optimum ~50–80 mM, close to the ~100 mM in cytosol): pyruvate kinase, phosphofructokinase, starch synthesis, vacuolar pyrophosphatase, protein synthesis on ribosomes. Na⁺ and Li⁺ **cannot** substitute.
  - Main osmoticum for turgor, cell expansion and movements (stomata, leaf movements, the Venus flytrap).
  - Low chaotropic effect: it balances the charge on macromolecules without disrupting hydrogen bonds.
- **Deficiency:** reduced turgor and growth; scorching of older-leaf margins; poorer stress tolerance.
- **Tracing:** ⁸⁶Rb⁺ is the usual K⁺ tracer (half-life 18.65 d), but it is an imperfect analog, especially for root-to-shoot transport. ⁴²K (half-life ~12.4 h) is more faithful but short-lived.

## Calcium (Ca): ~0.5% of dry weight
- **Soil:** abundant (calcite, dolomite, gypsum, apatite). Deficiency is rare except in acid, leached soils. Excess can induce P, K or Mg deficiency.
- **Uptake:** through non-selective Ca²⁺-permeable cation channels (plants have no Ca-selective channel like animals). Some reaches the xylem via the apoplast.
- **Movement:** Ca is **immobile** in the phloem and travels with the transpiration stream. High humidity, drought or salinity cut delivery to growing tips and fruits, causing blossom-end rot (tomato), bitter pit (apple), blackheart (celery) and tipburn. Fix with steady water supply and humidity management, not only more soil Ca.
- **Storage:** apoplast, ER and vacuole (mM levels). CAX H⁺/Ca²⁺ antiporters and ACA/ECA Ca-ATPases pump it in.
- **Functions:**
  - **Structural "glue":** cross-links pectins in cell walls, which strengthens walls and resists pathogens, and binds phospholipids to stabilize the outer face of the plasma membrane. Removing Ca from the apoplast causes membranes to leak electrolytes.
  - **Second messenger:** cytosolic free Ca²⁺ is kept at about 100–200 nM, so fast Ca²⁺ spikes can encode touch, pathogen, temperature, drought and nutrient signals.

## Magnesium (Mg): ~0.2–0.5% of dry weight
- **Soil:** large hydrated radius, so it is weakly held and easily displaced by H⁺. It leaches from acid, sandy, low-CEC soils.
- **Uptake:** MGT transporters. Vacuolar loading by Mg²⁺/H⁺ exchange.
- **Functions:**
  - Central atom of **chlorophyll**. 15–30% of plant Mg is in chloroplasts.
  - Cofactor for **Rubisco** (ribulose-1,5-bisphosphate carboxylase) and fructose-1,6-bisphosphatase.
  - Counter-ion that shapes the thylakoid proton-motive force.
  - Mg-chelatase in chlorophyll synthesis.
  - Cofactor for kinases, ATPases and polymerases; almost all ATP reactions use Mg-ATP.
  - Stabilizes DNA, RNA and ribosomes.
- **Deficiency:** interveinal chlorosis of **older** leaves. High K or NH₄⁺ supply can induce it.

## Phosphorus (P): ~0.1–0.4% of dry weight
- **Soil:** more than 90% is fixed in minerals or organic forms. Solution Pi is very low (typically ~0.1–10 µM). It is taken up as H₂PO₄⁻, the dominant form at pH below ~7. Release is slow and deficiency is widespread. Rock phosphate is a **finite** resource.
- **Uptake:** PHT1 H⁺-coupled transporters with high and low affinity.
- **Adaptations:**
  - Cluster (proteoid) roots exude citrate and malate to dissolve Ca-, Fe- and Al-phosphates.
  - **Mycorrhizae** often deliver most of the plant's P, at a real carbon cost to the plant.
  - Seeds store P as **phytate**.
- **Functions:**
  - Energy currency (ATP, UTP for sucrose, starch and cellulose, CTP for lipids, GTP).
  - Backbone of nucleic acids; phospholipid head groups.
  - **Protein phosphorylation** by kinases and phosphatases, a master regulatory switch.
- **Deficiency:** dark or purplish older leaves, stunting. Membranes shift to sulfolipids and galactolipids.

## Sulfur (S): ~0.1–0.5% of dry weight
- **Forms:** SO₄²⁻ in aerobic soils. Sulfides (H₂S, FeS) form in flooded soils. Leaves can also take up atmospheric SO₂. Toxicity is rare (sulfate-saline soils).
- **Uptake:** **SULTR** H⁺/sulfate symporters. High-affinity SULTR1 has a Km of about 10 µM and is induced under S deficiency, possibly signalled by glutathione in the phloem. Sulfate is mobile in the xylem; the surplus is stored in the vacuole.
- **Assimilation (mainly in shoots):** SO₄²⁻ → sulfite → sulfide → **cysteine**. Cysteine is the hub for methionine, glutathione and other compounds. Roots receive reduced S (glutathione) via the phloem.
- **Functions:**
  - Thiol groups (–SH) and disulfide bridges in protein structure and redox switching.
  - Sulfolipids in thylakoids.
  - **Glutathione** for reactive-oxygen detoxification.
  - **Phytochelatins** (γ-Glu-Cys)ₙ-Gly that bind heavy metals and arsenic, so metal stress raises S demand.
- **Diagnostic tip (Ch. 7):** the tissue **sulfate:malate ratio** from a single HPLC run indicates crop S status without absolute calibration or sample weighing.

## Chlorine (Cl⁻)
- Essential (shown in 1954) but usually abundant in soils. Deficiency has been seen in some wheat on very low-Cl sandy soils, and Cl can suppress some diseases.
- **Transporters:** CLC channels and exchangers (some are Cl⁻/NO₃⁻ antiporters), CCC cation-chloride co-transporters.
- **Roles:**
  - Mostly an inert, mobile counter-anion for K⁺ (turgor, stomatal guard cells). Wilting is a deficiency symptom.
  - **Irreplaceable** as a cofactor of the photosystem II oxygen-evolving complex.
- In practice Cl⁻ is more often a salinity/toxicity issue.

## Iron (Fe)
- **Availability:** abundant in the crust (the second most abundant metal after Al) but almost insoluble as Fe³⁺ in aerobic, neutral-to-alkaline soils.
- **Two uptake strategies:**
  - **Strategy I** (dicots and non-grass monocots): acidify the rhizosphere, reduce Fe³⁺ → Fe²⁺ at the root surface (ferric-chelate reductase), then take up Fe²⁺ through **IRT1**.
  - **Strategy II** (grasses): secrete **phytosiderophores** (mugineic acids) that chelate Fe³⁺, then take up the Fe³⁺–phytosiderophore complex (YS1/YSL transporters).
- **Transport inside the plant:** as Fe-citrate (xylem), Fe-nicotianamine and Fe-phytosiderophore. About 80% of leaf Fe is in chloroplasts.
- **Functions:** redox enzymes (cytochromes, Fe-S proteins, ferredoxin), chlorophyll synthesis.
- **Deficiency:** interveinal chlorosis of **young** leaves. First shown by Gris in the 1840s, and reversible with Fe salts on roots or leaves.
- **Practical:** in hydroponics use chelated Fe (FeNaEDTA, Fe-DTPA; Fe-HBED or EDDHA at high pH). Keep Fe stocks dark (they are light-sensitive).

## Boron (B)
- Essential (shown for broad bean in 1923 and for non-legumes in 1926). Not part of any known enzyme.
- More than 80% (up to 95–98% under deficiency) is bound in cell walls, cross-linking **pectin** (rhamnogalacturonan-II).
- **Forms:** uncharged boric acid B(OH)₃ below pH ~7; borate at higher pH. Taken up by **NIP** aquaporins, loaded into the xylem by **BOR1** exporters.
- Phloem-immobile, except in species that make sugar alcohols (sorbitol, mannitol). Deficiency deforms growing organs (terminal buds, fruits, roots).
- **Narrow window between deficiency and toxicity:** B toxicity affects millions of hectares (e.g., more than 5 million ha of South Australian cropland). BOR efflux transporters confer tolerance, and breeding targets them.

## Manganese (Mn)
- Redox-active. Found in the **4-Mn cluster of the photosystem II oxygen-evolving complex** and in Mn-superoxide dismutase.
- The micronutrient most involved in **disease resistance** (phenolics, lignin).
- High-affinity uptake by **NRAMP1** (Km ≈ 30 nM). Other NRAMP, CAX and CDF (MTP) transporters handle vacuolar and plastid movement.
- **Deficiency:** "grey speck" of oats; interveinal chlorosis and necrotic spots.
- Mn **toxicity** occurs in acid and waterlogged soils.
- Reduce Mn about 10-fold in AM-fungus culture media, because Mn can inhibit spore germination (Ch. 3).

## Zinc (Zn)
- Exists only as Zn²⁺ (not redox-active). That makes it ideal for **DNA-binding proteins (zinc fingers)** and for many enzymes: carbonic anhydrase, Cu/Zn-SOD, alcohol dehydrogenase, RNA polymerase.
- **Deficiency** is common worldwide on calcareous, heavy clay, alluvial, peaty and sandy soils. Zn-efficient cultivars have better root growth, uptake and internal use.
- A major human-nutrition target for biofortification (HarvestPlus), alongside Fe, Se and Mg.

## Copper (Cu)
- Redox-active: plastocyanin (photosynthetic electron transport), Cu/Zn-SOD, cytochrome c oxidase, the ethylene receptor, ascorbate oxidase, polyphenol oxidase, laccases (lignification).
- **Uptake:** COPT transporters (COPT1 at the plasma membrane; COPT5 mobilizes Cu from the vacuole). P-type ATPases (HMAs) deliver it to organelles.
- **Deficiency:** chlorosis of young leaves, curled margins, poor pollen and seed viability.
- **Excess** generates reactive oxygen species (toxic). Cu is the basis of many fungicides. Some pathogens hijack rice COPTs to strip Cu from the xylem.

## Nickel (Ni)
- Most recently proven essential (1987): Ni-deficient barley seed is non-viable.
- Its only known role in higher plants is in **urease** (urea → NH₃ + CO₂). Deficiency causes urea accumulation and leaf-tip necrosis ("mouse-ear" in pecan).
- Taken up via Fe transporters (IRT1); no Ni-specific transporter is known.
- **Toxicity** is the bigger concern: serpentine soils, sludge, smelting. Hyperaccumulators chelate Ni with citrate and histidine.

## Molybdenum (Mo)
- Soil molybdate (MoO₄²⁻) is about 1 mg/kg and **more available at higher pH**. Taken up by **MOT1** (Km ≈ 7–20 nM).
- Cofactor (Moco) for nitrate reductase, sulfite oxidase, xanthine dehydrogenase, aldehyde oxidase (ABA and auxin synthesis) and bacterial nitrogenase.
- **Deficiency** looks like N deficiency ("whiptail" in brassicas), because nitrate can't be reduced.
- The smallest requirement of any nutrient: "one Mo atom organizes ~10⁸ C atoms."

## Beneficial elements
- **Na:** can partly replace K as an osmoticum; needed by some C4 and CAM plants. Toxic under salinity. Cytosolic Na⁺ can be measured with the SBFI dye (Ch. 15).
- **Si:** strengthens cell walls; improves pathogen, lodging and stress resistance, especially in grasses and rice. Added to some hydroponic recipes (0.1–0.5 mM sodium silicate).
- **Co:** needed by rhizobia for N₂ fixation (cobalamin). Included in some legume media.
- **Se:** not essential for plants, but essential for humans; a biofortification target.

---

## Quick reference

### Widely cited average "sufficient" concentrations in shoot dry matter
From the classic Epstein compilation, shown here for orientation. The book's text uses similar round numbers. Critical levels vary with species, organ and stage, so use species-specific tables for diagnosis.

| Element | Typical DW concentration |
|---|---|
| N | 1.5% (15,000 µg/g) |
| K | 1.0% |
| Ca | 0.5% |
| Mg | 0.2% |
| P | 0.2% |
| S | 0.1% |
| Cl | 100 µg/g |
| Fe | 100 µg/g |
| Mn | 50 µg/g |
| B | 20 µg/g |
| Zn | 20 µg/g |
| Cu | 6 µg/g |
| Mo | 0.1 µg/g |
| Ni | ~0.1 µg/g or less |

### Typical anion contents and uptake rates (Ch. 7; seedlings, wheat and Brassica)

| Measure | Root | Shoot |
|---|---|---|
| NO₃⁻ content | 100–400 µmol/g DW | 200–800 µmol/g DW |
| Phosphate content | 5–300 µmol/g DW | 5–300 µmol/g DW |
| SO₄²⁻ content | cereals 10–20; Brassica ~100 µmol/g DW | 100–400 µmol/g DW |

- NO₃⁻ uptake: ~7.5 µmol/g FW root/h.
- Phosphate uptake: 200–1,500 nmol/g FW/h in cereals; more than 500 in Brassica; higher when P-starved.
- SO₄²⁻ uptake: 50–1,000 nmol/g FW/h; higher when S-starved.

### Symptom key (confirm with tissue analysis)
- **Older leaves first:**
  - N: uniform yellowing.
  - P: dark green or purple, stunted.
  - K: marginal scorch.
  - Mg: interveinal chlorosis.
  - Mo: N-like symptoms, whiptail.
- **Young leaves or growing points first:**
  - Fe: interveinal chlorosis, veins stay green.
  - Mn: interveinal chlorosis with grey or brown specks.
  - Zn: small leaves, rosetting, short internodes.
  - Cu: pale, curled, wilting tips.
  - S: uniform pale young leaves.
  - B: dead growing points, brittle or cracked tissue.
  - Ca: tip burn, blossom-end rot, bitter pit.
- **Toxicities:** Mn (acid or waterlogged soils: brown spots), B (marginal necrosis of older leaves, where it accumulates at the transpiration end), Na/Cl (salinity: tip and margin burn), NH₄⁺ (as sole N source: stunting, root damage, acidification), heavy metals (induced Fe chlorosis, root stunting).
- **Rule out look-alikes** (water stress, pH-induced lock-up, disease, herbicide) and check the interactions:
  - Excess K or NH₄⁺ → Mg deficiency.
  - High P → Zn deficiency.
  - High pH → Fe, Mn, Zn, Cu and B deficiency, but more available Mo.
  - Low transpiration → Ca and B disorders.
