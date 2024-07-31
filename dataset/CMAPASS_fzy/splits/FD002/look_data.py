import numpy as np

#导入npy文件路径位置
arr_outcomes = np.load('./FD002_split1.npy', allow_pickle=True)
# data = np.load('./PTdict_list_2.npy', allow_pickle=True)

# print(arr_outcomes["Length_of_stay"])
print(arr_outcomes)