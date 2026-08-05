# EN.645.782 — Foundations of Digital and Mission Engineering

**Credits:** 3

This course provides an introduction to Digital Engineering and Mission Engineering, both of which are topics of emerging emphasis, particularly in the U.S. Defense community. The course begins with a review of the systems engineering process, with its technical and technical management processes, as it is applied in the U.S. Department of Defense (DoD) acquisition lifecycle. It then provides an overview of the DoD Digital Engineering Strategy, and discusses key competencies needed for Digital Engineering. As Modeling and Simulation (M&S) and Model Based Systems Engineering (MBSE) are key to the implementation of Digital Engineering, the course discusses fundamental concepts of M&S and how models and simulations are used in the various phases of the systems engineering process. Key MBSE concepts are then presented, along with an overview of the Systems Modeling Language (SysML) and its constituent diagrams, followed by an overview of the Object-Oriented Systems Engineering Method (OOSEM). The course then discusses how to apply these MBSE concepts to analyze several selected real-world case studies. A generic framework for a collaborative environment to support digital engineering is presented, along with how it might be used to support the development of digital twins and digital threads for a system. The underlying concepts and the key methodology elements of Mission Engineering are then described, based on the DoD Mission Engineering Guidebook. Finally, the course examines how and why Digital Engineering supports the implementation of Mission Engineering.
Prerequisite(s): EN.645.662 Introduction to Systems Engineering

Here’s a **12-week study plan for EN.645.782 Foundations of Digital and Mission Engineering** built around the course description: DoD systems engineering and acquisition context, Digital Engineering strategy and competencies, M&S and MBSE fundamentals, SysML and OOSEM, collaborative digital engineering environments, digital threads and digital twins, Mission Engineering, and how Digital Engineering enables Mission Engineering. The strongest current anchors are DoDI **5000.97 Digital Engineering** (issued December 21, 2023), the DoD **Digital Engineering Strategy**, the DoD **Mission Engineering Guide** (October 2023), the current DoD systems engineering guidebooks, OMG’s SysML v2 materials, and INCOSE’s OOSEM working-group resources. ([ESD WHS][163])

### How to use this plan

Use one **running defense-oriented or mission-oriented case** for all 12 weeks so the artifacts build on each other. Good options:

* integrated air-defense mission thread
* unmanned ISR mission package
* contested logistics resupply mission
* autonomous maritime surveillance mission
* joint disaster-response command-and-control mission

Budget about **8–10 hours per week**:

* 3 hours reading
* 2 hours lecture/video/tutorials
* 2–3 hours modeling or analysis
* 1–2 hours reflection and write-up

By the end, you should have a compact **digital-and-mission-engineering portfolio**: acquisition-context summary, digital-engineering ecosystem map, M&S/MBSE baseline, SysML/OOSEM starter artifacts, digital thread/twin concept, mission-engineering analysis, and a final recommendation memo. That matches the course’s emphasis on using Digital Engineering and MBSE to analyze real-world cases and to support Mission Engineering. ([ESD WHS][163])

---

### Week 1 — DoD systems engineering and acquisition context

**Goal**
Understand the DoD systems engineering process and where Digital Engineering and Mission Engineering fit.

**Read**

* DoD **Systems Engineering Guidebook**. ([Chief Technology Officer][51])
* DoD **Engineering of Defense Systems Guidebook**. ([Chief Technology Officer][173])

**Exercises**

1. Write a 1-page memo explaining the difference between:

   * technical processes
   * technical management processes
   * acquisition lifecycle activities
2. Define your case-study system or mission problem.
3. List the key acquisition or milestone decisions where engineering evidence is needed.

**Deliverable**

* DoD SE/acquisition summary
* Case-study definition

---

### Week 2 — The DoD Digital Engineering strategy and competencies

**Goal**
Learn what Digital Engineering means in current DoD practice.

The 2018 DoD **Digital Engineering Strategy** sets out five strategic goals for digital engineering, and DoDI **5000.97** makes digital engineering a formal DoD policy expectation, including digital models, digital threads, digital artifacts, and authoritative sources of truth in a digital engineering ecosystem. ([ac.cto.mil][174])

**Read**

* DoD **Digital Engineering Strategy**. ([ac.cto.mil][174])
* DoDI **5000.97 Digital Engineering**. ([ESD WHS][163])
* DoD **Digital Engineering Fundamentals**. ([Chief Technology Officer][175])

