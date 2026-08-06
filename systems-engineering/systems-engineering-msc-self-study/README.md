# Systems Engineering MSc Self-Study

**Release:** Version 1.0.0  
**Status:** Curriculum specification complete; ready for controlled piloting  
**Last audited:** 2026-08-05

This repository is an independent, self-directed systems-engineering curriculum inspired by publicly available Johns Hopkins Engineering for Professionals course descriptions and syllabi. It organizes 20 courses into a coherent prerequisite sequence and expands each course into a 12-week plan with readings, worked examples, guided and independent practice, deliverables, rubrics, mastery gates, formal reviews, and a portfolio handoff.

The curriculum is intended for serious professional development. It is not affiliated with Johns Hopkins University, does not reproduce university instruction, and does not confer academic credit, enrollment status, certification, or an accredited degree.

---

## Curriculum structure

The curriculum is organized into six phases. Each phase has its own overview and each course has a separate Markdown file containing its course information, readings, references, exercises, deliverables, rubrics, and other instructional material.

| Phase | Focus | Courses |
|---|---|---:|
| [Phase 0](phase-0/README.md) | Foundations, readiness, prerequisites, and sequencing | 2 |
| [Phase 1](phase-1/README.md) | Modeling languages and software-intensive systems | 3 |
| [Phase 2](phase-2/README.md) | Core systems-development lifecycle | 3 |
| [Phase 3](phase-3/README.md) | Quantitative analysis and model-driven decision support | 6 |
| [Phase 4](phase-4/README.md) | Agile, digital, mission, and process-centered engineering | 3 |
| [Phase 5](phase-5/README.md) | Systems of systems, enterprises, and complex systems | 3 |

## How to use this repository

1. Begin with [Phase 0](phase-0/README.md), review the prerequisite policy and readiness gates, and follow the recommended sequence.
2. Read the `README.md` at the start of each phase before beginning its courses.
3. Complete each course from its own Markdown file. Maintain the specified artifacts, revision history, decision records, and portfolio evidence.
4. Use the program competency map below to understand how repeated subjects increase in independence, integration, complexity, and evidentiary rigor.
5. Use the reusable templates as the maintenance standard when revising a course, adding a new case, or replacing a reading, tool, exercise, or assessment.

> This is a self-study curriculum. It does not confer university credit, enrollment status, certification, or an academic-equivalency waiver.

---

## Release and implementation documents

- [Program-wide quality audit](PROGRAM-AUDIT.md)
- [Pilot and implementation guide](PILOT-GUIDE.md)
- [Release notes](RELEASE-NOTES.md)
- [Phase 0 OOP readiness bridge](phase-0/oop-readiness-bridge.md)
- [Phase 0 quantitative and computational bridge](phase-0/quantitative-and-computational-bridge.md)

## Planning assumptions

The full curriculum contains **20 courses and 240 instructional weeks**. Most courses target roughly **8–13 hours per week**, with additional time for tool setup, debugging, review preparation, revision, and optional stretch work. A reasonable planning range for the full program is approximately **2,400–3,000 hours**, excluding prerequisite remediation and extended project work.

For a first implementation:

- study one course at a time unless a phase README explicitly permits parallel work and you have enough time to preserve review and configuration discipline;
- schedule at least one recovery and portfolio-consolidation week between courses;
- schedule two to four consolidation weeks between phases;
- treat the weekly workload as a pilot estimate and record actual hours;
- do not claim course or program completion until critical mastery criteria and required revisions are closed.

---

## Current expansion status

| Course | Status | Last major revision |
|---|---|---|
| EN.645.662 Introduction to Systems Engineering | Fully expanded | 2026-08-05 |
| EN.645.667 Management of Systems Projects | Fully expanded | 2026-08-05 |
| EN.645.631 Introduction to Model Based Systems Engineering | Fully expanded | 2026-08-05 |
| EN.605.704 Object-Oriented Analysis and Design | Fully expanded | 2026-08-05 |
| EN.645.764 Software Systems Engineering | Fully expanded | 2026-08-05 |
| EN.645.767 System Conceptual Design | Fully expanded | 2026-08-05 |
| EN.645.768 System Design & Integration | Fully expanded | 2026-08-05 |
| EN.645.769 System Test & Evaluation | Fully expanded | 2026-08-05 |
| EN.645.757 Foundations of Modeling and Simulation | Fully expanded | 2026-08-05 |
| EN.645.784 Decision Science & Analytics | Fully expanded | 2026-08-05 |
| EN.645.781 Systems Thinking and Systems Dynamics | Fully expanded | 2026-08-05 |
| EN.645.756 Metrics, Modeling, and Simulation | Fully expanded | 2026-08-05 |
| EN.645.632 Applied Analytics for MBSE | Fully expanded | 2026-08-05 |
| EN.645.758 Advanced Systems Modeling and Simulation | Fully expanded | 2026-08-05 |
| EN.645.780 Agile Systems Engineering | Fully expanded | 2026-08-05 |
| EN.645.782 Foundations of Digital and Mission Engineering | Fully expanded | 2026-08-05 |
| EN.645.783 Systems Engineering Process Improvement | Fully expanded | 2026-08-05 |
| EN.645.771 System of Systems Engineering | Fully expanded | 2026-08-05 |
| EN.645.753 Enterprise Systems Engineering | Fully expanded | 2026-08-05 |
| EN.645.742 Management of Complex Systems | Fully expanded | 2026-08-05 |

