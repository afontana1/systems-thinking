# Notes on a Formal Taxonomy, Ontology, and Computational Representation of Systems

## Purpose of these notes

These notes consolidate the ideas about whether systems science has an analogue to computational complexity classes, and what a more useful framework might look like for describing, comparing, and computationally representing engineered, social, natural, and economic systems.

The analysis moved through five broad stages:

1. Surveying existing academic attempts to classify systems.
2. Distinguishing system attributes, mechanisms, capabilities, and emergent properties.
3. Replacing a single hierarchy with a compositional descriptor space.
4. Applying that framework to socioeconomic systems and ideological categories.
5. Treating the ontology as an intermediate representation for executable computational models.

The central research idea that emerged is:

> Build a formal, compositional systems ontology that describes entities, structures, relations, processes, rules, dynamics, capabilities, and emergent properties; then map those descriptions into one or more computational formalisms such as Petri nets, state machines, process calculi, graph transformations, dynamical systems, and agent-based models.

---

# 1. Initial question: is there a systems analogue to computational complexity classes?

Computational complexity theory provides a widely recognized, mathematically formal, and often nested classification of problems and algorithms. Typical relationships include:

$$
P \subseteq NP \subseteq PSPACE \subseteq EXPTIME.
$$

These classes work because complexity theory fixes several conventions:

- problems are represented in a canonical formal way;
- inputs have a measurable size;
- a computational model is specified;
- a resource such as time or space is chosen;
- reductions establish relative difficulty;
- class membership is defined by explicit resource bounds.

The question was whether systems science, complex adaptive systems, systems engineering, economics, cybernetics, and related fields possess an equivalent taxonomy of system types.

> There are many serious taxonomies and formal classifications of systems, but no universally accepted system hierarchy analogous to computational complexity classes.

The closest existing work falls into three families:

1. taxonomies of what systems are;
2. taxonomies of how systems behave or are organized;
3. formal classifications of system models, descriptions, and analysis problems.

The third family comes closest to computational complexity theory, but it usually classifies models under a chosen representation rather than classifying real systems independently of representation.

---

# 2. Major historical and academic system taxonomies

## 2.1 General Systems Theory

General Systems Theory sought principles and organizational patterns that recur across physics, biology, engineering, organizations, and society. Its purpose was not merely to list domains, but to identify cross-domain structural isomorphisms such as feedback, hierarchy, equilibrium, adaptation, growth, and self-maintenance.

Reference:

- General historical overview of General Systems Theory: <https://pmc.ncbi.nlm.nih.gov/articles/PMC4610108/>

## 2.2 Kenneth Boulding's hierarchy of systems

Kenneth Boulding's 1956 paper, *General Systems Theory—The Skeleton of Science*, is one of the clearest early attempts at a hierarchy of system types.

Boulding's hierarchy included approximately the following levels:

| Level | System type | Typical examples |
|---|---|---|
| 1 | Frameworks | crystals, maps, static structures |
| 2 | Clockworks | machines, celestial mechanics |
| 3 | Control systems | thermostats, feedback regulators |
| 4 | Open systems | self-maintaining cells |
| 5 | Genetic-societal systems | plants |
| 6 | Animal systems | organisms with perception and mobility |
| 7 | Human systems | symbolic, self-conscious agents |
| 8 | Social organizations | firms, communities, institutions |
| 9 | Transcendental systems | limiting or unknowable structures |

Boulding's hierarchy is important because higher levels introduce capabilities absent from lower levels, such as information processing, self-maintenance, cognition, purpose, and institutional organization.

However, it is not analogous to computational complexity classes because:

- membership is not defined by necessary and sufficient mathematical conditions;
- there are no standard reductions between levels;
- the hierarchy is developmental and organizational rather than formally extensional;
- system membership often depends on interpretation.

References:

- Boulding text: <https://www.panarchy.org/boulding/systems.1956.html>
- Publication record: <https://ideas.repec.org/a/inm/ormnsc/v2y1956i3p197-208.html>

## 2.3 James Grier Miller's Living Systems Theory

Miller developed a detailed classification for living systems. It combines:

- hierarchical levels such as cell, organ, organism, group, organization, society, and supranational system;
- recurring functional subsystems responsible for matter, energy, and information processing.

The result resembles a matrix:

$$
\text{System level} \times \text{Functional subsystem}.
$$

This is more systematic than Boulding's hierarchy, but it focuses on living and social systems rather than all possible systems.

Reference:

- <https://onlinelibrary.wiley.com/doi/abs/10.1002/bs.3830170102>

## 2.4 Russell Ackoff's purpose-based taxonomy

Ackoff classified systems by whether the whole and its components can exercise choice or pursue purposes.

| Type | Whole purposeful? | Parts purposeful? |
|---|---:|---:|
| Deterministic | No | No |
| Animate | Yes | No |
| Social | Yes | Yes |
| Ecological | Not necessarily as a unitary whole | Some parts are |

This taxonomy is useful for explaining why methods appropriate for machines may not be suitable for organizations whose constituent agents have their own goals.

Its limitation is that purpose, agency, and choice are difficult to define in a representation-independent formal way.

## 2.5 Peter Checkland and soft systems

Checkland's systems methodology distinguishes approximately among:

- natural systems;
- designed physical systems;
- designed abstract systems;
- human activity systems.

The hard-soft distinction concerns whether goals, system boundaries, and problem definitions can be objectively specified, or whether they are contested and value-laden.

In social systems, deciding what the system is may itself be part of the problem.

Reference:

- <https://www.sciencedirect.com/topics/psychology/systems-theory>

## 2.6 Mark Maier and systems of systems

Maier proposed an operational classification of systems of systems based on features such as:

- operational independence of constituent systems;
- managerial independence;
- geographic distribution;
- emergent behavior;
- evolutionary development.

This is closer to an engineering type system because systems can be tested against explicit criteria. However, it applies only to a particular region of the broader systems landscape.

Reference:

- <https://ideas.repec.org/a/wly/syseng/v1y1998i4p267-284.html>

## 2.7 Magee, Sheard, and engineering complexity typologies

Magee and colleagues proposed classifications of complex systems and engineering systems, distinguishing systems by technological, human, organizational, and natural components, as well as structural and behavioral features.

Sheard and Mostashari proposed a systems-engineering complexity typology that treats complexity as multidimensional rather than scalar.

References:

- Magee: <https://incose.onlinelibrary.wiley.com/doi/abs/10.1002/j.2334-5837.2004.tb00510.x>
- Sheard and Mostashari: <https://web.mst.edu/lib-circ/files/Special%20Collections/INCOSE2010/A%20Complexity%20Typology%20for%20Systems%20Engineering.pdf>

## 2.8 Ostrom's social-ecological systems framework

Elinor Ostrom's Social-Ecological Systems framework decomposes social-ecological systems into categories such as:

- resource system;
- resource units;
- governance system;
- actors or users;
- interactions;
- outcomes;
- broader social, economic, and ecological context.

The framework supports cumulative comparison across forests, fisheries, irrigation systems, and other commons while preserving domain-specific detail.

This is one of the strongest examples of a practical systems ontology, although it is closer to a diagnostic schema than a universal hierarchy.

Reference:

- <https://pubmed.ncbi.nlm.nih.gov/19628857/>

## 2.9 CLIOS

CLIOS stands for Complex, Large-scale, Interconnected, Open, Socio-technical systems.

It characterizes an important class of infrastructure and policy systems by features including:

- complex internal interactions;
- large spatial or institutional scale;
- coupling among subsystems;
- open boundaries;
- substantial social and institutional components.

CLIOS is better viewed as a methodology for analyzing one family of systems than as a universal system taxonomy.

---

# 3. Formal system classifications that are closer to computational complexity

## 3.1 Dynamical systems classifications

Once a system is represented mathematically as a dynamical system, it can be placed into precise classes:

- linear or nonlinear;
- continuous-time or discrete-time;
- deterministic or stochastic;
- autonomous or non-autonomous;
- finite-dimensional or infinite-dimensional;
- stable or unstable;
- controllable or uncontrollable;
- observable or unobservable;
- ergodic or non-ergodic;
- conservative or dissipative;
- chaotic or non-chaotic.

These are rigorous, but they classify models under a chosen representation.

The same city, firm, ecosystem, or economy can be represented as:

- a nonlinear dynamical system;
- a network;
- an agent-based model;
- a stochastic game;
- an input-output system;
- a system of systems.

Therefore, the classification depends partly on the modeling question and abstraction.

## 3.2 Zeigler's system specification hierarchy

Bernard Zeigler's system specification hierarchy classifies system descriptions according to how much structural information is known, moving from observed input-output behavior toward internal state-transition structure and coupled component models.

DEVS provides mathematically defined modular and hierarchical specifications for discrete-event systems.

This resembles machine-model or formal-language hierarchies because it classifies descriptions by structure and expressive content. However, it remains a classification of system specifications rather than all real systems.

References:

- <https://www.mdpi.com/2078-2489/14/1/22>
- <https://dl.acm.org/doi/10.1109/32.4640>

## 3.3 Herbert Simon and near decomposability

Simon's concept of near decomposability identifies systems in which:

- interactions within modules are relatively strong or fast;
- interactions between modules are relatively weak or slow.

This supports hierarchical analysis and timescale separation.

Near decomposability is more amenable to quantitative formalization than Boulding's hierarchy.

References:

- Simon, *The Architecture of Complexity*: <https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf>
- Formalized later work: <https://arxiv.org/abs/1512.08464>

## 3.4 Network morphospaces

Network science often represents systems as points in a multidimensional structural space using measures such as:

- degree distribution;
- modularity;
- hierarchy;
- centralization;
- assortativity;
- clustering;
- motif frequencies;
- spectral properties;
- controllability characteristics.

Formal morphospaces have been proposed for comparing hierarchical organization across ecological, biological, technological, and social networks.

Reference:

- <https://arxiv.org/abs/1303.2503>

---

# 4. Why system complexity is better represented as a vector

No universally privileged scalar measure of system complexity exists.

A system may be:

- structurally simple but dynamically unpredictable;
- structurally large but nearly decomposable;
- computationally universal but physically compact;
- predictable in aggregate but unpredictable microscopically;
- difficult to control but easy to simulate;
- easy to describe but difficult to infer from observations.

Relevant complexity measures include:

- algorithmic or description complexity;
- entropy and information measures;
- effective complexity;
- statistical complexity;
- logical depth;
- interaction information;
- structural complexity;
- computational mechanics;
- network complexity;
- dimensionality;
- coupling strength;
- sensitivity;
- uncertainty;
- nonlinearity.

References:

- Information-theoretic complexity metric: <https://kiwi.oden.utexas.edu/papers/Complexity-metric-Allaire-He-Deyst-Willcox.pdf>
- Multivariable information measures: <https://arxiv.org/abs/1302.6932>

The emerging conclusion was:

> Complexity is better treated as a vector of features, mechanisms, and task-relative difficulties than as a single total order.

A general system profile might be represented as:

$$
\mathcal{S} = (D,T,U,A,H,C,O,P,E,R),
$$

where, for example:

- $D$: dynamical regime;
- $T$: temporal form;
- $U$: uncertainty;
- $A$: agency;
- $H$: organization;
- $C$: coupling;
- $O$: openness;
- $P$: purpose and governance;
- $E$: evolution;
- $R$: analysis-resource profile.

Examples of dimensions:

- static, equilibrium, transient, oscillatory, chaotic;
- continuous, discrete, hybrid, event-based;
- deterministic, stochastic, epistemically uncertain;
- no agency, fixed-policy agents, learning agents, reflexive agents;
- flat, modular, hierarchical, heterarchical;
- weak, strong, sparse, dense, multiplex coupling;
- closed, environmentally coupled, materially open, informationally open;
- externally assigned goals, internally maintained goals, plural or contested goals;
- fixed structure, adaptive parameters, changing topology, endogenous rule change.

System classes could then be logical regions in that descriptor space.

For example:

$$
\mathrm{CAS} = \{\mathcal{S} : A=\text{adaptive},\; E\neq\text{fixed},\; C=\text{interactive},\; \text{macro-emergence present}\}.
$$

And a system-of-systems class could be described as:

$$
\mathrm{SoS}=\{\mathcal{S}: \text{operational independence} + \text{managerial independence} + \text{emergence} + \text{evolution}\}.
$$

---

# 5. Terminology: attributes, mechanisms, capabilities, and emergent properties

A major conceptual refinement in the conversation was the rejection of using the word *property* for every descriptor.

The preferred distinction became:

| Category | Meaning | Examples |
|---|---|---|
| Attributes or features | Relatively persistent characteristics of organization or structure | modularity, openness, hierarchy, redundancy |
| Mechanisms | Processes that generate change or regulate behavior | feedback, selection, diffusion, bargaining, optimization |
| Capabilities | Things the system is able to do | learning, self-repair, coordination, adaptation |
| Emergent properties | System-level qualities produced by interactions among attributes and mechanisms | resilience, robustness, efficiency, adaptability, innovation |

Examples:

- Feedback is better understood as a **mechanism**.
- Adaptation is a **capability** enabled by mechanisms such as feedback and memory.
- Resilience is an **emergent property** resulting from structure, mechanisms, and capabilities.
- Modularity is an **attribute** of organization.

A useful architecture for describing a system is:

1. identity;
2. structure;
3. dynamics;
4. capabilities;
5. emergent behavior.

The first four may be explicitly specified or observed. The fifth must be derived, measured, or observed under conditions.

---

# 6. Why systems do not naturally form a single nested hierarchy

In complexity theory, inclusion relations have a precise meaning:

$$
P \subseteq NP
$$

means every problem in $P$ is also in $NP$.

For systems, there is no equivalent single natural ordering.

Consider a thermostat and an ant colony.

A thermostat may have:

- feedback;
- deterministic behavior;
- limited openness;
- no adaptation;
- no hierarchy;
- no agency.

An ant colony may have:

- feedback;
- adaptation;
- distributed control;
- agency;
- stochastic interactions;
- evolutionary history;
- weak or distributed hierarchy.

The ant colony is not simply a superset of the thermostat. It occupies a different region in a multidimensional feature space.

This led to the idea that systems resemble points in a feature space rather than members of a single ladder.

If

$$
S=(F,H,A,O,M,D,U,E,\ldots),
$$

where:

- $F$ = feedback richness;
- $H$ = hierarchy;
- $A$ = adaptation;
- $O$ = openness;
- $M$ = modularity;
- $D$ = distributed control;
- $U$ = uncertainty;
- $E$ = evolutionary capacity;

then system types become regions or clusters in that space.

Certain combinations may create qualitatively new system types:

### Control system

Requires approximately:

- state;
- feedback;
- controller.

### Adaptive system

Requires approximately:

- feedback;
- memory;
- parameter or policy modification.

### Complex adaptive system

Requires approximately:

- many interacting agents;
- local information;
- adaptation;
- nonlinear interactions;
- decentralized control;
- emergence.

### Evolutionary system

Requires:

- variation;
- inheritance;
- selection.

The emergence of a new type from a combination of features resembles a phase transition or configurational threshold more than ordinary set inclusion.

---

# 7. Type systems versus richer descriptor frameworks

The analogy to programming-language type systems was explored and then refined.

A type system usually answers:

- what operations are permitted;
- what invariants hold;
- what interfaces are implemented;
- which compositions are legal.

A system description must preserve much more latent structure, including:

- degree of centralization;
- number of hierarchical levels;
- distribution of control;
- openness;
- modularity;
- heterogeneity of agents;
- redundancy;
- strength and pattern of coupling;
- adaptation;
- endogenous versus exogenous change;
- changing topology;
- information flows;
- local versus global interaction;
- ergodicity;
- self-maintenance;
- goal structure;
- competing goals;
- timescales;
- stochastic versus epistemic uncertainty.

Therefore, the better concept is not merely a type system, but a **feature algebra**, **descriptive language**, or **formal systems ontology**.

A type label such as *complex adaptive system* should be treated as shorthand for a structured conjunction of descriptors rather than as the complete description.

For example:

$$
\mathrm{AdaptiveSystem}
=
\mathrm{Feedback}
\land
\mathrm{Memory}
\land
\mathrm{PolicyModification}.
$$

$$
\mathrm{ComplexAdaptiveSystem}
=
\mathrm{Adaptive}
\land
\mathrm{ManyAgents}
\land
\mathrm{NonlinearInteraction}
\land
\mathrm{Emergence}.
$$

This resembles description logics or formal ontology engineering more than classical taxonomy.

---

# 8. Existing work on system ontologies

## 8.1 Dori and Sillitto

Dori and Sillitto's *What Is a System? An Ontological Framework* reviewed more than one hundred definitions of system across disciplines and sought common concepts such as:

- physical versus conceptual systems;
- natural versus artificial systems;
- boundaries;
- environment;
- function;
- structure;
- interactions;
- stakeholders.

This is an important upper-level systems ontology, but it is more a common conceptual vocabulary than a rich universal descriptor language.

Reference:

- <https://incose.onlinelibrary.wiley.com/doi/10.1002/sys.21383>

## 8.2 Systems engineering ontologies

Ontology-based systems engineering uses technologies such as:

- OWL;
- RDF;
- SysML;
- knowledge graphs;
- machine-readable engineering vocabularies.

These ontologies represent:

- components;
- interfaces;
- functions;
- requirements;
- behaviors;
- dependencies.

Their primary goals are interoperability, traceability, and machine reasoning.

A review of systems engineering ontologies found broad scope but often limited formal semantic richness relative to the ambitions of a universal systems ontology.

Reference:

- <https://www.sciencedirect.com/science/article/pii/S0166361518307887>

## 8.3 The missing framework

The conversation's assessment was that the literature does not yet provide a mature framework with all of the following:

- dozens of fundamental cross-domain system descriptors;
- precise mathematical or logical definitions;
- explicit implication, dependence, incompatibility, and composition relations;
- observational mapping procedures;
- graded or contextual values;
- direct links to executable formalisms;
- support for comparing engineered, natural, social, and economic systems.

The proposed project would therefore be a synthesis of:

- formal ontology;
- knowledge representation;
- type theory;
- system science;
- institutional analysis;
- multi-formalism modeling;
- simulation;
- model checking.

---

# 9. Application to socioeconomic systems

The conversation then shifted from general systems to socioeconomic systems.

The motivating example was the debate over whether China is "communist" or "capitalist."

These terms have:

- colloquial meanings;
- meanings in political philosophy;
- meanings in economic history;
- meanings in party doctrine;
- meanings in comparative political economy.

Disagreement often occurs because participants silently use different definitions and prioritize different dimensions.

The proposed alternative is:

$$
\text{Observed economy}
\rightarrow
\text{formal system description}
\rightarrow
\text{comparison with idealized models}.
$$

rather than:

$$
\text{Observed economy}
\rightarrow
\text{capitalist or communist}.
$$

This separates three questions:

1. What structures, actors, rules, and processes are present?
2. How do they operate dynamically?
3. Which idealized political-economic model do they resemble, and along which dimensions?

An analyst claiming that China is capitalist may be emphasizing:

- commodity production;
- wage labor;
- private accumulation;
- market pricing;
- competition among firms.

An analyst claiming that China is communist or socialist may be emphasizing:

- party control over strategic appointments;
- state ownership in key sectors;
- administrative credit allocation;
- planning;
- political subordination of capital owners.

Both may identify real features while disagreeing because they treat different descriptors as constitutive.

---

# 10. Academic foundations for a socioeconomic systems ontology

## 10.1 Ostrom's Institutional Analysis and Development framework

The IAD framework identifies:

- actors;
- positions and roles;
- actions;
- information;
- control over decisions;
- costs and benefits;
- rules;
- biophysical and community context;
- interaction patterns;
- outcomes.

It is useful because it analyzes institutional arrangements without assuming every case belongs to one ideological category.

## 10.2 Institutional Grammar

