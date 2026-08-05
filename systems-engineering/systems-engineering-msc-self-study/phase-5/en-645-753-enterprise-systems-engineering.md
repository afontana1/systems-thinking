# EN.645.753 — Enterprise Systems Engineering

**Credits:** 3

Enterprise Systems Engineering is a multidisciplinary approach to the application of systems engineering principles and systems thinking to large sociotechnical enterprises as complex adaptive systems. Health, energy, food, disaster response, and global transportation systems are all examples of such systems. Systems engineering has been a critical enabler of development, and is key, to addressing the complexities of the evolution of complex systems and systems of systems.?In this course, we explore systems thinking and systems engineering approaches that can be applied to this new class of broad sociotechnical enterprise.? We will examine the characteristics of this class of enterprise and the challenges for applying systems engineering to this type of complex adaptive system. These enterprises are comprised of multiple independent organizations with their own objectives, resources, and authority structures without top-level cross cutting authority and may possess conflicting objectives. A process model will be created to describe the activities of key enterprise elements and interactions which, along with external factors, influence the evolution of such enterprises. This model will be used to understand the current enterprise composition and dynamics and evaluate the impact of issues or actions as the basis for systems engineering trades or recommendations.
Prerequisite(s): EN.645.769 System Test and Evaluation or advisor and instructor approval.

### How to use this plan

Use one **running enterprise case** for all 12 weeks so your artifacts build on each other. Good fits for this course are:

* regional healthcare delivery enterprise
* electric grid modernization enterprise
* national food distribution network
* disaster response enterprise
* global freight transportation ecosystem

Plan on about **8–10 hours per week**:

* 3 hours reading
* 2 hours lecture/video/course-note review
* 3 hours exercises and modeling
* 1–2 hours reflection and writing

This plan leans on SEBoK for the discipline framing, MITRE for enterprise systems engineering process ideas, and MIT system dynamics / socio-technical modeling material for process and feedback modeling. Those sources align especially well with the course description’s emphasis on enterprises as evolving sociotechnical systems with decentralized authority and dynamic interactions. ([SEBoK][210])

---

### Week 1 — What is an enterprise in systems engineering?

**Goal**
Understand how an enterprise differs from a single system or even a traditional system of systems.

**Read**

* SEBoK: **Enterprise Systems Engineering**. ([SEBoK][210])
* SEBoK: **Enterprise Systems Engineering Background**. ([SEBoK][211])
* INCOSE Enterprise Systems Engineering Working Group mission/scope. ([INCOSE][212])

**Exercises**

1. Write a 1-page memo: “Why my case is an enterprise, not just a system.”
2. Define:

   * mission or societal purpose
   * participating organizations
   * external environment
   * decision authorities
   * major tensions/conflicts
3. List 10 enterprise-level outcomes the enterprise is supposed to achieve.

**Deliverable**

* Enterprise definition memo
* Enterprise boundary/context sketch

---

### Week 2 — Sociotechnical enterprises as complex adaptive systems

**Goal**
Build the conceptual foundation for enterprises as adaptive, evolving sociotechnical systems.

SEBoK explicitly frames enterprises as complex adaptive sociotechnical systems, and its CAS glossary emphasizes independently acting elements whose interactions produce broader behavior. MIT’s engineering systems material similarly focuses on solving complex sociotechnical problems by combining engineering, management, and social-science perspectives. ([SEBoK][210])

**Read**

* SEBoK: **Enterprise Systems Engineering** and **Enterprise Systems Engineering Key Concepts**. ([SEBoK][210])
* SEBoK: **Complex Adaptive Systems Engineering (CASE)**. ([SEBoK][213])
* MIT Engineering Systems Division overview. ([OpenCourseWare][214])

**Exercises**

1. Identify adaptive features in your enterprise:

   * independent actors
   * local incentives
   * feedback effects
   * emergent outcomes
   * evolution over time
2. Write three examples of how local decisions could create enterprise-wide consequences.
3. Note where prediction is hard and why.

**Deliverable**

* CAS characteristics worksheet
* Enterprise behavior notes

---

### Week 3 — Stakeholders, organizations, and conflicting objectives

**Goal**
Map the independent organizations and conflicting objectives that make enterprise engineering difficult.

The course description emphasizes enterprises made up of multiple independent organizations with their own objectives, resources, and authority structures. SEBoK and MITRE both describe enterprise engineering in settings where coordination must occur without a single top-level authority and where broader mission outcomes depend on cross-organizational interaction. ([SEBoK][210])

**Read**

* SEBoK: **Enterprise Systems Engineering**. ([SEBoK][210])
* MITRE: **Systems of Systems Engineering in the Enterprise Context: A Unifying Framework for Dynamics**. ([MITRE][215])
* MITRE: **Enterprise Systems Engineering Theory and Practice**. ([MITRE][216])

**Exercises**

1. Build a stakeholder map showing:

   * organizations
   * objectives
   * authority
   * resources
   * constraints
2. Identify 5 objective conflicts.
3. Identify 5 cooperation dependencies.
4. Write a short note on which actors can block change even if they do not control the whole enterprise.

**Deliverable**

* Stakeholder/governance map
* Objective-conflict matrix

---

### Week 4 — Process modeling of enterprise activities

**Goal**
Create the process model the catalog description specifically calls for.

MITRE’s enterprise systems engineering process framework introduces enterprise-level processes such as technology planning, capability-based analysis, enterprise architecture, strategic technical planning, and enterprise analysis/assessment. The course description’s “process model” language aligns closely with using explicit activity-and-interaction models to explain enterprise behavior. ([MITRE][217])

**Read**

* MITRE: **A Framework for Enterprise Systems Engineering Processes**. ([MITRE][217])
* MITRE: **Enterprise Systems Engineering Theory and Practice**. ([MITRE][216])
* MITRE Systems Engineering Guide for practical modeling mindset. ([MITRE][218])

**Exercises**

1. Build a level-1 enterprise process model:

   * demand/need generation
   * resource allocation
   * operations/service delivery
   * governance/policy
   * feedback/learning
2. Add key inputs, outputs, and interactions.
3. Identify delays, bottlenecks, and handoffs.
4. Note where the enterprise adapts.

**Deliverable**

* Enterprise process model v1

---

### Week 5 — Enterprise dynamics and feedback loops

**Goal**
Move from static structure to dynamic behavior.

MIT’s system dynamics resources are especially useful here because they focus on modeling feedback and behavior over time in complex systems, and the socio-technical modeling course emphasizes model-building for design and decision-making in complex sociotechnical systems. ([MIT OpenCourseWare][127])

**Read / watch**

* MIT: **System Dynamics: Systems Thinking and Modeling for a Complex World**. ([MIT OpenCourseWare][127])
* MIT OCW: **Models, Data and Inference for Socio-Technical Systems** course description. ([MIT OpenCourseWare][219])

**Exercises**

1. Create a causal loop diagram for your enterprise.
2. Identify:

   * reinforcing loops
   * balancing loops
   * time delays
   * unintended consequences
3. Describe two “fixes that fail” patterns that could happen in your enterprise.
4. Write a 1-page explanation of the enterprise’s dominant feedback structure.

**Deliverable**

* Causal loop diagram
* Dynamics memo

---

### Week 6 — Enterprise architecture and capability thinking

**Goal**
Understand architecture not just as IT structure, but as an enterprise decision tool.

INCOSE’s ESE working group highlights mission architecture, capability planning, acquisition, and model-based approaches such as UAF, while MITRE’s enterprise process framework includes enterprise architecture and capability-based engineering analysis as key processes. ([INCOSE][212])

**Read**

* INCOSE ESE Working Group scope statement. ([INCOSE][212])
* MITRE: **A Framework for Enterprise Systems Engineering Processes**. ([MITRE][217])
* MITRE: **Enterprise Systems Engineering Theory and Practice**. ([MITRE][216])

**Exercises**

1. Define 5–8 enterprise capabilities.
2. Map organizations and resources to those capabilities.
3. Identify capability gaps and overlaps.
4. Create a simple enterprise architecture view showing:

   * organizations
   * processes
   * information flows
   * technologies
   * external forces

**Deliverable**

* Capability map
* Enterprise architecture sketch

---

### Week 7 — Current-state analysis of the enterprise

**Goal**
Use the process model to understand the enterprise “as is.”

The course description says the model should be used to understand the current enterprise composition and dynamics. MITRE’s enterprise analysis and assessment process directly supports this kind of diagnostic work. ([MITRE][217])

**Read**

* MITRE: **A Framework for Enterprise Systems Engineering Processes**. ([MITRE][217])
* SEBoK: **Enterprise Systems Engineering Key Concepts**. ([SEBoK][220])

**Exercises**

1. Write a current-state enterprise assessment:

   * who does what
   * where value is created
   * where delays happen
   * where incentives misalign
   * what external pressures matter
2. Identify 5 structural weaknesses.
3. Identify 5 enterprise strengths or stabilizers.
4. Build a simple heat map of pain points.

**Deliverable**

* Current-state assessment memo
* Pain-point map

---

### Week 8 — External factors and enterprise evolution

**Goal**
Account for policy, technology, market, environmental, and social pressures.

The catalog explicitly says that external factors influence enterprise evolution. MITRE’s enterprise work describes shaping enterprise evolution through variation, interaction, and selection, while SEBoK’s enterprise framing treats environment as part of the enterprise’s adaptive context. ([MITRE][217])

**Read**

* MITRE: **A Framework for Enterprise Systems Engineering Processes**. ([MITRE][217])
* MITRE: **Systems of Systems Engineering in the Enterprise Context**. ([MITRE][215])
* SEBoK: **Enterprise Systems Engineering Background**. ([SEBoK][211])

**Exercises**

1. List major external factors:

   * regulation
   * funding
   * market demand
   * technology change
   * geopolitical/environmental shocks
2. For each, explain how it changes incentives or structure.
3. Write three future-state scenarios:

   * optimistic
   * stressed
   * disruptive
4. Note which enterprise elements are most sensitive.

**Deliverable**

* External-factor assessment
* Scenario set

---

### Week 9 — Trades, recommendations, and intervention options

**Goal**
Turn analysis into systems engineering recommendations.

The course description explicitly says the model is the basis for systems engineering trades and recommendations. MITRE’s enterprise analysis/assessment framing and SEBoK’s enterprise concepts both support using models to compare alternatives rather than relying on intuition alone. ([MITRE][217])

**Read**

* MITRE: **Enterprise Systems Engineering Theory and Practice**. ([MITRE][216])
* MITRE: **A Framework for Enterprise Systems Engineering Processes**. ([MITRE][217])
* SEBoK: **Enterprise Systems Engineering**. ([SEBoK][210])

**Exercises**

1. Develop 3 intervention options, such as:

   * governance change
   * capability investment
   * information-sharing reform
   * incentive redesign
   * process standardization
2. Evaluate each option against:

   * mission benefit
   * feasibility
   * stakeholder resistance
   * cost/effort
   * adaptability
3. Write a trade-study memo recommending one option or phased combination.

**Deliverable**

* Trade-study package
* Recommendation memo

---

### Week 10 — Enterprise resilience and adaptation

**Goal**
Assess how well the enterprise responds to stress and change.

Enterprise systems are adaptive and evolve under external pressure; the useful question is often not “is it optimal?” but “can it absorb shocks and adapt without mission collapse?” That logic is consistent with SEBoK’s enterprise-as-adaptive-system framing and MIT system dynamics’ focus on behavior over time. ([SEBoK][210])

**Read**

* SEBoK: **Enterprise Systems Engineering Key Concepts**. ([SEBoK][220])
* MIT System Dynamics resource. ([MIT OpenCourseWare][127])
* MIT OCW socio-technical systems modeling description. ([MIT OpenCourseWare][219])

**Exercises**

1. Define 5 resilience indicators for your enterprise:

   * recovery time
   * service continuity
   * coordination quality
   * adaptability of resource allocation
   * decision latency
2. Identify brittle points.
3. Design a stress test scenario and describe how the enterprise would respond.
4. Suggest resilience-oriented changes.

**Deliverable**

* Enterprise resilience framework

---

### Week 11 — Writing the academic paper

**Goal**
Match the course expectation that students complete academic papers exploring concepts in depth.

The catalog explicitly says students will discuss readings and complete academic papers. A strong paper for this course should combine theory, model-based analysis, and a recommendation grounded in the enterprise’s observed dynamics. That is well aligned with SEBoK’s ESE framing and MITRE’s enterprise-analysis approach. ([SEBoK][210])

**Exercises**

1. Draft a **4–6 page paper** on one topic:

   * enterprise governance without top-level authority
   * modeling enterprise evolution
   * conflicting objectives in sociotechnical enterprises
   * using capability models for enterprise trades
   * adaptive interventions in a complex enterprise
2. Include:

   * problem statement
   * conceptual framework
   * enterprise model summary
   * findings
   * recommendations
3. Revise for clarity, argument strength, and evidence.

**Deliverable**

* Draft academic paper

---

### Week 12 — Final synthesis and presentation

**Goal**
Pull the entire course into one coherent enterprise systems engineering study.

**Exercises**

1. Assemble a final package containing:

   * enterprise definition
   * stakeholder/governance map
   * process model
   * causal loop diagram
   * capability/architecture view
   * current-state assessment
   * external-factor scenarios
   * trade-study and recommendation
   * resilience assessment
   * final paper
2. Write a **2-page executive summary** explaining:

   * the enterprise’s main structural and dynamic problems
   * what interventions are most promising
   * what tradeoffs leaders must accept
   * what should be monitored over time
3. Prepare a 10-minute presentation.

**Deliverable**

* Final enterprise systems engineering binder
* Executive summary
* Final presentation outline

---

### Best resource stack for this course

These are the best anchors for the whole 12 weeks:

* **SEBoK: Enterprise Systems Engineering** and related background/key-concept pages, because they directly define the field and frame enterprises as complex adaptive sociotechnical systems. ([SEBoK][210])
* **INCOSE Enterprise Systems Engineering Working Group**, because it reflects current practice areas such as mission architecture, capability planning, enterprise digital transformation, and model-based methods. ([INCOSE][212])
* **MITRE’s enterprise systems engineering papers**, because they provide a concrete enterprise process framework and a practical theory-and-practice perspective. ([MITRE][217])
* **MIT System Dynamics / sociotechnical systems resources**, because the course explicitly requires modeling interactions and evolution over time. ([MIT OpenCourseWare][127])

### What you should be able to do after 12 weeks

By the end, you should be able to:

* explain enterprise systems engineering as distinct from product or single-system engineering
* model a sociotechnical enterprise’s key processes and interactions
* account for decentralized authority and conflicting objectives
* analyze enterprise dynamics using feedback thinking
* evaluate intervention options with explicit tradeoffs
* produce graduate-level written recommendations grounded in enterprise models

---

[Back to Phase 5 README](README.md) · [Back to program README](../README.md)

## References

[127]: https://ocw.mit.edu/courses/res-15-004-system-dynamics-systems-thinking-and-modeling-for-a-complex-world-january-iap-2020/resources/systems-thinking-and-modeling-for-a-complex-world-iap-2020 "Systems Thinking and Modeling for a Complex World"
[210]: https://sebokwiki.org/wiki/Enterprise_Systems_Engineering "Enterprise Systems Engineering"
[211]: https://sebokwiki.org/wiki/Enterprise_Systems_Engineering_Background "Enterprise Systems Engineering Background"
[212]: https://www.incose.org/group/enterprise-systems-engineering "Enterprise Systems Engineering Working Group"
[213]: https://sebokwiki.org/wiki/Complex_Adaptive_Systems_Engineering_%28CASE%29 "Complex Adaptive Systems Engineering (CASE)"
[214]: https://opencw.aprende.org/courses/engineering-systems-division "Engineering Systems Division"
[215]: https://www.mitre.org/news-insights/publication/systems-systems-engineering-enterprise-context-unifying-framework "Systems of Systems Engineering in the Enterprise Context"
[216]: https://www.mitre.org/sites/default/files/publications/05_1483.pdf "Enterprise Systems Engineering Theory and Practice"
[217]: https://www.mitre.org/sites/default/files/pdf/06_1163.pdf "A Framework for Enterprise Systems Engineering Processes"
[218]: https://www.mitre.org/sites/default/files/publications/se-guide-book-interactive.pdf "Systems Engineering Guide"
[219]: https://ocw.mit.edu/courses/esd-86-models-data-and-inference-for-socio-technical-systems-spring-2007 "Models, Data and Inference for Socio-Technical Systems"
[220]: https://www.sebokwiki.org/wiki/Enterprise_Systems_Engineering_Key_Concepts "Enterprise Systems Engineering Key Concepts"
