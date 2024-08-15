import json
from matplotlib import pyplot as plt
import numpy as np
import os

kn_dir = './3_modify/'
fig_dir = './figs/'

# with open(os.path.join(kn_dir, 'modify_activation_rlt.json'), 'r') as f:
#     modified_rlts = json.load(f)
# with open(os.path.join(kn_dir, 'base_modify_activation_rlt.json'), 'r') as f:
#     base_modified_rlts = json.load(f)

with open(os.path.join(kn_dir, 'modify_activation_rlt_4.json'), 'r') as f:
    modified_rlts_4 = json.load(f)
with open(os.path.join(kn_dir, 'modify_activation_rlt_6.json'), 'r') as f:
    modified_rlts_6 = json.load(f)
with open(os.path.join(kn_dir, 'modify_activation_rlt_8.json'), 'r') as f:
    modified_rlts_8 = json.load(f)
with open(os.path.join(kn_dir, 'modify_activation_rlt_10.json'), 'r') as f:
    modified_rlts_10 = json.load(f)
with open(os.path.join(kn_dir, 'modify_activation_rlt_12.json'), 'r') as f:
    modified_rlts_12 = json.load(f)


rel_set = set()

for k, v in modified_rlts_4.items():
    rel = k.split('-')[-1]
    rel_set.update([rel])

rel_list = sorted(list(rel_set))
if not os.path.exists(fig_dir): # create figure directory
    os.makedirs(fig_dir)

# ================================== suppress ===========================================
# plt.figure(figsize=(22, 5.5), dpi=100)

# x_labels = []
# y_values = []
# for rel in rel_list:
#     x_labels.append(rel)
#     key = 'kn_bag-' + rel
#     base_key = 'base_kn_bag-' + rel
#     tmp_ys = []
#     tmp_ys.append(modified_rlts[key]['rm_own:ave_delta_ratio'])
#     tmp_ys.append(base_modified_rlts[base_key]['rm_own:ave_delta_ratio'])
#     y_values.append(tmp_ys)

# plt.ylabel('Correct Probability Change Ratio', fontsize=18)

# x1 = np.array([1 + i * 3 for i in range(len(rel_list))])
# x2 = x1 + 1
# ys = np.array(y_values)
# print(ys.mean(axis=0))

# plt.xticks([i * 3 + 1.5 for i in range(len(x_labels))], labels=x_labels)
# plt.bar(x1, ys[:, 0], width=1, edgecolor='black', hatch="//", color='#0165fc', label="Integrated gradients")
# plt.bar(x2, ys[:, 1], width=1, edgecolor='black', hatch="\\\\", color='#bfefff', label="Baseline")
# plt.yticks(np.arange(-0.6, 0.3, 0.1), [f'{y}%' for y in np.arange(-60, 30, 10)], fontsize=20)
# plt.xlim(-1, 3 * len(x_labels) + 1)
# plt.tick_params(axis="x", bottom=False, top=True, labelbottom=False, labeltop=True, rotation=25, labelsize=18)
# plt.grid(True, axis='y', alpha=0.3)

# plt.legend(loc='upper right', fontsize=20)

# plt.tight_layout()
# plt.savefig(os.path.join(fig_dir, 'suppress.pdf'))
# plt.close()

# ================================== amplify ===========================================
# plt.figure(figsize=(22, 5.5), dpi=100) # amplify_2
# plt.figure(figsize=(22, 12), dpi=100) # amplify_4
plt.figure(figsize=(22, 18), dpi=100) # amplify_6

x_labels = []

y_values_4 = []
y_values_6 = []
y_values_8 = []
y_values_10 = []
y_values_12 = []

for rel in rel_list:
    x_labels.append(rel)
    key = 'kn_bag-' + rel

    y_values_4.append(modified_rlts_4[key]['eh_own:ave_delta_ratio'])
    y_values_6.append(modified_rlts_6[key]['eh_own:ave_delta_ratio'])
    y_values_8.append(modified_rlts_8[key]['eh_own:ave_delta_ratio'])
    y_values_10.append(modified_rlts_10[key]['eh_own:ave_delta_ratio'])
    y_values_12.append(modified_rlts_12[key]['eh_own:ave_delta_ratio'])


plt.ylabel('Correct Probability Change Ratio', fontsize=18)

x = np.arange(len(rel_list))
width = 0.15

plt.bar(x - 2*width, y_values_4, width, label='Amplify 4', color='#5dade2', edgecolor='black')
plt.bar(x - width, y_values_6, width, label='Amplify 6', color='#f8c471', edgecolor='black')
plt.bar(x, y_values_8, width, label='Amplify 8', color='#27ae60', edgecolor='black')
plt.bar(x + width, y_values_10, width, label='Amplify 10', color='#ec7063', edgecolor='black')
plt.bar(x + 2*width, y_values_12, width, label='Amplify 12', color='#c39bd3', edgecolor='black')

plt.xticks(x, labels=x_labels, rotation=25, fontsize=18)
plt.yticks(np.arange(-0.6, 4.4, 0.1), [f'{y}%' for y in np.arange(-60, 440, 10)], fontsize=20)

plt.xlim(-1, len(x_labels))
plt.grid(True, axis='y', alpha=0.3)

plt.legend(loc='upper right', fontsize=20, bbox_to_anchor=(0.96, 0.99))

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'amplify_all.pdf'))
plt.close()