# Romain Ducarrouge
# Advanced Machine Learning
# Practical 3
''' Looking into Naive Bayes '''

# QUESTION 1
# Class Probability:
P_Yes = 4/10

# Feature Rain Recently
RainRecently_Light_Yes = 0/4
RainRecently_Moderate_Yes = 2/4
RainRecently_Heavy_Yes = 2/4
# Feature Rain Recently
RainToday_Light_Yes = 1/4
RainToday_Moderate_Yes = 2/4
RainToday_Heavy_Yes = 1/4
# Feature Temperature
Temperature_Warm_Yes = 3/4
Temperature_Cold_Yes = 1/4
# Feature Wind
Wind_Light_Yes = 2/4
Wind_Moderate_Yes = 2/4
Wind_Gale_Yes = 0/4
# Feature Sunshine
Sunshine_None_Yes = 2/4
Sunshine_Some_Yes = 2/4

##########################################
# Class Probability:
P_No = 6/10
# Feature Rain Recently
RainRecently_Light_No = 3/6
RainRecently_Moderate_No = 6/6
RainRecently_Heavy_No = 0/6
# Feature Rain Recently
RainToday_Light_No = 3/6
RainToday_Moderate_No = 3/6
RainToday_Heavy_No = 0/6
# Feature Temperature
Temperature_Warm_No = 1/6
Temperature_Cold_No = 5/6
# Feature Wind
Wind_Light_No = 2/6
Wind_Moderate_No = 2/6
Wind_Gale_No = 2/6
# Feature Sunshine
Sunshine_None_No = 2/6
Sunshine_Some_No = 4/6

#Classify the following 2 examples:
X1 = ['Heavy', 'Moderate', 'Warm', 'Light', 'Some', "???"]

value_X1_YES = (2/4 *2/4 * 3/4 *2/4 *2/4) *4/10
value_X1_NO =  (0/6 *3/6 *1/6 * 2/6 * 4/6) *6/10
if value_X1_NO > value_X1_YES:
	X1[-1] = "NO"
else:
	X1[-1] = "YES"
print('Question 1 \tX1=', X1)

X2 = ['Light', 'Moderate', 'Warm', 'Light', 'Some', "???"]

value_X2_YES = (0/4 *2/4 * 3/4 *2/4 *2/4) *4/10
value_X2_NO =  (3/6 *3/6 *1/6 * 2/6 * 4/6) *6/10
if value_X2_NO > value_X2_YES:
	X2[-1] = "NO"
else:
	X2[-1] = "YES"
print('Question 1 \tX2=', X2)


# QUESTION 2

# Class Probability:
P_None, P_Sunburned = 5/8, 3/8
# Feature Hair
Hair_blonde_None, Hair_blonde_Sunburned = 1/5, 2/3
Hair_brown_None, Hair_brown_Sunburned = 4/5, 0/3
Hair_red_None, Hair_red_Sunburned = 0/5, 1/3
# Feature Height
Height_short_None, Height_short_Sunburned = 2/5, 1/3
Height_avg_None, Height_avg_Sunburned = 1/5, 2/3
Height_tall_None, Height_tall_Sunburned = 2/5, 0/3
# Feature Build
Build_light_None, Build_light_Sunburned = 1/5, 1/3
Build_avg_None, Build_avg_Sunburned = 2/5, 1/3
Build_heavy_None, Build_heavy_Sunburned = 2/5, 1/3
# Feature Lotion
Lotion_Yes_None, Lotion_Yes_Sunburned = 0/5, 3/3
Lotion_No_None, Lotion_No_Sunburned = 4/6, 1/3

#Classify the following example:
X = ['blonde', 'avg', 'heavy', 'no', '???']

X_NONE = (1/5 *1/5 * 2/5 * 4/6) *5/8
X_Sunburned = (2/3 *2/3 *1/3 *1/3) *3/8

if X_NONE > X_Sunburned:
	X[-1] = "none"
else:
	X[-1] = "sunburned"
print('Question 2 \tX=', X)


# QUESTION 3

# Class Probability:
P_High, P_Medium, P_Low = 6/14, 3/14, 5/14
# Feature Credit History
CH_Bad_High, CH_Bad_Medium, CH_Bad_Low = 3/6, 1/3, 0/5
CH_Unknown_High, CH_Unknown_Medium, CH_Unknown_Low = 2/6, 1/3, 2/5
CH_Good_High, CH_Good_Medium, CH_Good_Low = 1/6, 1/3, 3/5

# Feature Debt
Debt_Low_High, Debt_Low_Medium, Debt_Low_Low = 2/6, 2/3, 3/5
Debt_High_High, Debt_High_Medium, Debt_High_Low = 4/6, 1/3, 2/5

# Feature Income
Inc_0to30_High, Inc_0to30_Medium, Inc_0to30_Low = 4/6, 0/3, 0/5
Inc_30to60_High, Inc_30to60_Medium, Inc_30to60_Low = 2/6, 2/3, 0/5
Inc_over60_High, Inc_over60_Medium, Inc_over60_Low = 0/6, 1/3, 5/5

#Classify the following example:
q3_X = ['bad', 'low', '30to60', '???']

X_risk_High = (3/6 *2/6 * 2/6) *6/14
X_risk_Medium = (1/3 *2/3 *2/3) *3/14
X_risk_Low = (0/5 *3/5 *0/5) *5/14


results = []
results.extend([X_risk_High, X_risk_Medium, X_risk_Low])
name = ("high", "medium","low")

maxResult = max(results)		# find the class with highest probability
a = results.index(maxResult)	# find the target category

q3_X[-1] = name[a]
print('Question 3 \tX=', q3_X)


















