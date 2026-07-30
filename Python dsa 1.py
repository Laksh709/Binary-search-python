#!/usr/bin/env python
# coding: utf-8

# In[1]:


def locate_card(cards,query):
    pass


# In[2]:


cards = [ 13,11,12,7,4,3,1,0]
query = 7
output = 3


# In[3]:


result = locate_card(cards,query)
print(result)


# In[4]:


result == output


# In[5]:


test = {
    'input': {
        'cards' : [13,11,12,7,4,3,1,0],
        'query' : 7
},
        'output': 3 
}


# In[6]:


locate_card(**test['input']) == test['output']


# In[7]:


tests = []


# In[8]:


tests.append(test)
#cards contain query in the middle
tests.append({
    'input': {
        'cards' : [13,11,12,7,4,3,1,0],
        'query' : 1
},
        'output': 6
})


# In[9]:


#cards contain query as the first element
tests.append({
    'input': {
        'cards' : [4,2,1,-1],
        'query' : 4
},
        'output': 0
})


# In[10]:


#cards contain only one element ,that is query itself
tests.append({
    'input': {
        'cards' : [6],
        'query' : 6
},
        'output': 0
})


# In[11]:


#cards contain query at the end of the list
tests.append({
    'input': {
        'cards' : [3,-1,-9,-127],
        'query' : -127
},
        'output': 3
})


# In[12]:


#cards does not contain the carry abd we assumne -1 to be the output in all such cases 
tests.append({
    'input': {
        'cards' : [9,7,5,2,-9],
        'query' : 4
},
        'output': -1
})


# In[13]:


#cards is empty
tests.append({
    'input': {
        'cards' : [],
        'query' : 4
},
        'output': -1
})


# In[14]:


tests.append({
    'input': {
        'cards' : [9,7,5,2,-9],
        'query' : 4
},
        'output': -1
})


# In[15]:


#query can occur multiple times , we expect the function to return the position of the first query
tests.append({
    'input': {
        'cards' : [8,8,6,6,6,6,6,6,2,2,2,1,1],
        'query' : 6
},
        'output': 2
})


# In[16]:


#there can be multiple numbers in cards
tests.append({
    'input': {
        'cards' : [2,2,2,2,3,3,4,4,4,5,6,6],
        'query' : 5
},
        'output': 9
})


# In[17]:


tests


# In[18]:


def locate_card(cards, query):
    position = 0 

    while True :
       if cards[position] == query:
        return position 

       position += 1

       if position == len(cards):
            return -1



# In[19]:


test


# In[20]:


result = locate_card(test['input']['cards'] , test['input']['query'])
result


# In[21]:


result == output


# In[22]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[23]:


from jovian.pythondsa import evaluate_test_case


# In[24]:


evaluate_test_case(locate_card , test)


# In[25]:


from jovian.pythondsa import evaluate_test_cases


# In[26]:


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


def locate_card(cards,query):
    lo,hi = 0,len(cards)-1
    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = cards[mid]
        print('low:', lo , 'high:', hi,'mid:',mid , 
              'mid_number:',mid_number)

        if mid_number == query:
            return mid
        elif mid_number< query:
            hi = mid - 1

        elif mid_number> query:
            lo = mid + 1


    return -1        






# In[ ]:


evaluate_test_cases(locate_card,tests)


# In[ ]:


def test_location(cards , query , mid):
    mid_number= cards[mid]
    if mid_number== query :
        if mid-1>=0 and cards[mid-1]==query:
            return 'left'
        else:
            return 'found'
    elif mid_number<query:
        return 'left'
    else:
        return 'right'

def locate_card(cards,query):
    lo,hi = 0,len(cards)-1
    while lo<=hi:

        print('low:', lo , 'high:', hi, )
        mid = (lo+hi)//2
        result = test_location(cards , query , mid)

        if result == 'found':
            return mid
        elif result == 'left':
             hi =  mid-1
        elif result == 'right':
             lo =  mid+1
    return -1      








# In[27]:


evaluate_test_case(locate_card,tests[8])


# In[ ]:





# In[ ]:




