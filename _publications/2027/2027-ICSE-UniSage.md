---
title:          "UniSage: A Unified and Diagnosis-Driven Sampling Framework for Microservice Systems"
date:           2027-04-25 00:00:00 +0800
selected:       false
pub:            >-
                The IEEE/ACM International Conference on Software Engineering.
pub_pre:        >-
                <span class="badge badge-custom badge-icse">ICSE'27</span>
pub_venue: "Dublin, Ireland"
abstract: >-
    Traces and logs are the backbone of observability in microservice systems, but their volume makes sampling unavoidable, and existing sample-before-analysis frameworks discard data before its diagnostic value is known.
    UniSage adopts a diagnosis-driven paradigm: a lightweight anomaly detection and root cause analysis module scans the full stream of traces and logs before sampling decisions are made, so that an analysis-guided sampler retains the data tied to detected anomalies while an edge-case sampler preserves rare but critical behaviors.
    At a 2.5% sampling rate, UniSage retains 71% of critical traces and 96.25% of relevant logs, far above the best existing methods, and processes a 20-minute multi-modal data block in about 10 seconds.

authors:
    - Zhouruixing Zhu
    - Zhihan Jiang
    - Tianyi Yang
    - Pinjia He

links:
  Paper: https://arxiv.org/pdf/2509.26336
  Arxiv: https://arxiv.org/abs/2509.26336
  BibTex: https://www.zhihan-jiang.com/files/ICSE27/UniSage-bibtex.txt
---
