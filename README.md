# Determining and erasing knowledge neurons in Transformer model

From 1/2024 to 8/2024, defense at Computer Science committee of Information Technology faculty - VNU-HCM University of Science. \
Advisor: Assoc. Prof. [Lê Hoàng Thái](https://www.fit.hcmus.edu.vn/~lhthai/).

| Name   | Nguyễn Trương Hoàng Thái[^1]  | Nguyễn Thiên Phúc[^1]  |
|---|---|---|
| Student ID  | 20127625  | 20127681  |

# Introduction
Our research focuses on determining and erasing knowledge neurons in [BERT-based-case](https://doi.org/10.48550/arXiv.1810.04805) model based on [integrated gradients](https://proceedings.mlr.press/v70/sundararajan17a.html) method, with the goal of privacy and saving retrain resource. Our experiment is conducted on cloze task [dataset](https://github.com/Thaifitus/determining_and_erasing_kns_in_transformer_thesis/blob/main/data/PARAREL/data_all_allbags.json) and evaluated with two main metrics which are model accuracy and perplexity. Our research mainly based on [Damai Dai 2022](https://doi.org/10.18653/v1/2022.acl-long.581) research.

# Task List
| Task  | Description  | Thai  | Phuc  |
|---|---|---|---|
| **I. Theory research**  |   | |   |
| Machine Unlearning survey  | Read survey paper [A Survey of Machine Unlearning](https://doi.org/10.48550/arXiv.2209.02299) and the [repository](https://github.com/tamlhp/awesome-machine-unlearning.git) to study Machine Unlearning and choose thesis topic. | <center>X</center>  | <center>X</center>  |
| Transformer architecture   | 1. RNN, LSTM, seq2seq model <br> 2. Attention mechanism <br> 3. Vanilla Transformer model | <center>X</center>  | <center>X</center>  |
| BERT model  | 1. Bidirectional property <br> 2. Model architecture <br> 3. Masked Language Model (MLM), Next Sentence Prediction (NSP).   | <center>X</center>  |   |
| Knowledge Neurons in Pretrained Transformers (proposed method)  | 1. Transformer is related to key-value <br> 2. Assessing Task (cloze task) <br> 3. Knowledge attribution method <br> 4. Neuron refining <br> 5. Experiments <br> 6. Erasing relation | <center>X</center>  | <center>X</center>[^2]  |
| Key-Value Memories  | Feed-forward layers as key-value memories, keys capture input patterns in paper [Transformer Feed-Forward Layers Are Key-Value Memories](https://doi.org/10.48550/arXiv.2012.14913).  | <center>X</center>  |   |
| Integrated Gradients  | Read paper [Axiomatic Attribution for Deep Networks](https://proceedings.mlr.press/v70/sundararajan17a.html).  | <center>X</center>[^3]  | <center>X</center>  |
| 	Self-attention attribution method | Read paper [Self-Attention Attribution: Interpreting Information Interactions Inside Transformer](https://ojs.aaai.org/index.php/AAAI/article/view/17533).  | <center>X</center>[^3]  | <center>X</center>  |
| Data  | Research PARAREL dataset.  | <center>X</center>[^3]  | <center>X</center>   |
| **II. Code research**  |   |   |   |
| EDA  | Basic Data Exploration (implemented in single notebook): row, column, duplication, WordCloud, length, template, prompt.  | <center>X</center>[^3]  | <center>X</center>  |
| Model  | Study custom BERT model in *custom_bert.py*.  | <center>X</center>  |   |
| Calculate attribution score of neurons  | Create function recipe and modify *1_analyze_mlm.py* for experiment.  | <center>X</center>  | <center>X</center>[^4]  |
| Refine neurons  | Create function recipe and modify *2_get_kn.py* for experiment.  | <center>X</center>  |   |
| Knowledge neuron statistic  | Create function recipe and modify *2_analyze_kn.py* for experiment.  | <center>X</center>  |   |
| Modify attribution score  | Create function recipe and modify (amplifying coefficient 4 and 6) *3_modify_activation.py* for experiment.  | <center>X</center>  |   |
| Erase knowledge  | Create function recipe and modify *7_erase_knowledge.py* for experiment; erase knowledge neurons in dense (hidden) layer.  | <center>X</center>  |   |
| Survey implement  | Create notebook files, research GPUs, apply Git.   | <center>X</center>  |   |
| **III. Write latex report**  | (1) Section: 1.1 + 2.1 + 2.2 + 3.1 + 3.2 + 3.3.2 + 4.1.1 <br> (2) Section: 1.2 &rarr; 1.4 + 2.3 + 2.4 + 3.3.1 + 3.4 + 4.1.2 &rarr; 4.6  | <center>X</center>[^5]  | <center>X</center>[^6]  |
| **IV. Other tasks**  |   |   |   |
| Remove gpt-1 research  |   | <center>X</center>  |   |
| Rewrite proposal, change thesis title  | Clarify contribution of the thesis.  | <center>X</center>  |   |

# Reproduce experiment results
To reproduce results, upload notebook files in `/exe_notebook` to Kaggle or Google , then modify survey parameter(s) and `Run all` cells. Please refer [Hunter-DDM/knowledge-neurons](https://github.com/Hunter-DDM/knowledge-neurons/blob/main/README.md) repository for parameters description.

# Hardware, language and framework
We use GPU P100, GPU L4 and GPU A100 for the experiment. The programming language is Python using Pytorch framework.

# Challenge
After proposal submission which was theoretical research, Phuc could not understand model's inference process and source code implementation. I had to complete tasks, remove GPT-1 with some survey tasks by myself. \
I want to give sincere thanks to my family and our advisor Assoc. Prof. Le Hoang Thai for supporting me during the thesis.

# Pricing (VND)
* Colab Pro+: $\approx$ 1 384 000 (Colab price + tax + bank charge)
* Printing: $\approx$ 180 000

Contribution formula: $`\frac{\text{task completed in Task List (I + II + IV)}}{\text{total task in three corresponding sections}}`$. Team tasks like Machine Unlearning survey, Transformer architecture in section I and section III are not contained in contribution. Phuc's contribution: $`\frac{0.5 \times 5 + 0.25}{16}`$, Thai's contribution: $`\frac{1 + 0.5 + 1 + 0.5 \times 4 + 1 + 0.75 + 7}{16}`$.
[^1]: Phuc's contribution percentage is 17.19% based on the above formula. Thai's contribution percentage is 82.81%.
[^2]: Research 2 + 3 + dataset in 5.
[^3]: Propose research structure and review result.
[^4]: Study two functions *example2feature* and *scaled_input*.
[^5]: Write sections listed in (2).
[^6]: Write sections listed in (1).