“Fully expanded” means the course has a complete course specification, detailed weekly outcomes and resources, worked examples, guided and independent practice, deliverable specifications, rubrics, mastery gates, review events, and a capstone.

---

## Program-level competency map

The competency map defines what the complete curriculum is intended to produce. It will govern the later expansion of course outcomes, weekly readings, exercises, assessments, and capstones. A repeated topic should not simply be taught again; it should move the learner to a higher level of independence, integration, complexity, or evidentiary rigor.

### Competency-development levels

* **I — Introduce:** explain the concepts, follow a worked method, and complete a bounded exercise with guidance.
* **D — Develop:** apply the competency independently to a realistic problem, compare alternatives, and justify decisions.
* **A — Advanced integration and assessment:** integrate the competency with other disciplines, work under uncertainty or organizational constraints, critique evidence, and defend conclusions in a formal review.

These codes describe each course's intended contribution. They do not by themselves prove mastery; mastery requires acceptable portfolio evidence and successful assessment.

### Program competencies and outcomes

#### C1 — Systems thinking, context, and lifecycle reasoning

Graduates of the self-study program should be able to:

* define a system of interest, its boundary, environment, lifecycle, stakeholders, and neighboring systems;
* reason across technical, human, organizational, operational, and lifecycle perspectives;
* identify feedback, delays, emergence, adaptation, and unintended consequences;
* select and tailor lifecycle approaches to the system, risk, and organizational context.

#### C2 — Stakeholder needs, operational analysis, and requirements

Graduates should be able to:

* elicit and structure stakeholder needs, objectives, constraints, and acceptance expectations;
* develop a concept of operations, mission threads, use cases, and nominal and off-nominal scenarios;
* formulate clear, singular, feasible, necessary, traceable, and verifiable requirements;
* derive and manage requirements across levels and assess coverage, conflict, volatility, and change impact.

#### C3 — Architecture, design, allocation, and interfaces

Graduates should be able to:

* develop logical, functional, physical, software, and operational architecture views;
* allocate requirements, functions, behaviors, and performance to system elements;
* identify, specify, control, and verify interfaces;
* evaluate architecture alternatives and maintain consistency across design viewpoints and baselines.

#### C4 — Model-based and digital engineering

Graduates should be able to:

* distinguish methodology, modeling language, model, simulation, tool, and repository;
* construct and maintain coherent UML/SysML-style requirements, structure, behavior, interface, allocation, and verification models;
* query models for traceability, coverage, consistency, and decision support;
* connect descriptive models, analytic models, digital threads, digital twins, and collaborative engineering environments.

#### C5 — Software-intensive systems engineering

Graduates should be able to:

* perform object-oriented requirements analysis, domain modeling, design, and responsibility assignment;
* evaluate software architectures for quality attributes and system-level alignment;
* reason about distributed, real-time, configurable, secure, networked, and maintainable software;
* plan implementation, version control, CI/CD, testing, operations, maintenance, and technical-debt management.

#### C6 — Integration, verification, validation, and test and evaluation

Graduates should be able to:

* distinguish verification, validation, qualification, acceptance, demonstration, and operational evaluation;
* develop integration strategies, build-up sequences, entry and exit criteria, and readiness evidence;
* construct verification cross-reference matrices, test plans, procedures, instrumentation strategies, and discrepancy workflows;
* analyze test results, uncertainty, deficiencies, and residual risk to make defensible readiness recommendations.

#### C7 — Modeling, simulation, and dynamic behavior

Graduates should be able to:

* formulate conceptual models and select appropriate analytic or simulation approaches;
* implement and interpret discrete, continuous, stochastic, dynamic, and multi-domain models;
* represent feedback, stocks and flows, delays, nonlinearities, and policy resistance;
* verify, validate, document, compose, and responsibly reuse models and simulations.

#### C8 — Metrics, statistics, experiments, and uncertainty

Graduates should be able to:

* define meaningful MOEs, MOPs, KPPs, TPMs, leading indicators, and decision-focused metrics;
* characterize inputs and outputs probabilistically and apply appropriate descriptive and inferential methods;
* design experiments, collect and analyze data, and recognize confounding, bias, and limits of inference;
* perform sensitivity, uncertainty, robustness, and error analyses and communicate their implications.

#### C9 — Decision analysis, trade-space exploration, affordability, and risk

Graduates should be able to:

* structure objectives, value measures, alternatives, constraints, dependencies, and decision criteria;
* perform qualitative and quantitative trade studies, multiobjective analysis, Pareto reasoning, and sensitivity analysis;
* integrate technical performance, cost, schedule, opportunity, and risk into decisions;
* document assumptions, rationale, uncertainty, and the conditions under which a recommendation would change.

#### C10 — Technical management, agile execution, and process improvement

Graduates should be able to:

* plan and govern technical work using systems engineering management plans, work breakdowns, schedules, reviews, metrics, configuration control, and decision records;
* integrate risk, issue, opportunity, supplier, customer, and change management into engineering execution;
* tailor incremental, agile, Lean, DevSecOps, and evidence-driven practices to software-intensive and cyber-physical systems;
* define, measure, analyze, redesign, implement, control, and sustain systems-engineering processes.