Institutional Grammar decomposes institutional statements into structured elements.

Institutional Grammar 2.0 distinguishes:

- regulative statements, which prescribe what actors may, must, or must not do;
- constitutive statements, which define entities, roles, statuses, and institutional facts.

A statement such as:

> State-owned banks must prioritize firms designated as strategically important.

could be decomposed into:

- actor;
- deontic operator;
- action;
- object;
- condition;
- enforcement or consequence;
- constitutive definition of "strategically important firm."

References:

- Institutional Grammar 2.0: <https://thecommonsjournal.org/articles/10.5334/ijc.1214>
- Formal syntax and software work: <https://arxiv.org/abs/2505.13393>

## 10.3 Social ontology

Social ontology supplies the categories needed to distinguish:

- material entities;
- persons;
- collective actors;
- institutional objects;
- rules;
- processes.

For example:

$$
\begin{aligned}
&\text{Material entities:} && \text{land, machinery, energy, goods},\\
&\text{Agents:} && \text{persons, households, officials},\\
&\text{Collective actors:} && \text{firms, ministries, unions},\\
&\text{Institutional objects:} && \text{money, property rights, contracts},\\
&\text{Rules:} && \text{laws, norms, administrative directives},\\
&\text{Processes:} && \text{production, exchange, allocation, accumulation}.
\end{aligned}
$$

Reference:

- <https://pmc.ncbi.nlm.nih.gov/articles/PMC10092928/>

## 10.4 Comparative political economy and Varieties of Capitalism

The Varieties of Capitalism literature compares institutional configurations in areas such as:

- corporate governance;
- industrial relations;
- education and skill formation;
- interfirm relations;
- employment relations.

Its major contribution is the idea that economies differ not only by degree of state intervention, but by institutional configurations and complementarities.

Institutional complementarity means that one institution may increase the effectiveness or viability of another.

References:

- Hall and Soskice context: <https://hall.scholars.harvard.edu/publications/varieties-capitalism-institutional-foundations-comparative-advantage>
- Empirical institutional complementarity work: <https://www.researchgate.net/publication/2485542_Varieties_of_Capitalism_and_Institutional_Complementarities_in_the_Political_Economy_An_Empirical_Analysis>

The limitation is that this literature usually begins within the category *capitalism* rather than building a neutral language for capitalist, socialist, cooperative, feudal, tributary, subsistence, and hybrid systems.

---

# 11. An economy as transformation, metabolism, and reproduction

A basic abstraction of an economy is a system that transforms inputs into outputs.

A possible representation is:

$$
\mathcal{E}:
(X,N,K,L,I)
\longrightarrow
(Y,W,\Delta K,\Delta N,\Delta I),
$$

where:

- $X$: material and energy inputs;
- $N$: natural stocks and ecological conditions;
- $K$: productive capital and infrastructure;
- $L$: labor and human activity;
- $I$: information and institutional arrangements;
- $Y$: useful goods and services;
- $W$: waste and externalities;
- $\Delta K$: reproduction or depletion of productive capacity;
- $\Delta N$: ecological regeneration or degradation;
- $\Delta I$: reproduction or transformation of institutions.

An economy is not merely an input-output mechanism. It also reproduces or transforms its own conditions:

- labor forces and skills;
- firms and organizational capacities;
- ownership relations;
- infrastructures;
- expectations and information;
- political authority;
- social legitimacy;
- ecological stocks.

A dynamic representation is:

$$
S_{t+1}=F(S_t,X_t,A_t,R_t,E_t),
$$

where:

- $S_t$: system state;
- $X_t$: external inputs;
- $A_t$: agent behavior;
- $R_t$: institutional rule configuration;
- $E_t$: external environment.

Because actors may change the rules:

$$
R_{t+1}=G(R_t,A_t,S_t,\text{conflict},\text{learning}).
$$

This makes the economy not merely adaptive, but institutionally evolutionary and potentially reflexive.

---

# 12. Layers of a compositional socioeconomic system description

A general socioeconomic ontology should include at least the following layers.

## 12.1 Boundary and environment

The analyst must specify what is being modeled:

- national economy;
- regional production network;
- firm;
- household sector;
- financial system;
- transnational supply chain.

System boundaries matter because the same economy may have different descriptions at domestic, sectoral, and global scales.

## 12.2 Stocks and flows

Relevant stocks and flows include:

- natural resources;
- labor;
- capital goods;
- money and credit;
- information;
- goods and services;
- ownership claims;
- taxes;
- subsidies;
- rents;
- profits;
- transfers.

## 12.3 Actors and organizational units

Examples include:

- households;
- private firms;
- state-owned enterprises;
- cooperatives;
- banks;
- ministries;
- local governments;
- political parties;
- trade unions;
- foreign investors.

Actors should not be assumed to possess homogeneous goals.

## 12.4 Institutional relations

The ontology should distinguish:

- ownership;
- operational control;
- residual income rights;
- appointment authority;
- regulatory jurisdiction;
- contracting rights;
- taxation rights;
- access to credit;
- responsibility for losses;
- rights of exit, voice, and participation.

This avoids compressing several distinct relations into the single word *ownership*.

## 12.5 Allocation and coordination mechanisms

An economy may contain multiple mechanisms simultaneously:

$$
\mathcal{M}=
\{\text{markets},\text{administrative commands},\text{bargaining},\text{networks},\text{auctions},\text{rationing},\text{household allocation},\text{reciprocity},\text{professional norms}\}.
$$

The meaningful question is not simply "market or plan?" but:

> Which objects are allocated by which mechanisms, under whose authority, at what scale, and under which constraints?

## 12.6 Governance and metagovernance

Relevant rule-changing authorities include:

- legislatures;
- courts;
- ministries;
- political parties;
- central banks;
- corporate boards;
- local administrations;
- popular votes;
- informal elite networks.

Metagovernance refers to control over how rules themselves are changed.

## 12.7 Dynamics and adaptation

Relevant processes include:

- learning;
- innovation;
- entry and exit;
- bankruptcy;
- organizational replication;
- selection among firms;
- policy experimentation;
- institutional change;
- technological evolution;
- endogenous preference formation.

## 12.8 Emergent properties

Emergent properties include:

- resilience;
- robustness;
- efficiency;
- inequality;
- legitimacy;
- adaptability;
- innovation capacity;
- ecological sustainability.

These must be indexed to goals, disturbances, time horizons, and distributions.

For example:

$$
\operatorname{Resilience}(S,d,\tau,\phi)
$$

could denote the ability of system $S$, after disturbance $d$, to recover within time $\tau$ while preserving function $\phi$.

A system can be resilient with respect to industrial output while being non-resilient with respect to household income, political legitimacy, or ecosystem integrity.

---

