---
title:          "SimServing: Native-Execution Simulation for Evolution-Resilient LLM Serving Configuration Tuning"
date:           2026-10-12 00:00:02 +0800
selected:       false
pub:            >-
                The IEEE/ACM International Conference on Automated Software Engineering.
pub_pre:        >-
                <span class="badge badge-custom badge-ase">ASE'26</span>
pub_venue: "Munich, Germany"
abstract: >-
    Large Language Model (LLM) services expose a large configuration space that critically affects performance, but tuning it on real hardware is prohibitively expensive, and state-of-the-art simulators re-implement the serving framework's control logic, creating a copy that inevitably drifts from the rapidly evolving upstream software. We present SimServing, a hybrid simulation framework that executes the native, unmodified serving software while replacing only the GPU computation with a pluggable latency estimator, thereby automatically inheriting upstream updates. Integrated with Particle Swarm Optimization, SimServing reduces throughput prediction error from 13.8% to 4.9%, achieves up to 21.18× simulation speedup, and discovers configurations that improve throughput by up to 10.2%.
authors:
    - Yujie Huang
    - Jiazhen Gu
    - Zhihan Jiang
    - Michael R. Lyu
links:
  Paper: https://www.zhihan-jiang.com/files/ASE26/SimServing.pdf
  # Arxiv:
  Project: https://figshare.com/articles/dataset/Artifact_for_SimServing_Native-Execution_Simulation_for_Evolution-Resilient_LLM_Serving_Configuration_Tuning_/31899004
  Slides: /files/ASE26/SimServing-slides.pdf
  DOI: https://doi.org/10.1145/3832783.3834362
  BibTex: https://www.zhihan-jiang.com/files/ASE26/SimServing-bibtex.txt
---
