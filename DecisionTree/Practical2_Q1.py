# Romain Ducarrouge
# Adv Machine Learning Practical2
# Decision Tree
import math
# QUESTION 1
#Features: 	NAME	#HAIR	#HEIGHT	#BUILD	#LOTION
data = [['Sarah','blonde','average','light','no','sunburned'], 
['Dana','blonde','tall','average','yes','none'],['Alex','brown','short','average','yes'],
['Annie','blonde','short','average','no','sunburned'],['Emily','red','short','heavy',
'no','sunburned'], ['Pete','red','tall','heavy','no','none'],['John','bronw','average',
'heavy','no','none'],['Katie','brown','short','light','yes','none']]

# a/ Calculate the Entropy of this dataset regarding the target class labelled Result
entropyDataset = -1 * (3.0/8 * math.log2(3.0/8) + 5.0/8*math.log2(5.0/8))
print("entropy of dataset: ", entropyDataset)

# b/ Build the Decision Tree (using the Information Gain formulas)
# Get entropy of each individual features:
entropyHair_BLONDE = -1 * (1.0/3 * math.log2(1.0/3) + 2.0/3*math.log2(2.0/3))
entropyHair_BROWN = -1 * (4.0/4*math.log2(4.0/4))
entropyHair_RED = -1 * (1/1 * math.log2(1/1))

entropyHeight_AVG = -1 * (1.0/3 * math.log2(1.0/3) + 2.0/3*math.log2(2.0/3))
entropyHeight_TALL = -1 * (2/2 * math.log2(2/2))
entropyHeight_SHORT = -1 * (1.0/3 * math.log2(1.0/3) + 2.0/3*math.log2(2.0/3))

entropyBuild_LIGHT = -1 * (1.0/2 * math.log2(1.0/2) + 1.0/2*math.log2(1.0/2))
entropyBuild_AVG = -1 * (1.0/3 * math.log2(1.0/3) + 2.0/3 * math.log2(2.0/3))
entropyBuild_HEAVY = -1 * (1.0/3 * math.log2(1.0/3) + 2.0/3*math.log2(2.0/3))

entropyLotion_No = -1 * (2.0/5 * math.log2(2.0/5) + 3.0/5*math.log2(3.0/5))
entropyLotion_Yes = -1 * (3/3 * math.log2(3/3))

# Get Information Gain value to choose best feature for tree
IG_Hair = entropyDataset - 3/8*entropyHair_BLONDE - 4/8*entropyHair_BROWN - 1/8*entropyHair_RED
IG_Height = entropyDataset - 3/8*entropyHeight_AVG - 2/8*entropyHeight_TALL - 3/8*entropyHeight_SHORT
IG_Build = entropyDataset - 2/8*entropyBuild_LIGHT - 3/8*entropyBuild_AVG - 3/8*entropyBuild_HEAVY
IG_Lotion = entropyDataset - 3/8*entropyLotion_Yes - 5/8*entropyLotion_No

def featureSelection(a,b,c,d):
    list = []
    list.extend([a,b,c,d])
    selectedFeature = max(list)
    if selectedFeature == IG_Hair:
        print('selected feature is Hair')
    elif selectedFeature == IG_Height:
        print('selected feature is Height')
    elif selectedFeature == IG_Build:
        print('selected feature is Build')
    elif selectedFeature == IG_Lotion:
        print('selected feature is Lotion')
    return selectedFeature
featureSelection(IG_Hair, IG_Height, IG_Build, IG_Lotion)
print("Solved for Brown and Red Hair, find next feature for impure Blonde node")
featureSelection(IG_Height, IG_Build, IG_Lotion, 0)
print('Solved for Blonde feature as Lotion splits remaining datapoint into 2 pure nodes')


# c/ Using the decision tree how would you classify:
test = ['blonde','average','heavy','no', '???']
# using no decision tree functions
def decisionTreePredict(x):
    for i in range(0, len(x)):
        # first split on Hair Feature
        if x[0]=='brown':
            x[4]='sunburned'
        elif x[0]=='red':
            x[4]='sunburned'
        elif x[0]=='blonde':
            if x[3]=='yes':
            # second split on Lotion Feature
                x[4] = 'none'
            elif x[3]=='no':
                x[4] = 'sunburned'
        else:
            print('error')
    print(x)
    return x

decisionTreePredict(test)