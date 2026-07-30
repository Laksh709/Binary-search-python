#!/usr/bin/env python
# coding: utf-8

# In[69]:


def locate_card(cards,query):
    pass


# In[70]:


cards = [ 13,11,12,7,4,3,1,0]
query = 7
output = 3


# In[71]:


result = locate_card(cards,query)
print(result)


# In[72]:


result == output


# In[73]:


test = {
    'input': {
        'cards' : [13,11,12,7,4,3,1,0],
        'query' : 7
},
        'output': 3 
}


# In[74]:


locate_card(**test['input']) == test['output']


# In[75]:


tests = []


# In[76]:


tests.append(test)
#cards contain query in the middle
tests.append({
    'input': {
        'cards' : [13,11,12,7,4,3,1,0],
        'query' : 1
},
        'output': 6
})


# In[77]:


#cards contain query as the first element
tests.append({
    'input': {
        'cards' : [4,2,1,-1],
        'query' : 4
},
        'output': 0
})


# In[78]:


#cards contain only one element ,that is query itself
tests.append({
    'input': {
        'cards' : [6],
        'query' : 6
},
        'output': 0
})


# In[79]:


#cards contain query at the end of the list
tests.append({
    'input': {
        'cards' : [3,-1,-9,-127],
        'query' : -127
},
        'output': 3
})


# In[80]:


#cards does not contain the carry abd we assumne -1 to be the output in all such cases 
tests.append({
    'input': {
        'cards' : [9,7,5,2,-9],
        'query' : 4
},
        'output': -1
})


# In[81]:


#cards is empty
tests.append({
    'input': {
        'cards' : [],
        'query' : 4
},
        'output': -1
})


# In[82]:


tests.append({
    'input': {
        'cards' : [9,7,5,2,-9],
        'query' : 4
},
        'output': -1
})


# In[83]:


#query can occur multiple times , we expect the function to return the position of the first query
tests.append({
    'input': {
        'cards' : [8,8,6,6,6,6,6,6,2,2,2,1,1],
        'query' : 6
},
        'output': 2
})


# In[84]:


tests


# In[85]:


def locate_card_linear(cards, query):
    position = 0 

    while True :
       if cards[position] == query:
        return position 

       position += 1

       if position == len(cards):
            return -1



# In[86]:


test


# In[87]:


result = locate_card(test['input']['cards'] , test['input']['query'])
result


# In[88]:


result == output


# In[89]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[90]:


from jovian.pythondsa import evaluate_test_case


# In[91]:


evaluate_test_case(locate_card , test)


# In[92]:


from jovian.pythondsa import evaluate_test_cases


# In[93]:


evaluate_test_cases(locate_card , tests)


# In[94]:


def locate_card_linear(cards, query):
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






# In[95]:


cards6 = tests[6]['input']['cards']
query6 = tests[6]['input']['query']
locate_card(cards6,query6)


# In[96]:


def locate_card_linear(cards, query):
    position = 0

    while position<len(cards) :
        if cards[position] == query:
            return position
        position +=1
    return -1   


# In[97]:


tests[6]


# In[98]:


import os
print(os.getcwd())


# In[99]:


def locate_card(cards,query):
    lo,hi = 0,len(cards)-1
    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = cards[mid]


        if mid_number == query:
            return mid
        elif mid_number< query:
            hi = mid - 1

        elif mid_number> query:
            lo = mid + 1


    return -1        






# In[100]:


evaluate_test_cases(locate_card,tests)


# In[101]:


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


        mid = (lo+hi)//2
        result = test_location(cards , query , mid)

        if result == 'found':
            return mid
        elif result == 'left':
             hi =  mid-1
        elif result == 'right':
             lo =  mid+1
    return -1      








# In[102]:


evaluate_test_case(locate_card,tests[8])


# In[103]:


def locate_card_linear(cards, query):
    position = 0

    while position<len(cards) :
        if cards[position] == query:
            return position
        position +=1
    return -1   


# In[104]:


large_test = {
    'input': {
        'cards':list(range(10000000,0,-1)) ,
        'query': 2,
    } , 
    'output':9999998
}


# In[105]:


result, passed, runtime = evaluate_test_case(locate_card_linear,large_test,display = False)
print("Result : {} \n Passed : {} \n Execution time : {} ms ".format(result,passed,runtime))


# In[106]:


result, passed, runtime = evaluate_test_case(locate_card,large_test,display = False)
print("Result : {} \n Passed : {} \n Execution time : {} ms ".format(result,passed,runtime))


# In[107]:


def binary_search(lo,hi,condition):
    while lo<=hi:
        mid = (lo+hi)//2
        result =condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid +1 
    return -1



# In[108]:


def locate_card(cards,query):

    def condition(mid):
        if cards[mid] == query:
            if  mid > 0 and cards[mid-1]== query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(cards)-1 , condition)        





# In[109]:


evaluate_test_cases(locate_card,tests)


# In[ ]:




