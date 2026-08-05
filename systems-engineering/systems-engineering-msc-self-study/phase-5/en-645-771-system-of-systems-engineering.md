# EN.645.771 — System of Systems Engineering

**Credits:** 3

This course addresses the special engineering problems associated with conceiving, developing, and operating systems composed of groups of complex systems closely linked to function as integral entities. The course will start with the underlying fundamentals of systems’ requirements, design, test and evaluation, and deployment, and how they are altered in the multi-system environment. These topics will then be extended to information flow and system interoperability, confederated modeling and simulation, use of commercial off-the-shelf elements, and systems engineering collaboration between different organizations. Advanced principles of information fusion, causality theory with Bayesian networks, and capability dependencies will be explored. Several case studies will be discussed for specific military systems of systems, including missile defense and combatant vehicle design, as well as selected commercial examples.Course Note(s): Selected as one of the electives in the MSE or MS program or a required course for the post-master’s certificate.
Prerequisite(s): EN.645.769 System Test and Evaluation OR EN.655.769 Healthcare Systems Engineering Test and Evaluation or advisor and instructor approval.

This course sits on top of core systems engineering, but shifts the focus to **systems made from independently useful constituent systems** that must still coordinate to produce a larger capability. That distinction is central to current SoS guidance from SEBoK and INCOSE. ([SEBoK][202])

### How to use this plan

Pick one **running SoS case** for all 12 weeks so your artifacts build on each other. Good options:

* integrated air and missile defense network
* autonomous vehicle fleet and traffic-control ecosystem
* emergency response communications SoS
* hospital network plus EMS plus public-health coordination system
* port logistics and freight tracking SoS

Budget about **8–10 hours per week**:

* 3 hours reading
* 2 hours lectures/course notes
* 3 hours exercises and artifacts
* 1–2 hours reflection

By the end, you should have a small **SoSE portfolio**:

* SoS context and constituent-system map
* requirements and capability-dependency model
* interoperability and information-flow analysis
* COTS assessment
* federated M&S concept
* fusion/Bayesian reasoning exercise
* collaboration/governance plan
* case-study memos
* final SoSE recommendation package

---

### Week 1 — What makes a system of systems different?

**Goal**
Understand how SoSE differs from ordinary systems engineering.

SEBoK describes SoSE as applying technical management to a mix of existing and new systems while the constituent systems still retain responsibility for their own technical management. DoD’s SoS guide similarly emphasizes that an SoS combines independently useful systems to deliver a capability no one constituent system can achieve alone. ([SEBoK][202])

**Read**

* SEBoK: **Systems of Systems (SoS)**. ([SEBoK][202])
* INCOSE **Systems of Systems Working Group** overview. ([INCOSE][203])
* DoD **Systems Engineering Guide for Systems of Systems** summary or full guide. ([CTO][204])

**Exercises**

1. Write a 1-page memo: “Why my case is an SoS and not just a large system.”
2. Identify constituent systems and what each can do independently.
3. Identify the higher-level mission enabled only by coordination.
4. Note where authority is centralized, federated, or absent.

**Deliverable**

* SoS framing memo
* Constituent-system map

---

### Week 2 — Revisiting requirements, design, test, and deployment in an SoS

**Goal**
See how classical lifecycle concepts change in a multi-system environment.

The course description explicitly starts with requirements, design, test/evaluation, and deployment, then asks how they are altered in a multi-system setting. Current SoS guidance emphasizes that these activities must now account for evolving constituent systems, partial control, and cross-system dependencies. ([SEBoK][202])

**Read**

* SEBoK: **Systems of Systems (SoS)**. ([SEBoK][202])
* DoD **Systems Engineering Guide for Systems of Systems**. ([CTO][204])
* DoD **Systems Engineering Guidebook** for the baseline classical SE view. ([Mission Capabilities][205])

**Exercises**

1. Compare single-system vs SoS handling of:

   * requirements ownership
   * architecture/design authority
   * integration sequencing
   * test responsibility
   * deployment control
2. For your case, list 10 SoS-level requirements.
3. Mark which requirements no single constituent can satisfy alone.
4. Note where verification will require multi-organization coordination.