# 13. Ideological categories as idealized prototypes

Capitalism, socialism, and communism should not necessarily be treated as mutually exclusive atomic types. They can be represented as idealized configurations or prototypes.

A simplified capitalist prototype may emphasize:

- alienable private ownership of productive assets;
- production for exchange;
- generalized commodity markets;
- wage labor;
- private residual claims;
- decentralized investment decisions;
- competition and bankruptcy as selection mechanisms;
- capital accumulation as an organizational imperative.

A socialist prototype may emphasize:

- public, social, cooperative, or worker control of productive assets;
- deliberate coordination of major investment;
- limitations on private residual claims;
- production governed by collective objectives;
- public accountability or participation in allocation.

A communist prototype, depending on the philosophical tradition formalized, may additionally include:

- absence of class domination;
- disappearance or reduction of generalized commodity relations;
- disappearance or transformation of the coercive state.

Observed systems can then be compared with idealized prototypes using a context- and weight-dependent similarity function:

$$
\operatorname{Sim}(S,P\mid C,W),
$$

where:

- $S$: observed system;
- $P$: idealized prototype;
- $C$: comparison context;
- $W$: weights assigned to descriptors.

No similarity score is theoretically neutral because different traditions assign different importance to:

- ownership;
- class power;
- market coordination;
- labor relations;
- governance;
- political authority;
- distribution;
- control over investment.

A formal language would distinguish:

$$
\text{disagreement about facts}
\neq
\text{disagreement about definitions}
\neq
\text{disagreement about weights}
\neq
\text{disagreement about values}.
$$

---

# 14. Why a flat vector is not enough

A simple feature vector such as:

$$
(\text{state ownership}=0.4,\;\text{planning}=0.7,\;\text{markets}=0.8)
$$

is too crude.

The same degree of state ownership can function differently depending on:

- which sectors are state-owned;
- who appoints management;
- whether firms maximize profit;
- whether firms face hard or soft budget constraints;
- how credit is allocated;
- whether political authorities intervene;
- whether private firms depend on state-controlled infrastructure;
- whether the state captures residual income;
- whether firms compete domestically or globally.

The correct formal object is closer to a typed multilayer graph:

$$
G=(V,E,\tau_V,\tau_E,\omega),
$$

where:

- $V$: nodes representing agents, organizations, resources, or institutions;
- $E$: relations such as ownership, authority, credit, information, production, or exchange;
- $\tau_V$: node types;
- $\tau_E$: edge types;
- $\omega$: weights, quantities, conditions, strengths, or probabilities.

Descriptors should often be derived from this relational structure rather than assigned impressionistically.

Features may also be:

- continuous;
- conditional;
- subsystem-specific;
- time-indexed;
- configuration-dependent.

For example:

$$
\text{administrative coordination}\in[0,1].
$$

And private autonomy may be conditional:

$$
\text{private autonomy}\mid \text{sector, firm size, political priority}.
$$

The framework should therefore support:

- graded membership;
- multiple simultaneous types;
- contextual descriptions;
- subsystem-specific classifications;
- configuration-dependent effects;
- historical change.

---

# 15. Ontology as a model-construction layer

The final major step in the discussion was the idea that the ontology should not only support description and comparison. It should also support construction of computational models.

The proposed pipeline is:

$$
\text{observations and documents}
\rightarrow
\text{system ontology}
\rightarrow
\text{formal model}
\rightarrow
\text{simulation, verification, or comparison}.
$$

The ontology would function as a semantic intermediate representation, analogous to an intermediate representation in a compiler.

The analyst would first encode the system without committing prematurely to one computational formalism.

For example, an institutional description might be decomposed into:

$$
\begin{aligned}
&\textbf{Entities:} && \text{Bank, Ministry, Firm, Worker, Commodity},\\
&\textbf{Relations:} && \text{owns, controls, lends-to, employs, trades-with},\\
&\textbf{Stocks:} && \text{credit, capacity, inventories, labor, money},\\
&\textbf{Processes:} && \text{allocate-credit, produce, hire, exchange, revise-policy},\\
&\textbf{Rules:} && \text{eligibility, priority, repayment, bankruptcy},\\
&\textbf{Information:} && \text{prices, production data, policy signals},\\
&\textbf{Objectives:} && \text{profit, employment, strategic capacity, stability}.
\end{aligned}
$$

Only after this semantic layer is specified would different components be mapped into suitable executable formalisms.

---

# 16. W. Brian Arthur and "Economics in Nouns and Verbs"

The relevant author is W. Brian Arthur.

In *Economics in Nouns and Verbs*, Arthur argues that standard mathematical economics is particularly comfortable with nouns:

- quantities;
- objects;
- static relations;
- equilibrium conditions.

It is less natural for representing verbs:

- actions;
- procedures;
- sequences;
- constructions;
- evolving processes.

Arthur proposes an algorithmic view in which economic agents execute and compose procedures rather than merely solve static optimization problems.

This perspective fits naturally with a systems ontology whose primitive categories include both entities and processes.

References:

- Journal paper: <https://sites.santafe.edu/~wbarthur/Papers/Nouns_Verbs_JEBO.pdf>
- Alternative version: <https://sites.santafe.edu/~wbarthur/Papers/Nouns_Verbs_ArXiv.pdf>

---

# 17. Matching system structures to computational formalisms

Different formalisms are appropriate for different aspects of an economic system.

## 17.1 Petri nets

Petri nets are appropriate for:

- resource flows;
- concurrency;
- synchronization;
- enabling conditions;
- capacity constraints;
- deadlocks;
- reachability;
- possible and impossible event sequences.

An example transition:

$$
\text{Credit available}
+
\text{Investment authorization}
\rightarrow
\text{Capacity expansion}.
$$

A production transition may consume:

- labor hours;
- energy;
- intermediate goods;
- machine capacity;

and produce:

- finished goods;
- wages;
- emissions;
- depreciation;
- tax liabilities.

Colored or typed Petri nets can distinguish commodities, ownership forms, regions, firms, and worker categories.

Petri-net reachability is computationally difficult and has non-elementary lower bounds.

Reference:

- <https://arxiv.org/abs/1809.07115>

## 17.2 State machines and statecharts

State machines are appropriate for institutional status and regime transitions.

For example:

$$
\text{Operating}
\rightarrow
\text{Financial distress}
\rightarrow
\begin{cases}
\text{Bankruptcy},\\
\text{State bailout},\\
\text{Restructuring}.
\end{cases}
$$

A guarded transition could be:

$$
\mathrm{Nationalize}(f)
\quad\text{if}\quad
\mathrm{Strategic}(f)
\land
\mathrm{Distressed}(f)
\land
\mathrm{AuthorizationGranted}.
$$

Hierarchical statecharts can represent nested and concurrent statuses.

