# Valorant Points Price Calculator

Simple Python 3 program for calculating the exact cost of a user-specified amount of Valorant Points (VP).

# Usage

Simply run the file from the command line:

    py valorant_points_calc.py

After running, you must input the region you want to calculate the pricing for, by typing in any of the following two character codes:

> **AU**: Australia \
> **BR**: Brazil \
> **EU**: Europe \
> **IN**: India \
> **MX**: Mexico \
> **NZ**: New Zealand \
> **NA**: North America \
> **UK**: United Kingdom 

After choosing your region, you will be prompted to input the amount of VP you want to calculate the cost for, followed by the option to input your current VP balance to deduct that from your specified target, leaving this blank will default to 0.

 # TODO

 Currently it only runs the calculation per each bundle, getting the minimum amount of that bundle needed to reach the specified target. This doesn't cover the option of buying two different bundles to meet the target. 
 
 I plan on implementing this calculation in the future as it can offer more price precision based on the target.