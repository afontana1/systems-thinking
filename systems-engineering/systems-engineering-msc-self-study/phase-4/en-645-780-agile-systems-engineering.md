# EN.645.780 — Agile Systems Engineering

**Credits:** 3

The development of large, complex, software-intensive hardware systems has become extremely challenging for systems engineers. Some examples are virtually all modern military systems, commercial automotive and aeronautical industries, even medical devices, each containing an extensive set of interconnected, software-driven electrical and mechanical components and are digitally connected to the outside world. This course will show you how to effectively lead teams capable of addressing this complexity using deliberate, incremental learning intervals throughout the system’s development and improvement lifecycles. You will explore how to successfully lead your team in executing these learning intervals using Agile methods, modular hardware and software architectures, integrated descriptive and analytic modeling, Lean and Design Thinking all integrated with the foundational principles of systems engineering. This course will show you how the increasingly ubiquitous, cross-industry digital transformation supports these learning intervals using Digital Threads, Digital Twins and development pipelines called DEVSECOPS. All of the lectures in this course are available asynchronously as recorded videos along with a textbook and other learning material.
Prerequisite(s): EN.645.662 Introduction to Systems Engineering

The backbone I used is current systems-engineering and defense/industry guidance on agile SE, digital engineering, and DevSecOps. INCOSE’s Agile Systems & Systems Engineering Working Group defines agility as a sustainable system capability fundamentally enabled and constrained by architecture. DoD’s current Digital Engineering instruction says programs initiated after December 21, 2023 are to incorporate digital engineering unless excepted, and it defines digital engineering as using integrated digital models and underlying data to support development, test and evaluation, and sustainment. NIST’s digital twin program frames digital twins as tools to monitor status, detect anomalies, predict behavior, and prescribe future operations, while also stressing lifecycle and system-of-systems integration. The DoD Enterprise DevSecOps Strategy Guide emphasizes cATO and real-time metrics across the software supply chain. ([INCOSE][159])

### How to use this plan

Pick one **software-intensive cyber-physical system** and use it for all 12 weeks. Good choices:

* autonomous drone or UAS subsystem
* connected medical device platform
* advanced driver assistance subsystem
* smart manufacturing cell
* unmanned ground vehicle payload/control system

Target about **8–10 hours per week**:

* 3 hours reading
* 2 hours lectures/videos
* 3 hours exercises/artifacts
* 1–2 hours review

By the end, you should have a mini **agile systems engineering portfolio**:

* product vision and stakeholder map
* learning-interval roadmap
* modular architecture views
* MBSE/modeling artifacts
* backlog and acceptance criteria
* DevSecOps pipeline sketch
* digital thread map
* digital twin concept
* final integration plan

---

### Week 1 — What agile systems engineering is

**Goal**
Understand how agile changes systems engineering for software-intensive hardware systems.

**Read**

* INCOSE Agile Systems & Systems Engineering Working Group overview. ([INCOSE][159])
* DoD Systems Engineering Guidebook overview for baseline SE context. ([CTO][160])
* Optional: SEI report on how agile software teams engage with systems engineering. ([SEI][161])

**Watch / review**

* Look for introductory recorded modules on agile systems engineering, MBSE, and digital engineering from the course platform or public INCOSE/DAU talks.

**Exercises**

1. Write a 1-page memo: “Why agile SE is different from traditional sequential SE.”
2. Define your case-study system, mission, users, operators, and constraints.
3. List the top 10 uncertainties that make incremental learning valuable.

**Deliverable**

* Agile SE framing memo
* Case-study definition

---

### Week 2 — Learning intervals and incremental development

**Goal**
Learn to organize development around deliberate learning, not one-shot specification.

The course description centers on “deliberate, incremental learning intervals,” and INCOSE’s agile systems view ties agility to response time, cost, predictability, and scope. ([INCOSE][159])

**Read**

* INCOSE Agile Systems WG description again, focusing on agile capability and architecture. ([INCOSE][159])
* SAFe System Architect role page for continuous technical vision in agile environments. ([Scaled Agile Framework][162])

**Exercises**

1. Break your project into **6 learning intervals** of 2 weeks each.
2. For each interval, define:

   * hypothesis to test
   * system increment
   * evidence to collect
   * exit criteria
