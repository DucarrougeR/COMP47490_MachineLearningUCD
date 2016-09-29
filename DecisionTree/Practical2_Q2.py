# Romain Ducarrouge
# Adv Machine Learning Practical2
# Decision Tree

import math
# QUESTION 2
# What is the entropy of the dataset?
e_dataset = ((6/14*math.log2(6/14)) + (3/14*math.log2(3/14)) + (5/14*math.log2(5/14))) *-1
print('the entropy for the dataset is %.4f' % e_dataset)

# Compute the entropy for each feature in the data
eCreditHistory_BAD = ((0.75*math.log2(0.75)) + (0.25*math.log2(0.25))) *-1
eCreditHistory_UNKNOWN = ((0.4*math.log2(0.4)) + (0.2*math.log2(0.2)) + (0.4*math.log2(0.4))) *-1
eCreditHistory_GOOD = ((0.2*math.log2(0.2)) + (0.2*math.log2(0.2)) + (0.6*math.log2(0.6))) *-1

eDebt_LOW = ((2/7*math.log2(2/7)) + (2/7*math.log2(2/7)) + (3/7*math.log2(3/7))) *-1
eDebt_HIGH = ((4/7*math.log2(4/7)) + (1/7*math.log2(1/7)) + (2/7*math.log2(2/7))) *-1

eIncome_0to30 = (4/4*math.log2(4/4)) *-1
eIncome_30to60 = ((2/4*math.log2(2/4)) + (2/4*math.log2(2/4))) *-1
eIncome_over60 = ((1/6*math.log2(1/6)) + (5/6*math.log2(5/6))) *-1

# Which predicting feature would be selected by ID3 at the root of the decision tree
IG_CreditHistory = e_dataset - 4/14*eCreditHistory_BAD - 5/14*eCreditHistory_UNKNOWN - 5/14*eCreditHistory_GOOD
IG_Debt = e_dataset - 7/14*eDebt_LOW - 7/14*eDebt_HIGH
IG_Income = e_dataset - 4/14*eIncome_0to30 - 4/14*eIncome_30to60 - 6/14*eIncome_over60

def rootFeature(a,b,c):
    list = []
    list.extend([a,b,c])
    selectedFeature = max(list)
    if selectedFeature == IG_CreditHistory:
        print('selected feature is Credit History')
    elif selectedFeature == IG_Debt:
        print('selected feature is Debt')
    elif selectedFeature == IG_Income:
        print('selected feature is Income')
    return selectedFeature
rootFeature(IG_CreditHistory, IG_Debt, IG_Income)


