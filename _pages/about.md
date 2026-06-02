---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

林燊，讲师/硕士生导师，于2025年6月获得西安电子科技大学网络空间安全专业博士学位（导师：陈晓峰教授），2025年8月加入福建师范大学计算机与网络空间安全学院许力教授团队。<a href='https://scholar.google.com/citations?user=ORwuKSYAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FTravaill%2FTravaill.github.io%40google-scholar-stats%2Fgs_data_shieldsio.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

邮箱：linshen@fjnu.edu.cn

主要研究方向：
- Machine Unlearning
- Model Watermarking
- Model Red Teaming
- Adversarial Examples
- Jailbreak Attacks
- Vision Language Models
- Multi-modal Large Language Models


<span class='anchor' id='news'></span>
# 🔥 近期新闻

- 招收27级网络空间安全学硕和人工智能专硕，欢迎感兴趣的同学发邮件咨询，详情请见**招生信息**

<span class='anchor' id='publications'></span>
# 📝 主要成果

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2023</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ERM-KTP: Knowledge-Level Machine Unlearning via Knowledge Transfer](https://openaccess.thecvf.com/content/CVPR2023/html/Lin_ERM-KTP_Knowledge-Level_Machine_Unlearning_via_Knowledge_Transfer_CVPR_2023_paper.html)

**Shen Lin**, Xiaoyu Zhang, Chenyang Chen, Xiaofeng Chen, Willy Susilo

[**Paper**](https://openaccess.thecvf.com/content/CVPR2023/html/Lin_ERM-KTP_Knowledge-Level_Machine_Unlearning_via_Knowledge_Transfer_CVPR_2023_paper.html) <strong><span class='show_paper_citations' data='ORwuKSYAAAAJ:YOUR_CITATION_ID'></span></strong>
- An interpretable knowledge-level machine unlearning method based on knowledge disentanglement and directed knowledge transfer.
</div>
</div> -->

## 已发表学术论文

- ``CVPR 2023`` **Shen Lin**, Xiaoyu Zhang, Chenyang Chen, Xiaofeng Chen, and Willy Susilo. ERM-KTP: Knowledge-Level Machine Unlearning via Knowledge Transfer. **Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)**. 2023: 20147-20155. **(CCF-A)**
- ``ACM MM 2024`` **Shen Lin**, Xiaoyu Zhang, Willy Susilo, Xiaofeng Chen, and Jun Liu. GDR-GMA: Machine Unlearning via Direction-Rectified and Magnitude-Adjusted Gradients. **Proceedings of the 32nd ACM International Conference on Multimedia (ACM MM)**. 2024: 9087-9095. **(CCF-A)**
- ``TNSE 2025`` **Shen Lin**, Xiaoyu Zhang, Xu Ma, Xiaofeng Chen, Willy Susilo. DeepAW: A Customized DNN Watermarking Scheme Against Unreliable Participants. **IEEE Transactions on Network Science and Engineering (TNSE)**, 2025, 12(4): 2758 - 2769. **(Q1, IF=7.9)** 
- ``TDSC 2023`` Xiaoyu Zhang, **Shen Lin**, Chao Chen, and Xiaofeng Chen. MODA: Model Ownership Deprivation Attack in Asynchronous Federated Learning. **IEEE Transactions on Dependable and Secure Computing (TDSC)**, 2023, 21(4): 4220-4235. **(CCF-A)**
- ``TDSC 2025`` Chenyang Chen, Xiaoyu Zhang, **Shen Lin**, Xiaofeng Chen. MPGStack: Membership Privacy Protection on Graph Data via Model Stacking. **IEEE Transactions on Dependable and Secure Computing (TDSC)**, 2025, 22(4): 3723-3726. **(CCF-A)**
- ``ECCV 2024`` Qihao Zhao, Yalun Dai, **Shen Lin**, Wei Hu, Fan Zhang, Jun Liu. LTRL: Boosting Long-tail Recognition via Reflective Learning. **European Conference on Computer Vision (ECCV)**, 2024: 1-18. **(Oral, CCF-B)**

## Preprints

- ``arXiv 2026`` **Shen Lin**, Junhao Dong, Rongjie Chen, Xiaoyu Zhang, Li Xu, Xiaofeng Chen. [CATA: Continual Machine Unlearning via Conflict-Averse Task Arithmetic](https://arxiv.org/abs/2605.18610)

- ``arXiv 2026`` **Shen Lin**, Jing Lin, Junhao Dong, Piotr Koniusz, Li Xu. [ICED: Concept-level Machine Unlearning via Interpretable Concept Decomposition](https://arxiv.org/abs/2605.14309)

## 发明专利
- 张肖瑜，金育霖，吴凯，陈晨洋，**林燊**. 即插即用预训练模型后门去除系统、方法、设备及介质, CN202210216214.7
- 许力，李雁姿，陈兰香，李家印，章静，**林燊**. 一种基于Transformer的Fiedler蛛网隐私保护噪声机制构建方法, CN202511409420.X
- 林丽美，陈伟鑫，吴际轩，黄艳泽，陈志德，**林燊**，方定邦，陈小薇，楼炜. 一种因果驱动的动态图神经网络解释生成方法, 202610216102X
- 林丽美，赵常宇，陈亮，陈志德，**林燊**，方定邦，陈小薇，黄艳泽，汪晓丁. 基于核空间映射与语义对齐的多模态大模型表征学习方法及系统, 2026100056870

<span class='anchor' id='projects'></span>
# 🔬 科研项目

- 福建省青年科技人员育成项目：面向多模态大模型的有害知识删除技术研究，项目负责人，2026.05-2028.04
- 福建省产业技术开发和应用计划项目：基于安全增强型人工智能模型的网络数据安全关键技术研发及示范应用，核心成员，2025.08-2027.01
- 福州市人工智能“揭榜挂帅”科技重大项目：面向人机协同的城市基层精细化治理多模态感知与决策大模型技术研发，核心成员，2025.09-2028.09


<span class='anchor' id='educations'></span>
# 📖 个人经历

- *2025.08 - Present*, Lecturer, College of Computer and Cyberspace Security, Fujian Normal University, China.

- *2023.10 - 2024.10*, Visiting Scholar, Singapore University of Technology and Design, Singapore.

- *2021.09 - 2025.06*, Ph.D. in Cyberspace Security, Xidian University, China, supervised by [Prof. Xiaofeng Chen](https://web.xidian.edu.cn/xfchen/index.html).


<span class='anchor' id='academic-services'></span>
# 💻 学术服务

- Reviewer for CVPR, ICCV, NeurIPS, ACM MM, IEEE TKDE, and IEEE TDSC.


<span class='anchor' id='students'></span>
# 👥 指导学生

### 研究生

- 李雁姿 (博三，协助指导) 
- 陈蓉杰 (研一，协助指导) 
- 陈伟琛 (研一，协助指导)

### 本科生

- 林晶 (2023级)
- 黄航翌 (2024级)
- 陈龙坤 (2024级)
- 洪凯翔 (2024级)
- 李佳麒 (2025级)
- 刘海林 (2025级)

<span class='anchor' id='prospective-students'></span>
# 📢 招生信息 

本人立志“长期处于科研一线，促进学生全面发展”，请先了解我的研究方向，欢迎感兴趣的同学附上个人简历发邮件咨询。

**对学生的期望：**

- 对学术有一定的追求，能够和我一起做一些有趣的工作
- 具备良好的英文阅读和写作能力，并养成高质量文献阅读习惯
- 具备一定的编程基础，能够较快上手科研代码的实现、复现、调试与分析


**FAQ**

1. **入组后的培养节奏大致是怎样的？**  我会根据每位同学的基础和兴趣，安排参与组内已有一定积累、相对成熟的课题，让大家先在真实任务中熟悉科研是怎么推进的：如何读论文、如何复现代码、如何设计实验、如何分析结果，以及如何把工作整理成论文。等大家逐渐熟悉科研节奏后，我会鼓励同学们结合自己的兴趣提出新想法，逐步走向独立的研究。

2. **本科没有科研经历可以联系吗？** 科研能力不是一开始就具备的，而是在持续阅读、讨论、实验和写作中逐渐训练出来的。相比已有成果，我更看重同学是否愿意主动学习、持续投入、认真反馈。如果你目前基础还不够扎实，也不用过度焦虑，但需要愿意补基础、写代码、读论文，并保持稳定的学习节奏。

3. **课题组需要打卡考勤吗？** 不强制打卡考勤。每个人高效学习和工作的时间不完全一样，我更希望大家能够在相对自由的氛围中找到适合自己的节奏。课题组更看重阶段性进展和实际成果，希望同学们能够自主安排时间，在完成阶段目标后主动和我交流讨论。

4. **平时怎么和导师交流？** 正常情况下，课题组每周会开一次组会。组会不会只是简单“汇报进度”，而是一个大家一起交流想法的地方。每位同学每周轮流分享近期看到的有趣论文、技术进展或实验发现，然后大家一起讨论。之后再交流近期进展、遇到的问题以及下一步计划。如果有额外问题，也欢迎单独约我讨论。

5. **硕士毕业有什么要求？** 首先需要满足学校和学院的毕业要求。在此基础上，我希望每位同学尽量完成一篇小论文，作为毕业论文的重要支撑，也降低盲审和毕业过程中的不确定性。

6. **是否支持实习？** 在不影响毕业和课题进展的前提下，支持同学们出去实习。

7. **课题组是否有补助或奖励？** 课题组会尽量为大家提供公平、透明的支持。对于承担额外工作、帮助课题组建设，或者取得高水平科研成果的同学，我会给予相应奖励。

8. **实验室氛围怎么样？** 我希望课题组是一个相互支持、彼此成就的地方。同学之间可以互相帮助、共同进步，而不是各做各的、彼此封闭。

9. **是否有国际交流机会？** 鼓励大家积极参加高水平学术会议，也鼓励有条件的同学争取国内外交流机会。对于有出国深造计划的同学，我会尽量提供硕士阶段出国交流、合作研究或提前联系海外导师的机会，帮助大家更早了解国外科研环境，提高后续申请成功率。

10. **是否支持继续深造？** 对于有继续读博或出国深造想法的同学，我会根据大家的研究方向、能力基础和个人规划，帮助推荐合适的导师和学校。海外方向包括新加坡 NTU、SUTD 等高校；国内方向包括西电、东南、港理工等高校。