## 17.3 Process calculi

Process calculi are appropriate for:

- communication;
- interaction protocols;
- message passing;
- synchronization;
- nondeterministic choice;
- creation of new relationships;
- contractual sequencing;
- concurrency.

A simplified exchange protocol could be represented as:

$$
\begin{aligned}
\mathrm{Buyer}
&=
\overline{\mathrm{request}}\langle q,p\rangle .\mathrm{awaitResponse},\\
\mathrm{Seller}
&=
\mathrm{request}(q,p).(\mathrm{accept}+\mathrm{reject}).\mathrm{end}.
\end{aligned}
$$

There are formal translations between process calculi and Petri nets. Multi-CCS, for example, was designed with Petri-net semantics and can represent finite place-transition nets within a process language.

Reference:

- <https://arxiv.org/abs/1011.6433>

## 17.4 Agent-based models

ABMs are appropriate where:

- actors differ;
- actors have internal state;
- information is local or incomplete;
- decision procedures vary;
- actors learn or imitate;
- networks evolve;
- aggregate patterns emerge.

An ontology-backed agent can be represented as:

$$
A_i=
(\text{roles},\text{resources},\text{capabilities},\text{information},\text{beliefs},\text{objectives},\text{decision procedures},\text{institutional permissions}).
$$

Arthur's procedural perspective suggests that each agent has a repertoire:

$$
\Pi_i=
\{\pi_{\text{price}},\pi_{\text{hire}},\pi_{\text{invest}},\pi_{\text{negotiate}},\pi_{\text{evade}},\pi_{\text{learn}}\}.
$$

Agents select, modify, or compose procedures according to context.

## 17.5 Dynamical systems and equations

Differential and difference equations remain appropriate for aggregate stocks and continuous relationships.

For example:

$$
K_{t+1}=K_t+I_t-\delta K_t,
$$

$$
N_{t+1}=N_t+r(N_t)-X_t.
$$

The proposal is not to reject algebra, but to use it where aggregate continuous relationships are the correct abstraction, while using procedural representations for sequence, construction, institutional contingency, and concurrency.

## 17.6 Multilayer networks

Networks can represent:

- ownership;
- trade;
- credit;
- authority;
- employment;
- information;
- supply dependencies.

A multilayer edge set may be:

$$
E=
E_{\text{ownership}}
\cup
E_{\text{credit}}
\cup
E_{\text{trade}}
\cup
E_{\text{authority}}.
$$

This permits distinctions such as a firm being:

- central in production;
- peripheral in finance;
- privately owned;
- dependent on public procurement;
- operationally autonomous;
- politically subordinate.

---

# 18. Multi-formalism and heterogeneous modeling

The conversation proposed combining several formalisms rather than forcing the entire economy into one representation.

Relevant research traditions include:

- multi-formalism modeling;
- multi-paradigm modeling;
- heterogeneous modeling;
- model composition;
- co-simulation;
- semantic adaptation.

DEVS has been used as a common execution framework for coupling heterogeneous models, including multi-agent and discrete-event models.

References:

- DEVS and multi-agent integration: <https://dl.acm.org/doi/10.5555/2872965.2872977>
- Semantic adaptation in heterogeneous co-simulation: <https://dl.acm.org/doi/10.5555/2872965.2872979>

A possible architecture for an economic model is:

| System aspect | Formalism |
|---|---|
| Material production | Petri net or stock-flow model |
| Firm behavior | Agent procedures |
| Legal status | State machines |
| Contracting and communication | Process calculus |
| Ownership and credit | Multilayer networks |
| Macroeconomic aggregates | Difference or differential equations |
| Institutional evolution | Rule rewriting or graph transformation |

An event sequence could proceed as follows:

1. An agent decides to apply for credit.
2. A process protocol sends the application to a bank.
3. A rule engine checks eligibility.
4. A state machine changes the application to `approved`.
5. A Petri net creates a credit token.
6. The firm's balance sheet and credit-network edges update.
7. Investment activates production transitions.
8. Aggregate capital and output variables change.
9. Policy agents observe aggregate results and revise rules.

This is an executable economics of verbs.

---

# 19. Ontology-driven formalism selection

The ontology could associate semantic patterns with formal modeling implications.

For example:

$$
\mathrm{Process}(p)
\land
\mathrm{Consumes}(p,x)
\land
\mathrm{Produces}(p,y)
$$

suggests a Petri-net transition or reaction-network representation.

$$
\mathrm{Agent}(a)
\land
\mathrm{HasInternalState}(a)
\land
\mathrm{UsesDecisionProcedure}(a)
$$

suggests an agent or actor representation.

$$
\mathrm{InstitutionalRole}(r)
\land
\mathrm{FiniteStatuses}(r)
$$

suggests a state machine.

$$
\mathrm{Protocol}(p)
\land
\mathrm{MessagePassing}(p)
\land
\mathrm{ConcurrentActors}(p)
$$

suggests a process calculus.

The complete pipeline is:

$$
\boxed{
\begin{array}{c}
\text{Economic-system ontology}\\
\downarrow\\
\text{Typed intermediate model}\\
\downarrow\\
\text{Formalism selection and transformation}\\
\downarrow\\
\text{Composed executable model}
\end{array}
}
$$

---

# 20. Complex types and conceptual precision

A strong type system within the ontology could prevent conceptual errors.

For example:

$$
\mathrm{OwnershipRight}
\neq
\mathrm{ControlRight}
\neq
\mathrm{IncomeClaim}
\neq
\mathrm{RegulatoryAuthority}.
$$

Similarly, prices could have subtypes:

$$
\begin{aligned}
&\mathrm{MarketPrice},\\
&\mathrm{AdministeredPrice},\\
&\mathrm{TransferPrice},\\
&\mathrm{ShadowPrice},\\
&\mathrm{AuctionPrice}.
\end{aligned}
$$

A state-owned enterprise should not be treated as an atomic label. It can be defined compositionally:

$$
\begin{aligned}
\mathrm{SOE}(x) \equiv
&\ \mathrm{Enterprise}(x)\\
&\land \exists s\,\mathrm{StateEntity}(s)\\
&\land \mathrm{ResidualClaimant}(s,x)\\
&\land \mathrm{AppointmentAuthority}(s,x).
\end{aligned}
$$

Alternative theoretical definitions could weaken, strengthen, or modify these conditions.

---

# 21. Rule semantics

Decision and institutional rules should be separated into multiple semantic levels.

## 21.1 Behavioral rules

What agents tend to do:

$$
\text{if inventories are low, increase production}.
$$

## 21.2 Constitutive rules

What creates an institutional fact:

$$
\text{registration} + \text{capital contribution}
\Rightarrow
\text{legal corporation}.
$$

## 21.3 Regulative rules