**Exercises**

1. Summarize the five Digital Engineering Strategy goals.
2. Create a chart of key Digital Engineering competencies:

   * digital models
   * data management
   * collaboration
   * toolchain awareness
   * model credibility
3. Write a short note on how your case project would benefit from an authoritative source of truth.

**Deliverable**

* Digital engineering strategy memo
* Competency checklist

---

### Week 3 — Modeling and simulation as Digital Engineering enablers

**Goal**
Understand how M&S supports Digital Engineering across the lifecycle.

DoDI **5000.97** explicitly places digital models and digital artifacts inside a broader digital engineering ecosystem, and DoD’s Digital Engineering, Modeling and Simulation resource hub treats M&S as a core enabling practice for digital engineering. ([ESD WHS][163])

**Read**

* DoDI **5000.97** sections on digital models, artifacts, and ecosystem. ([ESD WHS][163])
* DoD **Digital Engineering, Modeling and Simulation** resource page. ([Chief Technology Officer][112])

**Exercises**

1. Identify 5 places in your case where M&S could support:

   * concept analysis
   * requirements refinement
   * design tradeoffs
   * integration/test planning
   * mission analysis
2. Write one paragraph on the limits of M&S for your case.
3. Create a simple model-use matrix by lifecycle phase.

**Deliverable**

* M&S support matrix

---

### Week 4 — MBSE fundamentals in the Digital Engineering context

**Goal**
Connect Digital Engineering to MBSE basics.

OMG describes SysML as a general-purpose modeling language intended to support MBSE and to represent requirements, structure, behavior, analysis cases, and verification cases. DoDI **5000.97** also emphasizes digital models as a basis for engineering communication and knowledge generation. ([OMG][176])

**Read**

* OMG SysML “About” page. ([OMG][176])
* OMG SysML v2 overview page. ([OMG][177])
* DoDI **5000.97** refresher. ([ESD WHS][163])

**Exercises**

1. Write a 1-page memo: “Why MBSE is central to Digital Engineering.”
2. Define for your case:

   * top-level requirements
   * major system elements
   * a key behavior or mission thread
3. Sketch how a model could link all three.

**Deliverable**

* MBSE-in-DE memo
* Initial model scope

---

### Week 5 — SysML foundations

**Goal**
Get comfortable with the role of SysML diagrams in engineering analysis.

OMG’s current SysML materials describe SysML v2 as the next-generation systems modeling language, improving precision, expressiveness, usability, interoperability, and extensibility over SysML v1. The language is meant to represent requirements, structure, behavior, and analysis/verification concerns. ([OMG][177])

**Read**

* OMG **SysML v2 Introduction**. ([OMG][15])
* OMG **SysML v2** overview page. ([OMG][177])

**Exercises**

1. Create a simple starter artifact set for your case:

   * context view
   * requirements view
   * structural decomposition
   * behavior/use-case view
2. Note which diagrams help answer which engineering questions.
3. Identify what still requires narrative explanation.

**Deliverable**

* Starter SysML artifact package

---

### Week 6 — OOSEM and model-based method

**Goal**
Understand OOSEM as a method, not just a notation.

INCOSE’s OOSEM working group says OOSEM exists to facilitate integration of systems engineering with object-oriented software engineering and to apply OO modeling in a way that benefits the systems engineering process. The working group is actively evolving OOSEM to leverage SysML v2 and incorporate lessons learned from more than 15 years of SysML v1 use. ([INCOSE][178])

**Read**

* INCOSE **Object-Oriented SE Method Working Group** page. ([INCOSE][178])
* INCOSE OOSEM working-group overview PDF. ([INCOSE][179])
* INCOSE OOSEM overview PDF. ([INCOSE][180])

**Exercises**

1. Write a 1-page comparison:

   * language vs method
   * SysML vs OOSEM
2. Apply a lightweight OOSEM-style flow to your case:

   * define objectives
   * identify use cases / mission threads
   * derive structure and behavior
3. Note where the method improves consistency.

**Deliverable**

* OOSEM comparison memo
* OOSEM mini-walkthrough

---

### Week 7 — Real-world MBSE/Digital Engineering case analysis

**Goal**
Practice analyzing a real case the way the course describes.

The course explicitly emphasizes analyzing selected real-world case studies using MBSE concepts. DoD and INCOSE resources are strongest when tied back to actual engineering decisions, tradeoffs, and mission outcomes. ([ac.cto.mil][181])

**Read**

* Revisit DoDI **5000.97**. ([ESD WHS][163])
* Revisit the **Mission Engineering Guide**. ([ac.cto.mil][181])

**Exercises**

1. Pick one real or realistic case related to your project.
2. Analyze:

   * what models would be needed
   * what stakeholders need to collaborate
   * what decisions depend on engineering evidence
3. Compare that case to your running example.

**Deliverable**

* Case-study analysis memo

---

### Week 8 — Collaborative environments, digital threads, and digital twins

**Goal**
Understand the digital engineering environment beyond individual tools.

DoDI **5000.97** defines a digital engineering ecosystem that includes people, processes, methods, practices, data, software, tools, and networks. The Defense Business Board’s 2024 report on creating a DoD digital ecosystem also highlights digital engineering as an enterprise transformation issue. ([ESD WHS][163])

**Read**

* DoDI **5000.97** sections on digital engineering ecosystems. ([ESD WHS][163])
* **Creating a DoD Digital Ecosystem** report. ([Defense Business Board][182])

**Exercises**

1. Draw a collaborative digital environment for your case showing:

   * stakeholders
   * tools
   * models
   * data exchanges
   * review/approval loops
2. Map a notional digital thread across:

   * requirements
   * architecture/model
   * test evidence
   * operational feedback
3. Define one plausible digital twin use case.

**Deliverable**

* Digital ecosystem map
* Digital thread/twin concept sheet

---

### Week 9 — Foundations of Mission Engineering

**Goal**
Learn Mission Engineering as a distinct but related discipline.

The current DoD **Mission Engineering Guide** says mission engineering has direct application to systems engineering by providing a better understanding of system and SoS characteristics that affect mission outcomes. It defines the goal of mission engineering as engineering missions by identifying the right technologies, systems, SoS, or processes to achieve intended mission outcomes and provide mission-based inputs to systems engineering. ([ac.cto.mil][181])

**Read**

* DoD **Mission Engineering Guide**. ([ac.cto.mil][181])

**Exercises**

1. Write a 1-page memo: “How Mission Engineering differs from product-centric systems engineering.”
2. Define for your case:

   * mission objective
   * mission thread
   * mission outcome measures
   * participating systems/actors
3. Identify 3 mission-level questions the engineering team should answer.

**Deliverable**

* Mission engineering framing memo

---

### Week 10 — Mission Engineering methods and mission analysis

**Goal**
Apply mission-engineering thinking to a real mission problem.

The Mission Engineering Guide is centered on understanding mission outcomes, dependencies, and the systems, SoS, and processes that drive those outcomes. It is especially relevant where cross-system interactions matter more than any single platform. ([ac.cto.mil][181])

**Read**

* DoD **Mission Engineering Guide** again, focusing on methodology elements. ([ac.cto.mil][181])
* DoD **Systems Engineering Guidebook** references to mission engineering in SoS contexts. ([Chief Technology Officer][160])

**Exercises**

1. Build a mission thread for your case:

   * initiating event
   * participating systems
   * key information exchanges
   * mission success/failure points
2. Identify capability dependencies and bottlenecks.
3. Define 3 candidate interventions or upgrades.

**Deliverable**

* Mission thread model
* Capability-dependency matrix

---

### Week 11 — How Digital Engineering supports Mission Engineering

**Goal**
Tie the two halves of the course together.

Digital Engineering supports Mission Engineering by making mission-relevant engineering information more connected, more analyzable, and more shareable across organizations through digital models, threads, and artifacts. That link is consistent with both DoDI **5000.97** and the DoD **Mission Engineering Guide**. ([ESD WHS][163])

**Read**

* DoDI **5000.97**. ([ESD WHS][163])
* DoD **Mission Engineering Guide**. ([ac.cto.mil][181])
* DoD Digital Engineering Fundamentals. ([Chief Technology Officer][175])

**Exercises**

1. Write a 2-page paper explaining:

   * how digital models support mission analysis
   * how digital threads help mission-level traceability
   * where digital twins could support mission rehearsal, monitoring, or adaptation
2. Update your case with one integrated Digital Engineering + Mission Engineering workflow.

**Deliverable**

* Integration paper
* Updated workflow diagram

---

### Week 12 — Final synthesis project

**Goal**
Pull the course into one coherent digital-and-mission-engineering study.

**Exercises**
Assemble a final package with:

1. DoD SE/acquisition context summary
2. digital engineering strategy/competency summary
3. M&S support matrix
4. SysML starter artifacts
5. OOSEM mini-method application
6. digital ecosystem / digital thread / digital twin concept
7. mission engineering framing
8. mission thread and capability analysis
9. Digital Engineering–Mission Engineering integration memo

Write a **4–6 page final memo** covering:

* how Digital Engineering changes engineering practice
* what Mission Engineering adds at the mission/system-of-systems level
* how MBSE and M&S support both
* what collaborative environment would be needed
* what next steps you would recommend for your case

**Deliverable**

* Final digital-and-mission-engineering binder
* Executive summary memo

### Best resource stack

These are the strongest anchors for the course:

* **DoDI 5000.97 Digital Engineering** for current formal DoD policy on digital engineering, digital models, digital threads, and digital ecosystems. ([ESD WHS][163])
* **DoD Digital Engineering Strategy** for the strategic rationale and five-goal framing. ([ac.cto.mil][174])
* **DoD Mission Engineering Guide** for current methodology and mission-outcome framing. ([ac.cto.mil][181])
* **DoD Systems Engineering / Engineering of Defense Systems guidebooks** for acquisition and engineering-process context. ([Chief Technology Officer][51])
* **OMG SysML v2 materials** for current SysML direction and language framing. ([OMG][177])
* **INCOSE OOSEM working-group materials** for the method side of SysML-based MBSE. ([INCOSE][178])

### What you should be able to do after 12 weeks

You should be able to:

* explain Digital Engineering in the DoD acquisition context
* describe the role of M&S and MBSE in Digital Engineering
* read and use basic SysML/OOSEM concepts
* sketch a collaborative digital engineering environment
* define digital thread and digital twin use cases
* explain Mission Engineering and build a basic mission thread
* show how Digital Engineering enables Mission Engineering

---

[Back to Phase 4 README](README.md) · [Back to program README](../README.md)

## References

[15]: https://www.omg.org/cgi-bin/doc?syseng%2F25-03-04.pdf= "SysML v2 Introduction"
[51]: https://www.cto.mil/wp-content/uploads/2024/05/SE-Guidebook-Feb2022.pdf "Systems Engineering Guidebook"
[112]: https://www.cto.mil/sea/dems "Digital Engineering, Modeling and Simulation"
[160]: https://www.cto.mil/wp-content/uploads/2023/06/SE-Guidebook-2022.pdf "Systems Engineering Guidebook "
[163]: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500097p.PDF?ver=bePIqKXaLUTK_Iu5iTNREw%3D%3D "DoDI 5000.97, \"Digital Engineering,\" December 21, 2023"
[173]: https://www.cto.mil/wp-content/uploads/2024/10/Eng-Def-Sys-Change2-7October2024-v3.pdf "Engineering of Defense Systems Guidebook"
[174]: https://ac.cto.mil/wp-content/uploads/2019/06/2018-Digital-Engineering-Strategy_Approved_PrintVersion.pdf "DIGITAL ENGINEERING STRATEGY"
[175]: https://www.cto.mil/wp-content/uploads/2023/06/Dig-Eng-Fundamentals-2022.pdf "Department of Defense (DoD) Digital Engineering ..."
[176]: https://www.omg.org/spec/SysML/2.0/About-SysML "About the OMG System Modeling Language Specification ..."
[177]: https://www.omg.org/sysml/sysmlv2 "SysML® v2 Specification"
[178]: https://www.incose.org/group/object-oriented-se-method-working-group "Object-Oriented SE Method Working Group"
[179]: https://www.incose.org/docs/default-source/working-groups/oosem/202504oosemwgoverview.pdf?sfvrsn=b73e50c7_1 "Object Oriented Systems Engineering Method (OOSEM) Working ..."
[180]: https://www.incose.org/docs/default-source/events-documents/iw2020/wgis/iw2020-wgis2-object-oriented_se_method.pdf?sfvrsn=412a9dc6_2 "Object-Oriented SE Method"
[181]: https://ac.cto.mil/wp-content/uploads/2023/11/MEG_2_Oct2023.pdf "Department of Defense Mission Engineering Guide"
[182]: https://dbb.defense.gov/Portals/35/Documents/Reports/2024/FY24-03%20Digital%20Ecosystem%20-%20FINAL%20FOR%20PRINT%20with%20DOPSR%20Stamp%204-16-24.pdf "Creating A Digital Ecosystem"
