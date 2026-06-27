Below is a broad taxonomy of **models and diagrams used in systems engineering / systems architecture**. It is notation-neutral where possible, but I’ll map common artifacts to **SysML, UML, UAF/DoDAF/MODAF/NAF, MBSE, safety, software, physical engineering, and operations** practices.

A useful grounding principle: architecture is usually described through **multiple views governed by viewpoints**, rather than one “master diagram.” ISO/IEC/IEEE 42010 frames architecture descriptions around concerns, stakeholders, viewpoints, and views; viewpoint conventions can include model kinds, languages, notations, methods, and analysis techniques. ([IEEE Standards Association][1]) SysML is a general-purpose MBSE language for modeling requirements, structure, behavior, analysis cases, and verification cases. ([OMG][2]) UAF provides enterprise/system-of-systems architecture viewpoints such as Strategic, Operational, Services, Personnel, Resources, Security, Project, Standards, and Actual Resources. ([OMG][3])


**Table of Contents**

- [1. Views and Viewpoints](#1-views-and-viewpoints)
  - [1.1 Enterprise / Mission / Strategic View](#11-enterprise-mission-strategic-view)
  - [1.2 Stakeholder / Context View](#12-stakeholder-context-view)
  - [1.3 Operational View](#13-operational-view)
  - [1.4 Capability View](#14-capability-view)
  - [1.5 Functional / Logical View](#15-functional-logical-view)
  - [1.6 Behavioral / Dynamic View](#16-behavioral-dynamic-view)
  - [1.7 Information / Data View](#17-information-data-view)
  - [1.9 Service View](#19-service-view)
  - [1.1.0 Physical / Structural View](#110-physical-structural-view)
  - [1.1.1 Interface View](#111-interface-view)
  - [1.1.2 Allocation / Traceability View](#112-allocation-traceability-view)
  - [1.1.3 Requirements / Needs View](#113-requirements-needs-view)
  - [1.1.4 Verification, Validation, and Test View](#114-verification-validation-and-test-view)
  - [1.1.5 Analysis / Performance / Simulation View](#115-analysis-performance-simulation-view)
  - [1.1.6 Safety / Security / Assurance View](#116-safety-security-assurance-view)
  - [1.1.7 Deployment / Installation / Operational Support View](#117-deployment-installation-operational-support-view)
  - [1.1.8 Project / Lifecycle / Evolution View](#118-project-lifecycle-evolution-view)
  - [Compact checklist version](#compact-checklist-version)
- [2. Enterprise, mission, and strategic models](#2-enterprise-mission-and-strategic-models)
- [3. Stakeholder, context, and environment models](#3-stakeholder-context-and-environment-models)
- [4. Operational architecture models](#4-operational-architecture-models)
- [5. Capability models](#5-capability-models)
- [6. Functional architecture models](#6-functional-architecture-models)
- [7. Behavioral and dynamic models](#7-behavioral-and-dynamic-models)
- [8. Information and data architecture models](#8-information-and-data-architecture-models)
- [9. Service architecture models](#9-service-architecture-models)
- [10. Physical, structural, and resource architecture models](#10-physical-structural-and-resource-architecture-models)
- [11. Interface and integration models](#11-interface-and-integration-models)
- [12. Requirements and specification models](#12-requirements-and-specification-models)
- [13. Allocation, traceability, and consistency models](#13-allocation-traceability-and-consistency-models)
- [14. Verification, validation, and test models](#14-verification-validation-and-test-models)
- [15. Performance, analysis, and trade-study models](#15-performance-analysis-and-trade-study-models)
- [16. Safety, security, resilience, and assurance models](#16-safety-security-resilience-and-assurance-models)
- [17. Software architecture models](#17-software-architecture-models)
- [18. Human, organizational, and personnel models](#18-human-organizational-and-personnel-models)
- [19. Deployment, operations, sustainment, and lifecycle models](#19-deployment-operations-sustainment-and-lifecycle-models)
- [20. Project, program, and governance models](#20-project-program-and-governance-models)
- [21. Architecture framework-specific view families](#21-architecture-framework-specific-view-families)
  - [ISO/IEC/IEEE 42010 framing](#isoiecieee-42010-framing)
  - [UAF / DoDAF-style architecture families](#uaf-dodaf-style-architecture-families)
  - [SysML v1 diagram families](#sysml-v1-diagram-families)
  - [SysML v2 model emphasis](#sysml-v2-model-emphasis)
- [22. Cross-view “master hierarchy” of model types](#22-cross-view-master-hierarchy-of-model-types)
- [23. How the major views relate](#23-how-the-major-views-relate)
- [24. “Which diagram should I use?” by question](#24-which-diagram-should-i-use-by-question)
- [25. Minimal “complete architecture package” for a serious system](#25-minimal-complete-architecture-package-for-a-serious-system)

---

# 1. Views and Viewpoints

## 1.1 Enterprise / Mission / Strategic View

**Core question:** Why does this system exist?

Questions someone might ask:

1. What mission, business outcome, or strategic objective does this system support?
2. What problem are we trying to solve?
3. What opportunity are we trying to capture?
4. What mission gaps or capability gaps exist today?
5. What are the desired mission effects or business outcomes?
6. Who owns the mission or strategic objective?
7. What higher-level strategy does this system align with?
8. What would success look like at the enterprise or mission level?
9. What are the key measures of effectiveness?
10. What capabilities are required to achieve the mission?
11. Which capabilities already exist, and which are missing?
12. What is the future-state vision?
13. What is the current-state architecture or operating model?
14. What transition path moves us from current state to future state?
15. What alternatives were considered?
16. What strategic risks could prevent mission success?
17. What external forces shape the strategy: market, policy, threat, regulation, technology?
18. What assumptions are we making about the future environment?
19. What decisions must leadership make?
20. What happens if we do nothing?

---

## 1.2 Stakeholder / Context View

**Core question:** Who and what surrounds the system?

Questions someone might ask:

1. What is the system of interest?
2. Where is the system boundary?
3. What is inside the system versus outside the system?
4. Who are the stakeholders?
5. Who are the users?
6. Who are the operators?
7. Who are the maintainers?
8. Who are the owners, sponsors, regulators, and approvers?
9. What external systems interact with this system?
10. What organizations interact with this system?
11. What physical, cyber, regulatory, and operational environments surround it?
12. What external dependencies does the system have?
13. What external constraints are imposed on the system?
14. What assumptions are we making about external actors or systems?
15. What interfaces cross the system boundary?
16. What information, energy, material, money, or control flows cross the boundary?
17. What stakeholder concerns must the architecture address?
18. Which stakeholders have conflicting concerns?
19. Which external entities are authoritative sources of data, commands, or policy?
20. What context changes would break the architecture?

---

## 1.3 Operational View

**Core question:** How is the mission or work performed?

Questions someone might ask:

1. Who performs the operational activities?
2. What operational activities are performed?
3. In what sequence are activities performed?
4. What are the operational scenarios or mission threads?
5. What triggers the operation?
6. What are the expected operational outcomes?
7. What information is exchanged during the operation?
8. What decisions are made by operators, users, or organizations?
9. What roles participate in the operation?
10. What organizations are involved?
11. What operational constraints exist?
12. What rules of engagement, policies, or procedures apply?
13. What are the normal operating conditions?
14. What are the abnormal, degraded, emergency, or contingency operations?
15. What operational tempo, workload, or throughput is expected?
16. What operational measures of effectiveness apply?
17. What are the failure points in the operation?
18. Where are handoffs between people, systems, or organizations?
19. Which operational activities are automated, manual, or mixed?
20. Does the proposed system improve the operational workflow?

---

## 1.4 Capability View

**Core question:** What abilities must the enterprise or system provide?

Questions someone might ask:

1. What capabilities are required?
2. What capability gaps exist?
3. Which capabilities are mission-critical?
4. Which capabilities are optional or future enhancements?
5. How are capabilities decomposed?
6. Which capabilities depend on other capabilities?
7. Which operational activities require each capability?
8. Which systems or resources enable each capability?
9. Which organizations own or deliver each capability?
10. What capability level is required: basic, advanced, resilient, autonomous, scalable?
11. What capability maturity exists today?
12. What capability maturity is needed in the future?
13. What capability increments will be delivered over time?
14. Which capabilities are duplicated across the enterprise?
15. Which capabilities are missing, weak, obsolete, or at risk?
16. What measures show whether a capability is effective?
17. What threats or changes could degrade the capability?
18. What investments are needed to improve the capability?
19. What dependencies constrain capability delivery?
20. How does this system contribute to enterprise capability?

---

## 1.5 Functional / Logical View

**Core question:** What must the system do, independent of implementation?

Questions someone might ask:

1. What functions must the system perform?
2. What is the top-level system function?
3. How are functions decomposed?
4. What inputs does each function consume?
5. What outputs does each function produce?
6. What controls or constraints govern each function?
7. What resources or mechanisms enable each function?
8. What functions transform information, energy, material, or signals?
9. Which functions are mandatory, optional, or conditional?
10. Which functions happen sequentially?
11. Which functions happen concurrently?
12. Which functions are triggered by events?
13. Which functions support which operational activities?
14. Which requirements does each function satisfy?
15. Which functions are safety-critical, security-critical, or mission-critical?
16. Which functions are allocated to hardware, software, humans, services, or procedures?
17. What functional dependencies exist?
18. What functional interfaces exist?
19. Are any functions missing, duplicated, or misplaced?
20. Can the logical architecture support alternative physical implementations?

---

## 1.6 Behavioral / Dynamic View

**Core question:** How does the system behave over time?

Questions someone might ask:

1. What events can occur?
2. What states or modes can the system be in?
3. What causes transitions between states?
4. What behavior occurs in each state?
5. What behavior occurs during transitions?
6. What are the normal behavior sequences?
7. What are the abnormal or exception sequences?
8. What happens when inputs arrive out of order?
9. What happens when an expected event does not occur?
10. What timing constraints apply?
11. What concurrency exists?
12. What synchronization is required?
13. What race conditions or deadlocks are possible?
14. What are the startup, shutdown, reset, and recovery behaviors?
15. What degraded modes exist?
16. What emergency behaviors exist?
17. How does the system respond to faults?
18. How does the system respond to operator commands?
19. How does the system behave under high load or stress?
20. Is the behavior deterministic, probabilistic, adaptive, or emergent?

---

## 1.7 Information / Data View

**Core question:** What information exists, flows, changes, and is governed?

Questions someone might ask:

1. What data or information does the system use?
2. What data does the system create?
3. What data does the system store?
4. What data does the system exchange?
5. What are the key information entities?
6. What is the authoritative source for each data element?
7. Who owns the data?
8. Who can create, read, update, or delete the data?
9. What data quality requirements apply?
10. What data formats, schemas, or standards apply?
11. What metadata is required?
12. What data is sensitive, classified, regulated, or private?
13. What data retention rules apply?
14. What data lineage must be tracked?
15. What transformations are applied to data?
16. What information is exchanged between operational nodes or system components?
17. What data is needed for decisions?
18. What happens if data is missing, late, corrupted, stale, or inconsistent?
19. What semantic definitions must be shared across stakeholders?
20. Does the data model support the required operations and analytics?

---

## 1.9 Service View

**Core question:** What services are provided and consumed?

Questions someone might ask:

1. What services does the system provide?
2. What services does the system consume?
3. Who are the service providers?
4. Who are the service consumers?
5. What service contracts exist?
6. What operations does each service expose?
7. What messages, events, or APIs are exchanged?
8. What service-level objectives apply?
9. What availability, latency, throughput, or reliability is required?
10. What authentication and authorization are required?
11. What service dependencies exist?
12. What happens if a service is unavailable?
13. What services are reused from elsewhere?
14. What services are newly developed?
15. What services are external or third-party?
16. What orchestration or choreography is required?
17. What versioning strategy applies to services?
18. How are services discovered, monitored, and governed?
19. Which capabilities or operational activities does each service support?
20. Are service boundaries aligned with ownership, data, and operational needs?

---

## 1.1.0 Physical / Structural View

**Core question:** What is the system made of?

Questions someone might ask:

1. What are the major system elements?
2. How is the system decomposed into subsystems, components, parts, or assemblies?
3. What hardware exists?
4. What software exists?
5. What human elements, facilities, tools, or support equipment exist?
6. What physical connections exist between elements?
7. What logical connections exist between elements?
8. What ports, connectors, buses, networks, or physical interfaces exist?
9. What is the product breakdown structure?
10. What are the critical components?
11. What components are reused, acquired, modified, or newly developed?
12. What components are replaceable, upgradeable, or configurable?
13. What mass, volume, power, thermal, and environmental constraints apply?
14. What redundancy or fault tolerance is built into the structure?
15. What physical layout constraints exist?
16. What component dependencies exist?
17. Which components perform which functions?
18. Which requirements are allocated to which components?
19. What variants or configurations exist?
20. Is the structure feasible to build, integrate, test, maintain, and sustain?

---

## 1.1.1 Interface View

**Core question:** How do system elements interact across boundaries?

Questions someone might ask:

1. What interfaces exist?
2. Which interfaces cross the system boundary?
3. Which interfaces are internal?
4. Who owns each interface?
5. What elements are connected by each interface?
6. What information, energy, force, material, signal, or control passes through each interface?
7. What are the interface protocols, formats, and standards?
8. What timing, latency, frequency, or synchronization constraints apply?
9. What physical connector, pinout, or mechanical interface is required?
10. What electrical characteristics apply?
11. What API or message schema applies?
12. What error handling is required?
13. What security controls apply at the interface?
14. What happens if the interface fails?
15. What interface assumptions are being made?
16. What interface dependencies affect integration order?
17. Which interfaces are most volatile or risky?
18. Are all interfaces documented in an ICD or equivalent?
19. Are interface changes governed?
20. Have both sides of every interface agreed to the contract?

---

## 1.1.2 Allocation / Traceability View

**Core question:** How do requirements, functions, behaviors, components, tests, and risks connect?

Questions someone might ask:

1. Which requirements trace to which stakeholder needs?
2. Which requirements trace to which capabilities?
3. Which functions satisfy which requirements?
4. Which components perform which functions?
5. Which behaviors realize which functions?
6. Which interfaces support which functions or behaviors?
7. Which tests verify which requirements?
8. Which analyses validate which performance claims?
9. Which risks affect which requirements or components?
10. Which hazards are controlled by which design features?
11. Which security threats are mitigated by which controls?
12. Are there requirements with no allocated function or component?
13. Are there components with no allocated requirement?
14. Are there functions with no operational justification?
15. Are there tests with no requirement?
16. Are there requirements with no verification method?
17. Are allocations one-to-one, one-to-many, or many-to-many?
18. Are trace links current after design changes?
19. What is the impact of changing this requirement, function, interface, or component?
20. Can we demonstrate end-to-end traceability from mission need to verified solution?

---

## 1.1.3 Requirements / Needs View

**Core question:** What must the system satisfy?

Questions someone might ask:

1. What stakeholder needs have been identified?
2. Are the needs clear and agreed upon?
3. What are the system requirements?
4. What are the functional requirements?
5. What are the performance requirements?
6. What are the interface requirements?
7. What are the safety, security, reliability, maintainability, and usability requirements?
8. What constraints are imposed by regulation, policy, environment, or standards?
9. Are requirements necessary?
10. Are requirements unambiguous?
11. Are requirements feasible?
12. Are requirements verifiable?
13. Are requirements atomic and properly scoped?
14. Are requirements prioritized?
15. What assumptions underlie the requirements?
16. Which requirements conflict with each other?
17. Which requirements are derived from architecture or analysis?
18. Which requirements are allocated to subsystems?
19. What acceptance criteria apply?
20. What changes would invalidate or alter these requirements?

---

## 1.1.4 Verification, Validation, and Test View

**Core question:** How will we prove the system is correct and useful?

Questions someone might ask:

1. How will each requirement be verified?
2. Will verification use inspection, analysis, demonstration, or test?
3. What test cases are needed?
4. What validation scenarios are needed?
5. What evidence is required for acceptance?
6. What test environments are required?
7. What simulators, emulators, test benches, or prototypes are required?
8. What instrumentation is needed?
9. What data must be collected during testing?
10. What are the pass/fail criteria?
11. What requirements are not yet verifiable?
12. What requirements lack test coverage?
13. What functions, states, modes, and interfaces must be tested?
14. What abnormal, degraded, fault, or emergency cases must be tested?
15. What regression testing is required after changes?
16. What qualification or certification evidence is required?
17. Who witnesses or approves verification?
18. How will validation confirm stakeholder needs, not just requirements?
19. What risks remain after verification?
20. What is the relationship between model-based analysis, simulation, and physical test?

---

## 1.1.5 Analysis / Performance / Simulation View

**Core question:** How well does the system perform, and what tradeoffs matter?

Questions someone might ask:

1. What performance measures matter most?
2. What are the key measures of effectiveness, performance, and technical performance?
3. What budgets exist for mass, power, cost, latency, bandwidth, reliability, weight, volume, or energy?
4. What constraints govern the analysis?
5. What assumptions are built into the model?
6. What alternatives are being compared?
7. What trade space is being explored?
8. What variables drive system performance?
9. What sensitivities exist?
10. What uncertainty exists?
11. What probability distributions are assumed?
12. What simulations are required?
13. What fidelity is needed for each analysis?
14. Has the analysis model been validated?
15. What margins exist?
16. Which requirements are at risk based on analysis?
17. What bottlenecks limit performance?
18. What is the optimal or preferred architecture alternative?
19. What are the cost, schedule, performance, and risk tradeoffs?
20. How do analysis results affect requirements, architecture, or design decisions?

---

## 1.1.6 Safety / Security / Assurance View

**Core question:** How can the system cause harm, be compromised, or fail assurance expectations?

Questions someone might ask:

1. What hazards exist?
2. What losses or unacceptable outcomes must be prevented?
3. What failure modes exist?
4. What causes could lead to those failures?
5. What unsafe control actions are possible?
6. What threats exist?
7. What assets need protection?
8. What attack surfaces exist?
9. What vulnerabilities are known or plausible?
10. What mitigations or controls are required?
11. What safety requirements are derived from hazard analysis?
12. What security requirements are derived from threat analysis?
13. What assurance claims must be made?
14. What evidence supports those claims?
15. What standards, regulations, or certification criteria apply?
16. What residual risks remain?
17. Who has authority to accept residual risk?
18. What happens in degraded, emergency, or compromised conditions?
19. How are safety and security controls verified?
20. Could a safety mitigation create a security weakness, or vice versa?

---

## 1.1.7 Deployment / Installation / Operational Support View

**Core question:** How is the system fielded, operated, maintained, and supported?

Questions someone might ask:

1. Where will the system be deployed?
2. What deployment environments exist?
3. What installation steps are required?
4. What site, facility, rack, network, or infrastructure dependencies exist?
5. What configuration is deployed at each location?
6. What operational procedures are required?
7. What monitoring is required?
8. What alerts, logs, diagnostics, or telemetry are needed?
9. Who operates the system?
10. Who maintains the system?
11. What training is required?
12. What tools, spares, consumables, or support equipment are required?
13. What maintenance concept applies?
14. What failure detection and recovery procedures exist?
15. What backup, restore, and disaster recovery approach is needed?
16. What service levels must be maintained in operation?
17. How will patches, upgrades, and configuration changes be managed?
18. How will field issues be reported and resolved?
19. What sustainment risks exist?
20. What end-of-life, replacement, or decommissioning path exists?

---

## 1.1.8 Project / Lifecycle / Evolution View

**Core question:** How will the system change over time?

Questions someone might ask:

1. What lifecycle phase is the system in?
2. What increments, releases, blocks, spirals, or versions are planned?
3. What capabilities are delivered in each increment?
4. What architecture baseline applies now?
5. What future architecture baselines are planned?
6. What migration path moves from current architecture to target architecture?
7. What dependencies drive delivery sequence?
8. What technology insertion points exist?
9. What obsolescence risks exist?
10. What standards or policies must be adopted over time?
11. What decisions are pending?
12. What design decisions have already been made?
13. What assumptions must be revisited later?
14. What risks affect schedule, cost, scope, or technical feasibility?
15. What configuration variants must be managed?
16. What product line or family evolution is expected?
17. What governance process controls architecture change?
18. What reviews, gates, or approvals are required?
19. How will the architecture adapt to new threats, users, missions, or technologies?
20. What is the retirement or replacement strategy?

---

## Compact checklist version

| View                                | Primary engagement question                  |
| ----------------------------------- | -------------------------------------------- |
| Enterprise / Mission / Strategic    | Why are we doing this?                       |
| Stakeholder / Context               | Who and what surrounds the system?           |
| Operational                         | How is the work or mission performed?        |
| Capability                          | What abilities are needed?                   |
| Functional / Logical                | What must the system do?                     |
| Behavioral / Dynamic                | How does it behave over time?                |
| Information / Data                  | What information exists and flows?           |
| Service                             | What services are provided and consumed?     |
| Physical / Structural               | What is the system made of?                  |
| Interface                           | How do elements connect and interact?        |
| Allocation / Traceability           | How do all architecture elements relate?     |
| Requirements / Needs                | What must be satisfied?                      |
| Verification / Validation / Test    | How will we prove it works and is useful?    |
| Analysis / Performance / Simulation | How well will it perform?                    |
| Safety / Security / Assurance       | What can go wrong, and how is it controlled? |
| Deployment / Operational Support    | How is it fielded, run, and sustained?       |
| Project / Lifecycle / Evolution     | How will it change over time?                |

---

# 2. Enterprise, mission, and strategic models

These answer: **Why are we building or changing the system?**

| Model / diagram                 | Purpose                                                         | Common notation / framework                                 |
| ------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| Mission model                   | Captures mission objectives, effects, outcomes, mission threads | UAF Strategic / Mission, DoDAF capability/operational views |
| Business motivation model       | Goals, drivers, assessments, strategies, tactics                | BMM, ArchiMate, UAF Strategic                               |
| Goal tree / objective hierarchy | Decomposes top-level objectives into measurable sub-objectives  | SysML requirements, KAOS, GSN-like structures               |
| Capability map                  | Shows capabilities required by the enterprise or mission        | UAF Strategic, DoDAF CV, ArchiMate capability map           |
| Capability decomposition        | Breaks capabilities into sub-capabilities                       | UAF, DoDAF CV-2                                             |
| Capability-to-mission mapping   | Shows which capabilities support which missions or effects      | UAF Strategic / Operational                                 |
| Roadmap / capability phasing    | Shows capability increments over time                           | UAF Project, DoDAF CV-3                                     |
| Value stream map                | Shows value delivery flow across an enterprise                  | Lean, SAFe, ArchiMate                                       |
| Outcome map / benefits map      | Links investments to outcomes and benefits                      | Benefits dependency network                                 |
| Concept of operations summary   | Narrative plus diagrams describing intended use                 | CONOPS, OV-1/SOV-style diagrams                             |

**Typical outputs:** mission statement, operational problem, measures of effectiveness, capability gaps, future-state concept, transition roadmap.

---

# 3. Stakeholder, context, and environment models

These answer: **What is the system of interest, what surrounds it, and who cares?**

| Model / diagram               | Purpose                                                                   | Common notation                                      |
| ----------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------- |
| System context diagram        | Shows system boundary and external actors/systems                         | SysML block/context diagram, C4 context, DFD context |
| External systems diagram      | Shows neighboring systems and dependencies                                | UAF Resources, DoDAF SV/SvcV                         |
| Stakeholder map               | Identifies stakeholders and relationships                                 | Rich picture, onion diagram                          |
| Stakeholder concern matrix    | Maps stakeholders to concerns, decisions, and views                       | ISO 42010-style architecture description             |
| Use environment model         | Captures physical, cyber, social, regulatory, and operational environment | SysML blocks, domain models                          |
| Ecosystem map                 | Shows broader business, operational, or technical ecosystem               | Enterprise architecture, Wardley map                 |
| Rich picture                  | Informal diagram of problem situation, actors, conflicts                  | Soft systems methodology                             |
| Domain model                  | Key domain concepts and relationships                                     | UML class diagram, SysML block definition diagram    |
| System boundary diagram       | Explicitly separates inside/outside responsibilities                      | Context diagram, interface control boundary          |
| Assumption / constraint model | Captures environmental assumptions and imposed constraints                | Requirements model, decision log                     |

---

# 4. Operational architecture models

These answer: **How is work performed in the real world, independent of the solution design?**

UAF and DoDAF distinguish operational perspectives from implementation/resource perspectives. UAF’s Operational viewpoint, for example, deals with operational performers and activities supporting capabilities. ([Mission Capabilities][4])

| Model / diagram                         | Purpose                                                     | Common notation / equivalent            |
| --------------------------------------- | ----------------------------------------------------------- | --------------------------------------- |
| Operational context diagram             | Operational actors, organizations, systems, and environment | DoDAF OV-1, UAF Operational             |
| Operational node diagram                | Operational performers/nodes and relationships              | DoDAF OV-2                              |
| Operational activity model              | Activities performed by operational actors                  | DoDAF OV-5, SysML activity              |
| Operational activity decomposition      | Hierarchy of operational activities                         | Functional/activity tree                |
| Operational workflow                    | End-to-end operational process                              | BPMN, activity diagram, IDEF0           |
| Operational scenario                    | Story of a specific mission/use case                        | Sequence diagram, mission thread, OV-6c |
| Mission thread                          | End-to-end operational sequence across performers           | UAF, DoDAF, sequence/activity           |
| Use case diagram                        | User goals and system interactions                          | UML/SysML use case                      |
| Operational event trace                 | Ordered events among operational entities                   | Sequence diagram, OV-6c                 |
| Operational state model                 | Operational states, phases, and transitions                 | State machine, OV-6b                    |
| Operational rules model                 | Business/mission rules constraining activities              | Decision table, DMN, rule catalog       |
| Operational information exchange matrix | Who exchanges what information with whom                    | DoDAF OV-3, UAF information flows       |
| Swimlane activity diagram               | Allocates activities to operational roles                   | BPMN, SysML activity partitions         |
| Business process model                  | Operational/business process flow                           | BPMN, EPC, value stream                 |
| Organization model                      | Organizational units, roles, command relationships          | Org chart, UAF Personnel/Operational    |
| Role/responsibility matrix              | Responsibility assignment                                   | RACI, responsibility matrix             |
| Human task model                        | Human actions, decisions, workload                          | Human factors task analysis             |
| User journey map                        | User experience over time                                   | Service design / UX                     |

---

# 5. Capability models

These answer: **What abilities must the system or enterprise possess?**

| Model / diagram                            | Purpose                                       | Common notation            |
| ------------------------------------------ | --------------------------------------------- | -------------------------- |
| Capability taxonomy                        | Hierarchical list of capabilities             | UAF Strategic, DoDAF CV-2  |
| Capability map                             | Visual map of business/mission capabilities   | ArchiMate, UAF             |
| Capability dependency model                | Shows dependencies among capabilities         | UAF, ArchiMate             |
| Capability-to-operational-activity mapping | Connects capability to operations             | UAF/DoDAF matrices         |
| Capability-to-system mapping               | Shows which systems enable which capabilities | UAF Resources, DoDAF CV/SV |
| Capability gap analysis                    | Current vs needed capabilities                | Heat map, matrix           |
| Capability increment roadmap               | Capability delivery over time                 | DoDAF CV-3, UAF Project    |
| Capability maturity model                  | Capability levels and progression             | CMMI-like maturity models  |

---

# 6. Functional architecture models

These answer: **What must the system do?**

Functional architecture is often solution-independent or semi-logical: it decomposes required transformations and responsibilities before committing to physical implementation.

| Model / diagram                        | Purpose                                                      | Common notation                               |
| -------------------------------------- | ------------------------------------------------------------ | --------------------------------------------- |
| Functional decomposition               | Breaks top-level functions into subfunctions                 | Function tree, FAST, SysML activity hierarchy |
| Functional flow block diagram          | Sequences functions and alternatives                         | FFBD                                          |
| Enhanced functional flow block diagram | Adds triggering, data, timing, control                       | EFFBD                                         |
| IDEF0 model                            | Functions with inputs, controls, outputs, mechanisms         | IDEF0                                         |
| Activity diagram                       | Functional behavior, flows, decisions, concurrency           | SysML/UML activity                            |
| Data flow diagram                      | Functions/processes and data stores/flows                    | DFD                                           |
| Function allocation matrix             | Allocates functions to components, roles, software, hardware | N², allocation table                          |
| Functional interface diagram           | Interactions among functions                                 | N², activity/object flows                     |
| Function-to-requirement trace          | Shows which functions satisfy which requirements             | Traceability matrix                           |
| Function-to-state mapping              | Functions available in modes/states                          | Mode/function matrix                          |
| Control flow model                     | Logic and decision flow among functions                      | Activity, flowchart, control block diagram    |
| Signal flow diagram                    | Processing or control signal transformations                 | Signal flow graph, Simulink                   |
| Logical architecture diagram           | Logical subsystems/functions before physical design          | SysML blocks, logical components              |
| Functional chain / end-to-end thread   | Functions involved in a mission or feature                   | Activity/sequence hybrid                      |

---

# 7. Behavioral and dynamic models

These answer: **How does the system behave over time?**

| Model / diagram                 | Purpose                                           | Common notation                                        |
| ------------------------------- | ------------------------------------------------- | ------------------------------------------------------ |
| Sequence diagram                | Time-ordered messages among actors/components     | UML/SysML sequence                                     |
| Communication diagram           | Interactions emphasizing links rather than time   | UML communication                                      |
| State machine diagram           | States, events, transitions, guards, actions      | SysML/UML state machine                                |
| State transition table          | Tabular state/event behavior                      | State table                                            |
| Mode model                      | System modes and mode transitions                 | State machine, mode table                              |
| Activity diagram                | Behavior flow, concurrency, decisions             | SysML/UML                                              |
| Timing diagram                  | Value/state changes over time                     | UML timing diagram                                     |
| Event trace diagram             | Events across entities                            | DoDAF OV-6c/SV-10c                                     |
| Scenario model                  | Specific path through behavior                    | Use case scenario, sequence                            |
| Interaction overview diagram    | High-level control among interactions             | UML                                                    |
| Petri net                       | Concurrency, synchronization, resource contention | Petri net                                              |
| Discrete event simulation model | Queueing, events, resource use                    | DES tools                                              |
| System dynamics model           | Feedback loops, accumulations, delays             | Causal loop, stock-and-flow                            |
| Agent-based model               | Autonomous agents and emergent behavior           | ABM                                                    |
| Markov model                    | Probabilistic state transitions                   | Markov chain/MDP                                       |
| Hybrid automaton                | Continuous plus discrete behavior                 | Formal methods/control                                 |
| Executable architecture model   | Simulatable integrated structure/behavior         | SysML parametric/executable, Cameo, Rhapsody, Simulink |

---

# 8. Information and data architecture models

These answer: **What information exists, where it flows, and how it is structured?**

| Model / diagram                           | Purpose                                            | Common notation                 |
| ----------------------------------------- | -------------------------------------------------- | ------------------------------- |
| Conceptual data model                     | Business/domain information concepts               | ERD, UML class, SysML blocks    |
| Logical data model                        | Entities, attributes, relationships, normalization | ERD, class diagram              |
| Physical data model                       | Database tables, indexes, schemas                  | ERD, SQL schema                 |
| Information exchange model                | Information exchanged between nodes/systems        | DoDAF OV-3, SV-6, UAF exchanges |
| Data flow diagram                         | Data movement through processes/stores             | DFD                             |
| Data lineage diagram                      | Origin, transformation, and consumption of data    | Data governance tools           |
| CRUD matrix                               | Create/read/update/delete responsibilities         | Matrix                          |
| Information lifecycle model               | Creation, use, retention, archival, deletion       | Data governance                 |
| Message schema model                      | Message structure and constraints                  | JSON Schema, XML Schema, ASN.1  |
| Ontology / semantic model                 | Formal vocabulary and relationships                | OWL/RDF, knowledge graph        |
| Taxonomy                                  | Classification hierarchy                           | Tree/hierarchy                  |
| Data dictionary                           | Definitions of data elements                       | Tabular model                   |
| Data ownership model                      | Data stewards, owners, authoritative sources       | Matrix                          |
| Data quality model                        | Accuracy, completeness, timeliness, quality rules  | Rules and metrics               |
| Information security classification model | Sensitivity, releasability, handling rules         | Security architecture           |

---

# 9. Service architecture models

These answer: **What services are provided, consumed, orchestrated, and governed?**

| Model / diagram             | Purpose                                             | Common notation                       |
| --------------------------- | --------------------------------------------------- | ------------------------------------- |
| Service context diagram     | Service providers, consumers, external dependencies | UAF Services, SOA                     |
| Service taxonomy            | Catalog of services                                 | Service catalog                       |
| Service interface diagram   | Operations, endpoints, messages, contracts          | UML/SysML interfaces, OpenAPI         |
| Service dependency diagram  | Dependencies among services                         | C4 container/component, service graph |
| Service orchestration model | Centralized workflow of service calls               | BPMN, sequence                        |
| Service choreography model  | Peer-to-peer event/message interactions             | BPMN choreography, sequence           |
| API model                   | REST/gRPC/event APIs and schemas                    | OpenAPI, AsyncAPI, protobuf           |
| Event model                 | Published/subscribed events and topics              | Event storming, AsyncAPI              |
| Service-level model         | SLAs, SLOs, SLIs                                    | Reliability engineering               |
| Service deployment model    | Where services run                                  | Kubernetes, cloud architecture        |
| Service ownership model     | Teams owning services                               | Team topology, RACI                   |
| Service portfolio roadmap   | Lifecycle of services                               | UAF Project / EA                      |

---

# 10. Physical, structural, and resource architecture models

These answer: **What is the system made of?**

SysML structure is commonly represented using block definition and internal block diagrams. SysML v2 is described by OMG as improving precision, expressiveness, usability, interoperability, and extensibility over SysML v1. ([OMG][5])

| Model / diagram                    | Purpose                                                  | Common notation               |
| ---------------------------------- | -------------------------------------------------------- | ----------------------------- |
| Product breakdown structure        | Hierarchical decomposition of product/system elements    | PBS                           |
| System breakdown structure         | System/subsystem/component hierarchy                     | SBS, SysML BDD                |
| Block definition diagram           | Types, parts, properties, associations                   | SysML BDD                     |
| Internal block diagram             | Internal composition, ports, connectors, flows           | SysML IBD                     |
| Component diagram                  | Software or logical components and dependencies          | UML component, C4 component   |
| Deployment diagram                 | Nodes, devices, execution environments, artifacts        | UML deployment                |
| Network topology diagram           | Nodes, links, routing, zones                             | Network architecture          |
| Mechanical layout                  | Physical arrangement, geometry, packaging                | CAD, layout drawings          |
| Electrical architecture            | Power, signals, buses, grounding                         | Schematics, wiring diagrams   |
| Wiring/interconnect diagram        | Harnesses, connectors, pinouts                           | Electrical CAD, ICD           |
| Piping and instrumentation diagram | Process equipment, sensors, control loops                | P&ID                          |
| Bill of materials model            | Parts, assemblies, quantities                            | PLM/BOM                       |
| Mass properties model              | Weight, center of gravity, inertia                       | CAD/analysis                  |
| Thermal architecture               | Heat sources, sinks, thermal paths                       | Thermal network               |
| Power architecture                 | Sources, loads, distribution, budgets                    | Power tree, load analysis     |
| Communications architecture        | Radios, links, protocols, bandwidth                      | Link diagrams, network models |
| Hardware/software allocation       | Maps software to processors/devices                      | Deployment/allocation matrix  |
| Physical interface model           | Mechanical, electrical, thermal, fluid, human interfaces | ICD, interface diagrams       |
| Facilities/site layout             | Buildings, rooms, racks, installation environment        | Site plan, rack elevation     |
| Logistics/support equipment model  | Support systems, spares, tools                           | Supportability model          |

---

# 11. Interface and integration models

These answer: **How do elements connect and interact?**

| Model / diagram                  | Purpose                                          | Common notation                 |
| -------------------------------- | ------------------------------------------------ | ------------------------------- |
| Interface context diagram        | All external interfaces of system of interest    | Context + interface annotations |
| Interface control document/model | Authoritative interface specification            | ICD                             |
| N² diagram                       | Pairwise interactions among functions/components | N-squared                       |
| Interface matrix                 | Interfaces by source/target/type                 | Matrix                          |
| Port and connector diagram       | Ports, flows, connectors, item flows             | SysML IBD                       |
| API contract                     | Operations, inputs, outputs, errors              | OpenAPI, gRPC, WSDL             |
| Message sequence diagram         | Message timing and ordering                      | Sequence diagram                |
| Protocol stack diagram           | Layered communication protocols                  | OSI-like stack                  |
| Signal list / pinout model       | Electrical signals, pins, connectors             | Wiring tables                   |
| Data exchange specification      | Exchanged data elements and formats              | XSD, JSON Schema, ASN.1         |
| Mechanical interface drawing     | Mating dimensions, tolerances, loads             | CAD/drawing                     |
| Human-machine interface flow     | Screens, controls, operator interactions         | Wireframes, UX flow             |
| Integration dependency graph     | Build/integration order and dependencies         | Dependency graph                |
| Interface risk matrix            | Volatility, ownership, criticality of interfaces | Matrix                          |

---

# 12. Requirements and specification models

These answer: **What must be true for the system to be acceptable?**

| Model / diagram                | Purpose                                             | Common notation                  |
| ------------------------------ | --------------------------------------------------- | -------------------------------- |
| Requirements hierarchy         | Parent/child decomposition of requirements          | SysML requirement diagram, DOORS |
| Requirement diagram            | Requirements and relationships                      | SysML requirement diagram        |
| Stakeholder needs model        | Needs, expectations, problem statements             | Needs hierarchy                  |
| Use case model                 | Functional goals and actors                         | UML/SysML use case               |
| Quality attribute scenario     | Stimulus, environment, response, measure            | SEI-style QAS                    |
| Constraint model               | Physical, regulatory, interface, design constraints | Requirements model               |
| Measures model                 | MOEs, MOPs, TPMs, KPIs                              | Metrics tree                     |
| Requirement-to-function trace  | Requirements satisfied by functions                 | Trace matrix                     |
| Requirement-to-component trace | Requirements allocated to physical/logical elements | Trace matrix                     |
| Requirement-to-test trace      | Verification coverage                               | VCRM/RTM                         |
| Requirements dependency graph  | Derive/refine/satisfy/verify relationships          | SysML                            |
| Requirements conflict matrix   | Identifies competing requirements                   | Trade/conflict matrix            |
| Acceptance criteria model      | Conditions for acceptance                           | Testable criteria                |
| Regulatory compliance matrix   | Requirements mapped to standards/regulations        | Compliance matrix                |

---

# 13. Allocation, traceability, and consistency models

These answer: **How do the views connect?**

| Model / diagram                     | Purpose                                                                   |
| ----------------------------------- | ------------------------------------------------------------------------- |
| Requirement-to-function allocation  | Shows what functions satisfy requirements                                 |
| Function-to-component allocation    | Shows which components perform which functions                            |
| Function-to-interface allocation    | Shows which interfaces support each function                              |
| Behavior-to-structure allocation    | Maps activities/states/interactions to blocks/components                  |
| Logical-to-physical allocation      | Maps logical architecture to physical implementation                      |
| Operational-to-functional mapping   | Maps operational activities to system functions                           |
| Capability-to-system mapping        | Maps capabilities to enabling systems/resources                           |
| Requirement-to-verification mapping | Ensures every requirement is verified                                     |
| Risk-to-requirement mapping         | Links risks and mitigations to requirements/design                        |
| Hazard-to-control mapping           | Links hazards to safety controls                                          |
| Decision-to-architecture mapping    | Links architecture decisions to affected elements                         |
| Variant/configuration mapping       | Shows which elements appear in which product variants                     |
| Traceability matrix                 | Tabular cross-reference among model elements                              |
| Dependency graph                    | Network of dependencies among requirements, components, tests, interfaces |

This is the “glue” of MBSE. Without allocation and traceability, the views become disconnected pictures.

---

# 14. Verification, validation, and test models

These answer: **How will we prove the system is right and fit for purpose?**

| Model / diagram                      | Purpose                                                         | Common notation                            |
| ------------------------------------ | --------------------------------------------------------------- | ------------------------------------------ |
| Verification cross-reference matrix  | Requirements mapped to verification method and evidence         | VCRM                                       |
| Test architecture                    | Test environments, equipment, simulators, interfaces            | Test system diagram                        |
| Test case model                      | Test objectives, inputs, expected results                       | SysML verification case, test procedures   |
| Verification case                    | Formal model of how a requirement is verified                   | SysML v2 verification cases                |
| Validation scenario                  | Stakeholder/mission scenario used to validate need satisfaction | Operational scenario                       |
| Test sequence diagram                | Ordered test interactions                                       | Sequence diagram                           |
| Test coverage matrix                 | Coverage of requirements, states, functions, code               | Matrix                                     |
| Inspection/analysis/demo/test matrix | Verification method by requirement                              | V&V matrix                                 |
| Digital twin validation model        | Compares simulated vs observed system behavior                  | Simulation/data model                      |
| Acceptance test model                | End-user acceptance flow                                        | UAT scripts, scenarios                     |
| Qualification model                  | Qualification levels, environments, pass/fail criteria          | Qualification matrix                       |
| Fault injection test model           | Tests failure handling and resilience                           | Fault model/test scenario                  |
| Simulation testbench                 | Model used to execute scenarios                                 | Simulink, Modelica, SysML executable model |

---

# 15. Performance, analysis, and trade-study models

These answer: **How well does the architecture perform, and which option is better?**

| Model / diagram            | Purpose                                                     |
| -------------------------- | ----------------------------------------------------------- |
| Parametric diagram         | Equations and constraints among properties                  |
| Performance budget         | Allocation of mass, power, latency, cost, reliability, etc. |
| Trade space model          | Alternatives and decision variables                         |
| Trade study matrix         | Compares alternatives against weighted criteria             |
| Sensitivity analysis model | Shows which variables most affect outcomes                  |
| Monte Carlo model          | Probabilistic performance/risk simulation                   |
| Optimization model         | Objective functions, constraints, decision variables        |
| Reliability block diagram  | System reliability from component reliabilities             |
| Fault tree                 | Deductive analysis from top event to causes                 |
| Event tree                 | Inductive analysis from initiating event to outcomes        |
| FMEA/FMECA                 | Failure modes, effects, criticality, mitigations            |
| Queueing model             | Waiting time, throughput, resource contention               |
| Capacity model             | Demand vs capacity across resources                         |
| Latency model              | End-to-end timing and delay                                 |
| Throughput model           | Processing or flow rate                                     |
| Availability model         | Uptime, maintainability, redundancy                         |
| Maintainability model      | Repair time, access, support constraints                    |
| Cost model                 | Lifecycle cost, acquisition, operations, sustainment        |
| Schedule model             | Critical path, dependencies, milestones                     |
| Risk model                 | Probability, impact, exposure, mitigations                  |
| Physics-based model        | Mechanical, thermal, fluid, electrical, chemical behavior   |
| Control model              | Plant, controller, feedback, stability                      |
| Digital twin               | Runtime-connected model reflecting system state             |

---

# 16. Safety, security, resilience, and assurance models

These answer: **How can the system fail, be attacked, or behave unsafely, and how do we control that?**

| Model / diagram               | Purpose                                               | Common notation                    |
| ----------------------------- | ----------------------------------------------------- | ---------------------------------- |
| Hazard analysis               | Identifies hazards and causes                         | PHA, FHA                           |
| Fault tree analysis           | Top-down causal failure logic                         | FTA                                |
| Event tree analysis           | Event progression and consequences                    | ETA                                |
| FMEA/FMECA                    | Component/function failure modes and effects          | FMEA tables                        |
| STPA control structure        | Unsafe control actions in socio-technical systems     | STPA                               |
| Bow-tie diagram               | Threats, controls, consequences, mitigations          | Bow-tie                            |
| Safety case                   | Structured argument for safety                        | GSN, CAE                           |
| Goal Structuring Notation     | Claims, arguments, evidence                           | GSN                                |
| Threat model                  | Assets, threats, attack paths, mitigations            | STRIDE, attack trees               |
| Attack tree                   | Attacker goals decomposed into attack paths           | Security analysis                  |
| Misuse/abuse case             | Malicious or unintended use scenarios                 | UML use case variant               |
| Data flow threat model        | Trust boundaries, processes, data stores              | DFD + STRIDE                       |
| Security architecture diagram | Zones, trust boundaries, controls                     | Zero trust, network/security views |
| Cyber kill chain model        | Attack progression                                    | Lockheed kill chain, MITRE ATT&CK  |
| Resilience model              | Degraded modes, recovery, graceful degradation        | State/mode model                   |
| Business continuity model     | Continuity and recovery plans                         | BCP/DR diagrams                    |
| Assurance case                | Structured argument for safety/security/certification | GSN/CAE                            |
| Compliance model              | Controls mapped to regulations/standards              | Compliance matrix                  |

---

# 17. Software architecture models

These answer: **How is the software organized, deployed, and evolved?**

| Model / diagram                   | Purpose                                        | Common notation      |
| --------------------------------- | ---------------------------------------------- | -------------------- |
| C4 context diagram                | Software system in its environment             | C4                   |
| C4 container diagram              | Applications, services, databases, runtimes    | C4                   |
| C4 component diagram              | Internal components of a container             | C4/UML               |
| C4 code diagram                   | Classes/modules when useful                    | UML/class            |
| UML class diagram                 | Types, attributes, operations, relationships   | UML                  |
| UML component diagram             | Software components and dependencies           | UML                  |
| UML package diagram               | Namespace/module organization                  | UML                  |
| Deployment diagram                | Software artifacts on nodes                    | UML                  |
| Sequence diagram                  | Runtime interactions                           | UML/SysML            |
| State diagram                     | Stateful software behavior                     | UML                  |
| Entity relationship diagram       | Data persistence structure                     | ERD                  |
| API diagram                       | Endpoints and API dependencies                 | OpenAPI, AsyncAPI    |
| Event-driven architecture diagram | Producers, topics, consumers                   | Kafka/event diagrams |
| Microservice dependency graph     | Runtime/service dependencies                   | Service graph        |
| Layered architecture diagram      | Presentation/domain/data/infrastructure layers | Layer diagram        |
| Hexagonal architecture diagram    | Ports/adapters                                 | Ports-and-adapters   |
| Clean architecture diagram        | Dependency direction and layers                | Concentric/layered   |
| Domain-driven design context map  | Bounded contexts and relationships             | DDD                  |
| Build/deployment pipeline diagram | CI/CD flow                                     | DevOps               |
| Observability model               | Logs, metrics, traces, alerts                  | SRE diagrams         |

---

# 18. Human, organizational, and personnel models

These answer: **How do people, organizations, and responsibilities fit into the system?**

| Model / diagram              | Purpose                                                 |
| ---------------------------- | ------------------------------------------------------- |
| Organization chart           | Formal organizational structure                         |
| Role model                   | Roles, permissions, responsibilities                    |
| RACI matrix                  | Responsible, accountable, consulted, informed           |
| Personnel availability model | Staffing and shift coverage                             |
| Skill matrix                 | Required and available competencies                     |
| Human task analysis          | User tasks, steps, cognitive load                       |
| Workload model               | Operator workload under scenarios                       |
| Human reliability analysis   | Human error probabilities and contributors              |
| HMI model                    | Operator displays, controls, interaction flows          |
| Training model               | Training needs, qualification paths                     |
| Crew/team interaction model  | Coordination among humans                               |
| Procedure model              | Operational or maintenance procedures                   |
| User journey map             | End-to-end human experience                             |
| Service blueprint            | Frontstage/backstage interactions and support processes |

---

# 19. Deployment, operations, sustainment, and lifecycle models

These answer: **How is the system fielded, operated, maintained, upgraded, and retired?**

| Model / diagram                                | Purpose                                        |
| ---------------------------------------------- | ---------------------------------------------- |
| Deployment architecture                        | Where elements are installed or hosted         |
| Installation diagram                           | Site, rack, facility, mounting, cabling        |
| Operational support model                      | Support organizations, tools, spares           |
| Maintenance concept                            | Preventive/corrective maintenance approach     |
| Reliability/availability/maintainability model | RAM performance and sustainment                |
| Logistics support analysis                     | Spares, tools, supply chain, repair levels     |
| Configuration model                            | Baselines, variants, options, serial numbers   |
| Release roadmap                                | Versions and release increments                |
| Migration roadmap                              | Transition from current to future architecture |
| Technology roadmap                             | Planned technology insertion                   |
| Obsolescence model                             | End-of-life parts, support risks               |
| Disposal/decommissioning model                 | Retirement and disposal process                |
| Incident response model                        | Detect, respond, recover                       |
| Operations runbook                             | Operational procedures and recovery steps      |
| Monitoring architecture                        | Sensors, telemetry, logs, dashboards           |
| SLA/SLO model                                  | Operational service targets                    |

---

# 20. Project, program, and governance models

These answer: **How is the architecture delivered and governed?**

| Model / diagram                     | Purpose                                            |
| ----------------------------------- | -------------------------------------------------- |
| Work breakdown structure            | Deliverable/work decomposition                     |
| Product breakdown structure         | Product structure for planning                     |
| Integrated master schedule          | Time-phased activities and dependencies            |
| Gantt chart                         | Schedule visualization                             |
| PERT/critical path network          | Dependency and duration analysis                   |
| Risk register/model                 | Risks, probability, impact, mitigations            |
| Decision log                        | Architecture decisions and rationale               |
| Architecture decision record        | Decision, context, consequences                    |
| Governance model                    | Review boards, authorities, approval paths         |
| Standards profile                   | Applicable standards and constraints               |
| Compliance matrix                   | Compliance status by requirement/standard          |
| Technical performance measure model | TPM tracking over time                             |
| Earned value model                  | Cost/schedule performance                          |
| Roadmap                             | Capability, release, technology, or migration path |
| Portfolio map                       | Systems/projects and investment relationships      |

---

# 21. Architecture framework-specific view families

## ISO/IEC/IEEE 42010 framing

42010 does not prescribe one fixed set of views. It defines the architecture-description concepts: stakeholders, concerns, architecture viewpoints, architecture views, model kinds, and correspondence rules. ([IEEE Standards Association][1])

Use it as the meta-structure:

```text
Stakeholder concern → Viewpoint → View → Model(s)/diagram(s) → Model elements
```

## UAF / DoDAF-style architecture families

UAF covers enterprise and system-of-systems architecture and is based on UML/SysML plus defense architecture framework heritage. ([OMG][6]) A practical hierarchy is:

| UAF-like family         | What it covers                                              |
| ----------------------- | ----------------------------------------------------------- |
| Summary / Overview      | Big-picture architecture summary                            |
| Strategic               | Goals, drivers, capabilities, mission outcomes              |
| Operational             | Operational performers, activities, information exchanges   |
| Services                | Service providers, consumers, interfaces, service functions |
| Personnel               | People, organizations, roles, skills                        |
| Resources / Systems     | Systems, components, resources, functions, interfaces       |
| Security                | Assets, threats, controls, security constraints             |
| Project                 | Roadmaps, milestones, transitions                           |
| Standards               | Standards, rules, policies, technical profiles              |
| Actual Resources        | Real fielded instances, organizations, deployed assets      |
| Architecture Management | Metadata, assumptions, versions, governance                 |

## SysML v1 diagram families

SysML v1 is often summarized as having these major diagram types:

| SysML diagram            | Primary use                                |
| ------------------------ | ------------------------------------------ |
| Requirement diagram      | Requirements and relationships             |
| Use case diagram         | System uses and external actors            |
| Activity diagram         | Functional behavior and flows              |
| Sequence diagram         | Interactions over time                     |
| State machine diagram    | State/event behavior                       |
| Block definition diagram | Structural decomposition and relationships |
| Internal block diagram   | Internal parts, ports, connectors, flows   |
| Parametric diagram       | Constraints/equations for analysis         |
| Package diagram          | Model organization                         |

## SysML v2 model emphasis

SysML v2 keeps the broad MBSE purpose but improves semantic precision, consistency, interoperability, and textual/graphical usability. OMG describes SysML v2 as representing requirements, structure, behavior, analysis cases, and verification cases. ([OMG][5])

A practical SysML v2-oriented grouping:

| SysML v2 concern   | Typical content                                   |
| ------------------ | ------------------------------------------------- |
| Requirements       | Requirement definitions/usages, constraints       |
| Structure          | Parts, items, ports, connections                  |
| Behavior           | Actions, states, interactions                     |
| Interfaces         | Ports, items, flows, messages                     |
| Analysis           | Constraints, calculations, trade studies          |
| Verification       | Verification cases, test cases, evidence links    |
| Packages           | Namespaces, libraries, model organization         |
| Views / viewpoints | Stakeholder-oriented projections of model content |

---

# 22. Cross-view “master hierarchy” of model types

Here is a consolidated hierarchy you can use as a checklist.

```text
Systems Engineering / Architecture Models
│
├── 1. Intent and Strategy
│   ├── Mission model
│   ├── Goal/objective hierarchy
│   ├── Capability map
│   ├── Business motivation model
│   ├── Value stream
│   └── Roadmap
│
├── 2. Context and Stakeholders
│   ├── System context diagram
│   ├── Stakeholder map
│   ├── Domain model
│   ├── Environment model
│   ├── External systems diagram
│   └── Concern/viewpoint matrix
│
├── 3. Operational Architecture
│   ├── Operational context
│   ├── Operational node/performer model
│   ├── Operational activity model
│   ├── Operational scenario / mission thread
│   ├── Operational state model
│   ├── Operational information exchange
│   ├── Organization/role model
│   └── Business process model
│
├── 4. Requirements and Measures
│   ├── Stakeholder needs model
│   ├── Requirement hierarchy
│   ├── Requirement diagram
│   ├── Measures model: MOE/MOP/TPM/KPI
│   ├── Constraint model
│   └── Compliance matrix
│
├── 5. Functional / Logical Architecture
│   ├── Functional decomposition
│   ├── FFBD / EFFBD
│   ├── IDEF0
│   ├── Activity model
│   ├── Data flow model
│   ├── Logical component model
│   └── Function allocation model
│
├── 6. Behavior and Dynamics
│   ├── Sequence diagram
│   ├── State machine
│   ├── Timing diagram
│   ├── Event trace
│   ├── Mode model
│   ├── Petri net
│   ├── Discrete-event simulation
│   ├── System dynamics
│   └── Agent-based model
│
├── 7. Information / Data Architecture
│   ├── Conceptual data model
│   ├── Logical data model
│   ├── Physical data model
│   ├── Ontology
│   ├── Data dictionary
│   ├── Data flow diagram
│   ├── Information exchange matrix
│   └── Data governance model
│
├── 8. Service Architecture
│   ├── Service catalog
│   ├── Service context
│   ├── Service interface
│   ├── API model
│   ├── Event model
│   ├── Service orchestration
│   ├── Service choreography
│   └── SLA/SLO model
│
├── 9. Physical / Resource Architecture
│   ├── System breakdown structure
│   ├── Block definition diagram
│   ├── Internal block diagram
│   ├── Component diagram
│   ├── Deployment diagram
│   ├── Network topology
│   ├── Mechanical/electrical layout
│   ├── BOM
│   └── Physical interface model
│
├── 10. Interfaces and Integration
│   ├── Interface context
│   ├── ICD
│   ├── N² diagram
│   ├── Interface matrix
│   ├── Protocol model
│   ├── Message schema
│   ├── API contract
│   └── Integration dependency graph
│
├── 11. Analysis and Trade Studies
│   ├── Parametric model
│   ├── Budget model
│   ├── Trade space
│   ├── Trade study matrix
│   ├── Optimization model
│   ├── Monte Carlo model
│   ├── Reliability block diagram
│   ├── Performance simulation
│   └── Cost/schedule/risk model
│
├── 12. Safety, Security, and Assurance
│   ├── Hazard analysis
│   ├── FTA
│   ├── ETA
│   ├── FMEA/FMECA
│   ├── STPA
│   ├── Bow-tie
│   ├── Threat model
│   ├── Attack tree
│   ├── Security architecture
│   ├── Safety/security case
│   └── Compliance model
│
├── 13. Verification and Validation
│   ├── Verification matrix
│   ├── Test case model
│   ├── Verification case
│   ├── Validation scenario
│   ├── Test architecture
│   ├── Test sequence
│   ├── Coverage model
│   └── Qualification model
│
├── 14. Deployment, Operations, and Sustainment
│   ├── Deployment architecture
│   ├── Installation model
│   ├── Maintenance model
│   ├── Logistics support model
│   ├── Configuration model
│   ├── Monitoring model
│   ├── Incident response model
│   └── Decommissioning model
│
└── 15. Governance and Lifecycle
    ├── WBS/PBS/SBS
    ├── Integrated master schedule
    ├── Risk model
    ├── Decision log / ADRs
    ├── Standards profile
    ├── Architecture roadmap
    ├── Baseline/configuration model
    └── Portfolio model
```

---

# 23. How the major views relate

A common systems-engineering flow looks like this:

```text
Mission / business goals
        ↓
Capabilities
        ↓
Operational activities and scenarios
        ↓
System requirements and measures
        ↓
Functions / logical architecture
        ↓
Behavior models
        ↓
Physical / software / human / service architecture
        ↓
Interfaces and allocations
        ↓
Analysis, safety, security, trades
        ↓
Verification and validation
        ↓
Deployment, operations, sustainment
```

In practice, this is iterative. Physical constraints may force functional changes; safety analysis may create new requirements; verification planning may reveal ambiguous requirements; operational scenarios may expose missing interfaces.

---

# 24. “Which diagram should I use?” by question

| Question                                | Best-fit models                                           |
| --------------------------------------- | --------------------------------------------------------- |
| Why does the system exist?              | Mission model, goal tree, business motivation model       |
| What capability gap are we closing?     | Capability map, gap analysis, roadmap                     |
| Who uses or touches the system?         | Stakeholder map, context diagram, use case diagram        |
| What happens operationally?             | Operational activity, BPMN, mission thread, sequence      |
| What must the system do?                | Requirements, functional decomposition, activity diagram  |
| How does the system behave over time?   | State machine, sequence, timing, mode model               |
| What data moves through the system?     | DFD, information exchange matrix, data model              |
| What services are exposed?              | Service catalog, API model, service dependency diagram    |
| What is the system made of?             | BDD, IBD, component diagram, deployment diagram           |
| How do parts connect?                   | Interface diagram, N², ICD, port/connector model          |
| Which part satisfies which requirement? | Traceability matrix, allocation matrix                    |
| How do we know it works?                | Verification matrix, test case model, validation scenario |
| What can go wrong?                      | FMEA, FTA, STPA, threat model, attack tree                |
| How well will it perform?               | Parametric model, simulation, trade study, budget         |
| How is it deployed and maintained?      | Deployment, maintenance, logistics, configuration models  |
| How will it evolve?                     | Roadmap, migration model, project view, standards profile |

---

# 25. Minimal “complete architecture package” for a serious system

For many engineered systems, a practical baseline set is:

1. **Mission / capability model**
2. **System context diagram**
3. **Stakeholder needs and requirements model**
4. **Operational scenarios / mission threads**
5. **Functional decomposition or activity model**
6. **Logical architecture**
7. **Physical architecture / block structure**
8. **Interface model / ICD / N² diagram**
9. **Behavior models: state + sequence + mode model**
10. **Data/information exchange model**
11. **Allocation and traceability matrix**
12. **Performance budgets and parametric analyses**
13. **Safety/security/risk models**
14. **Verification and validation model**
15. **Deployment, operations, and sustainment model**
16. **Roadmap and configuration/baseline model**

That set gives coverage across **why, who, what, how, with what, how well, how safely, how verified, and how sustained**.

Below are engagement questions for each of the **17 top-level systems engineering / systems architecture views** from earlier.

These are the kinds of questions stakeholders, architects, engineers, reviewers, operators, testers, and decision-makers ask when inspecting or creating each view.

---

[1]: https://standards.ieee.org/ieee/42010/5334/? "IEEE/ISO/IEC 42010-2011"
[2]: https://www.omg.org/spec/SysML/2.0/About-SysML? "About the OMG System Modeling Language Specification ..."
[3]: https://www.omg.org/spec/UAF/1.3/About-UAF? "About the Unified Architecture Framework Specification ..."
[4]: https://ac.cto.mil/wp-content/uploads/2025/01/U-Mission-Architecture-Style-Guide-Final_07Jan2025.pdf? "Mission Architecture Style Guide"
[5]: https://www.omg.org/sysml/sysmlv2/? "SysML® v2 Specification"
[6]: https://www.omg.org/uaf/? "Unified Architecture Framework® (UAF®)"