What actors are permitted, required, or prohibited from doing:

$$
\text{banks must maintain a reserve ratio above } r.
$$

## 21.4 Metarules

How rules themselves may be changed:

$$
\text{the central bank may change } r \text{ under procedure } P.
$$

Metarules are essential for adaptive political economies because institutional actors can rewrite parts of the system's operating logic.

---

# 22. Benefits for agent-based modeling

Ontology-backed ABMs could improve several recurring weaknesses in agent-based economics.

## 22.1 Traceability

The gap between verbal theory and code is often large:

$$
\text{theoretical claim}
\not\equiv
\text{implemented behavior}.
$$

An ontology can link code constructs to explicit theoretical assumptions.

## 22.2 Explicit semantics

Every agent attribute, role, rule, permission, process, and relation can have a defined meaning.

## 22.3 Automated consistency checking

Invalid combinations of roles, rights, states, or rules can be detected before simulation.

## 22.4 Scenario generation

Institutional reforms can be expressed as formal transformations of the system description.

## 22.5 Model comparison

Two models that both claim to represent capitalism may differ substantially:

- one includes wage bargaining;
- one assumes fixed wages;
- one includes endogenous credit;
- one treats money as passive;
- one permits institutional evolution;
- one fixes all institutional rules.

An ontology can expose these differences directly.

## 22.6 Procedural transparency

Instead of an opaque method such as:

```text
firm.step()
```

the model can expose:

$$
\mathrm{ObserveDemand}
\rightarrow
\mathrm{Forecast}
\rightarrow
\mathrm{RequestCredit}
\rightarrow
\mathrm{ChooseCapacity}
\rightarrow
\mathrm{Hire}
\rightarrow
\mathrm{Produce}.
$$

Each process can have:

- preconditions;
- resource requirements;
- institutional permissions;
- effects;
- alternative implementations.

---

# 23. Example: market exchange with emergency rationing

A good is normally allocated through markets, but rationing is imposed during shortages.

The ontology describes:

- buyers and sellers;
- inventory;
- money;
- market bids;
- eligibility certificates;
- a shortage condition;
- an authority empowered to activate rationing;
- a rule that changes the allocation mechanism.

## State-machine layer

$$
\mathrm{NormalMarket}
\rightarrow
\mathrm{ShortageEmergency}
\rightarrow
\mathrm{Rationing}
\rightarrow
\mathrm{NormalMarket}.
$$

## Petri-net layer

Purchases under rationing require both:

- a money token;
- an entitlement token.

## Agent layer

Buyers may respond by:

- substituting goods;
- searching informal markets;
- lobbying;
- saving certificates;
- misreporting eligibility.

## Network layer

Informal trading connections may emerge over time.

## Aggregate layer

Inventory and consumption are tracked using equations or stock-flow models.

This example shows how a regime change alters:

- available actions;
- permissions;
- resource requirements;
- actor strategies;
- network formation;
- aggregate outcomes.

---

# 24. Main technical obstacle: semantic composition

Combining formalisms is possible, but not automatically valid.

Petri nets, state machines, ABMs, process calculi, and differential equations may make different assumptions about:

- time;
- simultaneity;
- causality;
- randomness;
- identity;
- state;
- event ordering;
- observation;
- determinism.

A continuous-time model and a round-based ABM may disagree about event ordering. A state machine may assume atomic transitions while a process calculus permits interleaving.

The framework therefore requires explicit semantic adapters specifying:

$$
\begin{aligned}
&\text{how time advances},\\
&\text{how events are ordered},\\
&\text{how state is shared},\\
&\text{how conflicts are resolved},\\
&\text{how abstractions at different scales interact}.
\end{aligned}
$$

The ontology supplies conceptual semantics, but an execution semantics is also necessary.

---

# 25. Proposed research architecture

A complete implementation could contain six layers.

## 25.1 Upper systems ontology

General concepts:

- system;
- environment;
- boundary;
- entity;
- relation;
- state;
- process;
- event;
- resource;
- information;
- function;
- mechanism.

## 25.2 Socioeconomic domain ontology

Domain concepts:

- person;
- household;
- firm;
- state;
- ministry;
- bank;
- market;
- contract;
- money;
- credit;
- labor;
- property right;
- authority;
- class;
- planning body;
- cooperative.

## 25.3 Institutional rule language

Formal constructs for:

- permissions;
- obligations;
- prohibitions;
- constitutive rules;
- enforcement;
- rule-changing procedures.

## 25.4 Procedural language

Arthur-style verbs:

- search;
- bid;
- bargain;
- produce;
- hire;
- lend;
- invest;
- imitate;
- innovate;
- regulate;
- organize.

## 25.5 Formalism mappings

Mappings into:

- Petri nets;
- process calculi;
- state machines;
- graph transformations;
- equations;
- optimization models;
- ABMs;
- discrete-event models.

## 25.6 Analysis layer

Capabilities for:

- simulation;
- reachability;
- model checking;
- causal analysis;
- sensitivity analysis;
- institutional comparison;
- resilience testing;
- counterfactual transformation.

---

# 26. The core methodological reversal

Conventional modeling often starts with a technique:

> How can this economy be represented using equations, optimization, or an ABM?

The proposed approach reverses the order:

> What entities, relations, processes, rules, structures, and dynamics constitute the system, and which formal representations preserve those characteristics?

The resulting principle is:

$$
\boxed{
\text{ontology determines semantics;}
\quad
\text{semantics guides formalism;}
\quad
\text{formalism enables computation.}
}
$$

The ontology is therefore not merely a vocabulary. It is a model-construction discipline.

---

# 27. Open research questions

The conversation suggests a number of unresolved research questions.

## 27.1 Descriptor primitives

What are the most fundamental descriptors that are sufficiently general across engineered, natural, social, and economic systems?

## 27.2 Ontological categories

Which distinctions are essential?

Possible candidates include:

- entity;
- relation;
- process;
- event;
- mechanism;
- rule;
- capability;
- emergent property;
- function;
- resource;
- information;
- authority;
- objective;
- boundary.

## 27.3 Graded versus categorical descriptors

Which descriptors should be:

- Boolean;
- ordinal;
- continuous;
- probabilistic;
- relational;
- contextual;
- time-dependent?

## 27.4 Implication and incompatibility relations

Which features imply, require, enable, inhibit, or preclude others?

For example:

$$
\mathrm{Adaptation}
\Rightarrow
\mathrm{Memory}
\land
\mathrm{Feedback}
\land
\mathrm{PolicyModification}
$$

may be useful as a conceptual axiom, but the exact conditions require careful formalization.

## 27.5 Emergence

How should emergent properties be formally linked to lower-level attributes and mechanisms?

## 27.6 Observation and identification

