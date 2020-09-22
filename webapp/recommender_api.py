import pickle as pkl
import numpy as np
import pandas as pd
from scipy.spatial import distance

with open("./all.pkl", "rb") as f:
    (category_word,topic_document,word_topic,identity) = pkl.load(f)

    
def get_recommendation(x_inputs):
    words=x_inputs['search_terms'].split('+')
    rating_limit=float(x_inputs['minimum_rating'])
    location=(float(x_inputs['latitude']),float(x_inputs['longitude']))
    radius=float(x_inputs['radius'])
    same=(x_inputs['same']=='Same・同')
    vector=np.zeros(10)
    for word in words:
        if word in set(topic_document['url']):
            vector+=np.array(topic_document[topic_document['url']==word][[0,1,2,3,4,5,6,7,8,9]])
        elif word in word_topic.columns:
            vector+=np.array(word_topic[word])
    vector=vector/np.sum(vector)
    test=pd.DataFrame()
    test['cosine_distance']=topic_document[[0,1,2,3,4,5,6,7,8,9]].apply(lambda x:
        distance.cosine(x,vector),axis=1, raw=True)
    test['distance']=((111*(identity['latitude']-location[0]))**2 + 
        (90*(identity['longitude']-location[1]))**2)**0.5
    test['rating']=identity['rating']
    test['url']=identity['url']
    test['name']=identity['name']
    test=test[test['rating']>=rating_limit]
    test=test[test['distance']<=radius]
    test.sort_values(by='cosine_distance',inplace=True,ascending=same,ignore_index=True)
    recommended ={}
    recommended_list=list(test['name'].head(5))
    for shop,url in zip(recommended_list,list(test['url'].head(5))):
        recommended[shop]=url
    return (x_inputs,recommended_list,recommended,vector)