**Deliverable**

* Lifecycle comparison table
* SoS requirements v1

---

### Week 3 — Capability dependencies and mission threads

**Goal**
Model how capabilities depend on interactions among constituent systems.

This is one of the most important SoSE habits: think in terms of **mission threads** and **cross-system capability dependencies**, not just component hierarchies. That fits both the course description and modern SoS practice. ([SEBoK][202])

**Read**

* SEBoK: **Systems of Systems (SoS)**. ([SEBoK][202])
* INCOSE SoS Working Group materials. ([INCOSE][203])

**Exercises**

1. Define 3–5 mission threads for your SoS.
2. For each thread, identify:

   * initiating event
   * participating systems
   * information exchanges
   * timing constraints
   * failure points
3. Build a capability-dependency map.

**Deliverable**

* Mission-thread set
* Capability-dependency matrix

---

### Week 4 — Information flow and interoperability

**Goal**
Study the heart of many SoS failures: systems can connect physically but still fail semantically, temporally, or organizationally.

The course description explicitly calls out **information flow and interoperability**, and that is a core SoS concern because independent systems often use different data models, update cycles, interfaces, and governance rules. ([SEBoK][202])

**Read**

* DoD **Systems Engineering Guide for Systems of Systems**. ([CTO][204])
* DoD **Engineering of Defense Systems Guidebook** for integration and interoperability context. ([CTO][206])
* SEBoK SoS page again, focusing on cross-system integration concerns. ([SEBoK][202])

**Exercises**

1. Build an information-exchange inventory:

   * sender
   * receiver
   * data type
   * format/protocol
   * latency tolerance
   * security constraints
2. Identify interoperability risks:

   * syntactic
   * semantic
   * timing
   * policy/access
   * version mismatch
3. Write 5 interoperability test cases.

**Deliverable**

* Information-flow model
* Interoperability risk register

---

### Week 5 — Confederated modeling and simulation

**Goal**
Learn how modeling and simulation change when multiple independently owned systems must be represented together.

The course explicitly names **confederated modeling and simulation**, which is a natural fit for SoS because no single model typically owns the whole truth. In practice, federated/confederated modeling helps examine behavior across systems without pretending there is one monolithic integrated design model. That need is consistent with modern SoS guidance about separately managed constituent systems. ([SEBoK][202])

**Read**

* DoD **Systems Engineering Guide for Systems of Systems**. ([CTO][204])
* SEBoK SoS page. ([SEBoK][202])

**Exercises**

1. Define what each constituent system model would represent.
2. Decide what must be simulated jointly:

   * timing
   * information flow
   * sensor uncertainty
   * command logic
   * logistics/resource constraints
3. Sketch a federated simulation concept:

   * participating models
   * exchanged variables
   * synchronization assumptions
   * validation concerns
4. Note what cannot be trusted from the model alone.

**Deliverable**

* Confederated M&S concept note

---

### Week 6 — COTS elements in systems of systems

**Goal**
Analyze how commercial off-the-shelf elements help and hurt SoS development.

The catalog explicitly includes **COTS**, and SoS environments often rely on COTS because constituent systems evolve on different timelines and budgets. The tradeoff is reduced development time versus reduced control over interfaces, upgrades, cybersecurity posture, and lifecycle alignment. That concern is consistent with SoS practice in DoD guidance. ([CTO][204])

**Read**

* DoD **Engineering of Defense Systems Guidebook**. ([CTO][206])
* DoD **Systems Engineering Guide for Systems of Systems**. ([CTO][204])

**Exercises**

1. List candidate COTS elements in your SoS.
2. For each, assess:

   * interoperability fit
   * vendor dependency
   * update cadence
   * security implications
   * data rights / integration burden
3. Write a 1-page trade memo: custom vs COTS for one critical function.

**Deliverable**

* COTS assessment table
* COTS trade memo

---

### Week 7 — Cross-organization collaboration and governance

**Goal**
Address the fact that SoS engineering usually spans organizations with separate budgets, priorities, and authorities.

SEBoK and INCOSE both treat this as a defining SoSE condition: the constituent systems remain independently managed, so collaboration mechanisms matter as much as technical interfaces. ([SEBoK][202])

**Read**

* SEBoK: **Systems of Systems (SoS)**. ([SEBoK][202])
* INCOSE **Systems of Systems Working Group** page. ([INCOSE][203])
* DoD **Systems Engineering Guide for Systems of Systems**. ([CTO][204])

**Exercises**

1. Map the organizations involved in your SoS.
2. For each, note:

   * objectives
   * authority
   * resources
   * change-control power
   * data-sharing limits
3. Design a governance scheme:

   * interface control board
   * joint test forum
   * configuration coordination
   * dispute escalation
4. Identify 5 likely collaboration failures.

**Deliverable**

* SoS collaboration/governance plan

---

### Week 8 — Information fusion and distributed sensemaking

**Goal**
Study how multiple systems combine observations into useful decisions.

The course explicitly includes **advanced principles of information fusion**. In SoS contexts, fusion is not just an algorithm problem; it also depends on data pedigree, timing, uncertainty, and trust across systems. ([SEBoK][202])

**Read**

* Revisit DoD and SEBoK SoS guidance with a focus on information dependency and decision support. ([SEBoK][202])

**Exercises**

1. Pick one fusion problem in your case:

   * multiple sensors
   * multiple logistics feeds
   * multiple operational-status sources
2. Define:

   * sources
   * uncertainties
   * conflicts
   * timing/skew
   * confidence reporting
3. Create a fusion logic sketch.
4. List failure modes:

   * double counting
   * stale data
   * conflicting reports
   * hidden bias
   * missing-source dependency

**Deliverable**

* Information-fusion worksheet

---

### Week 9 — Causality and Bayesian networks

**Goal**
Use probabilistic and causal reasoning for diagnosis and decision support.

The catalog explicitly mentions **causality theory with Bayesian networks**. MIT OCW has good open materials for Bayesian and probabilistic inference, and MIT also has causal-inference material that helps separate correlation from causal reasoning. ([MIT OpenCourseWare][207])

**Read / watch**

* MIT OCW: **Probabilistic Systems Analysis** Bayesian inference lecture. ([MIT OpenCourseWare][207])
* MIT OCW: **Artificial Intelligence** probabilistic inference material. ([MIT OpenCourseWare][208])
* MIT OCW: **Causal Inference, Part 1**. ([MIT OpenCourseWare][209])

**Exercises**

1. Build a small Bayesian network for one SoS problem, such as:

   * target identification confidence
   * fault diagnosis across systems
   * route disruption likelihood
   * mission success probability
2. Define nodes, causal links, and prior assumptions.
3. Run 3 evidence-updating examples by hand.
4. Write a 1-page reflection on where Bayesian reasoning helps and where it may mislead.

**Deliverable**

* Small Bayesian-network model
* Causality reflection memo

---

### Week 10 — Test, evaluation, and deployment in the multi-system environment

**Goal**
Return to V&V, but now with SoS-specific realities.

The course says it begins with classical requirements/design/test/deployment and then extends them for the multi-system environment. In SoS, validation often depends on joint mission behavior, not just constituent-system conformance. That aligns with current SEBoK and DoD SoS guidance. ([SEBoK][202])

**Read**

* SEBoK SoS page. ([SEBoK][202])
* DoD **Systems Engineering Guide for Systems of Systems**. ([CTO][204])
* DoD **Systems Engineering Guidebook** as baseline test/deployment context. ([Mission Capabilities][205])

**Exercises**

1. Build an SoS verification/validation matrix.
2. Identify what can be verified at constituent level vs only at SoS level.
3. Define 3 joint test scenarios.
4. Identify deployment risks caused by asynchronous upgrades across constituent systems.

**Deliverable**

* SoS V&V matrix
* Deployment risk memo

---

### Week 11 — Military and commercial case studies

**Goal**
Learn how SoSE principles show up in real domains.

