# Verification report: knowledge_robot_learning.json

Rows checked: 88 (16 knowledge nodes, 24 robots/models, 48 project candidates). Verified: 86. Corrected: 2. Rejected: 0.

## Method
- Extracted all 49 distinct URLs in the file and opened each with curl: 49/49 returned HTTP 200.
- Resolved every arXiv ID (22) via arxiv.org/abs and checked title, date and topic against the claim. The 2026 preprints are real and match the claims made about them: 2610.39054 (Robotic Data Inoculation, Levine group), 2611.03622 (D&A, VLM reward models), 2611.09145 (Augmentron), 2611.11089 (control-aware async inference, Osa & Ota).
- Spot-checked key facts on source pages: RLDS archived Nov 29 2025; robomimic v0.5.0 diffusion + multi-dataset; MimicGen code release July 2024; FAST+ tokenizer; CortexBench 17 tasks; VC-1 CC-BY-NC; CrossFormer Berkeley/CMU; SayCan and Code as Policies open-source code; LeRobot async inference docs.
- Validated all select/multi-select values against schemas/notion-schema.md: all valid. All 48 project work splits sum to 100. All Prerequisites and Knowledge nodes relations resolve within the file. The prerequisite graph is acyclic (16 chains of 3).
- Schema cleanup: removed the non-Notion key `_accessibility_reason` from all 16 nodes. `Project ideas` is empty (deprecated). There is no `Used in projects` key.
- Status: nodes and robots/models are "To verify". Projects stay "Idea", because the Projects Status field has no "To verify" option.
- Not applicable: Ecosystem organizations. The file contains none, and Built by / Used by / Relevant orgs are all empty.

## Flags for human review
- Project `Robots & models` relations name rows that are not defined in this file: `LeRobot`, `SmolVLA` (defined in ecosystem_paris_all / embedded_electronics), `pi0` and `Diffusion Policy` (defined in knowledge_manipulation), and `ACT (Action Chunking Transformer)` (not found in any main output file, so it must be a Notion pilot row or be added). The syncer must resolve these names across files.
- Release year is null for LeRobotDataset v3, RLDS and Tensor2Robot. The opened pages do not state a year, so I left them unknown.
- VC-1 and CortexBench have Open source = true, but their code is CC-BY-NC (non-commercial). This is noted in Price / access.
- Every node has Starter hardware cost "€0 (sim only)" and identical Discipline values. This is plausible for a sim-first branch, but it is coarse.

## Rows