How can empirical observations, laws, documents, organizational charts, financial data, interviews, and historical records be mapped into the ontology?

## 27.7 Model generation

Which ontology patterns should map to which formalism templates?

## 27.8 Formal verification

Can institutional claims be checked through:

- reachability;
- invariant checking;
- deadlock analysis;
- liveness;
- safety;
- temporal logic;
- probabilistic model checking?

## 27.9 Comparison of ideal types

How should ideological and theoretical prototypes be encoded without hiding contestable assumptions?

## 27.10 Scale and boundary dependence

How can the same system receive different, compatible descriptions at:

- firm level;
- sector level;
- national level;
- transnational level;
- short-run level;
- long-run evolutionary level?

## 27.11 Reflexivity

How should the ontology represent agents who react to descriptions, predictions, classifications, and policies directed at the system itself?

---

# 28. Synthesis

The conversation's main conclusion can be summarized as follows.

There is no universal taxonomy of systems analogous to computational complexity classes. Existing traditions provide important partial structures:

- General Systems Theory contributes cross-domain organizational principles.
- Boulding, Miller, Ackoff, and Checkland contribute system hierarchies and classifications.
- Simon contributes hierarchy and near decomposability.
- Zeigler and DEVS contribute formal model-specification hierarchies.
- Maier and systems engineering contribute operational classifications.
- Ostrom contributes nested institutional and social-ecological schemas.
- Social ontology contributes precise categories of entities and institutions.
- Institutional Grammar contributes formal rule representation.
- Comparative political economy contributes configurational comparison and institutional complementarity.
- Network science contributes relational structure and measurable descriptors.
- Arthur contributes an algorithmic economics of procedures and processes.
- Multi-formalism modeling contributes methods for combining computational representations.

The proposed research program is not a single ladder of system classes. It is a compositional formal language in which:

- systems are described through typed entities, relations, processes, rules, mechanisms, and dynamics;
- attributes are distinguished from capabilities and emergent properties;
- types are defined as logical or graded configurations of descriptors;
- ideological categories are modeled as idealized prototypes;
- observed systems can be mapped into the formal language;
- the ontology serves as an intermediate representation for executable models;
- different system components are rendered in the formalisms best suited to them;
- semantic adapters make heterogeneous model composition explicit.

A compact statement of the project is:

$$
\boxed{
\text{Upper systems ontology}
+
\text{socioeconomic ontology}
+
\text{institutional grammar}
+
\text{relational model}
+
\text{dynamic process model}
+
\text{formalism mappings}
+
\text{analysis tools}
}
$$

This would allow researchers to move from vague labels such as *capitalist*, *communist*, *market-based*, *planned*, *resilient*, or *adaptive* toward explicit descriptions of the system's actual composition and behavior.

---

# 29. Consolidated reference list

## General systems theory and taxonomies

1. General Systems Theory historical overview: <https://pmc.ncbi.nlm.nih.gov/articles/PMC4610108/>
2. Kenneth Boulding, *General Systems Theory—The Skeleton of Science*: <https://www.panarchy.org/boulding/systems.1956.html>
3. Boulding publication record: <https://ideas.repec.org/a/inm/ormnsc/v2y1956i3p197-208.html>
4. James Grier Miller, Living Systems Theory: <https://onlinelibrary.wiley.com/doi/abs/10.1002/bs.3830170102>
5. Checkland / systems theory overview: <https://www.sciencedirect.com/topics/psychology/systems-theory>
6. Mark Maier, Systems of Systems: <https://ideas.repec.org/a/wly/syseng/v1y1998i4p267-284.html>
7. Magee, complex system classification: <https://incose.onlinelibrary.wiley.com/doi/abs/10.1002/j.2334-5837.2004.tb00510.x>
8. Sheard and Mostashari, systems engineering complexity typology: <https://web.mst.edu/lib-circ/files/Special%20Collections/INCOSE2010/A%20Complexity%20Typology%20for%20Systems%20Engineering.pdf>
9. George Klir, *Facets of Systems Science*: <https://link.springer.com/chapter/10.1007/978-1-4615-1331-5_4>

## Formal system models and complexity

10. Zeigler / system specification hierarchy overview: <https://www.mdpi.com/2078-2489/14/1/22>
11. DEVS foundational publication: <https://dl.acm.org/doi/10.1109/32.4640>
12. Herbert Simon, *The Architecture of Complexity*: <https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf>
13. Formal near-decomposability work: <https://arxiv.org/abs/1512.08464>
14. Hierarchical network morphospaces: <https://arxiv.org/abs/1303.2503>
15. Information-theoretic system complexity metric: <https://kiwi.oden.utexas.edu/papers/Complexity-metric-Allaire-He-Deyst-Willcox.pdf>
16. Multivariable information measures: <https://arxiv.org/abs/1302.6932>
17. Petri-net reachability complexity: <https://arxiv.org/abs/1809.07115>
18. Multi-CCS and Petri-net semantics: <https://arxiv.org/abs/1011.6433>

## Systems ontologies and systems engineering

19. Dori and Sillitto, *What Is a System? An Ontological Framework*: <https://incose.onlinelibrary.wiley.com/doi/10.1002/sys.21383>
20. Review of systems engineering ontologies: <https://www.sciencedirect.com/science/article/pii/S0166361518307887>

## Institutions, social ontology, and comparative political economy

21. Ostrom, Social-Ecological Systems framework: <https://pubmed.ncbi.nlm.nih.gov/19628857/>
22. Institutional Grammar 2.0: <https://thecommonsjournal.org/articles/10.5334/ijc.1214>
23. Formal syntax and software for Institutional Grammar: <https://arxiv.org/abs/2505.13393>
24. Social ontology overview: <https://pmc.ncbi.nlm.nih.gov/articles/PMC10092928/>
25. Hall and Soskice, Varieties of Capitalism: <https://hall.scholars.harvard.edu/publications/varieties-capitalism-institutional-foundations-comparative-advantage>
26. Institutional complementarities in comparative political economy: <https://www.researchgate.net/publication/2485542_Varieties_of_Capitalism_and_Institutional_Complementarities_in_the_Political_Economy_An_Empirical_Analysis>

## Algorithmic economics and heterogeneous modeling

27. W. Brian Arthur, *Economics in Nouns and Verbs*: <https://sites.santafe.edu/~wbarthur/Papers/Nouns_Verbs_JEBO.pdf>
28. Alternative Arthur version: <https://sites.santafe.edu/~wbarthur/Papers/Nouns_Verbs_ArXiv.pdf>
29. DEVS and multi-agent modeling: <https://dl.acm.org/doi/10.5555/2872965.2872977>
30. Semantic adaptation in heterogeneous co-simulation: <https://dl.acm.org/doi/10.5555/2872965.2872979>

