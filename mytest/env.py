import numpy as np
import time
import sys
import ndcg_computing

class docenv:
    def __init__(self, candidate_list):
        self.doc_obs={}
        self.candidate_docs_dict=candidate_list
        self.length=len(candidate_docs_dict)
        self.build_doc_env(dco_obs)
        self.action_space=['select','skip']
        self.n_actions = len(self.action_space)
    
    def step_and_update(self, action, doc):
        self.doc_obs[doc]=action


    def get_reward(self):
        result_list=[]
        grade_list=[]
        for k in self.doc_obs.it:
            if self.doc_obs[k]='select':
                result_list.append(k)
        for l in result_list:
            grade=self.candidate_docs_dict[l]
            grade_list.append(grade)
            r=np.array(grade_list)
        ndcg_score=ndcg_computing.computing(r)
        if ndcg> :
            reward=1
        elif  ndcg> :
            reword=0
        
        return reword