| Table | Row | Verdict | Reason |
|---|---|---|---|
| Knowledge node | Robot learning problem formulation: observations, actions, policies | verified | sources load and support claims |
| Knowledge node | Robot learning toolchains & data formats | verified | sources load and support claims |
| Knowledge node | Policy evaluation & real-world testing methodology | verified | sources load and support claims |
| Knowledge node | Diffusion & flow-matching policies | verified | sources load and support claims |
| Knowledge node | Action chunking & action tokenization | verified | sources load and support claims |
| Knowledge node | Pretrained visual representations for robots | verified | sources load and support claims |
| Knowledge node | Offline reinforcement learning | verified | sources load and support claims |
| Knowledge node | Reward learning & reward specification | verified | arXiv 2611.03622 (D&A, Nov 2026) confirmed as VLM zero-shot reward/progress model |
| Knowledge node | Interactive imitation & human-in-the-loop correction | verified | arXiv 2610.39054 Robotic Data Inoculation (Li, Zhou, Xu, Levine; Oct 2026) confirmed |
| Knowledge node | Data augmentation & synthetic demonstration generation | verified | arXiv 2611.09145 Augmentron multi-view augmentation (Nov 2026) confirmed |
| Knowledge node | Fine-tuning & adapting pretrained robot policies | verified | sources load and support claims |
| Knowledge node | Real-time learned-policy execution & inference scheduling | verified | arXiv 2611.11089 asynchronous control-aware command generation (Nov 2026) confirmed; LeRobot async docs load |
| Knowledge node | LLM/VLM task planning & code-as-policies | verified | sources load and support claims |
| Knowledge node | Cross-embodiment learning | verified | sources load and support claims |
| Knowledge node | Autonomous self-improvement & continual robot learning | verified | sources load and support claims |
| Knowledge node | Failure detection & uncertainty for learned policies | verified | sources load and support claims |
| Robot/model | LeRobotDataset v3 | verified | Parquet+MP4 sharded format confirmed; Release year left null (not stated on page) |
| Robot/model | RLDS | verified | repo page confirms archived Nov 29, 2025 |
| Robot/model | robomimic | verified | v0.5.0 (06/2025) adds Diffusion Policy + multi-dataset confirmed |
| Robot/model | FAST tokenizer | verified | FAST+ universal tokenizer on HF confirmed |
| Robot/model | R3M | verified | sources load; builder matches paper/repo |
| Robot/model | VC-1 | verified | CC-BY-NC license confirmed on repo |
| Robot/model | DINOv2 | verified | sources load; builder matches paper/repo |
| Robot/model | CortexBench | verified | 17 tasks confirmed in arXiv 2303.18240 |
| Robot/model | CQL reference implementation | verified | sources load; builder matches paper/repo |
| Robot/model | IQL reference implementation | verified | sources load; builder matches paper/repo |
| Robot/model | Eureka | verified | sources load; builder matches paper/repo |
| Robot/model | MimicGen | verified | "Data Generation Code released July 2024" confirmed |
| Robot/model | LIBERO | verified | sources load; builder matches paper/repo |
| Robot/model | RoboCasa | verified | sources load; builder matches paper/repo |
| Robot/model | GR00T N1 | corrected | repo now ships N1.7; Price / access set to code Apache 2.0 + weights NVIDIA Open Model License (per repo README) |
| Robot/model | Real-Time Chunking (RTC) | verified | sources load; builder matches paper/repo |
| Robot/model | Code as Policies | verified | code + colab linked from project page |
| Robot/model | SayCan | verified | open-source sim tabletop version confirmed |
| Robot/model | CrossFormer | verified | UC Berkeley + CMU affiliations confirmed |
| Robot/model | RT-1-X | verified | sources load; builder matches paper/repo |
| Robot/model | RoboCat | verified | sources load; builder matches paper/repo |
| Robot/model | RLPD reference implementation | verified | sources load; builder matches paper/repo |
| Robot/model | KnowNo | verified | sources load; builder matches paper/repo |
| Robot/model | Tensor2Robot | corrected | github page shows repo archived Oct 22, 2025; added to Key specs |
| Project | Observation-to-action contract visualizer | verified | selects valid, split=100, prereqs resolve |
| Project | Hidden-state memory challenge | verified | selects valid, split=100, prereqs resolve |
| Project | Action-coordinate mismatch detective | verified | selects valid, split=100, prereqs resolve |
| Project | Episode timeline and schema inspector | verified | selects valid, split=100, prereqs resolve |
| Project | RLDS-to-LeRobot semantic round trip | verified | selects valid, split=100, prereqs resolve |
| Project | Robot data provenance firewall | verified | selects valid, split=100, prereqs resolve |
| Project | Policy scorecard with honest error bars | verified | selects valid, split=100, prereqs resolve |
| Project | Kitchen generalization tournament | verified | selects valid, split=100, prereqs resolve |
| Project | Physical-policy qualification gate | verified | selects valid, split=100, prereqs resolve |
| Project | Multimodal action distribution movie | verified | selects valid, split=100, prereqs resolve |
| Project | Denoising-budget control shootout | verified | selects valid, split=100, prereqs resolve |
| Project | Flow-versus-diffusion reproducibility challenge | verified | selects valid, split=100, prereqs resolve |
| Project | FAST action compression oscilloscope | verified | selects valid, split=100, prereqs resolve |
| Project | Chunk-horizon disturbance challenge | verified | selects valid, split=100, prereqs resolve |
| Project | Frequency-aware token allocation study | verified | selects valid, split=100, prereqs resolve |
| Project | Robot-camera feature atlas | verified | selects valid, split=100, prereqs resolve |
| Project | Frozen-encoder low-data race | verified | selects valid, split=100, prereqs resolve |
| Project | Precision-versus-semantics encoder audit | verified | selects valid, split=100, prereqs resolve |
| Project | Offline value optimism microscope | verified | selects valid, split=100, prereqs resolve |
| Project | CQL and IQL dataset-quality ladder | verified | selects valid, split=100, prereqs resolve |
| Project | Offline-policy release stress test | verified | selects valid, split=100, prereqs resolve |
| Project | Reward hacking museum | verified | selects valid, split=100, prereqs resolve |
| Project | VLM reward confusion gallery | verified | selects valid, split=100, prereqs resolve |
| Project | Eureka reward-code safety tournament | verified | selects valid, split=100, prereqs resolve |
| Project | DAgger distribution-shift sandbox | verified | selects valid, split=100, prereqs resolve |
| Project | Correction timing replay lab | verified | selects valid, split=100, prereqs resolve |
| Project | Shared-control coverage ablation | verified | selects valid, split=100, prereqs resolve |
| Project | Augmentation label-validity microscope | verified | selects valid, split=100, prereqs resolve |
| Project | MimicGen reset-coverage laboratory | verified | selects valid, split=100, prereqs resolve |
| Project | Multi-camera augmentation consistency challenge | verified | selects valid, split=100, prereqs resolve |
| Project | Pretrained-policy adaptation budget explorer | verified | selects valid, split=100, prereqs resolve |
| Project | Normalization and camera adaptation clinic | verified | selects valid, split=100, prereqs resolve |
| Project | Adapter merge versus forgetting benchmark | verified | selects valid, split=100, prereqs resolve |
| Project | Latency injection action-queue viewer | verified | selects valid, split=100, prereqs resolve |
| Project | Real-time chunk stitching bake-off | verified | selects valid, split=100, prereqs resolve |
| Project | Supervised arm deadline qualification | verified | selects valid, split=100, prereqs resolve |
| Project | Skill-API hallucination test stage | verified | selects valid, split=100, prereqs resolve |
| Project | Affordance-grounded plan ranking lab | verified | selects valid, split=100, prereqs resolve |
| Project | Generated robot-code contract arena | verified | selects valid, split=100, prereqs resolve |
| Project | Embodiment action-space passport | verified | selects valid, split=100, prereqs resolve |
| Project | Cross-robot negative-transfer benchmark | verified | selects valid, split=100, prereqs resolve |
| Project | Held-out embodiment adaptation challenge | verified | selects valid, split=100, prereqs resolve |
| Project | Continual-learning forgetting flipbook | verified | selects valid, split=100, prereqs resolve |
| Project | Self-generated data acceptance audit | verified | selects valid, split=100, prereqs resolve |
| Project | Rollback-first autonomous curriculum | verified | selects valid, split=100, prereqs resolve |
| Project | Uncertainty calibration help button | verified | selects valid, split=100, prereqs resolve |
| Project | Failure early-warning precision-recall lab | verified | selects valid, split=100, prereqs resolve |
| Project | Shift-aware stop-or-continue arena | verified | selects valid, split=100, prereqs resolve |