#### C11 — Mission, system-of-systems, enterprise, and complexity engineering

Graduates should be able to:

* distinguish a system of systems, enterprise, and complex adaptive system from a large single system;
* analyze interoperability, information flow, capability dependencies, mission threads, decentralized authority, and evolutionary development;
* reason about governance, incentives, organizational boundaries, conflicting objectives, resilience, and legacy constraints;
* develop interventions that acknowledge emergence, uncertainty, adaptation, and possible unintended consequences.

#### C12 — Technical communication, collaboration, and professional judgment

Graduates should be able to:

* produce clear, reviewable technical models, analyses, plans, reports, briefings, and decision records;
* tailor communication to decision-makers, customers, operators, specialists, and reviewers;
* conduct and respond to technical reviews, critiques, red-team challenges, and oral defenses;
* make assumptions and limitations explicit and distinguish evidence, inference, judgment, and unresolved uncertainty.

### Course-to-competency contribution matrix

| Course | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EN.645.662 Introduction to Systems Engineering | I | I | I | — | — | I | — | I | I | I | — | I |
| EN.645.667 Management of Systems Projects | D | — | — | — | — | — | — | D | D | I | — | D |
| EN.645.631 Introduction to MBSE | D | D | D | I | — | D | — | — | — | — | — | D |
| EN.605.704 Object-Oriented Analysis and Design | — | D | D | I | I | — | — | — | — | — | — | D |
| EN.645.764 Software Systems Engineering | D | D | D | D | A | D | — | D | D | D | — | D |
| EN.645.767 System Conceptual Design | D | A | D | D | — | I | — | D | A | D | — | A |
| EN.645.768 System Design & Integration | D | D | A | D | D | D | — | — | D | A | — | A |
| EN.645.769 System Test & Evaluation | D | D | D | D | D | A | — | D | D | D | — | A |
| EN.645.757 Foundations of Modeling and Simulation | D | — | — | — | — | D | I | I | D | — | — | D |
| EN.645.784 Decision Science & Analytics | D | D | — | — | — | — | D | D | A | — | — | D |
| EN.645.781 Systems Thinking and Systems Dynamics | A | — | — | — | — | — | A | D | D | — | D | D |
| EN.645.756 Metrics, Modeling, and Simulation | D | — | D | — | — | D | A | A | A | — | — | D |
| EN.645.632 Applied Analytics for MBSE | D | D | D | A | — | D | D | A | A | — | — | A |
| EN.645.758 Advanced Systems Modeling and Simulation | D | — | D | — | — | D | A | A | D | — | D | A |
| EN.645.780 Agile Systems Engineering | D | D | D | D | D | D | — | D | D | A | — | A |
| EN.645.782 Foundations of Digital and Mission Engineering | D | D | D | A | — | D | D | D | D | D | A | A |
| EN.645.783 Systems Engineering Process Improvement | D | — | — | D | — | — | D | A | D | A | D | A |
| EN.645.771 System of Systems Engineering | A | D | A | D | — | D | D | D | D | D | A | A |
| EN.645.753 Enterprise Systems Engineering | A | D | D | D | — | — | D | D | D | D | A | A |
| EN.645.742 Management of Complex Systems | A | D | D | — | — | — | A | D | A | D | A | A |

### Competency ownership and culminating evidence

Each competency has several contributing courses, but the following courses carry primary responsibility for advanced evidence:

| Competency | Primary advanced courses | Minimum culminating evidence |
|---|---|---|
| C1 Systems thinking and lifecycle | 645.781, 645.771, 645.753, 645.742 | Context and lifecycle analysis that explains feedback, emergence, organizational constraints, and intervention risks |
| C2 Needs, operations, requirements | 645.767, 645.632 | Traced needs-to-requirements baseline with operational scenarios, quality audit, coverage analysis, and change rationale |
| C3 Architecture and interfaces | 645.768, 645.771 | Multi-view architecture baseline, interface-control package, allocation rationale, and consistency review |
| C4 Model-based and digital engineering | 645.632, 645.782 | Queryable model baseline connected to analytic evidence and a defined digital thread |
| C5 Software-intensive systems | 645.764 | Software systems package covering architecture, quality attributes, lifecycle, CI/CD, test, operations, and maintenance |
| C6 Integration and T&E | 645.769 | Integration and T&E package with traceability, procedures, evidence analysis, discrepancies, and readiness recommendation |
| C7 Modeling and simulation | 645.756, 645.758, 645.781 | Verified and validated model or simulation with assumptions, data, experiments, uncertainty, and interpretation |
| C8 Metrics and uncertainty | 645.756, 645.632, 645.758 | Metric hierarchy, experimental or observational analysis, uncertainty/sensitivity results, and decision implications |
| C9 Decisions, trades, and risk | 645.767, 645.784, 645.756 | Reproducible trade-space analysis with value structure, risk, affordability, uncertainty, and sensitivity |
| C10 Technical management and process | 645.768, 645.780, 645.783 | Executable technical-management or process-improvement plan with measures, governance, and sustainment controls |
| C11 Mission, SoS, enterprise, complexity | 645.771, 645.753, 645.742 | Mission/enterprise analysis addressing interoperability, governance, evolution, resilience, and unintended consequences |
| C12 Communication and judgment | All courses; advanced reviews in Phases 2–5 | Written technical report, review briefing, decision record, critique response, and recorded oral defense |