3. Write a short rationale for why this sequence reduces program risk.

**Deliverable**

* Learning-interval roadmap

---

### Week 3 — Agile requirements and stakeholder value

**Goal**
Translate system needs into evolving, testable backlog items.

**Read**

* DoD Digital Engineering instruction sections on shared authoritative sources of truth and digital models that reflect system architecture, attributes, and behaviors. ([Defense Logistics Agency][163])
* DoD SE Guidebook sections on requirements and stakeholder alignment. ([CTO][160])

**Exercises**

1. Create:

   * 8 stakeholder needs
   * 10 system capabilities
   * 20 backlog items or features
2. For 10 items, write acceptance criteria.
3. Tag each item as:

   * user value
   * risk reduction
   * architectural runway
   * compliance/safety/security
4. Build a simple trace:

   * need → feature → test/evidence

**Deliverable**

* Agile requirements/backlog v1
* Traceability sheet

---

### Week 4 — Modular hardware and software architectures

**Goal**
See architecture as the enabler of agility.

INCOSE’s Agile Systems WG explicitly says agility is enabled and constrained by architecture, and SAFe’s system architect guidance centers on a shared technical and architectural vision that supports continuous flow across teams and systems. ([INCOSE][159])

**Read**

* INCOSE Agile Systems WG overview. ([INCOSE][159])
* SAFe System Architect page. ([Scaled Agile Framework][162])
* SAFe for Hardware course overview for hardware-reliant agile development. ([Scaled Agile][164])

**Exercises**

1. Draw a modular architecture for your system:

   * hardware modules
   * software services/components
   * interfaces
   * externally connected systems
2. Identify which modules can evolve independently.
3. Identify coupling risks that would slow agile delivery.
4. Write a 1-page architecture decision record for one major modularity choice.

**Deliverable**

* Modular architecture package
* Architecture decision record

---

### Week 5 — Integrated descriptive and analytic modeling

**Goal**
Use models as part of everyday engineering, not just documentation.

DoD’s digital engineering policy explicitly calls out model-based systems engineering, product lifecycle management, and digital models that accurately reflect system architecture and behavior. ([Defense Logistics Agency][163])

**Read**

* DoDI 5000.97 on digital engineering and digital engineering ecosystem. ([Defense Logistics Agency][163])
* Optional de-bok references linked from the instruction for deeper MBSE and digital engineering topics. ([Defense Logistics Agency][163])

**Exercises**

1. Create a lightweight model set:

   * context diagram
   * state model
   * interface model
   * verification/evidence model
2. Separate:

   * descriptive models for communication
   * analytic models for decision support
3. Pick one uncertain subsystem and define what model would help reduce uncertainty.

**Deliverable**

* Model set v1
* Modeling rationale memo

---

### Week 6 — Lean and flow in systems engineering

**Goal**
Apply Lean thinking to reduce waste and improve learning speed.

**Read**

* INCOSE Lean Systems Design resource page. ([INCOSE][165])
* SAFe values/principles overview for flow, scale, and coordination. ([Atlassian][166])

**Exercises**

1. Map your current concept-to-test flow.
2. Identify waste:

   * waiting
   * overproduction of documentation
   * handoff delays
   * rework
   * approval bottlenecks
3. Define 5 Lean improvements.
4. Create one simple value-stream sketch.

**Deliverable**

* Value-stream map
* Lean improvement plan

---

### Week 7 — Design thinking and early concept learning

**Goal**
Use design thinking to shape better increments and reduce solution bias.

The current INCOSE Systems Engineering Handbook preview shows Design Thinking as a named method area and Agile Systems Engineering and Lean Systems Engineering as explicit tailoring/application considerations in the current handbook structure. ([Accuris Standards Store][167])

**Read**

* INCOSE handbook preview lines showing Design Thinking and Agile/Lean SE sections. ([Accuris Standards Store][167])
* Optional public design thinking primers from IDEO or Stanford d.school for methods.

**Exercises**

1. Interview or simulate 3 stakeholder perspectives:

   * operator
   * maintainer
   * safety/compliance authority
2. Build:

   * empathy map
   * “how might we” statements
   * 3 concept sketches
