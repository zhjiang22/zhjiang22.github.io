---
title:          "AutoSQL: Extracting SQL Templates from Imperative ORM Code in Large-Scale Repositories"
date:           2026-10-12 00:00:00 +0800
selected:       false
pub:            >-
                The IEEE/ACM International Conference on Automated Software Engineering.
pub_pre:        >-
                <span class="badge badge-custom badge-ase">ASE'26</span>
pub_venue: "Munich, Germany"
abstract: >-
    Suboptimal SQL queries can significantly degrade the performance of cloud systems, motivating the extraction and auditing of SQL statements before deployment. However, Go ORM frameworks construct SQL imperatively through scattered method-call sequences, making the resulting SQL templates difficult to recover statically. We present AutoSQL, which builds a Code Index, a directed graph capturing structural dependencies among functions, types, and global variables, and traces upstream call chains from ORM invocation sites to identify database-interacting entry points. For each entry point, an LLM agent traverses the Code Index to collect the code slices that influence SQL generation, switching to pattern-based search when the graph cannot resolve a retrieval goal, and then synthesizes SQL templates. On 579 test-covered entry points and 1,186 runtime-traced SQL statements from five large-scale Go repositories, AutoSQL achieves 68.04% to 72.18% recall, outperforming existing methods by 8.52% to 21.50%.
authors:
    - Junsong Pu
    - Yichen Li
    - Zhuangbin Chen
    - Zhihan Jiang
    - Zibin Zheng
links:
  Paper:
  Arxiv: https://arxiv.org/abs/2608.15595
  Project: https://zenodo.org/records/21872535
  Slides:
  DOI:
  BibTex:
---
