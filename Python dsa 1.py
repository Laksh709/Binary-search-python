#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def locate_card(cards,query):
    pass


# In[ ]:


cards = [ 13,11,12,7,4,3,1,0]
query = 7
output = 3


# In[ ]:


result = locate_card(cards,query)
print(result)


# In[ ]:


result == output


# In[ ]:


test = {
    'input': {
        'cards' : [13,11,12,7,4,3,1,0],
        'query' : 7
},
        'output': 3 
}


# In[ ]:


locate_card(**test['input']) == test['output']


# In[ ]:


tests = []


# In[ ]:


tests.append(test)
#cards contain query in the middle
tests.append({
    'input': {
        'cards' : [13,11,12,7,4,3,1,0],
        'query' : 1
},
        'output': 6
})


# In[ ]:


#cards contain query as the first element
tests.append({
    'input': {
        'cards' : [4,2,1,-1],
        'query' : 4
},
        'output': 0
})


# In[ ]:


#cards contain only one element ,that is query itself
tests.append({
    'input': {
        'cards' : [6],
        'query' : 6
},
        'output': 0
})


# In[ ]:


#cards contain query at the end of the list
tests.append({
    'input': {
        'cards' : [3,-1,-9,-127],
        'query' : -127
},
        'output': 3
})


# In[ ]:


#cards does not contain the carry abd we assumne -1 to be the output in all such cases 
tests.append({
    'input': {
        'cards' : [9,7,5,2,-9],
        'query' : 4
},
        'output': -1
})


# In[ ]:


#cards is empty
tests.append({
    'input': {
        'cards' : [],
        'query' : 4
},
        'output': -1
})


# In[ ]:


tests.append({
    'input': {
        'cards' : [9,7,5,2,-9],
        'query' : 4
},
        'output': -1
})


# In[ ]:


#query can occur multiple times , we expect the function to return the position of the first query
tests.append({
    'input': {
        'cards' : [8,8,6,6,6,6,6,6,2,2,2,1,1],
        'query' : 6
},
        'output': 2
})


# In[ ]:


#there can be multiple numbers in cards
tests.append({
    'input': {
        'cards' : [2,2,2,2,3,3,4,4,4,5,6,6],
        'query' : 5
},
        'output': 9
})


# In[ ]:


tests


# In[ ]:


def locate_card(cards, query):
    position = 0 

    while True :
       if cards[position] == query:
        return position 

       position += 1

       if position == len(cards):
            return -1



# In[ ]:


test


# In[ ]:


result = locate_card(test['input']['cards'] , test['input']['query'])
result


# In[ ]:


result == output


# In[ ]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[ ]:


from jovian.pythondsa import evaluate_test_case


# In[ ]:


evaluate_test_case(locate_card , test)


# In[ ]:


from jovian.pythondsa import evaluate_test_cases


# In[ ]:


evaluate_test_cases(locate_card , tests)


# In[ ]:


def locate_card(cards, query):
    position = 0 
    print('cards:',cards)
    print('query:',query)

    while True :
        print('position:',position)

        if cards[position]==query:
            return position


        position += 1
        if position == len(cards):
            return -1






# In[ ]:


cards6 = tests[6]['input']['cards']
query6 = tests[6]['input']['query']
locate_card(cards6,query6)


# In[ ]:


def locate_card(cards, query):
    position = 0

    while position<len(cards) :
        if cards[position] == query:
            return position
        position +=1
    return -1   


# In[ ]:


tests[6]


# In[ ]:


import os
print(os.getcwd())


# In[ ]:




