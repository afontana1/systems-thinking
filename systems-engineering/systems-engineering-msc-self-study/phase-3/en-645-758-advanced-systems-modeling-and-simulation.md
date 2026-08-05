# EN.645.758 — Advanced Systems Modeling and Simulation

**Credits:** 3

This course provides in-depth exposure to the field of modeling and simulation (M&S) from the perspective of M&S as an essential tool for systems engineering. Advanced statistical methods are used to conduct requirements-driven simulation analysis and experimentation. The course provides treatment of advanced M&S topics, including methods for simulation interoperability and composability; modeling of the system environment, both natural and man-made; modeling of system costs; and the establishment of collaborative M&S environments. The course also explores continuous and real-time simulation. Students are exposed to the techniques used to form conceptual models of mechanical (both translational and rotational), electrical, fluid, thermal, biological, and hybrid systems. The conceptual models are transformed into mathematical models and implemented in a modern simulation package. State-of-the-art tools are explored, and each student is given the opportunity to conduct a simulation study of a complex system. Each student will present a case study and complete a project. Upon completion of the course, the student will be able to conduct or lead the development of the model of a complex physical system, model the input data, and analyze the results to support decisions at key milestones of a system's life cycle.
Prerequisite(s): EN.645.662 Introduction to Systems Engineering

I anchored it to current, primary sources where possible. NASA’s Systems Engineering Handbook treats modeling and simulation as a lifecycle decision-support tool. The DoD’s current M&S instruction and VV&A guidance cover standards, reuse, and credibility. For multi-domain physical-system modeling, Modelica is still a strong open standard for cyber-physical systems, and MathWorks’ Simscape remains a widely used commercial environment for physical-network modeling across mechanical, electrical, hydraulic, and thermal domains. ([NASA][27])

### How to use this plan

Use one **complex physical-system case** all 12 weeks so the work compounds. Good choices:

* hybrid electric drone
* smart HVAC and thermal-control system
* infusion pump with sensing and control
* robotic manipulator with electro-mechanical actuation
* autonomous underwater vehicle subsystem

Plan on about **8–10 hours per week**:

* 3 hours reading
* 2 hours lectures/tutorials
* 2–3 hours modeling and simulation
* 1–2 hours write-up

A strong outcome is a compact **advanced M&S portfolio**:

* conceptual model
* requirements-driven simulation plan
* statistical input model
* interoperability/composability assessment
* environment model
* cost model
* continuous or real-time simulation prototype
* final case-study report and presentation

---

### Week 1 — Advanced M&S in the systems engineering lifecycle

**Goal**
Understand where advanced M&S fits beyond introductory simulation.

**Read**

* NASA Systems Engineering Handbook sections on concept development, iterative modeling, simulation, and lifecycle decision support. ([NASA][27])
* NASA “Systems Analysis, Modeling, and Simulation” overview for a concise framing of utility and purpose. ([NASA Technical Reports Server][120])
* DoD Instruction 5000.61 overview for the current defense view of modeling, simulation, distributed simulation, and VV&A standardization. ([ESD WHS][153])

**Exercises**

1. Write a 1-page memo: “What makes M&S ‘advanced’ from a systems engineering perspective?”
2. Define your case-study system, mission, stakeholders, and the top decisions the model should support.
3. List 5 lifecycle milestones where simulation could influence the decision.

**Deliverable**

* Project charter
* Lifecycle-use memo

---

### Week 2 — Requirements-driven simulation analysis

**Goal**
Tie simulation directly to requirements and technical decisions.

NASA explicitly links iterative modeling and simulation to assessing whether concepts and products can meet key requirements and ConOps. ([NASA][27])

**Read**

* NASA Systems Engineering Handbook passages on requirements, ConOps, and analytical support. ([NASA][27])
* NASA systems analysis overview for framing models around decision questions. ([NASA Technical Reports Server][120])

**Exercises**

1. Define:

   * 8–12 requirements or KPPs
   * 5 simulation outputs tied to those requirements
   * pass/fail or threshold criteria
2. Build a simple trace:

   * requirement → model element → output metric → decision use
3. Identify which requirements are best addressed by simulation versus test or inspection.

**Deliverable**

* Requirements-to-simulation trace matrix

---

### Week 3 — Advanced statistical input modeling

**Goal**
Use better stochastic assumptions for input data and experimentation.

The course description explicitly calls for advanced statistical methods, and the current DoD M&S VV&A context emphasizes data-backed uncertainty quantification for model results. ([Dote][154])

**Read**

* DoD M&S policy/VV&A materials for current uncertainty and data-backed-analysis framing. ([ESD WHS][153])
* Supplement with your preferred probability/statistics notes from earlier coursework.

**Exercises**

1. Identify 4–6 uncertain inputs.
2. Assign distributions and justify them.
3. Compare at least two candidate distributions for one input and explain the impact on results.
4. Define what data you would need to validate the input assumptions.

**Deliverable**

* Input uncertainty model

---

### Week 4 — Conceptual modeling of complex physical systems

**Goal**
Form high-quality conceptual models before tool implementation.

**Read**

* NASA systems analysis overview for framing model purpose and abstraction level. ([NASA Technical Reports Server][120])
* Modelica Association overview and language pages for first-principles, reusable, equation-based modeling of cyber-physical systems. ([modelica.org][155])

**Exercises**

1. Create a conceptual model showing:

   * subsystems
   * state variables
   * energy/material/information flows
   * environment interactions
2. Separate:

   * what must be modeled explicitly
   * what can be abstracted
3. Identify the dominant physics or process interactions.

**Deliverable**

* Conceptual model package

---

### Week 5 — Multi-domain physical modeling

**Goal**
Work across mechanical, electrical, fluid, thermal, biological, or hybrid domains.

Modelica explicitly supports acausal, reusable multi-domain modeling for complex cyber-physical systems, and Simscape supports network-based physical modeling across mechanical, electrical, hydraulic, pneumatic, and thermal domains. ([modelica.org][155])

**Read**

* Modelica Association language and tools pages. ([modelica.org][156])
* MathWorks Simscape/physical-modeling overview. ([MathWorks][157])

**Exercises**

1. Choose two interacting domains in your system.
2. Define governing relationships at a conceptual level.
3. Build a small prototype model in your chosen environment or on paper:

   * translational/rotational mechanics
   * electrical subsystem
   * thermal or fluid path
4. Note what coupling effects matter most.

**Deliverable**

* Multi-domain subsystem model

---

### Week 6 — From conceptual model to mathematical model

**Goal**
Translate system understanding into equations, states, and simulation structure.

**Read**

* Modelica overview/specification-oriented material for equation-based system representation. ([modelica.org][155])
* MathWorks physical-modeling pages for implementation mindset in simulation tools. ([MathWorks][158])

**Exercises**

1. Identify:

   * states
   * inputs
   * outputs
   * parameters
2. Write the governing equations or pseudo-equations for one subsystem.
3. Note simplifying assumptions and expected validity range.
4. Implement a minimal mathematical model in your tool or in a computational notebook.

**Deliverable**

* Mathematical model note
* Prototype executable model

---

### Week 7 — Interoperability and composability

**Goal**
Understand how models can work together and where they fail to compose cleanly.

The DoD’s current M&S policy explicitly addresses distributed simulations and reuse, and the VV&A guide exists partly because reused or composed models still need credibility for a specific intended use. ([ESD WHS][153])

**Read**

* DoD Instruction 5000.61 for distributed simulation and standardization context. ([ESD WHS][153])
* DoD VV&A Recommended Practices Guide introduction. ([Chief Technology Officer][106])

**Exercises**

1. List the model components or federates you would want to compose.
2. Identify interoperability issues:

   * units
   * timing
   * resolution/fidelity
   * data semantics
   * ownership/versioning
3. Write a composability risk memo.
4. Sketch an integration architecture for a collaborative model environment.

**Deliverable**

* Interoperability/composability assessment

---

### Week 8 — Environment modeling: natural and man-made

**Goal**
Model the operating environment, not just the system.

The course description explicitly calls out natural and man-made environments, and NASA’s systems-engineering framing makes environment assumptions part of whether simulated results are decision-relevant. ([NASA][27])

**Read**

* NASA Systems Engineering Handbook sections on operational scenarios and off-nominal situations. ([NASA][27])
* NASA systems analysis overview. ([NASA Technical Reports Server][120])

**Exercises**

1. Identify environmental drivers:

   * temperature
   * weather/load
   * terrain/network
   * user behavior
   * regulatory or infrastructure constraints
2. Build an environment model or scenario set.
3. Test how the environment changes one key system metric.
4. Note which assumptions are most fragile.

**Deliverable**

* Environment model and scenario set

---

### Week 9 — Cost modeling and lifecycle tradeoffs

**Goal**
Incorporate cost into simulation-supported decisions.

NASA’s systems-engineering guidance frames trade studies as balancing technical performance, risk, and other constraints across lifecycle decisions. ([NASA][27])

**Read**

* NASA Systems Engineering Handbook sections on trade studies and lifecycle reasoning. ([NASA][27])
* NASA systems analysis overview. ([NASA Technical Reports Server][120])

**Exercises**

1. Define cost categories:

   * development
   * integration
   * operations
   * maintenance
   * replacement
2. Build a simple cost model tied to your simulation outputs.
3. Compare two or three design alternatives on both performance and cost.
4. Write a short trade-study memo.

**Deliverable**

* Cost model
* Tradeoff memo

---

### Week 10 — Continuous and real-time simulation

**Goal**
Study simulation for dynamically evolving physical systems and time-sensitive behavior.

MathWorks’ physical-modeling ecosystem is directly aimed at dynamic physical-system simulation and control-oriented workflows, while Modelica remains strong for continuous-time, equation-based simulation of hybrid cyber-physical systems. ([MathWorks][158])

**Read**

* MathWorks physical-modeling and Simscape overview. ([MathWorks][157])
* Modelica Association language overview. ([modelica.org][156])

**Exercises**

1. Identify whether your case needs:

   * continuous-time simulation
   * event-driven simulation
   * real-time or near-real-time execution
2. Build or sketch a continuous or hybrid simulation example.
3. Explain where real-time constraints would matter.
4. Compare continuous and discrete-event representations for the same system aspect.

**Deliverable**

* Continuous/real-time simulation note

---

### Week 11 — Verification, validation, and credibility of advanced models

**Goal**
Assess whether the model is credible enough for the decision.

The DoD VV&A Recommended Practices Guide and current M&S policy remain the most relevant public references here. They emphasize intended use, evidence, and uncertainty rather than blanket claims that a model is simply “valid.” ([Chief Technology Officer][106])

**Read**

* DoD VV&A Recommended Practices Guide. ([Chief Technology Officer][106])
* DoD Instruction 5000.61 for standards context. ([ESD WHS][153])

**Exercises**

1. Build a VV&A plan for your project:

   * code/model verification
   * validation evidence
   * uncertainty characterization
   * intended-use statement
2. Identify top threats to credibility.
3. Decide what additional evidence would be needed before a program milestone decision.

**Deliverable**

* VV&A and credibility package

---

### Week 12 — Final simulation study and presentation

**Goal**
Pull the course together into a full advanced M&S case study.

**Exercises**
Assemble a final package with:

1. system and decision context
2. conceptual model
3. mathematical model
4. statistical input model
5. interoperability/composability assessment
6. environment model
7. cost model
8. continuous or real-time simulation component
9. VV&A plan
10. results and recommendation

Prepare:

* a **4–6 page final report**
* a **10-minute case-study presentation**
* a short slide on limitations and next steps

**Deliverable**

* Final case-study binder
* Presentation deck outline

### Best resource stack

These are the strongest anchors for the course:

* **NASA Systems Engineering Handbook**, for how modeling and simulation support decisions across the lifecycle. ([NASA][27])
* **DoD Instruction 5000.61** and the **VV&A Recommended Practices Guide**, for current policy and credibility guidance on M&S, distributed simulations, and reuse. ([ESD WHS][153])
* **Modelica Association** resources, for open, equation-based, multi-domain physical-system modeling. ([modelica.org][155])
* **MathWorks Simscape / physical-modeling pages**, for practical physical-system implementation across multiple engineering domains. ([MathWorks][157])
* **NASA Systems Analysis, Modeling, and Simulation** overview, for a concise analytical perspective on the role of M&S in systems engineering. ([NASA Technical Reports Server][120])

### What you should be able to do after 12 weeks

You should be able to:

* frame a requirements-driven simulation study
* create conceptual and mathematical models of complex physical systems
* model stochastic inputs and analyze results under uncertainty
* reason about interoperability and composability of models
* incorporate environment and cost into simulation-based decisions
* distinguish when continuous, event-driven, or real-time simulation is appropriate
* lead a credible M&S effort through VV&A and decision support

---

[Back to Phase 3 README](README.md) · [Back to program README](../README.md)

## References

[27]: https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf "NASA Systems Engineering Handbook"
[106]: https://www.cto.mil/sea/vva_rpg "Verification, Validation, and Accreditation (VV&A) ..."
[120]: https://ntrs.nasa.gov/api/citations/20160004390/downloads/20160004390.pdf "Systems Analysis, Modeling, and Simulation"
[153]: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500061p.pdf "DoD Instruction 5000.61, \"DoD Modeling and Simulation ..."
[154]: https://www.dote.osd.mil/LinkClick.aspx?fileticket=Dt45nHpTB6A%3D&portalid=97 "DoD Manual (DoDM) 5000.102 Modeling and Simulation ( ..."
[155]: https://modelica.org "Modelica Association"
[156]: https://modelica.org/language "Learning the Modelica Language"
[157]: https://www.mathworks.com/help/simulink/physical-modeling.html "Physical Modeling - MATLAB & Simulink"
[158]: https://www.mathworks.com/solutions/physical-modeling.html "Physical Modeling - MATLAB and Simulink"
