# Understanding the AI Ecosystem
## A Beginner's Handbook

**Second (expanded) edition · June 12, 2026** · Market data as of the June 11–12, 2026 closes unless noted. This edition adds three layers the first edition under-served — **networking & optics, systems & data centers, and power & energy** — growing the company universe from 36 to **61**.

---

### About This Handbook

You've used ChatGPT. Maybe you've heard that NVIDIA briefly became the most valuable company in history, that tech giants are spending hundreds of billions of dollars a year on "AI infrastructure," or that a machine in the Netherlands is the only one of its kind on Earth and the entire industry depends on it. This handbook connects those dots.

It assumes **zero technical background**. Every concept is built up from scratch, with analogies before equations (there are no equations). By the end, you will understand what AI actually is, how it's made, which companies make it, how they all depend on one another, and how to think about where it's going.

**How to use it.** Read front to back the first time — the chapters build on each other. Afterward, it works as a reference: Chapter 4 is a company-by-company field guide, and Chapter 8 is a glossary you can return to whenever a term in the news is unfamiliar. Sidebars (marked 📦) are optional deep-dives. Each chapter ends with **Key Takeaways**.

**The companion apps.** This handbook ships with two interactive companions, built on the same data:
- *AI Ecosystem Explorer* (`index.html`) — a 3D map of the core stack: floating layers, the 36 central companies, and the supply lines and money flows between them, with guided tours that retrace this book's main stories.
- *The $725 Billion Machine* (`the-machine.html`) — an interactive essay covering the **full 61-company universe in ten layers**, with live calculators for the two load-bearing questions (can they power it? does the revenue math close?). Chapter 3's machine table and Chapter 4's field guide mirror it section for section.

**Honesty notes.** (1) Facts are cited inline like this: [Source: NVIDIA Q1 FY2027 results, May 20, 2026], with full links in the References. Where something is a company claim or a press report rather than an audited fact, the text says so. (2) AI moves brutally fast; figures are stamped "as of June 2026" because some will be stale within months. (3) Several companies discussed here compete with one another; this handbook profiles strengths *and* weaknesses for all of them and recommends none. **Nothing in this handbook is investment advice.**

---

### Contents

1. **Introduction** — What AI is, where it came from, and why 2026 is a hinge year
2. **Foundations** — The dozen core concepts that explain everything else
3. **The AI Technology Stack** — The ten-layer machine that turns sand into intelligence
4. **The Companies** — A field guide to the public giants (and the private labs)
5. **How Everything Connects** — Supply chains, money loops, and choke points
6. **Trends, Challenges & Outlook** — Energy, regulation, the bubble debate, and jobs
7. **A Practical Guide** — How individuals and businesses can engage today
8. **Glossary, Further Reading & References**

---

# Chapter 1 — Introduction: What Is AI, and Why Now?

## 1.1 A definition you can actually use

**Artificial intelligence (AI)** is software that performs tasks we normally associate with human thinking — understanding language, recognizing images, making predictions, writing, coding, planning — *without being explicitly programmed step-by-step for each task*.

That last clause is the whole trick. Traditional software is a recipe: a programmer writes exact instructions ("if the user clicks here, do this"). AI flips it: instead of writing the recipe, engineers build a system that **learns the recipe itself from examples**. Show it millions of photos labeled "cat" and "not cat," and it figures out what makes a cat a cat. Show it most of the text on the internet, and it figures out how language works — well enough to write a sonnet, a legal summary, or working software.

When people say "AI" in 2026, they usually mean a specific family of systems: **generative AI**, and especially **large language models (LLMs)** like the ones behind ChatGPT, Google's Gemini, and Anthropic's Claude. These are programs that generate new content — text, images, code, video, audio — rather than just classifying or ranking existing content. Chapter 2 explains how they work; for now, hold onto this: *modern AI is learned, not programmed, and learning at this scale requires astonishing amounts of data, electricity, and specialized chips.* That physical reality is what creates the ecosystem this handbook maps.

> **Figure 1 — "Recipe vs. Learner."** *Suggested visual:* a two-panel diagram. Left panel: a flowchart labeled "Traditional software" with a human writing explicit IF/THEN rules feeding a computer. Right panel: "Machine learning" showing a mountain of examples (text, images) flowing into a "training" funnel, out of which comes a model that then answers new questions. Caption: "Classic software is written. AI is grown."

## 1.2 Seventy-five years in five minutes

AI is not new — the current *boom* is. A compressed history explains the pattern of hype, winter, and breakthrough:

- **1950** — Alan Turing publishes "Computing Machinery and Intelligence," proposing his famous test: can a machine converse indistinguishably from a human?
- **1956** — The Dartmouth workshop coins the term "artificial intelligence." Early optimism is wild; money pours in.
- **1970s–80s** — Progress stalls twice. Funding collapses in the "**AI winters**." The lesson: ideas were ahead of the available computing power and data.
- **1986–1997** — Quiet foundations: the "backpropagation" technique makes training neural networks practical; IBM's Deep Blue beats world chess champion Garry Kasparov (1997) — impressive, but narrow.
- **2012** — The modern era begins. A neural network called **AlexNet**, trained on *graphics cards designed for video games*, crushes the field in an image-recognition contest. The recipe of the next 14 years is set: neural networks + big data + GPUs.
- **2016** — DeepMind's AlphaGo defeats Go champion Lee Sedol — a game thought to be a decade away from machine mastery.
- **2017** — Google researchers publish "Attention Is All You Need," introducing the **transformer**, the architecture behind every modern chatbot. (The "T" in ChatGPT.)
- **2020** — OpenAI's GPT-3 shows that simply making transformers *much bigger* makes them *much smarter* — the "scaling laws" era begins.
- **November 30, 2022** — **ChatGPT** launches and reaches 100 million users in two months, the fastest-adopted consumer product in history to that point. AI stops being a research topic and becomes an industry.
- **2023–2024** — GPT-4-class models arrive; NVIDIA passes $1 trillion, then $3 trillion in market value; "reasoning models" that think step-by-step before answering appear.
- **2025** — The year of scale and shocks: China's DeepSeek shows frontier-ish models can be trained cheaply (January); the $500B "Stargate" data-center project launches; GPT-5 ships (August); NVIDIA becomes the first **$5 trillion** company (October) [Source: CNBC, Oct 29, 2025]; Google's Gemini 3 tops the leaderboards (November).
- **2026 (so far)** — Big Tech guides to roughly **$700 billion of combined annual infrastructure spending** [Source: company Q1 2026 earnings calls, Apr 2026]; OpenAI and Anthropic both file confidentially for IPOs [Source: Bloomberg, Jun 8, 2026]; memory-chip makers join the trillion-dollar club; and the market has its first real AI scare — a one-day, $1-trillion-plus chip selloff on June 5 [Source: Seeking Alpha, Jun 5, 2026].

> **Figure 2 — Timeline: 1950–2026.** *Suggested visual:* a horizontal timeline with the events above, drawn so the spacing compresses early decades and expands 2012–2026. Overlay a rising "compute used to train the largest models" curve to show why the recent period is different. Mark the two AI winters as shaded gaps.

## 1.3 Hype vs. reality — both are real

Every technology cycle mixes genuine transformation with froth, and AI in 2026 has plenty of both. A balanced scorecard:

**The reality (verifiable, today):**
- Roughly **900 million people use ChatGPT weekly** [Source: TechCrunch, Feb 27, 2026], and Google reports its systems process **3.2 quadrillion tokens a month** — about 7× more than a year earlier [Source: Google I/O, May 2026].
- **88% of organizations** say they use AI in at least one business function [Source: McKinsey State of AI, Nov 2025]; over **half of U.S. businesses on the Ramp card platform now pay for AI tools** [Source: Ramp AI Index, Mar 2026].
- AI assistants now write a meaningful share of the world's new software code, and frontier models match or beat human experts on roughly half of tested white-collar work products in one benchmark [Source: OpenAI GDPval, Sep 30, 2025].
- The cost to get a fixed level of AI capability has been falling roughly **40× per year** [Source: Epoch AI; Stanford AI Index].

**The hype (also verifiable):**
- An MIT-affiliated study found **95% of corporate generative-AI pilots produced no measurable profit impact** — partly a measurement problem, but a caution nonetheless [Source: MIT NANDA, Aug 2025].
- The leading AI labs **lose billions of dollars a year** building toward the future (OpenAI reported ~$13B of 2025 revenue against much larger spending) [Source: Fortune, Nov 12, 2025].
- Bain estimates the industry would need **~$2 trillion of *annual* AI revenue by 2030** to justify the infrastructure being built — far above any current trajectory [Source: Bain Global Technology Report, Sep 2025].
- Famous investors are publicly short; one chapter of this handbook (6.2) is devoted to the bubble debate.

Both columns are true at once. The dot-com era is the standard analogy, and it cuts both ways: the 2000 crash was real, *and* the internet really did change everything afterward. The useful skill — which this handbook tries to teach — is separating the **physical layer** (chips, fabs, power plants: real, scarce, hard) from the **narrative layer** (valuations, promises: fast-moving, sometimes wrong).

## 1.4 Why 2026 matters

Three forces converged to make this the moment worth understanding:

1. **The capability threshold.** Models crossed from "autocomplete with style" to systems that reason through problems, use tools, browse, and complete multi-step work ("**agents**"). That moved AI from novelty to labor.
2. **The capex supercycle.** Microsoft, Alphabet, Amazon, and Meta alone guided to **$695–725 billion of 2026 capital spending**, up roughly 70%+ from 2025's ~$400B [Sources: company earnings calls Apr 2026; Yahoo Finance, May 2026]. For perspective, that approaches the inflation-adjusted scale of the Apollo program — *every year*. AI infrastructure has become a measurable driver of U.S. GDP growth [Source: Jason Furman / Fortune, Oct 7, 2025].
3. **The political turn.** Chips are now treated like oil: export-controlled, tariffed, smuggled, and summit-negotiated. Electricity has become the binding constraint, and data centers decided real elections in 2025.

The rest of this handbook unpacks each force. First, the concepts.

---

### ✅ Chapter 1 — Key Takeaways
- AI is **learned, not programmed**: systems that acquire skills from examples rather than explicit rules.
- The field is 75 years old, but three ingredients matured together only after 2012: **neural networks, internet-scale data, and gaming chips (GPUs)**.
- ChatGPT (Nov 2022) turned research into an industry; by 2026 the buildout runs at ~$700B/year among four companies alone.
- Hype and reality coexist. Anchor on the physical layer — chips, fabs, electricity — when narratives get loud.

---

# Chapter 2 — Foundations: The Core Concepts

You need about a dozen concepts to read any AI headline intelligently. Here they are, in dependency order — each builds on the last.

## 2.1 Algorithms, and software that learns

An **algorithm** is just a precise procedure — a recipe. **Machine learning (ML)** is the family of algorithms whose output is *another program*: you feed in examples, and out comes a **model** — a learned program that maps inputs to outputs (email → spam/not-spam; photo → caption; question → answer).

Three classic flavors, in plain terms:
- **Supervised learning** — learn from labeled examples ("this is a cat," "this loan defaulted"). Most industrial ML.
- **Unsupervised / self-supervised learning** — find structure in unlabeled data. Crucially, language models are trained self-supervised: the "label" is just *the next word of real text*, so the entire internet becomes free training material.
- **Reinforcement learning (RL)** — learn by trial, error, and reward, like training a dog. Used to make chatbots helpful and polite (see 2.6) and to teach models to reason.

> **Figure 3 — The nesting dolls.** *Suggested visual:* concentric circles. Outermost: "Artificial Intelligence (any machine that mimics cognition)." Inside it: "Machine Learning (learns from data)." Inside that: "Deep Learning (neural networks, many layers)." Innermost, glowing: "Generative AI / LLMs (ChatGPT, Gemini, Claude)." A small separate bubble outside ML labeled "rule-based AI (e.g., 1980s expert systems)" for contrast.

## 2.2 Neural networks — the universal learner

A **neural network** is a web of simple number-crunching units ("neurons") arranged in layers. Each connection has a **weight** — a dial. Information flows in (your photo, your sentence, encoded as numbers), gets transformed layer by layer, and flows out as an answer.

**Training** is the process of turning those dials. The network makes a guess, the guess is compared to the right answer, and an algorithm called backpropagation nudges every dial slightly toward "would have made that guess better." Repeat *trillions* of times. Nobody hand-sets a single dial; the knowledge is in the final configuration of all of them.

Those dials are the famous **parameters**. When you read "a 1-trillion-parameter model," it means: a network with a trillion learned dials. More parameters = more capacity to store patterns — and more chips, electricity, and money to train. (DeepSeek's V4-Pro reportedly has ~1.6 trillion parameters [Source: DeepSeek API docs, Apr 2026]; frontier labs no longer disclose theirs.)

📦 **Sidebar: Why "deep" learning?** "Deep" just means *many layers*. Early networks had 2–3; modern ones have dozens to hundreds. Depth lets networks build concepts hierarchically — edges → shapes → faces → "my grandmother" — the way visual cortex seems to.

## 2.3 Tokens and transformers — how ChatGPT actually works

Language models don't see words; they see **tokens** — chunks of text (roughly ¾ of a word in English) converted to numbers. The model's one and only native skill is: **given a sequence of tokens, predict a plausible next token.** Then append it, and predict the next. And the next. Every essay, poem, and program a chatbot has ever produced was generated one token at a time.

How is next-word prediction enough to produce *reasoning*? Because predicting text well at internet scale forces the model to internalize the things text is *about* — grammar, facts, logic, code, persuasion, chess notation. The skill is humble; the side effects are profound.

The **transformer** (2017) is the architecture that made this work at scale. Its key mechanism, **attention**, lets every token "look at" every other token in the input and decide what's relevant — so in "the trophy didn't fit in the suitcase because *it* was too big," the model attends from "it" back to "trophy." Attention is also why transformers train so well on GPUs: the math is massively parallel.

The amount of text a model can attend over in one go is its **context window** — its working memory. GPT-4 launched with ~8K tokens (a dozen pages); by 2026, **1-million-token windows** (a small library shelf) are standard at the frontier [Source: Anthropic/Google model releases, 2026].

> **Figure 4 — One token at a time.** *Suggested visual:* a conveyor-belt diagram. Input prompt "The capital of France is" enters a stylized transformer block (layers + attention arrows linking words); output distribution shows "Paris 97%, Lyon 1%, …"; chosen token loops back to the input. Caption: "Everything a chatbot says is generated by repeating this loop."

## 2.4 Training vs. inference — the two economies of AI

This distinction quietly organizes the entire industry, so dwell on it:

- **Training** is *building* the model: months of running thousands-to-hundreds-of-thousands of chips in one synchronized job, costing hundreds of millions to billions of dollars per frontier run. Done rarely, by few companies.
- **Inference** is *using* the model: every ChatGPT reply, every Copilot suggestion. Each one is cheap (fractions of a cent to cents) — but it happens **billions of times a day, forever**.

Early in the boom, training dominated spending. By 2026 the balance has tipped: inference — serving nearly a billion weekly chatbot users plus a fast-growing swarm of business agents — is the volume business, and chips are increasingly designed specifically for it (Microsoft's Maia 200, Qualcomm's AI200, Amazon's Inferentia line) [Sources: Microsoft, Jan 26, 2026; Qualcomm, Oct 27, 2025]. A helpful analogy: training is *building the factory*; inference is *running the production line*. Factories are impressive; production lines pay the bills.

> **Figure 5 — Training vs. inference.** *Suggested visual:* split infographic. Left ("Training"): one giant data center, calendar showing months, price tag "$100M–$1B+ per frontier run," few players' logos. Right ("Inference"): millions of phones/laptops, stopwatch showing milliseconds, price tag "~$0.001–0.05 per reply × billions/day." Arrow between them labeled "model weights copied once, served everywhere."

## 2.5 Scaling laws and reasoning — why bigger kept winning

Around 2020, researchers documented something eerie: model capability improves *predictably* as you increase three things together — **parameters, data, and compute**. These "**scaling laws**" turned AI progress from an art into a capital-allocation problem, and they are the single best explanation for the spending you read about: if intelligence scales with compute, then compute is the product, and whoever assembles the most wins.

Two refinements since:
1. **Data quality and post-training matter as much as size.** Labs now spend enormously on curated and synthetic data and on **post-training**: RLHF (reinforcement learning from human feedback — humans rate answers; the model is tuned toward the good ones), instruction-tuning, and safety tuning. This is the difference between a raw internet-prediction engine and a helpful assistant.
2. **Test-time compute.** Since 2024's "reasoning models" (OpenAI's o-series, then everyone), models can be allowed to *think longer at inference time* — generating internal chains of reasoning before answering. Capability now scales on a second axis: not just bigger models, but more thinking per question. This made inference even more compute-hungry — another reason the chip buildout accelerated.

> **Figure 6 — The scaling staircase.** *Suggested visual:* log-scale chart, x-axis "training compute (FLOPs)," y-axis "benchmark performance," with model dots from GPT-2 (2019) through GPT-5.5 / Gemini 3.5 / Claude 5 (2026) climbing a straight line; a second branch line from 2024 labeled "reasoning: thinking longer per answer" climbing off the main line.

## 2.6 Data, hallucinations, and alignment

**Where the knowledge comes from.** Pre-training data is mostly the public internet plus licensed text, code, images, audio — trillions of tokens. The legal status of that ingestion is the subject of landmark litigation (see 6.3): courts so far lean toward "training on lawfully acquired data is fair use, but pirating the data is not" [Source: *Bartz v. Anthropic* ruling, Jun 2025; $1.5B settlement, Sep 2025].

**Why models make things up.** A language model is a *plausibility* engine, not a truth database. When the most statistically plausible continuation is wrong, it states it with perfect confidence — a **hallucination**. Mitigations exist (retrieval from real documents — "RAG"; citations; tool use; reasoning), and rates have fallen, but the failure mode is intrinsic: treat every unverified model claim the way you'd treat a confident colleague's memory.

**Alignment** is the engineering discipline of making models *want* what their users and society want — refusing harmful requests, expressing uncertainty, staying honest under pressure. It matters commercially (an assistant that ignores instructions is useless) and societally (these systems now act in the world). It is the explicit founding focus of Anthropic and a major research area at every lab.

## 2.7 Compute: GPUs, accelerators, and "FLOPs"

📦 **Sidebar: What is a GPU and why did gaming chips take over AI?** A CPU (the chip running your laptop) is a few brilliant generalists — great at doing *one complicated thing* fast. A **GPU** (graphics processing unit) is *tens of thousands of simple workers* — built to color millions of pixels simultaneously for video games. Neural-network math (multiplying huge grids of numbers) is exactly that kind of embarrassingly parallel work. NVIDIA noticed early, and in 2006 released **CUDA**, software letting scientists program GPUs for general math. When deep learning arrived in 2012, the tooling was waiting — the foundation of NVIDIA's still-running dominance. Specialized cousins now exist: Google's **TPUs**, Amazon's **Trainium**, custom "**XPUs**" co-designed with Broadcom, all chasing the same parallel math with different trade-offs.

Compute is measured in **FLOPs** (floating-point operations per second; "flop" ≈ one arithmetic step). Frontier training runs are measured in the *yottaFLOP* range overall (10²⁶ operations is now a regulatory threshold in California law [Source: California SB 53, Sep 2025]). Two practical bottlenecks dominate real systems and explain several companies in Chapter 4:
- **Memory bandwidth** — moving numbers to the math units is harder than the math. Hence **HBM** (high-bandwidth memory): stacks of memory chips bonded directly beside the processor. HBM is why Micron, SK Hynix, and Samsung became central AI players (and, in 2026, trillion-dollar ones).
- **Interconnect** — thousands of chips must act as one computer. Hence NVIDIA's NVLink, InfiniBand, and the Ethernet-switch empire of Broadcom.

## 2.8 From models to agents

A chatbot answers; an **agent** *acts*. Give a model tools (a browser, a code terminal, your calendar API), let it plan multi-step tasks, observe results, and retry — and you get software that can research a market, file the expense report, refactor a codebase, or staff a help desk. Standards like **MCP** (Model Context Protocol, 2024) emerged so any model can plug into any tool. Agents are 2026's main commercial frontier: 62% of organizations report at least experimenting with them [Source: McKinsey, Nov 2025], and "agentic coding" alone is a multi-billion-dollar market (Chapter 4.19). They are also why **inference demand keeps compounding** — an agent may burn thousands of model calls to complete one human request.

---

### ✅ Chapter 2 — Key Takeaways
- A **model** is a program learned from data; its **parameters** are billions of tuned dials. Nobody writes the knowledge in by hand.
- Chatbots generate **one token at a time**; the **transformer**'s attention mechanism made that scale.
- **Training** (build the factory, rare and huge) vs. **inference** (run the line, tiny but billions of times daily) is the industry's central economic split.
- **Scaling laws** — capability rises predictably with compute — are the intellectual justification for the $700B/year buildout; **reasoning** added a second scaling axis at inference time.
- Real systems are bottlenecked by **memory (HBM)** and **networking**, not just raw chip speed — that's why memory makers and Broadcom matter.
- **Hallucination** is intrinsic; verification is a user skill. **Agents** — models that act — are the current frontier.

# Chapter 3 — The AI Technology Stack

## 3.1 The ten-layer machine

Everything in the AI economy fits a layered "stack" — each layer consumes what the one below produces and feeds the one above. If you want it as a slogan, the compressed version is five words long — *hardware → clouds → models → apps* — but the working version this handbook uses has **ten layers**, because four of the decade's biggest investment stories (memory, networking, the boxes-and-buildings trade, and electricity) live in rows the compressed version hides. Hold this picture; Chapter 4 populates it with companies, and the companion apps render it interactively.

> **Figure 7 — The AI Technology Stack.** *Suggested visual:* ten stacked, glowing horizontal slabs, widest at the base, with representative logos on each, and two vertical arrows alongside: "⬆ chips, capacity, intelligence flow up" and "⬇ money flows down." Annotate each layer with its combined market value from the table below (drawn as proportional bars).

Two consistent yardsticks size each row, both computed across this handbook's 61-company universe: **combined market value** (June 11–12, 2026 closes; private labs at last-round valuations) and **combined revenue run-rate** (latest quarter annualized, or full-year guidance — *whole-company* figures, so Amazon includes retail and Apple includes iPhones).

| # | Layer | What it is | Key players | Combined value | Revenue run-rate |
|---|-------|-----------|-------------|---------------:|-----------------:|
| 1 | **Design & Equipment** | Lithography, deposition/etch/inspection tools, chip-design software (EDA), architecture IP | ASML, Applied Materials, Lam, KLA, Synopsys, Cadence, Arm | $2.47T | ~$127B/yr |
| 2 | **Fabrication** | The foundries that print chips | TSMC, Samsung, SMIC | $3.24T* | ~$542B/yr |
| 3 | **Memory & Storage** | HBM feeding the GPUs; hard drives holding the data lakes | SK Hynix, Micron, Western Digital, Seagate (+Samsung) | $2.61T | ~$273B/yr |
| 4 | **Chips & Accelerators** | The processors that run AI math | NVIDIA, Broadcom, AMD, Intel, Qualcomm, Marvell, Monolithic Power | $8.71T | ~$565B/yr |
| 5 | **Networking & Optics** | Switches, lasers, cables — the cluster's nervous system | Arista, Astera Labs, Coherent, Ciena, Credo, Lumentum, Amphenol | $718B | ~$62B/yr |
| 6 | **Systems & Data Centers** | Racks, power rooms, cooling, landlord REITs | Dell, Super Micro, Celestica, Vertiv, Eaton, Equinix, Digital Realty | $762B | ~$287B/yr |
| 7 | **Power & Energy** | Turbines, nuclear PPAs, renewables, reactors | GE Vernova, Constellation, Vistra, NextEra, Talen, Oklo | $597B | ~$144B/yr |
| 8 | **Clouds** | Warehouse-scale computers and the rental model | Microsoft, Amazon, Alphabet, Oracle, CoreWeave, Nebius, IREN | $10.53T | ~$1.59T/yr |
| 9 | **Models & Intelligence** | The labs selling intelligence by the token | OpenAI, Anthropic, DeepMind, Meta MSL, xAI, Mistral, DeepSeek | $2.08T† | ~$56B/yr† |
| 10 | **Applications & Devices** | Where AI meets users: apps, ads, phones, robots | Apple, Meta, Tesla, Palantir, Salesforce, ServiceNow | $7.84T | ~$826B/yr |
| | **Σ The whole machine** | | **61 companies** | **~$39.5T** | **~$4.5T/yr** |

*\*ex-SMIC's HK/STAR listing. †private valuations; revenue counts disclosed lab run-rates only (OpenAI, Anthropic, Mistral). The Σ row double-counts by design — Apple's revenue pays TSMC's, which pays ASML's; the AI-native slice of all of it is the ~$60–70B discussed in Chapter 5.2.*

Read the shape of that table before the company tour — it contains the whole story. The market pays the most for **chips** ($8.7T on $565B of revenue) and **clouds**; the most *revenue* flows through **clouds and devices**; and the **model layer earns the least while being valued like a layer ten times its size** — $2.1T of paper value on ~$56B of disclosed run-rate. Whether that asymmetry resolves upward (revenue grows into the valuations) or downward is the bubble debate of Chapter 6.

Three more observations:

**1. The stack narrows brutally in the middle.** Thousands of companies build applications; *one* company (ASML) makes the most advanced lithography machines, *one* (TSMC) prints ~90% of leading-edge logic chips, *one* (NVIDIA) supplies the overwhelming majority of AI accelerators, *three* (SK Hynix, Samsung, Micron) make all the HBM memory, *two* (Western Digital, Seagate) make the hard drives — sold out into 2027 — and the lasers inside the optics (Lumentum, Coherent) and the gas turbines behind the substations (GE Vernova: queued toward 2030) are sold out too. These narrow waists are where pricing power — and geopolitical risk — concentrate.

**2. Value capture ≠ value creation, layer by layer.** In gold rushes, sell shovels: in 2023–2026 the profit pooled overwhelmingly in layers 1–3 (NVIDIA's gross margin is ~75% [NVIDIA, May 2026]; TSMC's net margin hit 50.5% [TSMC Q1 2026]), while layer 5 labs burn cash to grow and layer 6 fights over margins. History suggests profit pools migrate upward over time — they did for the internet (first Cisco, later Google/Amazon) — which is exactly the bet the labs' investors are making.

**3. The same giants appear on multiple layers.** Google designs chips (TPUs, layer 3), runs clouds (layer 4), trains Gemini (layer 5), and ships apps (layer 6). Microsoft, Amazon, and Meta similarly span 3–6. Vertical integration is the megacap strategy; the pure-plays in between must be exceptional to survive it.

> **Figure 8 — Where the profit pools today.** *Suggested visual:* bar chart of trailing-year operating profit attributable to AI by layer (approximate, 2026): Equipment (~$30B), Fabrication & Memory (~$150B+ in the memory supercycle), Chips (~$160B+, mostly NVIDIA), Cloud (large but offset by depreciation), Models (negative, in aggregate), Applications (small but growing). Caption: "The shovel-sellers are paid first; the question of the decade is whether profits migrate up the stack."

## 3.2 The layer that earned its seat — and the one still missing

The first edition of this handbook treated electricity as a "missing layer." Six months of 2026 made that untenable: **power is now layer 7**, with its own sold-out order books (GE Vernova's ~100 GW turbine queue), its own Big Tech contracts (nuclear plants signed directly to Microsoft, Amazon, and Meta), and its own politics (data-center electricity bills swung the 2025 New Jersey and Virginia elections). Chapter 4.11 profiles the companies; Chapter 6.1 covers the physics and politics.

One input still binds every layer without fitting in any of them: **talent**. A few thousand researchers can train frontier models; compensation packages reported in the hundreds of millions of dollars [Source: TechCrunch, Jun 2025] and the wholesale acqui-hire of Scale AI's CEO by Meta ($14.3B for 49%) show how scarce the skill is.

---

### ✅ Chapter 3 — Key Takeaways
- Ten layers: **equipment → fabrication → memory & storage → chips → networking → systems & data centers → power → clouds → models → applications**. Intelligence flows up; money flows down.
- Two yardsticks size every layer consistently: **combined market value (~$39.5T across the universe)** and **revenue run-rate (~$4.5T, whole-company)** — against which all AI-native revenue is ~$60–70B.
- The middle of the stack is **monopoly-grade choke points all the way down**: one lithographer, one island, three memory makers, two drive makers, sold-out lasers, sold-out turbines.
- The model layer's **valuation-to-revenue asymmetry** ($2.1T on ~$56B) is the central bet of the era; **talent** remains the unlisted input everything depends on.

---

# Chapter 4 — The Companies: A Field Guide

Each profile: what the company does (in plain English), its place in the stack, current numbers, what makes it strong, and what could hurt it. Figures are as of the **June 11–12, 2026 closes** for market caps, and the **latest reported quarter** for financials. Read with Figure 9 (or the companion apps) open.

> **Figure 9 — The 2026 AI ecosystem map.** *Suggested visual:* the full network diagram — companies as circles sized by market cap, colored by stack layer, with arrows for the key supply/investment relationships described below (ASML→TSMC→NVIDIA→clouds→labs→apps, plus memory into NVIDIA and the investment loops). This is precisely what the companion apps render interactively.

## Layers 1–3 — The Foundation: Equipment, Fabrication, Memory & Storage

### 4.1 ASML — the monopoly nobody can replicate
**Veldhoven, Netherlands · ~$699B market cap**

ASML makes **lithography machines** — the instruments that project chip designs onto silicon wafers in lines a few atoms wide. For the most advanced chips there is exactly one supplier on Earth of the required **EUV (extreme ultraviolet)** machines: ASML. Each EUV tool is a bus-sized marvel (a laser vaporizes tin droplets 50,000 times a second to make 13.5nm light; mirrors are the flattest objects ever manufactured) costing ~$200M; the new **High-NA** generation runs ~$400M, and Intel installed the first commercial unit in December 2025 [Source: Tom's Hardware, Dec 2025].

- **Numbers:** Q1 2026 sales €8.8B (+13% YoY), net income €2.8B; 2026 guidance raised to €36–40B [Source: ASML, Apr 15, 2026]. Notably, China fell to 19% of system sales (from 36%) as export rules bite, while Korean memory makers surged to ~45% — the memory boom in one statistic.
- **Why it's a monopoly:** ~25 years and tens of billions in R&D, plus an irreplaceable supplier web (Zeiss optics). U.S.-led export controls ban EUV sales to China entirely — making ASML the single most strategic company in the U.S.–China tech conflict.
- **Strengths:** literal monopoly at the leading edge; every future chip roadmap routes through it; deep backlog.
- **Risks:** export-control whiplash; customer capex cycles; High-NA adoption slower than hoped (TSMC is skipping it for its 2028 node) [Source: TrendForce, Feb 2026]. A quirky 2026 footnote: it's also now the largest shareholder of French AI lab Mistral (€1.3B) — Europe's equipment champion backstopping Europe's model champion.

### 4.2 TSMC — the foundry the world stands on
**Hsinchu, Taiwan · ~$1.84T market cap**

Taiwan Semiconductor Manufacturing Company invented the **foundry** model: it designs no chips of its own, and instead manufactures everyone else's — NVIDIA's GPUs, Apple's iPhone chips, AMD's processors, Broadcom's custom accelerators. If a cutting-edge chip touched your life today, TSMC almost certainly printed it. It holds **~70% of the global foundry market** [Source: TrendForce, Mar 2026] and ~90% of the most advanced nodes.

- **Numbers:** Q1 2026 revenue $35.9B (+40.6% YoY) with a staggering **50.5% net margin**; high-performance computing (read: AI) is 61% of revenue; 2026 capex $52–56B [Source: TSMC Q1 2026 results, Apr 16, 2026]. May 2026 monthly revenue set another record (+30% YoY) [Source: TSMC, Jun 10, 2026].
- **Technology:** 2-nanometer (N2) production began late 2025 — Apple took most early capacity; A16 follows in 2H 2026. Equally important is **advanced packaging (CoWoS)** — the technique of bonding GPU + memory stacks together — which was *the* AI bottleneck of 2023–25; capacity roughly doubled in 2025 and is on track to nearly double again in 2026 [Source: TrendForce, Apr 2026].
- **Geography:** $165B committed to Arizona fabs (one operating, two more accelerated to 2027), but Taiwan keeps the leading edge under its "N-2" policy — the most advanced two generations stay home [Sources: Focus Taiwan, Jan 2026; New Bloom, Oct 2025]. That concentration is the famous **"silicon shield"** — and the single largest physical risk in the global economy (Chapter 5.4).
- **Strengths:** scale, yield, and trust no competitor matches; effectively *both* major AI chip rivals (NVIDIA and AMD) and the hyperscalers' custom chips all route through it.
- **Risks:** Taiwan-strait geopolitics (China's largest exercises in years ran December 2025–January 2026 [Source: Al Jazeera, Jan 2026]); U.S. tariff pressure; N2 margin dilution; single-customer concentration (NVIDIA).

### 4.3 Memory & storage: the supercycle layer
**SK Hynix ~$1.08T · Micron ~$1.12T · Samsung ~$1.4T · Western Digital ~$195B · Seagate ~$210B**

AI's dirty secret: the math units spend much of their time *waiting for data*. The fix is **HBM (high-bandwidth memory)** — DRAM chips stacked vertically and bonded beside the GPU. Only three companies on Earth can make it, and AI demand for HBM plus server DRAM has crowded out ordinary memory production so badly that **conventional DRAM contract prices roughly doubled in Q1 2026 alone** (+90–95%), with another +58–63% forecast in Q2 [Source: TrendForce, Feb–Mar 2026]. Gartner expects memory+SSD prices up ~130% by end-2026, raising average PC prices ~17% [Source: TechTimes/Gartner, Jun 2026]. Your next laptop costs more because of ChatGPT.

- **SK Hynix** is the HBM leader (~50–60% share, ~⅔ of NVIDIA's next-gen HBM4 orders [Source: TrendForce, Jan 2026]). Its Q1 2026: revenue ₩52.6T (+198% YoY) at an oil-state **72% operating margin**; it crossed **$1 trillion in market value in May 2026** [Source: CNBC, Apr 23 / May 27, 2026]. Its 2026 HBM supply: sold out.
- **Micron** — the only U.S. memory maker — reported fiscal-Q2 revenue of $23.9B (+196% YoY) and guided next quarter to **~81% gross margin**, numbers without precedent in memory history; it too joined the trillion-dollar club [Source: CNBC, Mar 18, 2026; stockanalysis.com, Jun 11, 2026].
- **Samsung Electronics** — the conglomerate (memory + foundry + phones) — posted record Q1 2026 revenue of ₩133.9T with operating profit up **~8×** YoY, more than its entire 2025; its HBM4 finally qualified at NVIDIA, and its foundry won Tesla's $16.5B AI6 chip deal for its Texas fab [Sources: Samsung Newsroom, Apr 2026; TechPowerUp, Apr 2026; CNN, Jul 2025].

**The storage duopoly (new to this edition).** One level below DRAM sits an even tighter squeeze: AI data lakes broke the **hard-drive** market. Only two companies make the high-capacity "nearline" drives clouds store training data on, and both are effectively out of stock: **Western Digital** ("pretty much sold out" for calendar 2026, gross margin a once-unthinkable 50.5%, stock **+924%** in twelve months) and **Seagate** (supply "largely allocated through calendar 2027," shipping its next-gen HAMR drives, **+618%**) [Sources: WDC FQ3 2026 call, Apr 30, 2026; Seagate FQ3 2026 call, Apr 28, 2026; stockanalysis.com, Jun 12, 2026]. Industry lead times passed 52 weeks and contract prices rose at the fastest pace in eight quarters [Source: TrendForce, Sep 2025]. Two of the five best-performing large caps of the AI era turned out to be the companies that make spinning rust — nobody's 2024 AI thesis included that.
- **Risks for all five:** memory and storage are history's most violently cyclical industries — supercycles end; massive capacity additions arrive 2027–28; NAND/QLC-flash substitution stalks the drive makers; China's CXMT is building domestic HBM (slowly) [Source: DigiTimes, Apr 2026].

> **Figure 10 — The HBM sandwich.** *Suggested visual:* exploded 3D diagram of an AI accelerator package: silicon interposer base (labeled "TSMC CoWoS packaging"), GPU die center (labeled "NVIDIA, designed in California"), flanked by 8 towers of stacked DRAM dies (labeled "HBM4 — SK Hynix / Samsung / Micron"), with callouts: "memory moved next door to the processor because the commute was the bottleneck."

## Layer 4 — The Chip Designers

### 4.4 NVIDIA — the sun the system orbits
**Santa Clara, CA · ~$4.96T market cap (world's largest company)**

NVIDIA designs the GPUs that train and run most of the world's AI — and, just as decisively, the **software** (CUDA) and **networking** (NVLink, InfiniBand, Spectrum-X Ethernet) that make 100,000 GPUs behave like one computer. It manufactures nothing itself (TSMC does that), yet captures the largest profit pool in technology.

- **Numbers that strain belief:** fiscal Q1 2027 (Feb–Apr 2026) revenue **$81.6B, up 85% YoY**, of which data center $75.2B; gross margin ~75%; guidance for next quarter **$91B** [Source: NVIDIA Q1 FY27 results, May 20, 2026]. Full fiscal-2026 revenue was $215.9B — roughly *quadruple* two years prior. Networking alone (~$15B/quarter, tripled YoY) would be a Fortune-100 company.
- **Products:** the Blackwell generation (GB300) is the current workhorse; the next platform, **Vera Rubin**, entered full production with shipments beginning H2 2026 — claiming up to dramatically higher inference throughput per rack [Source: NVIDIA GTC, Mar 2026]. The cadence is now one platform per year, each requiring new HBM generations and more CoWoS — pulling the whole stack along.
- **Market position:** analysts put NVIDIA at **~75–90% of AI accelerator revenue** depending on year and method [Sources: TechInsights; analyst estimates 2026] — eroding slowly as AMD and custom chips scale, from a base so high it hardly matters yet.
- **The moat:** 20 years of CUDA software; every AI framework optimized for it first; switching costs measured in engineer-years. Plus annual product cadence and allocation power over scarce HBM/CoWoS supply.
- **Entanglements (important):** NVIDIA invests in its own customers — up to $10B in Anthropic, $5B in Intel (closed Dec 2025), a stake in xAI's chip-buying vehicle, and a famous **up-to-$100B letter of intent with OpenAI that, as of mid-2026, remains non-binding and reportedly "on ice"** [Sources: Microsoft/NVIDIA/Anthropic announcement, Nov 18, 2025; Reuters, Dec 2025; press reports, Jan–Mar 2026]. Critics call this circular revenue; Chapter 5.3 weighs the debate.
- **Risks:** China revenue is effectively **zero** (export politics — Chapter 5.4); customers becoming competitors (Google TPU, Amazon Trainium, OpenAI/Broadcom chips); valuation that prices in years of flawless execution; memory/packaging supply.
- **Recent stress test:** on June 5, 2026, a soft AI-revenue guide *from Broadcom* erased >$1T from chip stocks in a day, NVIDIA included (−6%) [Source: Seeking Alpha, Jun 5, 2026] — a reminder that the whole complex now trades as one nervous organism.

### 4.5 Broadcom — the other winner, hiding in plain sight
**Palo Alto, CA · ~$1.83T market cap**

Broadcom is two businesses: an infrastructure-software arm (VMware) that prints cash, and the semiconductor arm that has quietly become **the arms dealer of the anti-NVIDIA resistance**. When a hyperscaler wants its *own* AI chip instead of paying NVIDIA's margins, Broadcom co-designs and delivers it: Google's TPUs (a decade-long partnership), Meta's MTIA, **OpenAI's 10-gigawatt custom-chip program** (silicon delivered, production late 2026) [Source: Broadcom Q2 FY26 call, Jun 3, 2026], and a multi-gigawatt Anthropic TPU arrangement. It also dominates the Ethernet switch silicon (Tomahawk) connecting all those chips.

- **Numbers:** Q2 FY2026 revenue $22.2B (+48%); **AI semiconductor revenue $10.8B, up 143% YoY**; full-year AI revenue guided to ~$56B, and management pointed to **>$100B in fiscal 2027** [Source: Broadcom Q2 FY26 results, Jun 3, 2026].
- **Strengths:** every credible custom-silicon program routes through it or Marvell; networking is layer-agnostic (it wins whoever's accelerator wins); software cash flows cushion cycles.
- **Risks:** extreme customer concentration (a handful of hyperscalers + OpenAI, whose own finances are unproven); the June 5 selloff was triggered by *its* guidance missing sky-high expectations — expectations risk is now its biggest risk.

### 4.6 AMD — the credible challenger
**Santa Clara, CA · ~$796B market cap**

AMD is the only company with a full merchant alternative to NVIDIA's stack: Instinct GPUs (MI350 today; **MI400-series with the rack-scale "Helios" system launching H2 2026**), EPYC server CPUs, and an open software layer (ROCm). For years the knock was software maturity and scale; 2025–26 brought the validating customer: **OpenAI signed for 6 gigawatts of AMD accelerators**, taking warrants for up to ~10% of AMD stock as deployment milestones hit — an extraordinary structure that aligns OpenAI with AMD's success [Source: AMD press release & 8-K, Oct 6, 2025]. Oracle followed with an order for 50,000 MI450s [Source: Oracle, Oct 14, 2025].

- **Numbers:** Q1 2026 revenue $10.25B (+38%), data center $5.8B (+57%) [Source: AMD Q1 2026 results, May 5, 2026]. Still mid-single-digit share of AI accelerators — but the 2H 2026 Helios ramp is the real test.
- **Strengths:** proven silicon execution under Lisa Su; the only merchant #2; OpenAI/Oracle anchor demand.
- **Risks:** NVIDIA's annual cadence and CUDA gravity; the OpenAI warrant dilutes shareholders if it works and embarrasses if it doesn't; depends on the same scarce TSMC/HBM supply as everyone.

### 4.7 Intel — the fallen king's strange comeback
**Santa Clara, CA · ~$588B market cap (+~550% in 12 months)**

Intel dominated computing for 40 years, then missed mobile, then AI, and by 2024 was in genuine crisis. What followed is one of the strangest corporate rescues in U.S. history: the **U.S. government converted CHIPS Act grants into a ~10% equity stake** (Aug 2025), **NVIDIA invested $5B** (closed Dec 2025) alongside a partnership putting Intel x86 chiplets inside NVIDIA systems, SoftBank added $2B — and the stock rose ~550% in a year [Sources: CNBC, Aug 22, 2025; Reuters, Dec 2025; stockanalysis.com, Jun 11, 2026].

- **Substance behind the squeeze:** the **18A process node is real** — Panther Lake laptop chips built on it have shipped since January 2026, with yields improving; the next node (14A) is courting external customers including, reportedly, decisions from major designers in late 2026 [Source: Intel Q1 2026 results, Apr 23, 2026; trade press]. Q1 2026 revenue $13.6B (+7%), still GAAP-unprofitable.
- **Why it matters to the ecosystem:** Intel is the only plausible **U.S.-soil, U.S.-flag leading-edge foundry** — the strategic hedge against the Taiwan concentration. That's precisely why Washington owns a tenth of it.
- **Risks:** foundry economics remain brutal (it loses money making chips mostly for itself); its own AI accelerator line (Crescent Island, 2027) is far behind; the stock now prices a turnaround that is still mostly promise.

### 4.8 Quick profiles: Qualcomm, Arm, Marvell, Monolithic Power
- **Qualcomm (~$214B):** the mobile-chip king (every premium Android phone) is entering the data-center fray with **AI200/AI250 inference racks**, first deployments 2026, anchored by Saudi Arabia's Humain. Its fiscal Q2 2026 ($10.6B revenue, −3% YoY, record automotive +38%) showed the core handset business under pressure from memory costs — the data-center option is the growth story [Sources: Qualcomm FQ2 2026 results, Apr 29, 2026; Qualcomm, Oct 27, 2025].
- **Arm (~$366B):** doesn't make chips — licenses the instruction-set architecture inside ~99% of smartphones, and now the CPUs in AWS Graviton, NVIDIA Grace, and Microsoft Cobalt. Fiscal 2026 revenue $4.9B (+23%); data-center royalties doubled; it's now designing its own server CPU (>$2B of demand booked) — a fateful step from referee toward player [Source: Arm FY26 results, May 2026].
- **Marvell (~$246B):** the quieter #2 custom-silicon house (Amazon's Trainium line is its anchor); record Q1 FY27 revenue $2.42B, 76% from data center [Source: Marvell, May 27, 2026].
- **Monolithic Power (~$78B):** the stealth chip story of the rack era — voltage regulators and vertical power-delivery modules feeding kilowatt-class GPU sockets. Its enterprise-data segment grew **+98% YoY** in Q1 2026, and it's sampling 800-volt parts for NVIDIA's next-generation rack architecture (where Texas Instruments and Infineon are attacking the same sockets) [Sources: MPS Q1 2026 results, Apr 30, 2026; TI, Mar 16, 2026].

## Layer 5 — The Nervous System: Networking & Optics

### 4.9 Seven companies wiring the clusters together

A 100,000-GPU cluster is only as smart as its wiring: every chip must talk to every other chip at terabit speeds, or the whole machine idles. That unglamorous fact produced the wildest stock charts of the AI era — because the wiring, like everything else in this book, turned out to be supply-constrained. The layer splits into three jobs:

**Switching (the traffic cops).** **Arista Networks (~$207B, +78% in 12 months)** supplies the Ethernet switches running hyperscaler AI fabrics — Microsoft and Meta are anchor customers — and raised its 2026 AI revenue target to $3.5B as a fourth major customer defected from NVIDIA's InfiniBand to Ethernet at production scale; its constraint is silicon supply (52-week lead times), not demand [Source: Arista Q1 2026 results, May 5, 2026]. (Broadcom's Tomahawk switch chips, profiled in 4.5, sit inside many competing boxes — the layer's other toll collector.)

**Optics (the light).** Between racks, data travels as light through transceivers — and the lasers inside them became 2026's scarcest component. **Lumentum (~$72B)** grew revenue 90% YoY with its EML lasers *sold out* and rode the squeeze to a **+959%** twelve-month return — the single best chart in the ecosystem; **Coherent (~$75B, +519%)** grew datacom revenue 40% on vertically-integrated laser capacity; **Ciena (~$64B, +524%)** carries AI traffic *between* data centers — its coherent-optics business grew 40% and it raised fiscal-2026 guidance to +32% just last week [Sources: Lumentum FQ3 2026, May 5; Coherent FQ3 2026, May 6; Ciena FQ2 2026, Jun 4, 2026].

**Interconnect (the copper and glue).** Inside the rack: **Astera Labs (~$64B, +305%)** sells the retimers and fabric switches that let GPUs share memory across NVIDIA racks (+93% YoY); **Credo (~$47B, +338%)** dominates the "active electrical cables" lashing GPUs to switches — fiscal-2026 revenue grew **+206%** at 68% gross margins; and **Amphenol (~$189B)**, the quiet giant of connectors, booked $9.4B of orders in a single quarter with IT-datacom now 41% of sales [Sources: Astera Q1 2026, May 5; Credo FQ4 2026, Jun 1; Amphenol Q1 2026, Apr 29, 2026].

- **Why this layer matters to a beginner:** networking is ~10–15% of an AI data center's cost but determines whether the other 85% performs. And it's the cleanest demonstration of the era's pattern — *every* physical input to AI, even cables, eventually goes sold-out.
- **Layer risks:** these are the highest-multiple stocks in the ecosystem (Lumentum ~175× trailing earnings; Astera ~255×); optics is a historically boom-bust industry; and a single hyperscaler digestion pause hits everyone at once.

> **Figure 11a — Anatomy of a cluster's wiring.** *Suggested visual:* cutaway of two AI racks and the aisle between them: copper AECs inside the rack (Credo/Amphenol), optical transceivers with laser chips at the rack top (Lumentum/Coherent), Ethernet switches above (Arista/Broadcom), and long-haul coherent optics leaving the building (Ciena) — each labeled with its 12-month stock move to show where scarcity priced in.

## Layer 6 — Systems & Data Centers

### 4.10 Boxes, buildings, and landlords

Somebody has to bolt the machine together, keep it cool, and own the floor it stands on.

**The box builders.** **Dell (~$259B, +243%)** became the largest branded AI-server company almost overnight: **$24.4B of AI-server orders in a single quarter**, a ~$51B backlog, and fiscal-2027 AI-server revenue guided to ~$60B — constrained, like everyone, by memory supply [Source: Dell FQ1 2027 results, May 28, 2026]. **Super Micro (~$18.5B, −31%)** is the cautionary tale of the same trade: revenue +123% but gross margins near 10% — speed-to-market is a real edge with a thin moat. **Celestica (~$44B, +225%)** builds the hyperscalers' switches and custom compute as an ODM, raising 2026 guidance to $19B on 800G→1.6T network upgrades [Sources: SMCI FQ3 2026, May 5; Celestica Q1 2026, Apr 28, 2026].

**The building outfitters.** Inside every data hall, two companies dominate the electrical-and-thermal plumbing: **Vertiv (~$116B, +172%)** — power distribution, UPS, and the liquid cooling that 130-kilowatt racks made mandatory; backlog +109% to $15B, book-to-bill 2.9×, and co-designer (with NVIDIA) of the 800-volt architecture for 2027's racks — and **Eaton (~$154B)**, whose electrical backlog grew 48% with data-center orders up ~240%; management's arithmetic: the U.S. data-center pipeline equals **12 years of demand** at 2025 build rates [Sources: Vertiv Q1 2026, Apr 22; Eaton Q1 2026, May 5, 2026].

**The landlords.** **Equinix (~$104B)** — the interconnection hub where 8 of the top-10 model providers meet the clouds — and **Digital Realty (~$66B)**, which just signed the largest lease in its history (200MW, for AI inference) and has 1.2GW under construction, 61% pre-leased. Both now ration growth on the same constraint as everyone else: **grid connections**, not customer demand [Sources: Equinix Q1 2026, Apr 29; Digital Realty Q1 2026, Apr 23, 2026].

- **Layer risks:** EMS/OEM margins are structurally thin (the value accrues to chip suppliers above and landlords below); REIT economics strain against rising capital costs; and all of it is a direct derivative of hyperscaler capex plans.

## Layer 7 — The Power Layer

### 4.11 Utilities, turbines, and reactors — where AI meets the grid

The layer Wall Street discovered last, and the one this handbook's first edition under-served. Once chips stopped being the bottleneck, electrons became it (Chapter 6.1 has the macro numbers); these are the companies on the other side of that trade:

**The equipment maker.** **GE Vernova (~$252B, +91%)** is the pickaxe-seller of the power buildout: its heavy-duty gas-turbine queue reached **~100 GW** — slots effectively sold out toward 2030 — and its grid-equipment unit booked more data-center orders in Q1 2026 than in all of 2025 [Source: GE Vernova Q1 2026 8-K, Apr 22, 2026]. You cannot build a data center faster than you can buy a turbine; right now, that's years.

**The nuclear fleet, contracted to Big Tech.** The signature deals of the era: **Constellation (~$90B)** is restarting Three Mile Island (the 835MW "Crane" unit) for Microsoft — on track for 2027 — and supplying Meta 1.1GW from Clinton; post its Calpine acquisition it's the largest clean-baseload owner in America, with Q1 revenue +64% [Source: CEG Q1 2026, May 11, 2026]. **Vistra (~$50B)** signed 20-year deals selling Meta **2.6 GW** of nuclear from its PJM fleet [Source: Vistra, Jan 9, 2026]. **Talen (~$16B, +29%)** sends Amazon **1.92 GW** from Susquehanna through 2042 — roughly $18B of contracted revenue anchoring an AI campus [Source: Talen, Jun 11, 2025]. The pattern: hyperscalers stopped buying *power* and started buying *power plants' output for decades*.

**The builders of new supply.** **NextEra (~$179B)** — America's renewables giant — holds a record 33 GW backlog and was selected to develop 9.5 GW of gas generation under the U.S.–Japan investment framework [Source: NEE Q1 2026, Apr 23, 2026]. And at the speculative frontier, **Oklo (~$10B)** — pre-revenue, ~$2.5B in cash — holds ~14 GW of *letters of intent* (Switch, Meta, Equinix) for small modular reactors whose first unit is now targeted for 2028 [Source: Oklo Q1 2026, May 12, 2026]. SMRs are the option everyone wants and no one has yet collected on.

- **Why this layer matters to a beginner:** it's the clearest case of AI demand colliding with physical-world lead times — turbines take years, reactors take a decade, transmission lines take longer. When you read "capacity constrained" in a cloud earnings call, this layer is why.
- **Layer risks:** utility stocks carry regulatory and rate-payer politics (PJM's record capacity auctions are already a campaign issue); merchant generators swing with weather and gas prices; Oklo-style SMR plays are venture bets wearing utility costumes; and if AI capex pauses, a 100-GW turbine backlog becomes a liability.

> **Figure 11b — Who powers whom.** *Suggested visual:* a map of the eastern U.S. grid (PJM highlighted) with arrows from named plants to named buyers: Three Mile Island/Crane → Microsoft (835MW, 2027), Susquehanna → Amazon (1.92GW, through 2042), Clinton + Perry/Davis-Besse → Meta (1.1GW + 2.6GW), plus a Texas inset (Vistra/Comanche Peak, NextEra hubs) and a "queued turbines: ~100GW" badge over a GE Vernova factory icon.

## Layer 8 — The Cloud Giants

The "hyperscalers" rent computing by the hour. They are AI's distribution system — and its biggest spenders: their combined 2026 capital budgets (~$695–725B) exceed the GDP of Belgium.

### 4.12 Microsoft — the enterprise toll road
**Redmond, WA · ~$2.90T market cap**

Microsoft turned an early, audacious bet — $1B into OpenAI in 2019, ~$13B+ since — into the strongest enterprise-AI position in the world: Azure rents the infrastructure, Copilot sells AI inside Office/Windows/GitHub, and Microsoft holds **~27% of OpenAI itself** (valued ~$135B at the October 2025 restructuring, which also committed OpenAI to purchase $250B of Azure and gave Microsoft model rights into the 2030s) [Source: Microsoft–OpenAI announcement, Oct 28, 2025].

- **Numbers:** FY26 Q3 (Jan–Mar 2026): revenue $82.9B (+18%); Azure +40%; **AI business run-rate $37B, +123% YoY**; commercial backlog (RPO) **$627B** [Source: Microsoft FY26 Q3 results, Apr 29, 2026]. Calendar-2026 capex guided to ~$190B — raised $25B *just to cover memory-price inflation* [Source: CNBC, Apr 29, 2026].
- **Copilot:** 20M+ paid Microsoft 365 Copilot seats (of 450M commercial seats — the upsell runway is the bull case) [Source: TechCrunch, Apr 29, 2026].
- **Silicon & models:** its Maia 200 inference chip entered production (Jan 2026), and post-restructuring Microsoft is openly building frontier models in-house (the MAI family — seven models unveiled at Build 2026) while also investing up to $5B in **Anthropic**, which committed $30B to Azure — Microsoft now profits whichever lab wins [Sources: Microsoft, Jan 26 / Nov 18, 2025; GeekWire, Jun 2026].
- **Strengths:** distribution into every enterprise on Earth; the OpenAI stake; balance sheet.
- **Risks:** it slipped to the *third*-largest company as investors questioned capex-to-revenue conversion; OpenAI's independence cuts both ways; $190B/year must eventually show up in earnings, not just backlog.

### 4.13 Alphabet (Google) — the vertically integrated one
**Mountain View, CA · ~$4.37T market cap (now #2, behind only NVIDIA)**

For two years the market's story was "AI kills Google search." 2025–26 flipped the script: Gemini 3 (Nov 2025) topped benchmarks, the Gemini app passed ~750M monthly users, AI Mode in Search passed 1B monthly users, search revenue *kept growing*, and Alphabet became the second company ever to cross **$4 trillion** (Jan 12, 2026) — helped by news that **Apple chose Gemini to power the new Siri** [Sources: Alphabet Q1 2026 results, Apr 29, 2026; CNBC, Jan 12, 2026].

- **Numbers:** Q1 2026 revenue $109.9B (+22%); Google Cloud $20.0B (+63%) with backlog **$462B** (nearly doubled in a quarter); 2026 capex $180–190B [Source: Alphabet Q1 2026, Apr 29, 2026].
- **The unique asset — TPUs:** Google is the only player with frontier models *and* its own frontier chips (TPU v7 "Ironwood," built with Broadcom) *and* its own global cloud. It now sells TPU capacity externally — ~1GW+ to Anthropic, and reportedly to Meta — directly attacking NVIDIA's monopoly margin [Sources: DCD, Oct 2025; SiliconANGLE, Feb 2026].
- **Also inside Alphabet:** DeepMind (the research lab — Chapter 4.19), Waymo (500K+ paid robotaxi rides weekly across 11 cities — the largest physical-AI deployment anywhere) [Source: TechCrunch, Mar 2026], YouTube, Android.
- **Strengths:** full-stack integration nobody else has; research pedigree; distribution to billions.
- **Risks:** the antitrust remedies (data-sharing with rivals) are under appeal [Source: DOJ, Sep 2025]; AI answers still cannibalize some search economics; capex discipline.

### 4.14 Amazon — the quiet arms-and-armory play
**Seattle, WA · ~$2.60T market cap**

Amazon's AWS invented the cloud and remains its largest landlord (28% share [Source: Synergy Research, Q1 2026]). Its AI strategy is characteristically unglamorous and characteristically shrewd: be the *neutral utility* — every model available for rent (Bedrock), plus its own cheap silicon (**Trainium**), plus a deep alliance with Anthropic (now **up to ~$33B invested**, with Anthropic committing **>$100B of AWS spending** and AWS building it "Project Rainier," a 500K+-chip supercomputer) [Sources: TechCrunch/CNBC, Apr 20, 2026; Amazon Q1 2026 call].

- **Numbers:** Q1 2026: revenue $181.5B; **AWS $37.6B, +28% — its fastest growth in 15 quarters**; AWS backlog $364B *before* counting the new Anthropic deal; 2026 capex ~$200B, the largest of anyone [Source: Amazon Q1 2026 results, Apr 29, 2026].
- **Silicon:** the in-house chip line (Graviton CPUs, Trainium accelerators) is already a **>$20B-a-year business growing triple digits** [Source: Amazon Q1 2026 call] — the strongest evidence that custom silicon genuinely works at scale.
- **Consumer AI:** Alexa+ relaunched free for Prime members across the U.S. (Feb 2026).
- **Strengths:** the most workloads, the most pragmatic strategy, silicon that actually ships at volume.
- **Risks:** free cash flow collapsed ~95% under capex weight [Source: Amazon Q1 2026]; it owns no frontier lab outright; if AI rewires how software is built, the "rent primitives" model must evolve.

### 4.15 Oracle — the leveraged bet
**Austin, TX · ~$530B market cap**

Oracle, the 1970s database company, made the most aggressive wager in enterprise history: it borrowed tens of billions to build GPU data centers largely for **one customer — OpenAI** (a reported ~$300B, five-year contract; Oracle is the operating partner of Stargate's flagship Abilene, Texas campus). The reward: backlog (**RPO $638B**, up 363% YoY) and OCI infrastructure revenue +93% in the just-reported Q4 FY26 [Source: Oracle Q4 FY26 results, Jun 10, 2026]. The price: **negative free cash flow, ~$125B of debt and rising, a Moody's negative outlook, and a stock that round-tripped from +36%-in-a-day euphoria (Sep 2025) to −47% below its peak** — including an 8.5% drop the day before this handbook's data cut, on news it will raise another ~$40B [Sources: CNBC, Jun 10, 2026; Yahoo Finance, Jun 11, 2026; Bloomberg, Sep 2025].

Oracle is the ecosystem's cleanest test of one question: *is an AI-era backlog from a money-losing customer an asset or a liability?* Bulls see locked-in growth; bears see concentration risk wearing a toga. Watch it as a leading indicator for AI credit broadly.

📦 **Sidebar — CoreWeave and the "neoclouds."** A new species: clouds that *only* rent GPUs. **CoreWeave** (~$52B market cap) grew Q1 2026 revenue 112% to $2.1B and holds a **$99.4B contract backlog** (OpenAI ~$22B; Meta ~$35B) — financed with GPU-collateralized debt, a structure that worried enough people that its $8.5B facility earning an investment-grade rating in 2026 was itself news [Sources: CoreWeave Q1 2026, May 7, 2026; CoreWeave IR, 2026]. The peers are no longer footnotes: **Nebius (~$60B, +367%)** grew Q1 revenue **+684%** on a $17.4B Microsoft contract and a backlog approaching $50B, with 2026 capex of $20–25B against under $1B of trailing revenue; **IREN (~$21B, +649%)** converted Bitcoin-mining power sites into a $9.7B Microsoft GPU-cloud contract plus $5.6B of NVIDIA deals [Sources: Nebius Q1 2026, May 13, 2026; IREN FQ3 2026, May 7, 2026; IREN, Nov 3, 2025]. Neoclouds are the ecosystem's high-beta tissue: first to feast in booms, first to starve in droughts.

## Layer 10 — Platforms, Devices, Applications

*(Layer 9 — the model labs — gets its own section, 4.19, because the biggest ones are private.)*

### 4.16 Meta — the in-house consumer
**Menlo Park, CA · ~$1.44T market cap**

Meta is AI's biggest *internal* customer: ranking and recommendation models drive its $56B-a-quarter ad machine (Q1 2026, +33% YoY — AI-driven ad improvements are explicitly credited on earnings calls), and Meta AI rides inside WhatsApp/Instagram/Facebook's ~3.5B users [Source: Meta Q1 2026 results, Apr 29, 2026]. Strategically, 2025–26 brought a dramatic pivot: after its open-source Llama 4 disappointed, Mark Zuckerberg spent **$14.3B on Scale AI to hire Alexandr Wang**, built "Meta Superintelligence Labs" with nine-figure pay packages, **shipped its first closed frontier model ("Muse Spark," April 2026) — ending its open-weights era at the frontier** — and cut ~8,000 jobs in an AI-driven restructuring (May 2026) [Sources: CNBC, Jun 12, 2025 & Apr 8, 2026; NPR, May 20, 2026].

- **Infrastructure:** 2026 capex $125–145B; gigawatt-scale data centers (Hyperion, Louisiana — ~5GW design; Prometheus, Ohio) financed with novel structures — a $27B Blue Owl private-credit JV plus a record $30B bond sale [Sources: Meta/Blue Owl, Oct 21, 2025; Bloomberg, Oct 30, 2025].
- **Strengths:** distribution (a third of humanity daily), proven AI→revenue loop in ads, Ray-Ban AI glasses tripling usage YoY.
- **Risks:** the superintelligence org is openly turbulent (leadership reshuffles, the Llama→closed whiplash); it spends hyperscaler money without a cloud business's revenue; stock −11% YTD reflects the doubt.

### 4.17 Apple — the patient distributor
**Cupertino, CA · ~$4.34T market cap**

Apple spent 2023–25 labeled the AI laggard, and ended up with the last laugh of the cycle so far: rather than build frontier models, it **rented one — Google's Gemini, in a reported ~$1B/year deal — to power the rebuilt Siri**, running on Apple's own Private Cloud Compute servers for privacy [Sources: CNBC, Jan 12, 2026; Bloomberg, Nov 2025]. Meanwhile the iPhone 17 cycle boomed (FQ2 2026: revenue $111.2B, +17%; iPhone +22%), services hit records, and the stock sits near all-time highs while big spenders derated [Source: Apple FQ2 2026 results, Apr 30, 2026]. The new Siri and a dedicated AI app eco arrive with iOS 27 (previewed at WWDC, June 9, 2026 — the same event where **Tim Cook announced he hands the CEO role to hardware chief John Ternus on Sept 1, 2026**) [Source: TechCrunch, Jun 9, 2026].

- **The strategic read:** Apple owns the *edge* — 2B+ devices with its own M-series/A-series silicon (fabbed by TSMC) capable of running small models locally — and pays ~$14B/year of capex versus rivals' $200B. If AI value accrues to whoever owns the customer relationship and the device, Apple wins without ever training a frontier model.
- **Risks:** dependence on a direct rival (Google) for its assistant's brain; tariff exposure; the risk that agents, not apps, become the interface — weakening the App Store toll booth.

### 4.18 Palantir, Tesla, and the enterprise-software question

**Palantir (~$314B):** the purest *application-layer* AI bet among large caps. It builds operational AI systems for governments (defense, intelligence — including major U.S. Army and NATO programs) and enterprises (its AIP platform). Q1 2026 was extraordinary by software standards — **revenue +85% YoY, U.S. commercial +133%, a "Rule of 40" score of 145** — and the stock *still fell*, because it trades at ~100× forward sales, among the richest valuations in the index [Sources: Palantir Q1 2026 results, May 4, 2026; TIKR, Jun 2026]. Palantir is the test case for "the application layer can capture AI value too" — and for how much of that hope is already priced.

**Tesla (~$1.50T):** the physical-AI flag-bearer: robotaxis (unsupervised in Austin, Dallas, Houston as of spring 2026 — still a small fleet vs. Waymo), the Optimus humanoid program (factory line being prepped at Fremont), and custom AI chips (AI5 taped out; the $16.5B Samsung deal covers AI6) [Sources: Tesla Q1 2026; Electrek, Apr 2026]. It also invested $2B in Musk's xAI — which, in February 2026, **merged into SpaceX** (Chapter 4.19). Tesla is less an AI-stack company than a wager that intelligence-in-motion (cars, robots) becomes the largest application of all.

📦 **Sidebar — the SaaS scare.** Q1 2026 saw roughly **$2 trillion of enterprise-software market value erased** as investors gamed out agents replacing seat-priced software; sector multiples compressed ~25% [Source: MarketMinute, Mar 2026]. The two bellwethers tell both sides: **Salesforce** (~$136B — roughly *halved* in a year) grew its Agentforce AI line to $1.2B ARR (+205%) yet trades at ~12× earnings on disruption fear; **ServiceNow** (~$106B) raised its 2026 AI revenue target to $1.5B with +22% subscription growth and was punished anyway [Sources: Salesforce FQ1 27 results, May 27, 2026; Futurum, Apr 2026]. The open question of the application layer: does AI make incumbent software *more* valuable (new features, same distribution) or *less* (agents commoditize the interface)? 2026's market votes "less," loudly — possibly wrongly.

## Layer 9 — The Model Labs (mostly private)

### 4.19 The intelligence merchants

**OpenAI** — the household name. ~900M weekly ChatGPT users [Source: TechCrunch, Feb 27, 2026]; 1M+ business customers; revenue from ~$13B recognized in 2025 to a >$25B annualized pace by early 2026 — against multi-billion losses, by design [Sources: Fortune, Nov 2025; Sacra, 2026]. Its compute ambitions defined the era: the famous ~$1.4 trillion of announced commitments (Stargate/Oracle, $250B Azure, AWS, AMD, Broadcom custom chips, the NVIDIA LOI) was later **reframed to ~$600B through 2030** as messaging sobered [Source: CNBC, Feb 20, 2026]. Closed a **$122B round at an $852B valuation (Mar 31, 2026)**, then **filed confidentially for what could be a $1T+ IPO** [Sources: CNBC, Mar 31, 2026; Bloomberg, Jun 8, 2026]. Models: the GPT-5 line (GPT-5.5 current, Apr 2026); it killed the Sora video app when the economics didn't work — evidence of new discipline [Source: TechBuzz, Apr 2026]. Owner-of-record trivia: Microsoft 27%, the nonprofit OpenAI Foundation 26%.

**Anthropic** — the enterprise-and-safety lab, and 2026's stunner. Founded 2021 by ex-OpenAI researchers around a thesis of safety-focused frontier AI; revenue run-rate went **$1B → ~$7B (2025) → $30B+ (April 2026, with the company claiming ~$47B by late May)** — ~80% from enterprises, with Claude Code (its agentic-coding product) alone at a reported ~$2.5B run-rate [Sources: Anthropic announcements; VentureBeat, Apr 7, 2026; Anthropic Series H, May 28, 2026 — growth figures are company-stated pending its IPO filing]. Raised a **$65B Series H at a $965B valuation (May 28, 2026) — overtaking OpenAI as the most valuable AI startup** — and submitted its own draft IPO filing days later [Sources: Anthropic, May 28, 2026; CNBC, May 28, 2026]. Its Claude 5 family launched June 9, 2026 and tops the public leaderboards as this handbook goes to print [Source: Anthropic, Jun 9, 2026; Artificial Analysis, Jun 2026]. Strategically remarkable: it buys compute from *all three* clouds (AWS Trainium "Project Rainier," Google TPUs ~1GW+, $30B Azure) plus, per its own announcement, SpaceX's Colossus — making it everyone's partner and no one's captive. Backers: Amazon (up to ~$33B), Google, Microsoft, NVIDIA.

**Google DeepMind** — not a startup (Alphabet's lab) but the deepest research bench in the field: Gemini 3 (Nov 2025) reset the leaderboards ("Google won 2025" became the industry meme), Gemini 3.5 followed at I/O 2026; AlphaFold-style science models remain unmatched [Sources: Google, Nov 18, 2025 & May 19, 2026].

**xAI / SpaceX** — Elon Musk's lab built "Colossus," a >1GW Memphis supercluster, at record speed, then **merged into SpaceX (Feb 2, 2026) at a $250B xAI valuation inside a $1.25T combined entity** with a mega-IPO planned [Source: Bloomberg/CNBC, Feb 2–3, 2026]. Grok models are capable; the brand is battered by a serious deepfake scandal and litigation [Source: Al Jazeera, Jun 11, 2026]. Unique asset: vertical integration with Tesla data, X distribution, and SpaceX capital.

**Mistral AI** (France, ~€12–14B) — Europe's champion: open-weight Mistral 3 models, ASML as anchor investor, sovereignty as the pitch. **DeepSeek** (China) — the January 2025 shockwave; its V4 (Apr 2026) is a 1.6T-parameter open-weights model offered at prices ~5–30× below U.S. peers; constrained mainly by chip access [Source: DeepSeek, Apr 2026; BenchLM, 2026]. **Alibaba's Qwen** — the world's most-downloaded open model family (>1B downloads) [Source: Pandaily, 2026]. The pattern: U.S. labs lead at the frontier by a modest margin (~single-digit points on composite benchmarks), while Chinese and European open models compete ferociously on *price* and *openness* [Source: Stanford AI Index 2026].

> **Figure 11 — The lab scoreboard, June 2026.** *Suggested visual:* a table-graphic: rows = OpenAI, Anthropic, Google DeepMind, xAI/SpaceX, Meta MSL, Mistral, DeepSeek, Qwen; columns = flagship model & date, valuation/owner, revenue run-rate (with "company-stated" flags), users, compute partners, open vs. closed weights. Highlight cell: Anthropic's $965B — "a startup founded in 2021 is now worth more than Oracle and Salesforce combined."

---

### ✅ Chapter 4 — Key Takeaways
- **NVIDIA, TSMC, ASML** form the hardware trinity — each near-monopoly in its niche; the memory trio joined them in market-cap heaven during the 2026 supercycle, and the storage duopoly (WDC +924%, Seagate +618%) rode the same wave.
- The **wiring and the walls** turned out to be investable layers of their own: sold-out lasers (Lumentum +959%), Ethernet fabrics (Arista), rack power-and-cooling (Vertiv, backlog +109%), and $24B-a-quarter AI-server orders (Dell).
- **Power became a layer, not a footnote**: a ~100 GW turbine queue (GE Vernova), nuclear plants contracted to Microsoft/Amazon/Meta for decades (Constellation, Talen, Vistra), and SMR optionality (Oklo).
- Every hyperscaler now plays multiple layers: chips (TPU/Trainium/Maia), cloud, models, and apps. **Vertical integration is the megacap moat.**
- **Broadcom and Marvell** monetize the *resistance* to NVIDIA; **AMD** is the lone merchant challenger; **Intel** is the geopolitical hedge the U.S. government literally bought into.
- The labs are no longer small: OpenAI ($852B) and Anthropic ($965B) out-value most of the S&P 100 — on private marks and company-stated revenue, both heading to IPO.
- The application layer is where conviction is weakest: Palantir priced for perfection, SaaS priced for disruption, Apple priced for patience.

---

# Chapter 5 — How Everything Connects

## 5.1 The journey of a chip (follow the atoms)

The single best way to understand the ecosystem is to follow one AI accelerator from sand to sentence:

1. **Design (California/UK).** NVIDIA architects the GPU using **Synopsys/Cadence** design software, often with **Arm**-based CPU companions.
2. **Lithography (Netherlands → Taiwan).** An **ASML** EUV machine — containing **Zeiss** optics — is shipped to **TSMC** in Taiwan.
3. **Fabrication (Taiwan).** TSMC prints the design onto 300mm silicon wafers over ~3 months using equipment from **Applied Materials, Lam Research, KLA** (deposit, etch, inspect — repeated thousands of times).
4. **Memory (Korea/Idaho).** **SK Hynix / Samsung / Micron** fabricate HBM4 stacks.
5. **Packaging (Taiwan).** TSMC's **CoWoS** lines bond GPU + HBM onto an interposer — the step that was the global bottleneck of 2023–25.
6. **Systems (Taiwan/Mexico/US).** Foxconn, Quanta, **Dell, Super Micro, Celestica** assemble GB300/VR200 racks — 72 GPUs, a tonne-plus each, liquid-cooled (**Vertiv** plumbing, **Eaton** switchgear), laced with **Amphenol** connectors and **Credo** cables.
7. **Networking (US/global).** **Arista/Broadcom** switches and **Lumentum/Coherent** laser-driven optics stitch 100,000 GPUs into one computer; **Ciena** links the campuses to each other.
8. **Power & deployment (Texas/Virginia/Wisconsin…).** Racks land in a **Microsoft/Amazon/Google/Oracle/CoreWeave** hall — or an **Equinix/Digital Realty** building — behind a substation fed by **GE Vernova** turbines or a **Constellation/Talen/Vistra** nuclear unit contracted years ahead.
9. **Intelligence (everywhere).** **OpenAI/Anthropic/Google** train and serve models on them; **apps** — Copilot, ChatGPT, Siri-via-Gemini, Palantir AIP — deliver answers to you.

Count the single points of failure: **one** lithography supplier, **one** dominant fab island, **three** memory makers, **two** drive makers, **one** dominant chip designer, sold-out lasers, and a years-long turbine queue. Six to nine months, four continents, and the most complex manufactured object in human history — repeated millions of times a year.

> **Figure 12 — From sand to sentence.** *Suggested visual:* a horizontal flow infographic of the nine steps above with a world-map ribbon underneath showing the geography hops (NL → TW → KR → TW → US), each hop annotated with its choke-point risk. This is Tour 1 in the Explorer app.

## 5.2 The money loop (follow the dollars)

Now run the river in reverse — revenue flowing downhill:

**You / enterprises** pay subscriptions and API fees → **apps and labs** (ChatGPT Plus, Claude, Copilot) → labs pay **clouds** for compute (OpenAI→Azure/Oracle/AWS; Anthropic→all three) → clouds pay **NVIDIA/AMD/Broadcom** for silicon → chip designers pay **TSMC** for wafers and **SK Hynix/Micron/Samsung** for HBM → fabs pay **ASML & friends** for tools. At every stage, some revenue exits to **power utilities, construction, and debt service**.

The uncomfortable arithmetic of 2026: the top of the funnel (all AI software/labs revenue, generously ~$60–70B a year) is **about one-tenth** of the infrastructure spending at the bottom (~$700B/year) [Sources: Menlo Ventures 2025; Epoch AI 2026]. Either the top grows into the bottom — the scaling-believers' bet, supported by 40–100%+ lab growth rates — or the bottom overbuilt. That gap *is* the bubble debate (6.2).

## 5.3 Circular deals — genius or mirage?

A 2025–26 specialty deserves its own lens: **vendors financing their customers**. NVIDIA invests (up to) $100B in OpenAI, which buys NVIDIA GPUs. Microsoft and NVIDIA invest $15B in Anthropic, which commits $30B to Azure (running NVIDIA chips). AMD grants OpenAI warrants for ~10% of itself in exchange for 6GW of purchases. Oracle borrows to build data centers for OpenAI's promised $300B [Sources: Bloomberg circular-deals graphics, 2025–26; deal announcements cited in Ch. 4].

- **The bear reading:** this is revenue round-tripping — demand conjured by the suppliers' own balance sheets, the classic late-cycle tell (see: 1990s telecom vendor financing).
- **The bull reading:** it's rational risk-sharing to bootstrap a capital-starved but real demand curve — and notably, the most circular headline deal (NVIDIA–OpenAI's $100B) has **quietly stalled** ("on ice" per January 2026 reporting; "never a commitment" per NVIDIA) [Source: press reports, Dec 2025–Mar 2026], suggesting discipline does exist.
- **The honest reading:** both. Track *cash actually invoiced* vs. press-release totals; the gap is the froth.

> **Figure 13 — The circular-deal map.** *Suggested visual:* a circular chord diagram: NVIDIA, Microsoft, Amazon, Google, Oracle, AMD, Broadcom, CoreWeave on the rim; OpenAI and Anthropic at center; colored chords for equity investments (one direction) and compute/chip purchase commitments (other direction), with $ widths. Caption: "When your investor is your supplier is your customer."

## 5.4 Geopolitics: chips as statecraft

- **Export controls.** Since 2022 the U.S. has barred advanced AI chips from China, tightening and loosening tactically: the H20 ban-then-unban of 2025 (with an unprecedented 15%-of-revenue export levy), Beijing's retaliatory ban on foreign AI chips in state data centers (Nov 2025), and a January 2026 framework allowing case-by-case H200 sales — which China has so far blocked on its side. Net effect: **NVIDIA's China data-center revenue is approximately zero**, by *both* governments' choice [Sources: NPR, Aug 2025; Reuters, Nov 2025; BIS, Jan 13, 2026; NVIDIA Q1 FY27, May 2026].
- **China's counter-stack.** SMIC pushes 7nm (and pilot 5nm) without EUV at painful yields; Huawei's Ascend chips ship by the hundreds of thousands with a public roadmap through 2028; CloudMatrix racks substitute scale for efficiency; CXMT attempts domestic HBM. The credible estimate: the U.S. compute lead remains large (~30×+ in new 2026 capacity under full restrictions) but China's floor keeps rising [Sources: SemiAnalysis 2025–26; IFP, 2026].
- **The truce.** The Trump–Xi summits (Busan Oct 2025; Beijing May 2026) produced a fragile détente — rare-earth export pauses traded against tariff relief, big agricultural and Boeing purchases, the TikTok JV — expiring late 2026, with Taiwan named by Xi as "the most important issue" [Sources: CNBC, Oct 30, 2025 & May 18, 2026].
- **Taiwan.** December 2025–January 2026 brought China's largest exercises in years — a simulated blockade. Meanwhile TSMC's $165B Arizona buildout proceeds, but leading-edge stays home by policy. The **"silicon shield"** theory — Taiwan is too valuable to attack *and* too valuable to abandon — is the load-bearing assumption of the entire industry. Every company in Chapter 4 is, knowingly or not, short a Taiwan crisis.
- **Sovereign AI.** Nations now buy compute like they once bought aircraft carriers: Stargate UAE (1GW first phase), Saudi Arabia's Humain (NVIDIA/AMD/Qualcomm gigawatts), EU "AI gigafactories" (€20B program, sites still unselected), Japan, India [Sources: The National, Dec 2025; Commerce Dept, Nov 20, 2025; EC, 2026]. For chipmakers it's a genuine third demand pillar after hyperscalers and labs.

> **Figure 14 — The choke-point world map.** *Suggested visual:* world map with five glowing nodes — Veldhoven (EUV, 1 supplier), Hsinchu (advanced fabs, ~90%), Seoul/Icheon (HBM), Silicon Valley (design), plus shaded "export-controlled" China; arrows showing legal flows (solid), banned flows (red dashed), and smuggling enforcement cases (dotted, via Singapore/Malaysia).

---

### ✅ Chapter 5 — Key Takeaways
- One chip crosses **four continents** and a half-dozen monopolies before it ever answers a prompt.
- Money flows down the stack; today's AI **revenue (~$60–70B/yr) is ~1/10th of infrastructure spend (~$700B/yr)** — the central tension of the era.
- **Circular deals** are real but disciplined skepticism is warranted: count invoices, not announcements.
- Chips are now **statecraft**: export controls, a fragile U.S.–China truce, China's domestic counter-stack, and Taiwan as the world economy's single point of failure.

# Chapter 6 — Major Trends, Challenges & the Road Ahead

## 6.1 Energy: the binding constraint

The 2026 consensus inside the industry is striking: the limit on AI is no longer chips — it's **electricity and the buildings to put it in**. Microsoft's CFO and Google's CEO both describe being "capacity constrained"; Satya Nadella has described having chips he can't plug in [Sources: earnings calls, 2025–26].

The numbers: global data centers used ~415 TWh in 2024, grew ~17% in 2025, and the IEA projects ~**945 TWh by 2030** — about 3% of world electricity, with AI the main driver [Source: IEA Energy & AI, Apr 2025; IEA Electricity 2026, Feb 2026]. In the U.S., data centers may reach **7–12% of all electricity by 2028–30** [Source: LBNL, Dec 2024]. Consequences already visible:

- **Grid prices and politics.** The PJM grid (13 mid-Atlantic states) set record capacity prices three auctions running, with ~$9B+ of the increase attributed to data centers; surging bills were a winning campaign issue in the 2025 New Jersey and Virginia elections, and remain live for the 2026 midterms [Sources: PJM, Dec 17, 2025; Axios, Nov 5, 2025].
- **The gas-turbine queue.** GE Vernova's order book hit ~100 GW of turbines and reservations in Q1 2026 — management expects to be sold out through 2030 by year-end — and lead times run 3–5 years [Sources: GE Vernova Q1 2026, Apr 22, 2026; Utility Dive, 2026]. You cannot Amazon-Prime a power plant. (The companies on the winning side of this constraint are profiled in Chapter 4.11.)
- **The nuclear renaissance, bought by Big Tech.** Microsoft is restarting Three Mile Island (835MW, 2027–28); Amazon expanded to 1.92GW from Susquehanna; Meta signed 1.1GW at Clinton plus 1.2GW of Oklo microreactors; Google backs Kairos SMRs [Sources: CNBC, Sep 2024; Data Center Frontier, 2026]. None of it arrives before 2027 — hence the gas bridge, and controversies like xAI's unpermitted Memphis turbines now in federal litigation [Source: CNBC/Earthjustice, Apr 2026].
- **The efficiency counterpoint.** Per-query energy keeps collapsing — Google disclosed a median Gemini text prompt uses **0.24 Wh** (≈9 seconds of TV) and cut it 33× in a year [Source: Google/MIT Tech Review, Aug 2025]. Efficiency gains, however, fuel *more* usage (Jevons paradox) — total demand still climbs.

> **Figure 15 — The power gap.** *Suggested visual:* dual-axis chart 2020–2030: bars = global data-center TWh (415 → 945); line = U.S. data-center share of electricity (4% → ~7–12%); annotated icons for TMI restart, PJM price records, gas-turbine backlog, first SMRs (~2030).

## 6.2 The bubble question — both cases, honestly

**The bear case (real economists, real shorts):**
- **The revenue gap.** ~$700B/yr of 2026 infrastructure vs. ~$60–70B of AI revenue; Bain's math says ~$2T/yr of revenue is needed by 2030 [Source: Bain, Sep 2025].
- **Depreciation.** Michael Burry (of *Big Short* fame) argues GPUs last 2–3 years while hyperscalers depreciate over ~6 — overstating profits by his estimate ~$176B through 2028 [Source: TechCrunch, Nov 2025]. (Counterpoint: 2020-era A100s still run profitably; NVIDIA published a rebuttal.)
- **Adoption reality.** MIT's "95% of pilots fail" finding; METR's study showing experienced developers were *19% slower* with 2025 AI tools while believing they were faster [Sources: MIT NANDA, Aug 2025; METR, Jul 2025].
- **Leverage creeping in.** Oracle's negative FCF and CDS widening; GPU-collateralized neocloud debt; Meta's $27B off-balance-sheet SPV; ~$1.5T of the projected buildout needing credit markets [Sources: Ch. 4 citations; Morgan Stanley, 2025]. The BIS and IMF have both flagged it [Sources: BIS Bulletin 120; IMF GFSR, Apr 2026].
- **2026's tremors:** a Nasdaq correction in March; the June 5 trillion-dollar chip wipeout on one soft guide [Sources: Motley Fool, Apr 2026; Seeking Alpha, Jun 5, 2026].

**The bull case (also real):**
- **The spenders are cash machines.** Unlike dot-com telecoms, the big four fund capex largely from ~$100B+/quarter of operating cash flow; margins *expanded* during the buildout (Amazon 10.7%→13.1% operating margin; Alphabet 31.6%→36.1%) [Source: company filings, 2026].
- **Demand is observable, not theoretical.** Azure +40%, Google Cloud +63%, AWS reaccelerating to +28%, with **$1.4T+ of combined contracted backlog** at Microsoft+Google+Amazon+Oracle alone; every CEO reports being supply-constrained [Source: Q1 2026 earnings].
- **Costs fall fast enough to create markets.** 40×/year capability-cost decline turns yesterday's $30-per-million-token model into today's $0.10 one — historically that's how electricity and bandwidth found their killer apps [Source: Epoch AI].
- **Lab revenue is compounding violently.** OpenAI ~$13B→$25B+ pace; Anthropic $1B→$30B+ run-rate in ~30 months (company-stated) — if even roughly real, the "revenue gap" closes faster than skeptics model.

**A sane synthesis:** the *physical* layer is probably not a bubble (compute scarcity is real and contracted); the *financial* layer contains bubble behavior (circularity, leverage, valuation perfection); and as 2026's selloffs showed, the market is now differentiating layer by layer rather than buying everything labeled "AI" — which is what maturing, not popping, looks like. Watch three dials: backlog-to-cash conversion, lab gross margins, and power-delivery timelines.

## 6.3 Regulation: three philosophies, one omnibus retreat

- **United States — accelerate, preempt, and equity-stake.** The 2025 AI Action Plan and "Genesis Mission" treat AI as a national race; Washington took ~10% of Intel, brokered chip-export levies, and tried (so far unsuccessfully) to preempt state AI laws by executive order — while **states** filled the vacuum: California's SB 53 (frontier-model safety disclosures), Texas, New York's RAISE Act; Colorado repealed-and-replaced its pioneering act before it ever took effect [Sources: White House, Jul 23 & Nov 24, 2025; state sources, 2025–26].
- **European Union — regulate first, then blink.** The AI Act entered force in 2024, but in May 2026 the EU provisionally agreed to **delay its high-risk obligations to December 2027** (the "Digital Omnibus") under competitiveness pressure — a landmark retreat that pleased industry and infuriated civil society [Source: EU Council, May 7, 2026].
- **China — control content, subsidize compute.** Strict model-registration and content rules domestically, massive state funding for chips, and a mirror-image ban on *American* chips in state data centers.
- **Courts > legislatures (for now).** The decisions that most shaped AI law were judicial: *Bartz v. Anthropic* (training on lawfully acquired books = fair use; piracy ≠ — $1.5B settlement, final approval pending as of June 2026); Getty's UK loss against Stability; the music industry's pivot from suing Suno/Udio to *licensing* them; NYT v. OpenAI grinding through discovery [Sources: Ch. 5 agent citations, 2025–26].

> **Figure 16 — Three regulatory philosophies.** *Suggested visual:* triptych panels (US flag / EU flag / China flag), each with a dial from "accelerate" to "restrain," key statutes listed beneath, and a timeline bar 2024–2028 showing the EU's high-risk delay visually sliding right.

## 6.4 Competition dynamics to watch

1. **Custom silicon vs. NVIDIA.** Google TPUs (now sold externally), Amazon Trainium (>$20B/yr run-rate), OpenAI×Broadcom, Microsoft Maia, Meta MTIA. NVIDIA's share erodes at the edges while the pie grows — the question is which force wins the decade.
2. **Open vs. closed models.** Meta's pivot to closed (Muse Spark) ended the era of U.S. open-weights at the frontier; the open torch passed to China (Qwen, DeepSeek) and Europe (Mistral) — with real strategic consequences: the world's default free AI increasingly speaks with non-U.S. accents [Source: Stanford AI Index 2026].
3. **The agent platform war.** Whoever owns the agent owns the workflow: Microsoft (Copilot), Google (Gemini), OpenAI (ChatGPT/Atlas), Anthropic (Claude/MCP), Salesforce (Agentforce). MCP's emergence as a cross-vendor standard is quietly the most hopeful interoperability story in tech.
4. **Consolidation at the top.** Microsoft owns 27% of OpenAI; Alphabet effectively arms both itself and Anthropic; xAI lives inside SpaceX; Meta bought its leadership. Antitrust scrutiny of AI partnerships is inevitable — the EU and FTC have both circled.

## 6.5 Jobs and society — early, real, uneven

The honest 2026 picture: **aggregate** employment effects remain modest; **targeted** effects are no longer deniable. Entry-level workers (ages 22–25) in the most AI-exposed occupations show a ~13% relative employment decline since 2022 [Source: Stanford Digital Economy Lab, Aug 2025]; "AI" became the #1 cited reason in U.S. layoff announcements for three straight months through May 2026 [Source: Challenger Gray, 2026], even as economists caution that "AI" sometimes launders ordinary cost-cutting (Amazon's CEO: "it's culture," not AI). Productivity evidence is genuinely mixed — strong gains for novices and call centers, *negative* results for experts in some rigorous trials [Sources: Brynjolfsson 2023; METR 2025]. The transition looks like every general-purpose technology's: slower than the hype, harsher at specific seams (junior knowledge work, support, translation), with new roles (AI operations, agent supervision) emerging behind it. WEF's net forecast remains positive (+78M jobs by 2030) — forecasts deserve the same skepticism as everything else in this chapter.

---

### ✅ Chapter 6 — Key Takeaways
- **Electricity** is the real bottleneck: 945 TWh by 2030, nuclear restarts, turbine queues, and rate-payer politics.
- The bubble debate resolves into: **physical layer real, financial layer frothy** — track backlog conversion, lab margins, and power timelines.
- Regulation diverged: U.S. accelerates, EU delayed its own rules, courts set the precedents that matter.
- Labor effects are **real but concentrated** — watch entry-level knowledge work, not the aggregate unemployment rate.

---

# Chapter 7 — A Practical Guide: Engaging with AI Today

## 7.1 For individuals

1. **Use a frontier assistant daily — properly.** The free tiers of ChatGPT, Gemini, and Claude are more capable than anything money could buy in 2023. The skill that compounds is **prompting-as-delegation**: give context ("you are reviewing a lease for a first-time renter in California"), give the raw material, ask for structure, then iterate. Treat the first answer as a draft, not an oracle.
2. **Verify like a pro.** Ask for sources; click them. For anything factual, numerical, legal, or medical, assume hallucination is possible. The mental model from Chapter 2: a brilliant, confident colleague with no shame about guessing.
3. **Build AI literacy as career insurance.** The evidence says AI most threatens *routine, junior* knowledge work and most rewards people who can **supervise, verify, and integrate** AI output. Concretely: learn one agentic tool in your domain (coding: Claude Code/Cursor/Copilot; analysis: notebook AIs; writing: long-context drafting), and become the person on your team who knows what the tools can't do.
4. **Mind the data.** Don't paste secrets into consumer tiers; understand that "deleted" chats may persist in logs (the NYT litigation made 20M of them discoverable). Use business/enterprise tiers for work data.
5. **If you invest** — see 7.3 first.

## 7.2 For businesses

1. **Start from use cases, not technology.** The McKinsey finding worth memorizing: 88% of firms "use AI"; only ~⅓ scale it; the scalers started with a P&L owner and a measurable workflow (claims triage, support deflection, code review, contract analysis) — not an "AI strategy."
2. **Buy before build, RAG before fine-tune, pilot before platform.** The cost curve (-40×/yr) punishes premature infrastructure. Frontier APIs + retrieval over your documents covers most needs; custom training is for the few with unique data at scale.
3. **Instrument ROI from day one.** The "95% fail" statistic is mostly a *measurement* failure. Define the baseline metric (handle time, cycle time, cost per ticket) before the pilot, or you'll be a statistic too.
4. **Governance is now table stakes.** An acceptable-use policy, a human-in-the-loop rule for consequential decisions, vendor data-handling review, and (if you operate in the EU) a compliance calendar for August 2026/December 2027 obligations.
5. **Expect the agent shift.** Budget owners in 2026 are moving from "AI features in seats we already buy" toward "agents that do tasks." Pilot one bounded agent (e.g., tier-1 support, invoice matching) with hard guardrails and an audit log; the learning compounds.

## 7.3 For investors — a framework, not advice

*(Reminder: nothing here is investment advice; this section teaches the map, not the trade.)*

- **Know which layer you're buying.** A dollar of "AI exposure" means utterly different things in ASML (monopoly equipment, cyclical), NVIDIA (dominant but priced for it), Micron (supercycle — and memory cycles *end*), Microsoft (diversified toll road), Oracle (leveraged single-customer bet), Palantir (~100× sales application hope), or an index (you already own ~34% Mag-7 [Source: Motley Fool, Jun 2026]).
- **Concentration cuts both ways.** The same handful of names drove most index returns 2023–26; passive investors are making an AI bet whether they know it or not.
- **Respect the cycle indicators** from 6.2: backlog→cash conversion, lab gross margins, power timelines, and credit spreads of the levered players (Oracle CDS, neocloud debt).
- **Beware narrative purity.** 2026's best AI performers included a memory maker, a fallen CPU giant, and Apple-the-laggard; 2026's worst included star software names. The market rewards *position in the physical stack*, not adjacency to the word "AI."

---

### ✅ Chapter 7 — Key Takeaways
- Individuals: use frontier tools daily, verify ruthlessly, become your team's AI supervisor.
- Businesses: measurable use cases, buy-before-build, governance, and one well-guarded agent pilot.
- Investors: layer awareness beats theme awareness; the cycle dials from Chapter 6 are your instrument panel.

---

# Chapter 8 — Glossary, Further Reading & References

## 8.1 Glossary

- **AEC (active electrical cable)** — a copper cable with signal-boosting chips inside, linking GPUs and switches within a rack; Credo's specialty.
- **Agent** — AI that doesn't just answer but *acts*: plans multi-step tasks, uses tools (browsers, code, APIs), and iterates toward a goal.
- **AGI (artificial general intelligence)** — hypothetical AI matching humans across most cognitive work. Contractually significant (the Microsoft–OpenAI deal has an AGI clause); scientifically undefined.
- **AI accelerator** — any chip specialized for AI math: GPUs, TPUs, Trainium, custom XPUs.
- **Alignment** — engineering models to be helpful, honest, and harmless — to want what their users/society want.
- **API (application programming interface)** — how software rents AI: send a prompt over the internet, pay per token.
- **Attention** — the transformer mechanism letting each word weigh every other word's relevance.
- **Backlog / RPO (remaining performance obligations)** — contracted future revenue not yet delivered; the metric of the 2026 cloud era (Microsoft $627B, Oracle $638B, Google $462B).
- **Capex (capital expenditure)** — spending on long-lived assets: data centers, chips, power.
- **Context window** — how much text a model can consider at once; ~1M tokens at the 2026 frontier.
- **CoWoS** — TSMC's advanced packaging bonding GPU + HBM; the great bottleneck of 2023–25.
- **CPU / GPU / TPU / XPU** — generalist processor / parallel processor (AI's workhorse) / Google's AI chip / catch-all for custom accelerators.
- **CUDA** — NVIDIA's programming layer; the software moat under its hardware empire.
- **Data center** — warehouse-scale buildings of servers; "AI factories" in 2026 vernacular; measured now in gigawatts.
- **Deep learning** — machine learning with many-layered neural networks.
- **Diffusion model** — image/video generator that learns to turn noise into pictures step-by-step.
- **EDA (electronic design automation)** — chip-design software; a Synopsys/Cadence duopoly.
- **EUV (extreme ultraviolet lithography)** — the light-printing technology behind advanced chips; ASML's monopoly.
- **Fab / foundry** — chip factory / a company that runs fabs for others (TSMC).
- **Fine-tuning** — further training a model on specialized data.
- **FLOPs** — floating-point operations (per second); the unit of compute.
- **Foundation model** — a giant, general model others build upon.
- **Generative AI** — models that create content (text, images, video, code) rather than just classify it.
- **Hallucination** — confident, fluent, false output; intrinsic to plausibility engines.
- **HAMR (heat-assisted magnetic recording)** — Seagate's laser-heated disk technology packing more data per hard-drive platter; the cost-per-terabyte lead in AI storage.
- **HBM (high-bandwidth memory)** — stacked memory bonded beside the processor; made only by SK Hynix, Samsung, Micron.
- **Hyperscaler** — a giant cloud operator (Microsoft, Amazon, Google, Meta, and increasingly Oracle).
- **Inference** — running a trained model (every chat reply); the volume economy of AI.
- **LLM (large language model)** — a transformer trained on vast text to predict tokens; the engine of chatbots.
- **MCP (Model Context Protocol)** — open standard connecting models to tools and data.
- **Model weights / parameters** — the learned numbers (billions–trillions) that *are* the model.
- **Multimodal** — handling text, images, audio, and video together.
- **Nearline drive** — a high-capacity hard disk for cloud "data lakes" — cheaper than flash, slower than memory; a Western Digital/Seagate duopoly, sold out through 2026–27.
- **Neural network** — layered web of simple units whose connection strengths are learned.
- **Neocloud** — a GPU-only cloud (CoreWeave, Nebius, IREN, Lambda).
- **Node (process node)** — chip-manufacturing generation (3nm, 2nm); smaller = denser = faster.
- **Open weights** — model weights downloadable for anyone to run/modify (Llama historically; Qwen, DeepSeek, Mistral today).
- **Post-training / RLHF** — the polishing phase that turns a raw predictor into a helpful assistant (reinforcement learning from human feedback).
- **PPA (power purchase agreement)** — a long-term contract to buy a plant's electricity; how Microsoft, Amazon, and Meta locked up nuclear output for decades.
- **Pre-training** — the long, expensive first phase: learning from internet-scale data.
- **Prompt** — your input to a model; prompting well = delegating well.
- **RAG (retrieval-augmented generation)** — letting a model look things up in real documents before answering; the standard cure for hallucination in business use.
- **Reasoning model** — a model that generates internal chains of thought, trading time for accuracy (the 2024–26 frontier).
- **Scaling laws** — the empirical rule that capability rises predictably with compute + data + parameters.
- **SMR (small modular reactor)** — factory-built nuclear reactors (tens to hundreds of megawatts) pitched as data-center power; ordered enthusiastically (Oklo's ~14 GW of letters of intent), delivered by nobody yet.
- **Token** — the unit of model text (~¾ of a word); also the billing unit of the intelligence economy.
- **Training** — building a model by adjusting parameters against data; the factory-construction economy of AI.
- **Transceiver (optical) / EML laser** — the plug-in module that converts a switch's electrical signals to light for fiber links between racks; the laser chip inside it (Lumentum, Coherent) was 2026's scarcest component.
- **Transformer** — the 2017 architecture (attention-based) behind all modern frontier models.

## 8.2 Further reading (a short shelf)

- **Stanford HAI — AI Index Report 2026** — the annual statistical bible: hai.stanford.edu/ai-index
- **IEA — Energy and AI (2025) & Electricity 2026** — the energy ground truth: iea.org
- **Epoch AI** — data on compute, costs, and model trends: epoch.ai
- **Stratechery (Ben Thompson)** — strategy of the platforms, weekly.
- **SemiAnalysis (Dylan Patel)** — the chip supply chain, technically deep.
- **Anthropic / OpenAI / Google DeepMind blogs** — primary sources for model capabilities; read announcements, not headlines about them.
- **"The Chip War" by Chris Miller (2022)** — the historical backstory of Chapters 3–5 in book form.
- The companion apps — the **AI Ecosystem Explorer** (live 3D map) and **The $725 Billion Machine** (interactive essay with the full 61-company dataset and calculators).

## 8.3 References

*Primary sources and reporting cited in this handbook (accessed June 2026). Grouped by chapter; titles abbreviated.*

**Chapters 1–2 (history, concepts, adoption):**

1. TechCrunch — "ChatGPT reaches 900M weekly active users" (Feb 27, 2026): techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users/
2. Google I/O 2026 token volume (3.2 quadrillion/month) — shacknews.com/article/149205/google-3-2-quadrillion-monthly-ai-tokens
3. McKinsey — "The State of AI" (Nov 2025): mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
4. Ramp AI Index (paid adoption >50%, Mar 2026): ramp.com/data/ai-index
5. OpenAI — GDPval benchmark (Sep 30, 2025): openai.com/index/gdpval/
6. Epoch AI — LLM inference price trends: epoch.ai/data-insights/llm-inference-price-trends
7. MIT NANDA — "The GenAI Divide" via Fortune (Aug 18, 2025): fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
8. Bain — 6th Annual Global Technology Report ($2T revenue need, Sep 23, 2025): bain.com/about/media-center/press-releases/20252/
9. Fortune — OpenAI losses/profitability path (Nov 12, 2025): fortune.com/2025/11/12/openai-cash-burn-rate-annual-losses-2028-profitable-2030-financial-documents/
10. CNBC — NVIDIA first to $5T (Oct 29, 2025): cnbc.com/2025/10/29/nvidia-on-track-to-hit-historic-5-trillion-valuation-amid-ai-rally.html
11. METR — developer RCT (Jul 10, 2025): metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
12. Stanford HAI — AI Index 2026: hai.stanford.edu/ai-index/2026-ai-index-report

**Chapters 3–4, semiconductors & equipment:**

13. NVIDIA — Q1 FY2027 results (May 20, 2026): investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/
14. NVIDIA — Q4 & FY2026 results (Feb 25, 2026): nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
15. NVIDIA — Vera Rubin full production (GTC, Mar 2026): nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer
16. AMD — Q1 2026 results (May 5, 2026): stocktitan.net/news/AMD/amd-reports-first-quarter-2026-financial-bu7e2cbxpd14.html
17. AMD–OpenAI 6GW agreement & warrant (Oct 6, 2025): ir.amd.com/news-events/press-releases/detail/1260/
18. Oracle–AMD 50K MI450 (Oct 14, 2025): oracle.com/news/announcement/ai-world-oracle-and-amd-expand-partnership-2025-10-14/
19. Broadcom — Q2 FY2026 results (Jun 3, 2026): prnewswire.com/news-releases/broadcom-inc-announces-second-quarter-fiscal-year-2026-financial-results-and-quarterly-dividend-302790698.html
20. Intel — Q1 2026 results (Apr 23, 2026): nasdaq.com/press-release/intel-reports-first-quarter-2026-financial-results-2026-04-23
21. CNBC — US government ~10% Intel stake (Aug 22, 2025): cnbc.com/2025/08/22/intel-goverment-equity-stake.html
22. Reuters/Yahoo — NVIDIA $5B Intel stake closed (Dec 2025): finance.yahoo.com/news/nvidia-takes-5-billion-stake-121442962.html
23. TSMC — Q1 2026 via Investing.com (Apr 16, 2026): investing.com/news/company-news/tsmc-q1-2026-slides-margins-soar-past-guidance-on-hpc-demand-93CH-4617201
24. TSMC — May 2026 revenue (Jun 10, 2026): pr.tsmc.com/english/news/3320
25. TrendForce — foundry market share 4Q25 (Mar 12, 2026): trendforce.com/presscenter/news/20260312-12965.html
26. ASML — Q1 2026 results (Apr 15, 2026): asml.com/en/news/press-releases/2026/q1-2026-financial-results
27. Tom's Hardware — Intel installs first High-NA EXE:5200B (Dec 2025): tomshardware.com/tech-industry/semiconductors/intel-installs-industrys-first-commercial-high-na-euv-lithography-tool
28. Bloomberg — ASML €1.3B into Mistral (Sep 9, 2025): bloomberg.com/news/articles/2025-09-09/asml-pumps-1-3-billion-into-mistral-in-boost-for-european-ai
29. CNBC — SK Hynix record Q1, $1T valuation (Apr 23 / May 27, 2026): cnbc.com/2026/04/23/sk-hynix-earnings-ai-memory-shortage-hbm-demand.html; cnbc.com/2026/05/27/sk-hynix-shares-ai-chip-rally-1-trillion.html
30. TrendForce — SK Hynix ~⅔ of NVIDIA HBM4 (Jan 28, 2026): trendforce.com/news/2026/01/28/news-sk-hynix-reportedly-to-supply-about-two-thirds-of-nvidia-hbm4-samsung-targets-early-delivery/
31. CNBC — Micron FQ2 2026 results (Mar 18, 2026): cnbc.com/2026/03/18/micron-mu-q2-earnings-report-2026.html
32. TechPowerUp — Samsung Q1 2026 (Apr 2026): techpowerup.com/348675/samsung-q1-2026-results-memory-profit-up-nearly-50x-warns-of-2027-shortage
33. CNN — Samsung–Tesla $16.5B (Jul 28, 2025): cnn.com/2025/07/28/business/tesla-samsung-chip-deal
34. TrendForce — 1Q26 DRAM +81% QoQ to $97B (Jun 1, 2026): trendforce.com/presscenter/news/20260601-13070.html
35. TrendForce — DRAM contract prices +90–95% 1Q26 (Feb 2, 2026): trendforce.com/presscenter/news/20260202-12911.html
36. TechTimes/Gartner — memory +130% by end-2026 (Jun 5, 2026): techtimes.com/articles/317872/20260605/
37. SEMI — equipment forecast ~$139B 2026: semi.org/en/semi-press-release/global-total-semiconductor-equipment-sales-forecast-to-reach-a-record-of-dollar-139-billion-in-2026-semi-reports
38. TrendForce — CoWoS capacity expansion (2025–26): trendforce.com/news/2025/01/02/ and trendforce.com/news/2026/04/13/
39. Qualcomm — AI200/AI250 (Oct 27, 2025): qualcomm.com/news/releases/2025/10/qualcomm-unveils-ai200-and-ai250-redefining-rack-scale-data-cent
40. Arm — FY2026 results (May 2026): stocktitan.net/sec-filings/ARM/
41. Marvell — Q1 FY2027 results (May 27, 2026): investor.marvell.com/news-events/press-releases/detail/1023/

**Chapter 4, cloud & platforms:**

42. Microsoft — FY26 Q3 results (Apr 29, 2026): microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast
43. CNBC — Microsoft $190B calendar-2026 capex (Apr 29, 2026): cnbc.com/2026/04/29/microsoft-msft-q3-earnings-report-2026.html
44. Microsoft — OpenAI partnership next chapter (Oct 28, 2025): blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/
45. Microsoft — Maia 200 (Jan 26, 2026): blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/
46. TechCrunch — 20M paid M365 Copilot seats (Apr 29, 2026): techcrunch.com/2026/04/29/microsoft-says-it-has-over-20m-paid-copilot-users-and-they-really-are-using-it/
47. Alphabet — Q1 2026 8-K (Apr 29, 2026): sec.gov/Archives/edgar/data/0001652044/000165204426000043/googexhibit991q12026.htm
48. CNBC — Alphabet $4T market cap; Gemini-powered Siri (Jan 12, 2026): cnbc.com/2026/01/12/alphabet-4-trillion-market-cap.html
49. DCD — Google–Anthropic 1GW+ TPU deal (Oct 2025): datacenterdynamics.com/en/news/google-and-anthropic-confirm-massive-1gw-cloud-deal-with-up-to-one-million-google-tpus/
50. DOJ — Google search remedies (Sep 2025): justice.gov/opa/pr/department-justice-wins-significant-remedies-against-google
51. TechCrunch — Waymo ridership (Mar 27, 2026): techcrunch.com/2026/03/27/waymo-skyrocketing-ridership-in-one-chart/
52. Amazon — Q1 2026 results (Apr 29, 2026): s2.q4cdn.com/299287126/files/doc_earnings/2026/q1/earnings-result/AMZN-Q1-2026-Earnings-Release.pdf
53. CNBC — AWS Q1 2026 +28% (Apr 29, 2026): cnbc.com/2026/04/29/aws-earnings-q1-2026.html
54. TechCrunch/CNBC — Amazon–Anthropic up to $25B more; >$100B AWS commit (Apr 20, 2026): techcrunch.com/2026/04/20/anthropic-takes-5b-from-amazon-and-pledges-100b-in-cloud-spending-in-return/
55. Synergy Research — cloud market Q1 2026: srgresearch.com/articles/cloud-market-annual-revenue-run-rate-topped-half-a-trillion-dollars-in-q1-as-growth-surge-continues
56. Oracle — Q4 FY2026 results (Jun 10, 2026): prnewswire.com/news-releases/oracle-announces-record-q4-and-fy-2026-results-driven-by-cloud-infrastructure--cloud-applications-302797201.html
57. CNBC — Oracle Q4 FY26 & new raise (Jun 10, 2026): cnbc.com/2026/06/10/oracle-orcl-q4-earnings-report-2026.html
58. CoreWeave — Q1 2026 8-K (May 7, 2026): sec.gov/Archives/edgar/data/0001769628/000176962826000220/coreweave1q26earningspress.htm
59. CNBC — Meta +$21B CoreWeave commitment (Apr 9, 2026): cnbc.com/2026/04/09/meta-commits-to-spending-additional-21-billion-with-coreweave-.html
60. Meta — Q1 2026 results & capex raise (Apr 29, 2026) via Yahoo Finance: finance.yahoo.com/sectors/technology/article/meta-stock-sinks-after-q1-earnings-160136308.html
61. Meta/Blue Owl — Hyperion JV (Oct 21, 2025): prnewswire.com/news-releases/meta-announces-joint-venture-with-funds-managed-by-blue-owl-capital-302590584.html
62. CNBC — Meta Muse Spark closed model (Apr 8, 2026): cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html
63. NPR — Meta 8,000 layoffs (May 20, 2026): npr.org/2026/05/20/nx-s1-5826917/meta-layoffs-ai-jobs
64. MacRumors — Apple FQ2 2026 results (Apr 30, 2026): macrumors.com/2026/04/30/apple-2q-2026-earnings/
65. CNBC — Apple picks Gemini for Siri (Jan 12, 2026): cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html
66. TechCrunch — WWDC 2026; Cook→Ternus (Jun 9, 2026): techcrunch.com/2026/06/09/wwdc-2026-everything-announced-on-siri-ai-os-27-apple-intelligence-and-more/
67. Palantir — Q1 2026 results (May 4, 2026): businesswire.com/news/home/20260503338048/en/
68. Tesla Q1 2026 via StockTitan: stocktitan.net/sec-filings/TSLA/8-k-tesla-inc-reports-material-event-1911b8f568a6.html
69. Salesforce — FQ1 2027 results (May 27, 2026): salesforce.com/news/press-releases/2026/05/27/fy27-q1-earnings/
70. MarketMinute — "Great SaaS Reset" (Mar 26, 2026): markets.financialcontent.com/stocks/article/marketminute-2026-3-26-the-great-saas-reset

**Chapter 4.19 & 5, labs, deals, geopolitics:**

71. CNBC — OpenAI $852B round (Mar 31, 2026): cnbc.com/2026/03/31/openai-funding-round-ipo.html
72. Bloomberg — OpenAI confidential IPO filing; $3.6T pipeline (Jun 8, 2026): bloomberg.com/news/articles/2026-06-08/openai-filed-confidentially-for-ipo-as-rivals-race-to-market
73. CNBC — OpenAI ~$600B spend reframing (Feb 20, 2026): cnbc.com/2026/02/20/openai-resets-spend-expectations-targets-around-600-billion-by-2030.html
74. Anthropic — Series H, $965B (May 28, 2026): anthropic.com/news/series-h
75. CNBC — Anthropic Series G $30B at $380B (Feb 12, 2026): cnbc.com/2026/02/12/anthropic-closes-30-billion-funding-round-at-380-billion-valuation.html
76. Anthropic — Claude Fable 5 & Mythos 5 (Jun 9, 2026): anthropic.com/news/claude-fable-5-mythos-5
77. Microsoft/NVIDIA/Anthropic partnerships (Nov 18, 2025): blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/
78. Bloomberg — SpaceX–xAI merger (Feb 2, 2026): bloomberg.com/news/articles/2026-02-02/elon-musk-s-spacex-said-to-combine-with-xai-ahead-of-mega-ipo
79. NVIDIA–OpenAI 10GW LOI (Sep 22, 2025): nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems
80. NPR — 15% H20 export levy (Aug 11, 2025): npr.org/2025/08/11/nx-s1-5498689/nvidia-h20-chip-sales-china
81. Reuters/Yahoo — China bans foreign chips in state DCs (Nov 5, 2025): finance.yahoo.com/news/exclusive-china-bans-foreign-ai-080808297.html
82. BIS — revised H200 license policy (Jan 13, 2026): bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china
83. IFP — "The B30A decision": ifp.org/the-b30a-decision/
84. CNBC — Trump–Xi Busan summit (Oct 30, 2025): cnbc.com/2025/10/30/trump-xi-south-korea-rare-earth-tariff-trade-war-nvidia.html
85. CNBC — Trump–Xi Beijing summit deals (May 18, 2026): cnbc.com/2026/05/18/us-china-announce-deals-after-trump-xi-summit.html
86. White House — Section 232 semiconductor proclamation (Jan 2026): whitehouse.gov/presidential-actions/2026/01/adjusting-imports-of-semiconductors/
87. DigiTimes — Huawei Ascend roadmap (Sep 18, 2025): digitimes.com/news/a20250918PD234/huawei-ascend-hbm-ai-chip-roadmap.html
88. Al Jazeera — Taiwan drills (Jan 1, 2026): aljazeera.com/news/2026/1/1/us-says-chinese-military-drills-around-taiwan-cause-unnecessary-tensions
89. CNBC — US–Taiwan chip deal & silicon shield (Jan 19, 2026): cnbc.com/2026/01/19/us-taiwan-chip-deal-silicon-shield-tsmc-trump-tapei-ai-semiconductor-supply-chain.html
90. The National — Stargate UAE Q3 2026 (Dec 5, 2025): thenationalnews.com/business/2025/12/05/stargate-uaes-first-phase-to-be-completed-in-third-quarter-of-2026/
91. Commerce Dept — UAE/Saudi GB300 export approvals (Nov 20, 2025): commerce.gov/news/press-releases/2025/11/statement-uae-and-saudi-chip-exports

**Chapter 6, policy, energy, economy:**

92. White House — America's AI Action Plan (Jul 23, 2025): whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf
93. White House — Genesis Mission EO (Nov 24, 2025): whitehouse.gov/presidential-actions/2025/11/launching-the-genesis-mission/
94. Governor of California — SB 53 signed (Sep 29, 2025): gov.ca.gov/2025/09/29/
95. EU Council — AI omnibus provisional agreement (May 7, 2026): consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/
96. Authors Guild — Anthropic settlement status: authorsguild.org/news/anthropic-settlement-update-91-percent-of-books-claimed/
97. Bloomberg Law — OpenAI must produce 20M chat logs (Jan 2026): news.bloomberglaw.com/ip-law/openai-must-turn-over-20-million-chatgpt-logs-judge-affirms
98. UK High Court — Getty v. Stability judgment (Nov 4, 2025): judiciary.uk/wp-content/uploads/2025/11/Getty-Images-v-Stability-AI.pdf
99. IEA — Energy and AI (Apr 2025): iea.org/reports/energy-and-ai/executive-summary
100. IEA — Electricity 2026 (Feb 2026): iea.org/reports/electricity-2026/executive-summary
101. LBNL — 2024 US Data Center Energy Usage Report (Dec 2024): eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf
102. PJM — capacity auction results (Dec 17, 2025): pjm.com/-/media/DotCom/about-pjm/newsroom/2025-releases/20251217-pjm-auction-procures-134479-mw-of-generation-resources.pdf
103. Axios — electricity politics in NJ/VA elections (Nov 5, 2025): axios.com/2025/11/05/nj-virginia-election-electricity-costs-spanberger-sherrill
104. Utility Dive — GE Vernova turbine backlog: utilitydive.com/news/ge-vernova-gas-turbine-investor/807662/
105. CNBC — Constellation/Three Mile Island for Microsoft (Sep 20, 2024): cnbc.com/2024/09/20/constellation-energy-to-restart-three-mile-island-and-sell-the-power-to-microsoft.html
106. Data Center Frontier — nuclear deals roundup (2026): datacenterfrontier.com/energy/article/55239739/
107. CNBC/Earthjustice — xAI Memphis turbines litigation (Apr 14, 2026): cnbc.com/2026/04/14/elon-musk-xai-memphis-data-centers.html
108. MIT Technology Review — Google per-prompt energy 0.24 Wh (Aug 21, 2025): technologyreview.com/2025/08/21/1122288/google-gemini-ai-energy/
109. Morgan Stanley — "Who Will Fund AI's $3 Trillion Ask?" (2025): morganstanley.com/insights/podcasts/thoughts-on-the-market/ai-investing-credit-markets-andrew-sheets
110. Fortune — Furman: AI capex and GDP growth (Oct 7, 2025): fortune.com/2025/10/07/data-centers-gdp-growth-zero-first-half-2025-jason-furman-harvard-economist/
111. BIS — Bulletin 120, "Financing the AI boom": bis.org/publ/bisbull120.pdf
112. IMF — Global Financial Stability Report (Apr 14, 2026): imf.org/en/publications/gfsr/issues/2026/04/14/
113. TechCrunch — Burry vs. NVIDIA depreciation fight (Nov 27, 2025): techcrunch.com/2025/11/27/this-thanksgivings-real-drama-may-be-michael-burry-versus-nvidia/
114. Seeking Alpha — $1T+ chip selloff (Jun 5, 2026): seekingalpha.com/news/4601211-over-1t-erased-chip-selloff-impacts-nvidia-broadcom
115. Stanford Digital Economy Lab — "Canaries in the Coal Mine" (Aug 2025): digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine/
116. Challenger, Gray & Christmas — layoff reports (2025–26): challengergray.com/blog/challenger-report-march-cuts-rise-25-from-february-ai-leads-reasons/
117. Gartner — worldwide AI spending 2026 $2.59T (May 19, 2026): gartner.com/en/newsroom/press-releases/2026-05-19-gartner-forecasts-worldwide-ai-spending-to-grow-47-percent-in-2026
118. IDC — AI infrastructure spending: idc.com/resource-center/blog/ai-infrastructure-spending-caps-historic-year/
119. Menlo Ventures — State of GenAI in the Enterprise (2025): menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/
120. WEF — Future of Jobs Report 2025 (Jan 2025): weforum.org/press/2025/01/future-of-jobs-report-2025/

**Expanded edition — Layers 5–7, storage & neoclouds (added June 12, 2026):**

121. Arista Networks — Q1 2026 results (May 5, 2026): businesswire.com/news/home/20260505592008/en/
122. Astera Labs — Q1 2026 results (May 5, 2026): ir.asteralabs.com/news-releases/news-release-details/astera-labs-reports-first-quarter-2026-financial-results
123. Coherent — FQ3 2026 results (May 6, 2026): globenewswire.com/news-release/2026/05/06/3289361/
124. Ciena — FQ2 2026 results (Jun 4, 2026): investor.ciena.com/news/news-details/2026/Ciena-Reports-Fiscal-Second-Quarter-2026-Financial-Results/
125. Credo — FQ4 2026 8-K (Jun 1, 2026): sec.gov/Archives/edgar/data/0001807794/000162828026039474/credoq42026ex-991.htm
126. Lumentum — FQ3 2026 8-K (May 5, 2026): sec.gov/Archives/edgar/data/0001633978/000162828026030530/lite_ex991xq3fy26.htm
127. Amphenol — Q1 2026 results (Apr 29, 2026): businesswire.com/news/home/20260429563708/en/
128. Monolithic Power — Q1 2026 results (Apr 30, 2026): globenewswire.com/news-release/2026/04/30/3285426/
129. Dell — FQ1 2027 results (May 28, 2026): dell.com/en-us/dt/corporate/newsroom/announcements/detailpage.press-releases~usa~2026~05~
130. Super Micro — FQ3 2026 8-K (May 5, 2026): sec.gov/Archives/edgar/data/0001375365/000137536526000013/exhibit991_20260331.htm
131. Celestica — Q1 2026 coverage (Apr 28, 2026): investing.com/news/company-news/celestica-q1-2026-slides-revenue-surges-53-ai-demand-drives-outlook-raise-93CH-4641771
132. Vertiv — Q1 2026 8-K (Apr 22, 2026): sec.gov/Archives/edgar/data/1674101/000162828026026379/q12026exhibit991vrt04222026.htm
133. Eaton — Q1 2026 8-K (May 5, 2026): sec.gov/Archives/edgar/data/1551182/000155118226000010/etn03312026exhibit99.htm
134. Equinix — Q1 2026 coverage (Apr 29, 2026): investing.com/news/company-news/equinix-q1-2026-slides-record-bookings-drive-guidance-raise-margins-hit-51-93CH-4647474
135. Digital Realty — Q1 2026 transcript (Apr 23, 2026): fool.com/earnings/call-transcripts/2026/04/23/digital-realty-dlr-q1-2026-earnings-transcript/
136. Western Digital — FQ3 2026 transcript (Apr 30, 2026): fool.com/earnings/call-transcripts/2026/04/30/western-digital-wdc-q3-2026-earnings-transcript/
137. Seagate — FQ3 2026 transcript (Apr 28, 2026): fool.com/earnings/call-transcripts/2026/04/28/seagate-stx-q3-2026-earnings-transcript/
138. TrendForce — nearline HDD shortage (Sep 15, 2025): trendforce.com/presscenter/news/20250915-12714.html
139. GE Vernova — Q1 2026 8-K (Apr 22, 2026): sec.gov/Archives/edgar/data/1996810/000199681026000063/gevpressrelease1q26.htm
140. Constellation — Q1 2026 8-K (May 11, 2026): sec.gov/Archives/edgar/data/1868275/000186827526000063/ceg-20260511991.htm
141. Vistra–Meta nuclear agreements (Jan 9, 2026): investor.vistracorp.com/2026-01-09-Vistra-and-Meta-Announce-Agreements
142. Talen–Amazon expanded PPA (Jun 11, 2025): ir.talenenergy.com/news-releases/news-release-details/talen-energy-expands-nuclear-energy-relationship-amazon
143. NextEra — Q1 2026 8-K (Apr 23, 2026): sec.gov/Archives/edgar/data/753308/000075330826000028/neeq12026exhibit99.htm
144. Oklo — Q1 2026 transcript (May 13, 2026): fool.com/earnings/call-transcripts/2026/05/13/oklo-oklo-q1-2026-earnings-call-transcript/
145. Nebius — Q1 2026 transcript (May 13, 2026): fool.com/earnings/call-transcripts/2026/05/13/nebius-nbis-q1-2026-earnings-transcript/
146. IREN — $9.7B Microsoft contract (Nov 3, 2025): globenewswire.com/news-release/2025/11/03/3178993/
147. Samsung — Q1 2026 results (Apr 2026): news.samsung.com/global/samsung-electronics-announces-first-quarter-2026-results
148. SMIC — Q1 2026 coverage (May 2026): tipranks.com/news/company-announcements/smic-posts-modest-q1-gain-and-signals-stronger-growth-ahead
149. Qualcomm — FQ2 2026 results (Apr 29, 2026): s204.q4cdn.com/645488518/files/doc_financials/2026/q2/FY2026-2nd-Quarter-Earnings-Release.pdf

*Market capitalizations throughout: stockanalysis.com, June 11–12, 2026 (Korean listings via KRX, approximate USD conversion; some June 12 figures intraday). Layer-level "combined value" and "revenue run-rate" figures in Chapter 3 are computed across this universe per the methodology stated there.*

---

*© 2026. Compiled June 11, 2026. This handbook is for education only and is not investment, legal, or professional advice. Verify time-sensitive figures before relying on them — in this industry, six months is a geological age.*



