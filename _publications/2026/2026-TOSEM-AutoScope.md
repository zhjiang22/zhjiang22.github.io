---
title:          "AutoScope: Code Knowledge Enhanced Span-level Sampling for Distributed Tracing"
date:           2026-06-27 00:00:00 +0800
selected:       false
pub:            >-
                ACM Transactions on Software Engineering and Methodology.
pub_pre:        >-
                <span class="badge badge-custom badge-tosem">TOSEM'26</span>
abstract: >-
    Distributed tracing is essential for diagnosing microservice systems, yet the sheer volume of traces burdens backend storage, and existing trace-level sampling typically keeps only anomalous traces while discarding the normal ones needed for comparative analysis. We introduce AutoScope, a span-level sampling method that leverages static code analysis to extract execution logic and preserve critical spans while maintaining trace structure consistency. This span-level paradigm substantially shrinks stored traces without sacrificing coverage of faulty spans, improving downstream root cause analysis.
authors:
    - Yulun Wu
    - Guangba Yu
    - Zhihan Jiang
    - Yichen Li
    - Michael R. Lyu
links:
  Paper: https://www.zhihan-jiang.com/files/TOSEM2026/AutoScope.pdf
  Arxiv: https://arxiv.org/abs/2509.13852
  Project:
#   Slides:
  DOI:
  BibTex: https://www.zhihan-jiang.com/files/TOSEM2026/AutoScope-bibtex.txt
---