The catalog explicitly mentions **missile defense**, **combatant vehicle design**, and selected commercial examples. INCOSE and DoD materials are especially relevant for the military side, while the same SoS principles transfer to transportation, logistics, and emergency response ecosystems. ([INCOSE][203])

**Read**

* INCOSE SoS Working Group materials. ([INCOSE][203])
* DoD **Engineering of Defense Systems Guidebook**. ([CTO][206])
* DoD **Systems Engineering Guide for Systems of Systems**. ([CTO][204])

**Exercises**

1. Write two short case briefs:

   * one defense-oriented
   * one commercial
2. For each, analyze:

   * constituent systems
   * interoperability challenge
   * governance problem
   * capability dependency
   * likely V&V difficulty
3. Compare both to your running case.

**Deliverable**

* Two case-study briefs

---

### Week 12 — Final synthesis and recommendation package

**Goal**
Pull the course together into one coherent SoSE study.

**Exercises**
Assemble a final package with:

1. SoS definition and constituent-system map
2. SoS requirements and mission threads
3. capability-dependency model
4. information-flow and interoperability analysis
5. federated M&S concept
6. COTS assessment
7. collaboration/governance plan
8. fusion/Bayesian reasoning example
9. SoS V&V/deployment view
10. final recommendation memo

Write a **4–6 page synthesis memo** explaining:

* what makes the case an SoS
* where the main capability dependencies sit
* which interoperability risks matter most
* where governance is as important as engineering
* how uncertainty and evidence should be handled
* what next engineering actions you recommend

**Deliverable**

* Final SoSE binder
* Executive summary memo

---

### Best resource stack for this course

These are the strongest anchors for the full 12 weeks:

* **SEBoK v2.13** and especially the **Systems of Systems (SoS)** entry, because it reflects current SoSE framing and was updated in late 2025. ([SEBoK][202])
* **INCOSE Systems of Systems Working Group**, because it directly tracks current SoSE practice and community thinking. ([INCOSE][203])
* **DoD Systems Engineering Guide for Systems of Systems**, because it addresses integrating independently useful systems into a larger SoS capability. ([CTO][204])
* **DoD Engineering of Defense Systems Guidebook**, because it gives broader engineering context for complex defense SoS work. ([CTO][206])
* **MIT OCW Bayesian/probabilistic/causal materials**, because they map well to the course’s Bayesian networks and causality portion. ([MIT OpenCourseWare][207])

### What you should be able to do after 12 weeks

By the end, you should be able to:

* explain how SoSE differs from single-system engineering
* model capability dependencies across constituent systems
* analyze interoperability and information-flow problems
* reason about federated modeling and simulation
* evaluate COTS choices in an SoS context
* design collaboration structures for cross-organization engineering
* apply basic Bayesian-network reasoning to SoS uncertainty
* create SoS-level V&V and deployment plans grounded in mission threads

---

[Back to Phase 5 README](README.md) · [Back to program README](../README.md)

## References

[202]: https://sebokwiki.org/wiki/Systems_of_Systems_%28SoS%29 "Systems of Systems (SoS)"
[203]: https://www.incose.org/group/systems-of-systems-working-group "Systems of Systems Working Group"
[204]: https://www.cto.mil/wp-content/uploads/2024/06/DoD-SE-for-SoS-2008.pdf "Systems Engineering Guide for Systems of Systems, V 1.0"
[205]: https://ac.cto.mil/wp-content/uploads/2022/02/Systems-Eng-Guidebook_Feb2022-Cleared-slp.pdf "Systems Engineering Guidebook"
[206]: https://www.cto.mil/wp-content/uploads/2023/06/Eng-Def-Sys-2022.pdf "Engineering of Defense Systems Guidebook"
[207]: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/resources/lecture-22-video-1 "Lecture 22: Bayesian Statistical Inference - II | Probabilistic ..."
[208]: https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/resources/lecture-22-probabilistic-inference-ii "Lecture 22: Probabilistic Inference II | Artificial Intelligence"
[209]: https://ocw.mit.edu/courses/6-s897-machine-learning-for-healthcare-spring-2019/resources/lecture-14-causal-inference-part-1 "Causal Inference, Part 1 | Machine Learning for Healthcare"
