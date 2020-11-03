#!/usr/bin/env python
# coding: utf-8

# In[1]:


import jieba

jieba.set_dictionary('dict.txt.big.txt')

jieba.load_userdict('user_dict.txt')

with open('stopword.txt','r', encoding='utf-8-sig') as file:
    swds = file.read().split('\n')
print("停用詞："+'|' . join(swds))




documents = ['我來自國立台中教育大學，','就讀數位系', '我喜歡出國旅遊，', '關心社會時事。']
# 精確模式 預設 false
for sentence in documents:
    seg_list = jieba.cut(sentence)
    print('/'.join(seg_list))

print('---------------')

# 全模式
for sentence in documents:
    seg_list = jieba.cut(sentence, cut_all=True)
    print('/'.join(seg_list))

print('---------------')

# 搜索引擎模式
for sentence in documents:
    seg_list = jieba.cut_for_search(sentence)
    print('/'.join(seg_list))



# In[2]:


import jieba.analyse
news = '中央流行疫情指揮中心今日宣布，國內新增2例武漢肺炎（新型冠狀病毒病，COVID-19）境外移入，分別為分別自菲律賓及美國入境。指揮中心發言人莊人祥表示，案549為20多歲菲律賓籍女性，因工作於今年9月30日入境台灣，搭機前3日內檢驗陰性，入境時至集中檢疫期滿均無症狀，10月13日檢疫期滿前採檢結果為陰性，檢疫期滿後由仲介安排至隔離宿舍進行自主健康管理，並於10月22由仲介安排至醫院自費檢驗，於今日確診，目前住院隔離中。'
tags = jieba.analyse.extract_tags(news, topK=5, withWeight=True)

# 引用文字來源 ：https://news.ltn.com.tw/news/life/breakingnews/3331012

for tag in tags:
    print('word:', tag[0], 'tf-idf:', tag[1])
# 程式參考來源： https://blog.kennycoder.io/categories/Python/


# In[ ]:




