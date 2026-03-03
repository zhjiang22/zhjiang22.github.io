---
title:          "ErrorPrism: Reconstructing Error Propagation Paths in Cloud Service Systems"
date:           2025-11-16 00:00:00 +0800
selected:       false
pub:            >-
                The IEEE/ACM International Conference on Automated Software Engineering.
pub_pre:        >-
                <span class="badge badge-custom badge-ase">ASE'25</span>
pub_venue: "Seoul, South Korea"
abstract: >-
    Reliability management in cloud service systems is challenging due to the cascading effect of failures.
    Error wrapping, a practice prevalent in modern microservice development, enriches errors with context at each layer of the function call stack, constructing an error chain that describes a failure from its technical origin to its business impact.
    However, this also presents a significant traceability problem when recovering the complete error propagation path from the final log message back to its source. Existing approaches are ineffective at addressing this problem.
    To fill this gap, we present ErrorPrism for automated reconstruction of error propagation paths in production microservice systems by integrating static analysis and an LLM agent.


authors:
    - Junsong Pu
    - Yichen Li
    - Zhuangbin Chen†
    - Jinyang Liu
    - Zhihan Jiang
    - Jianjun Chen
    - Rui Shi
    - Zibin Zheng
    - Tieying Zhang


links:
  Paper: https://www.zhihan-jiang.com/files/ASE25/ErrorPrism.pdf
  Arxiv: https://arxiv.org/abs/2509.26463
  Slides: https://www.zhihan-jiang.com/files/ASE25/ErrorPrism-slides.pdf
  DOI: https://doi.org/10.1109/ASE63991.2025.00292
  BibTex: https://www.zhihan-jiang.com/files/ASE25/ErrorPrism-bibtex.txt
---