3. Choose one concept experiment for the next learning interval.

**Deliverable**

* Design thinking worksheet
* Concept experiment brief

---

### Week 8 — DevSecOps and development pipelines

**Goal**
Connect agile SE to continuous integration, security, and delivery.

The DoD Enterprise DevSecOps Strategy Guide advocates a versioned DevSecOps governance process and cATO driven by real-time metrics across the software supply chain. ([U.S. Department of Defense][168])

**Read**

* DoD Enterprise DevSecOps Strategy Guide. ([U.S. Department of Defense][168])
* DoDI 5000.97 sections linking digital engineering to development, testing, evaluation, production, and sustainment. ([Defense Logistics Agency][163])

**Exercises**

1. Sketch a DevSecOps pipeline for your case:

   * code/model commit
   * build
   * test
   * security scan
   * deploy to lab/sim
   * evidence capture
2. Identify what applies to hardware, software, and integrated system artifacts.
3. Define 6 pipeline metrics:

   * lead time
   * failure rate
   * test pass rate
   * vulnerability age
   * deployment frequency
   * mean time to restore
4. Note where approval gates should be automated vs manual.

**Deliverable**

* DevSecOps pipeline concept
* Metrics dashboard sketch

---

### Week 9 — Digital thread and authoritative data

**Goal**
Understand how digital thread ties lifecycle artifacts together.

DoDI 5000.97 requires credible and coherent authoritative sources of truth shared with stakeholders, and NIST’s digital twin work emphasizes lifecycle integration and avoiding redundant information exchange. ([Defense Logistics Agency][163])

**Read**

* DoDI 5000.97 sections on authoritative sources of truth and digital engineering ecosystem. ([Defense Logistics Agency][163])
* NIST digital twin overview. ([NIST][169])

**Exercises**

1. Build a digital-thread map linking:

   * requirements
   * architecture/model artifacts
   * code/CAD
   * tests
   * operational data
   * sustainment feedback
2. Identify where data gets re-entered manually.
3. Mark which artifacts should be authoritative vs derived.
4. Write a 1-page note on thread breaks and consequences.

**Deliverable**

* Digital thread map
* ASoT assessment memo

---

### Week 10 — Digital twins for development and sustainment

**Goal**
Use digital twins as part of agile learning and operational improvement.

NIST says digital twins can monitor status, detect anomalies, predict behaviors, and prescribe future operations, and it emphasizes integrated lifecycle views and subsystem coordination. NIST has also been expanding its digital-twin standardization work and state-of-the-art definitions in 2025–2026. ([NIST][169])

**Read**

* NIST digital twin overview. ([NIST][169])
* NIST digital twin standardization page. ([NIST][170])
* NIST “Definitions and State of the Art” page. ([NIST][171])
* Optional NIST IR on security and trust for digital twins. ([NIST Publications][172])

**Exercises**

1. Define a digital twin concept for your case:

   * what physical/operational thing it represents
   * what data feeds it
   * what decisions it supports
   * how it is validated
2. Identify twin use cases:

   * anomaly detection
   * predictive maintenance
   * what-if analysis
   * test rehearsal
3. Note trust/security risks.

**Deliverable**

* Digital twin concept sheet

---

### Week 11 — Leading teams in agile systems engineering

**Goal**
Focus on leadership, cross-discipline coordination, and scaling.

The course is framed around leading teams through learning intervals in complex, software-intensive hardware programs. SAFe’s materials are useful here for the architect/leadership angle, while INCOSE’s agile systems framing keeps the emphasis on architecture and sustainable agility rather than rituals alone. ([INCOSE][159])

**Read**

* SAFe System Architect page. ([Scaled Agile Framework][162])
* SAFe for Hardware overview. ([Scaled Agile][164])
* INCOSE Agile Systems WG overview. ([INCOSE][159])

**Exercises**

1. Define team structure for your project:

   * systems engineer
   * architect
   * software lead
   * hardware lead
   * test lead
   * cybersecurity/safety lead
2. Write a cadence for:

   * backlog refinement
   * architecture sync
   * demo/review
   * integration planning
   * retrospective
