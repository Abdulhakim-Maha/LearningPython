import pandas as pd

def find_covariance(lis):
	data_sets = pd.read_csv('GBvideos.csv',encoding='utf-8',usecols=['video_id','likes','dislikes'])
	filt = data_sets[data_sets['video_id'].isin(lis)]
	co = filt.cov()
	return co['likes'][1]

lis = ['_JbpTEtGTz8','24-AhdoN_Nk','I6YQz96PYvw','lERhNXw6FaQ','mTf3Dcj5NPU','LmOPXhFensg','lERhNXw6FaQ','24-AhdoN_Nk',
'HzILu6yyA20','Oa9c9JBBGxM','CE7SkcoyVAI','x1QroTKqG8c','3uGIEY7tdg8','ILDMJavIY-k','fAIX12F6958']

print('Covariance of likes and dislikes :',find_covariance(lis))