### Portfolio checkpoints by phase

**Phase 0 checkpoint**

* lifecycle and technical-process map;
* stakeholder/requirements/architecture/V&V concept diagnostic;
* project plan, risk register, configuration baseline, and decision log;
* passed OOP and quantitative gates where applicable.

**Phase 1 checkpoint**

* coherent MBSE baseline;
* OO analysis and design package;
* software architecture and lifecycle package showing alignment with the larger system.

**Phase 2 checkpoint**

* one continuously developed case moving from needs and ConOps through concept selection, design, interfaces, integration, verification, validation, and test evidence;
* formal concept, design, integration, and test-readiness reviews.

**Phase 3 checkpoint**

* reproducible analytic notebooks or models;
* verified and validated simulations;
* metrics, experiments, uncertainty analysis, and decision-support products connected to the Phase 2 case.

**Phase 4 checkpoint**

* incremental delivery and evidence strategy;
* digital thread or digital-twin concept tied to authoritative data and models;
* assessed current-state process and governed future-state improvement plan.

**Phase 5 checkpoint**

* system-of-systems mission-thread and interoperability analysis;
* enterprise capability, governance, and dependency model;
* complexity-aware intervention or resilience strategy with explicit uncertainties and possible unintended consequences.

### Rules for using the competency map during course expansion

1. Every course will receive six to ten measurable course learning outcomes linked to the program competencies.
2. Every week will identify the specific competency and development level it addresses.
3. A topic repeated across courses must increase at least one of: independence, system scale, uncertainty, quantitative rigor, integration, stakeholder complexity, or evidentiary burden.
4. Every major competency must have guided practice, independent practice, feedback, and a scored culminating artifact.
5. Course completion requires both an acceptable aggregate score and satisfaction of critical rubric criteria; strong performance in one area cannot compensate for missing critical traceability, safety, verification, or evidence requirements.
6. Portfolio artifacts should be reused and revised across courses rather than recreated without connection.

---

---

## Reusable instructional design templates

The templates in this section are the required structure for every course and every instructional week added or revised in this curriculum. They are intended to make the program teachable, assessable, and internally consistent rather than merely adding more reading links or assignments.

The templates should be adapted to the subject matter, but sections should not be removed without a stated reason. A course may add specialized sections—for example, laboratory safety, simulation accreditation, coding standards, or model configuration rules—when its discipline requires them.

### Template-use rules

1. Link every course learning outcome to one or more program competencies and to the intended **I**, **D**, or **A** development level.
2. Link every graded assignment and capstone criterion to at least one course learning outcome.
3. Assign exact chapters, sections, standards clauses, videos, tutorials, or tool procedures wherever possible; do not assign an entire handbook without guidance.
4. Include at least one worked example and one guided exercise before independent work on every major new method.
5. Require revision after feedback for at least two substantial artifacts in every course.
6. Reuse the program case and prior-course artifacts whenever that produces authentic lifecycle continuity.
7. Distinguish **required**, **recommended**, **reference**, and **advanced** resources.
8. State the evidence needed to complete a week and the evidence needed to pass the course.
9. Provide solutions, reference rationales, automated checks, or detailed rubrics for every assessed activity.
10. Keep nominal workload near **8–10 hours per week** unless a course explicitly declares a different expectation.

---

### Reusable course template

Copy this structure when creating or rebuilding a course.

#### [Course code] — [Course title]

**Credits or equivalent effort:** [For example, 3 credits / approximately 120 total hours]
**Nominal duration:** [For example, 12 weeks]
**Recommended weekly effort:** [For example, 8–10 hours]
**Curriculum phase:** [Phase number and name]
**Course type:** [Foundation / lifecycle core / quantitative / digital / enterprise / other]
**Primary program case:** [Case name or instructions for selecting one]

##### 1. Course purpose and professional context

[Explain in two to four paragraphs what professional problems this course prepares the learner to solve, where the work appears in the system lifecycle, and how the course differs from adjacent courses. Identify the decisions, artifacts, or reviews for which the learner will become responsible.]

##### 2. Source description and scope

**Source course description**

> [Preserve the source description or catalog language here.]

**Self-study interpretation**

[Explain what is included, what is intentionally excluded, and how the source description has been translated into a self-study course. Clearly identify any additions made to support prerequisites, practical work, or assessment.]

##### 3. Relationship to the curriculum

**Builds on**

* [Prior course, competency, or portfolio artifact]
* [Prior course, competency, or portfolio artifact]

**Prepares for**

* [Later course, competency, or review]
* [Later course, competency, or review]

**Artifact continuity**

[Identify which prior artifacts will be imported, revised, placed under configuration control, or extended. Identify the outputs that later courses will reuse.]

##### 4. Prerequisites and readiness assessment

**Required prior courses or competencies**

* [Prerequisite]
* [Prerequisite]

**Recommended preparation**

* [Preparation]
* [Preparation]

**Required tools and access**

* [Software, handbook, standard, repository, computing environment, modeling tool, or equipment]

**Readiness diagnostic**

[Provide a 30–90 minute diagnostic with knowledge questions and one small performance task. State the passing standard and the bridge work required when the standard is not met.]

##### 5. Course learning outcomes