3. List 5 failure modes in leading agile SE teams.
4. Write a 1-page leadership memo on balancing speed and rigor.

**Deliverable**

* Team operating model
* Leadership memo

---

### Week 12 — Capstone synthesis

**Goal**
Pull everything into one coherent agile systems engineering approach.

**Exercises**
Assemble a final package containing:

1. system vision and stakeholder map
2. learning-interval roadmap
3. backlog and traceability
4. modular architecture
5. model set
6. Lean flow improvements
7. design-thinking outputs
8. DevSecOps pipeline
9. digital-thread map
10. digital twin concept
11. team operating model

Write a **4–6 page synthesis memo** explaining:

* how your approach reduces uncertainty over time
* how architecture enables agility
* how digital engineering and DevSecOps support learning intervals
* where digital thread and digital twin add the most value
* what risks remain in scaling this approach

**Deliverable**

* Final agile SE binder
* Executive summary memo

### Best resource stack

These are the best anchors for the whole 12 weeks:

* **INCOSE Agile Systems & Systems Engineering Working Group**, for current agile-systems framing centered on architecture-enabled agility. ([INCOSE][159])
* **DoDI 5000.97 Digital Engineering (Dec. 21, 2023)**, for current policy and practical framing of digital engineering, models, and authoritative sources of truth. ([Defense Logistics Agency][163])
* **DoD Enterprise DevSecOps Strategy Guide**, for pipeline, governance, metrics, and cATO concepts. ([U.S. Department of Defense][168])
* **NIST Digital Twins**, for up-to-date digital twin applications, lifecycle integration, and standardization work. ([NIST][169])
* **SAFe System Architect / SAFe for Hardware**, for practical scaling patterns in agile technical leadership and hardware-reliant systems. ([Scaled Agile Framework][162])

### What you should be able to do after 12 weeks

You should be able to:

* explain agile systems engineering beyond software-only agile
* organize work into learning intervals with explicit evidence goals
* design modular architectures that support faster iteration
* use lightweight models to guide decisions
* connect Lean and Design Thinking to systems engineering
* sketch a DevSecOps pipeline for a software-intensive hardware system
* map a digital thread and define a realistic digital twin use case
* lead a cross-functional team with enough rigor for real systems work

---

[Back to Phase 4 README](README.md) · [Back to program README](../README.md)

## References

[159]: https://www.incose.org/group/agile-systems-systems-engineering-working-group "Agile Systems & Systems Engineering Working Group - INCOSE"
[160]: https://www.cto.mil/wp-content/uploads/2023/06/SE-Guidebook-2022.pdf "Systems Engineering Guidebook "
[161]: https://www.sei.cmu.edu/documents/2277/2014_004_001_295953.pdf "Agile Software Teams: How They Engage with Systems ..."
[162]: https://framework.scaledagile.com/system-architect "System Architect"
[163]: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500097p.PDF?ver=bePIqKXaLUTK_Iu5iTNREw%3D%3D "DoDI 5000.97, \"Digital Engineering,\" December 21, 2023"
[164]: https://scaledagile.com/certification/safe-for-hardware-certification-course "SAFe for Hardware Certification | Scaled Agile"
[165]: https://www.incose.org/resource/lean-systems-design "Lean Systems Design"
[166]: https://www.atlassian.com/agile/agile-at-scale/what-is-safe "Scaled Agile Framework (SAFe) Values & Principles"
[167]: https://store.accuristech.com/products/preview/3021457?srsltid=AfmBOorUZq3blSiSFJ_u4JBb8LQbkYgMgWSJAGpd8wCyVU72ZeYzIcbF "INCOSE Systems Engineering Handbook"
[168]: https://dodcio.defense.gov/Portals/0/Documents/Library/DoDEnterpriseDevSecOpsStrategyGuide.pdf "DoD Enterprise DevSecOps Strategy Guide"
[169]: https://www.nist.gov/digital-twins "Digital twins | NIST"
[170]: https://www.nist.gov/digital-twins/digital-twin-standardization "Digital Twin Standardization"
[171]: https://www.nist.gov/digital-twins/definitions-and-state-art "Definitions and State of the Art"
[172]: https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8356.pdf "Security and Trust Considerations for Digital Twin ..."