By the end of the course, the learner will be able to:

| ID | Measurable course learning outcome | Program competency | Level | Primary assessment evidence |
|---|---|---|:---:|---|
| CLO-1 | [Observable outcome using formulate, construct, analyze, evaluate, implement, validate, defend, or critique] | [C#] | [I/D/A] | [Artifact or assessment] |
| CLO-2 | [Outcome] | [C#] | [I/D/A] | [Artifact or assessment] |
| CLO-3 | [Outcome] | [C#] | [I/D/A] | [Artifact or assessment] |
| CLO-4 | [Outcome] | [C#] | [I/D/A] | [Artifact or assessment] |
| CLO-5 | [Outcome] | [C#] | [I/D/A] | [Artifact or assessment] |
| CLO-6 | [Outcome] | [C#] | [I/D/A] | [Artifact or assessment] |

Use six to ten outcomes. Together they must cover the complete source description and the major capstone expectations.

##### 6. Essential questions

[List three to six questions that organize the course and recur across several weeks. These should frame professional judgment rather than test isolated definitions.]

Examples:

* What evidence is sufficient to justify this engineering decision?
* How does uncertainty affect the recommended architecture or plan?
* Which assumptions are carrying the most decision risk?
* How will this artifact remain consistent with the rest of the technical baseline?

##### 7. Running case, datasets, and problem environment

**Case brief**

[Describe the system, mission, stakeholders, environment, constraints, available information, and initial uncertainties.]

**Provided materials**

* [Case brief]
* [Data files]
* [Initial requirements or models]
* [Templates]
* [Deliberately defective artifacts for review exercises]

**Configuration rules**

[Define file naming, versioning, repository structure, decision-log practice, baseline labels, and change-control expectations.]

**Alternate case policy**

[State whether the learner may substitute another case and what properties it must have.]

##### 8. Resource architecture

**Primary teaching resource**

* [Book, handbook, open course, or other coherent backbone]

**Authoritative standards and guidance**

* [Standard or guide]
* [Standard or guide]

**Practical and tool resources**

* [Tutorial or documentation]
* [Worked-example source]

**Case and failure-analysis resources**

* [Case study]
* [Incident, review, or lessons-learned source]

**Advanced references**

* [Optional deeper source]

For each weekly assignment, identify exact sections and state why the learner is reading them. Resource lists are not substitutes for assigned readings.

##### 9. Tool stack and technical setup

| Tool or environment | Purpose | Required or optional | Setup evidence |
|---|---|:---:|---|
| [Tool] | [Purpose] | [Required/Optional] | [Screenshot, test file, executed notebook, exported model, etc.] |
| [Tool] | [Purpose] | [Required/Optional] | [Evidence] |

Include installation or access instructions, free alternatives where practical, file formats, interoperability constraints, and a short setup verification activity.

##### 10. Instructional and assessment strategy

The course should use a repeated learning cycle:

1. prerequisite retrieval and diagnostic;
2. focused instruction and assigned reading;
3. worked example;
4. guided practice;
5. independent application;
6. feedback or comparison with reference evidence;
7. revision and reflection;
8. incorporation into the controlled course baseline.

**Default assessment structure**

| Assessment category | Suggested weight | Purpose |
|---|---:|---|
| Weekly knowledge checks and retrieval practice | 10% | Confirm terminology, concepts, and method selection |
| Guided laboratories or method exercises | 15% | Build procedural accuracy before independent work |
| Independent weekly applications | 20% | Apply methods to the running case |
| Technical memos, analyses, or model reviews | 15% | Develop argumentation, interpretation, and communication |
| Midcourse integration review | 15% | Test cross-week consistency and identify gaps early |
| Final capstone and oral defense | 25% | Demonstrate integrated, independent course mastery |

Adjust the weights when necessary, but preserve a balance among knowledge, method execution, integration, communication, and defense of judgment.

##### 11. Weekly course map

| Week | Topic and essential question | Competencies and level | Principal method or artifact | Major evidence |
|---:|---|---|---|---|
| 1 | [Topic] | [C#, I/D/A] | [Method/artifact] | [Evidence] |
| 2 | [Topic] | [C#, I/D/A] | [Method/artifact] | [Evidence] |
| 3 | [Topic] | [C#, I/D/A] | [Method/artifact] | [Evidence] |
| 4 | [Topic] | [C#, I/D/A] | [Method/artifact] | [Evidence] |
| 5 | [Topic] | [C#, I/D/A] | [Method/artifact] | [Evidence] |
| 6 | **Midcourse integration and diagnostic review** | [Multiple] | [Integrated review] | [Corrective-action plan] |
| 7 | [Topic] | [C#, I/D/A] | [Method/artifact] | [Evidence] |
| 8 | [Topic] | [C#, I/D/A] | [Method/artifact] | [Evidence] |
| 9 | [Topic] | [C#, I/D/A] | [Method/artifact] | [Evidence] |
| 10 | **Complex case, failure analysis, or red-team exercise** | [Multiple] | [Critique/recovery] | [Findings and revised baseline] |
| 11 | **Capstone review and revision** | [Multiple] | [Formal review] | [Dispositioned review record] |
| 12 | **Final synthesis, defense, and retrospective** | [Multiple] | [Capstone] | [Final baseline and oral defense] |

This rhythm is a default, not an inflexible topic schedule. Weeks 6, 10, 11, and 12 should normally consolidate and assess rather than introduce several unrelated new methods.

##### 12. Major assignments and review gates

For each major assignment, provide a complete specification using the weekly deliverable format below.

| Assignment or review | Due | Outcomes assessed | Inputs | Required outputs | Feedback and revision |
|---|---:|---|---|---|---|
| [Assignment] | [Week] | [CLOs] | [Inputs] | [Outputs] | [Process] |
| Midcourse integration review | 6 | [CLOs] | [Baseline] | [Review package and corrective actions] | Required revision |
| Capstone review | 11 | [CLOs] | [Draft capstone] | [Briefing, findings, dispositions] | Required revision |
| Final capstone and defense | 12 | [CLOs] | [Revised baseline] | [Final package and recorded defense] | Final evaluation |

##### 13. Feedback and self-evaluation plan

Every course must use at least three feedback mechanisms:

* detailed analytic rubrics;
* worked solutions or reference rationales;
* automated tests, model queries, calculations, or validation datasets where applicable;
* structured self-review checklists;
* peer or professional-community review where available;
* recorded explanation followed by self-critique;
* red-team review from a different stakeholder or disciplinary perspective.

State when feedback is received, which artifacts must be revised, and how revision quality affects the score.

##### 14. Standard course rubric

Tailor the descriptors to the discipline while retaining the common dimensions.

| Dimension | Exemplary | Proficient | Developing | Insufficient |
|---|---|---|---|---|
| Technical correctness | Methods and results are correct; limitations are handled explicitly | Minor errors do not alter the conclusion | Several errors or weak method execution affect confidence | Fundamental errors invalidate the work |
| Completeness and scope | All required elements and relevant edge cases are addressed | Required elements are present with small omissions | Important elements are incomplete | Major required elements are missing |
| Traceability and consistency | Claims and artifacts are fully traceable and mutually consistent | Traceability is substantially complete | Multiple orphaned or inconsistent elements remain | Critical trace chains are absent or contradictory |
| Assumptions, uncertainty, and rationale | Assumptions and uncertainty are explicit; decisions are strongly justified | Main assumptions and rationale are stated | Rationale is thin or assumptions are partly hidden | Conclusions are unsupported or misleading |
| Evidence and verification | Evidence is appropriate, reproducible, and sufficient for the claim | Evidence generally supports the claim | Evidence is incomplete or weakly matched | Evidence is absent or does not support the claim |
| Communication and configuration quality | Clear, audience-appropriate, reviewable, and under effective configuration control | Understandable and organized with minor defects | Ambiguous, difficult to review, or inconsistently controlled | Unclear, disorganized, or not reproducible |

##### 15. Critical criteria and mastery gates

A learner cannot pass the course through point accumulation alone. Define the noncompensable criteria for the subject.

**Default critical criteria**

* no unsupported safety-, mission-, or acceptance-critical conclusion;
* no unresolved contradiction in the controlled technical baseline;
* no critical requirement, interface, model result, or decision without appropriate traceability;
* no fabricated, unacknowledged, or irreproducible evidence;
* all mandatory review findings dispositioned or explicitly accepted as residual risk.

**Recommended completion standard**

* at least **80% overall**;
* at least **70% in each major assessment category**;
* all critical criteria satisfied;
* capstone rated at least **Proficient** on every critical rubric dimension;
* successful oral defense demonstrating that the learner personally understands and can justify the submitted work.

##### 16. Capstone specification

**Capstone problem**

[State the realistic engineering problem, decision, or review being addressed.]

**Required inputs**

* [Inputs]

**Required outputs**

* [Models, analyses, plans, procedures, results, report, briefing, repository, or other evidence]

**Required consistency checks**

* [Cross-artifact checks]
* [Coverage or trace queries]
* [Independent calculation or validation]

**Review format**

[Define a concept review, architecture review, model V&V review, test-readiness review, decision review, process review, or comparable event.]

**Oral defense prompts**

[Provide eight to twelve questions probing assumptions, method selection, evidence, alternatives, uncertainty, limitations, and conditions that would change the recommendation.]

##### 17. Portfolio and course-exit package

The final retained package should include:

* controlled final artifact baseline;
* key intermediate versions showing revision;
* completed rubrics and self-assessments;
* decision and assumption log;
* review findings and dispositions;
* final report or executive memo;
* review briefing;
* recorded oral defense or written defense transcript;
* one-page retrospective identifying strengths, limitations, and next development needs.

##### 18. Course maintenance record

| Revision date | Change | Reason | Source or evidence | Effect on outcomes or assessments |
|---|---|---|---|---|
| [Date] | [Change] | [Reason] | [Source] | [Effect] |

This prevents resource updates or assignment changes from silently breaking alignment with the competency map.

---

### Reusable weekly template

Use this structure for each instructional week. A weekly section should normally be detailed enough that the learner can begin work without having to invent the assignment, search broadly for basic resources, or guess how completion will be judged.

#### Week [number] — [Specific topic or professional task]

**Weekly role in the course:** [Foundation / method development / integration / review / capstone]
**Program competencies:** [C# at I/D/A]
**Course outcomes:** [CLO-#]
**Nominal effort:** [8–10 hours or declared alternative]
**Case-study baseline used:** [Artifact name and version]
**Primary evidence produced:** [Artifact or demonstrated capability]

##### 1. Why this week matters

[Explain the professional setting, decision, failure mode, review, or lifecycle need that makes the week's material important. Connect it to previous and later work.]

##### 2. Essential question

> [One decision-oriented question that the learner should be able to answer more convincingly by the end of the week.]

##### 3. Prerequisite retrieval and readiness check

**Retrieve from prior work**

* [Concept, method, or artifact]
* [Concept, method, or artifact]

**Readiness check**

Provide three to five short questions and one small task. Include answers or a scoring guide. State what to review when the learner cannot complete the check successfully.

##### 4. Detailed weekly learning outcomes

By the end of the week, the learner will be able to:

1. [Measurable outcome]
2. [Measurable outcome]
3. [Measurable outcome]
4. [Measurable outcome]
5. [Optional measurable outcome]
6. [Optional measurable outcome]

Each outcome must be assessed somewhere in the week's activities or deliverable.

##### 5. Key concepts, distinctions, and vocabulary

| Term or distinction | Working definition | Why it matters | Common error |
|---|---|---|---|
| [Term] | [Definition] | [Use] | [Misconception] |
| [Term] | [Definition] | [Use] | [Misconception] |

Include important notation, equations, model elements, decision rules, or standards terminology where applicable.

##### 6. Required learning resources

| Resource and exact assignment | Classification | Purpose | Guiding questions | Expected time |
|---|---|---|---|---:|
| [Author/source, title, chapter/section/pages or timestamp] | Required | [What this teaches] | [Two or three questions] | [Time] |
| [Source and exact section] | Required | [Purpose] | [Questions] | [Time] |
| [Tool tutorial or demonstration] | Required | [Purpose] | [Questions] | [Time] |
| [Supplement] | Recommended | [Purpose] | [Question] | [Time] |
| [Standard or handbook] | Reference | [When to consult it] | — | — |
| [Advanced source] | Advanced | [Deeper extension] | [Question] | [Time] |

Do not require more material than can reasonably be studied within the weekly time budget. Prefer a small number of coherent, high-value assignments.

##### 7. Instructor-style lesson notes or mini-lecture

[Provide a structured explanation of the week's central method or concept. It should include the problem addressed, inputs, steps, outputs, assumptions, limitations, and situations in which a different method is preferable.]

**Method summary**

1. [Step]
2. [Step]
3. [Step]
4. [Step]

**Decision points**

* [Where judgment is required]
* [Where assumptions materially affect results]

**Frequent mistakes**

* [Mistake and correction]
* [Mistake and correction]

##### 8. Fully worked example

**Problem**

[Provide a bounded example with all required inputs.]

**Assumptions**

* [Assumption]

**Worked solution**

1. [Step and intermediate result]
2. [Step and intermediate result]
3. [Step and result]

**Interpretation**

[Explain what the result means and what it does not establish.]

**Checks**

* [Sanity, traceability, dimensional, consistency, verification, or validation check]

**Alternative or failure case**

[Show how the result changes when an assumption, method, or input is inappropriate.]

##### 9. Guided practice

Provide a partially scaffolded activity that uses the same method in a different but comparable situation.

**Inputs provided**

* [Input]

**Steps supplied to the learner**

1. [Prompt]
2. [Prompt]
3. [Prompt]

**Checkpoints**

[Provide intermediate expected results, hints, queries, or automated checks so errors are caught before the independent assignment.]

##### 10. Independent exercises

**Foundation exercise — method mechanics**

[Short exercise that confirms correct execution of the basic method.]

**Application exercise — running case**

[Apply the method independently to the controlled case baseline.]

**Analysis exercise — critique or compare**

[Diagnose defects, compare alternatives, interpret evidence, or explain why two plausible approaches differ.]

**Synthesis exercise — create and defend**

[Produce a new artifact or recommendation requiring integration and judgment.]

**Stretch exercise — advanced extension**

[Optional use of a more complex dataset, tool, standard, model, uncertainty treatment, or cross-disciplinary constraint.]

For each exercise, state inputs, constraints, required outputs, completion criteria, and solution availability.

##### 11. Case-study integration and configuration update

**Baseline changes required**

* [Artifact to create or revise]
* [Trace or interface to update]
* [Decision or assumption to record]

**Consistency checks**

* [Orphan/coverage query]
* [Cross-model or cross-document check]
* [Independent calculation or review]

**Configuration action**

[Define version label, change-log entry, review status, and files to commit or archive.]

##### 12. Weekly deliverable specification

**Deliverable title:** [Name]
**Purpose:** [Decision or capability supported]
**Audience:** [Reviewer, customer, chief engineer, test lead, program manager, etc.]
**Format and length:** [File formats, page range, model scope, notebook, code, briefing length]
**Inputs:** [Required baseline and data]
**Due evidence:** [Files and demonstration]

**Required contents**

1. [Content]
2. [Content]
3. [Content]
4. [Content]

**Acceptance checks**

* [Objective check]
* [Objective check]
* [Traceability or evidence check]

**Critical failures**

* [Condition that makes the deliverable unacceptable regardless of total points]

##### 13. Weekly analytic rubric

| Criterion | Weight | Exemplary | Proficient | Developing | Insufficient |
|---|---:|---|---|---|---|
| Technical correctness | [%] | [Descriptor] | [Descriptor] | [Descriptor] | [Descriptor] |
| Completeness | [%] | [Descriptor] | [Descriptor] | [Descriptor] | [Descriptor] |
| Traceability and consistency | [%] | [Descriptor] | [Descriptor] | [Descriptor] | [Descriptor] |
| Assumptions, uncertainty, and rationale | [%] | [Descriptor] | [Descriptor] | [Descriptor] | [Descriptor] |
| Evidence and checks | [%] | [Descriptor] | [Descriptor] | [Descriptor] | [Descriptor] |
| Communication and configuration quality | [%] | [Descriptor] | [Descriptor] | [Descriptor] | [Descriptor] |

Use only criteria relevant to the week, ensure weights total 100%, and define at least one critical criterion when the artifact affects later technical work.

##### 14. Knowledge check and answer key

Include five to ten items using a mixture of:

* concept distinction;
* method selection;
* defect diagnosis;
* short calculation or model interpretation;
* scenario-based professional judgment;
* explanation of an assumption or limitation.

Provide an answer key with concise rationales, not only the correct option. A recommended threshold is **80%**, followed by targeted review and a second attempt when necessary.

##### 15. Feedback, revision, and recovery

**Feedback source**

[Rubric, worked solution, automated tests, peer review, model query, validation data, or recorded self-review.]

**Required revision**

[Identify what must be corrected or improved and what evidence will show that the issue is resolved.]

**Recovery path**

[Provide remedial reading, a smaller practice problem, or a second attempt when the learner does not meet the threshold.]

**Revision record**

[Require a short note listing findings, changes made, and unresolved limitations.]

##### 16. Reflection and retrieval practice

Answer briefly:

1. What is the most important judgment made this week?
2. Which assumption or input had the greatest effect?
3. What error would be most dangerous in professional practice?
4. What changed in the controlled baseline?
5. What should be reproducible from memory next week?
6. How does this week's work affect a later lifecycle decision or artifact?

##### 17. Time budget

| Activity | Planned time | Actual time |
|---|---:|---:|
| Retrieval and readiness check | [Time] | [Record] |
| Required reading and notes | [Time] | [Record] |
| Lesson or tutorial | [Time] | [Record] |
| Worked example | [Time] | [Record] |
| Guided practice | [Time] | [Record] |
| Independent exercises | [Time] | [Record] |
| Deliverable, checking, and revision | [Time] | [Record] |
| Knowledge check and reflection | [Time] | [Record] |
| **Total** | **[8–10 hours]** | **[Record]** |

Recording actual time helps recalibrate an unrealistically dense or sparse week during curriculum maintenance.

##### 18. Weekly completion checklist

The week is complete when:

* [ ] the readiness check has been passed or remedial work completed;
* [ ] all required resources have been studied with notes answering the guiding questions;
* [ ] the worked example and guided exercise have been reproduced successfully;
* [ ] the independent application has been completed;
* [ ] all required baseline and traceability updates have been made;
* [ ] the deliverable meets the minimum rubric and all critical criteria;
* [ ] feedback has been reviewed and required revisions completed;
* [ ] the knowledge check meets the threshold;
* [ ] time, decisions, assumptions, and reflections have been recorded.

##### 19. Solution and instructor-material package

Keep learner-facing prompts separate from solution material. The solution package should contain:

* readiness-check answers;
* worked-example source files;
* guided-practice checkpoints;
* independent-exercise solution or reference rationale;
* completed example deliverable or annotated excerpt;
* scoring rubric with sample judgments;
* knowledge-check answer key;
* common-error notes;
* optional extension solution.

For open-ended engineering work, provide a defensible reference rationale and evaluation criteria rather than implying that only one architecture, model, or recommendation is correct.

---

### Template adoption plan

The templates are being applied in this order:

1. **Completed:** create and fully expand EN.645.662 and EN.645.667;
2. **Completed:** stabilize the templates after Phase 0 by separating semantic/engineering quality from presentation quality and requiring reproducible source, queries, coverage, and change-impact evidence where applicable;
3. **Completed:** rebuild and fully expand EN.645.631 Introduction to Model Based Systems Engineering;
4. **Completed:** rebuild and fully expand EN.605.704 Object-Oriented Analysis and Design;
5. **Completed:** rebuild and fully expand EN.645.764 Software Systems Engineering;
6. **Completed:** rebuild and fully expand all three Phase 2 lifecycle courses—EN.645.767 System Conceptual Design, EN.645.768 System Design & Integration, and EN.645.769 System Test & Evaluation—while preserving one controlled concept-to-evidence chain;
7. **Completed:** fully expand all six Phase 3 quantitative and analytic courses;
8. **Completed:** fully expand all three Phase 4 agile, digital/mission, and process-improvement courses;
9. **Completed:** fully expand all three Phase 5 courses—EN.645.771 System of Systems Engineering, EN.645.753 Enterprise Systems Engineering, and EN.645.742 Management of Complex Systems;
10. **Completed:** conduct the program-level quality review, add pilot and remediation guidance, calibrate planning assumptions, correct repository-status inconsistencies, and prepare the Version 1.0 release package.

Existing course material should be retained when it fits the template, rewritten when it is underspecified, and removed only when it is redundant, unsupported, obsolete, or outside the source course's intended scope.

---
