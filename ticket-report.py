# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:40:12 2016

@author: Christopher Zaman
"""
#Open the file, read the lines and close it.
file = open('C:/Users/Dell/Desktop/input.txt')
lines = file.readlines()
file.close()

#iterate through the file, split columns, add to the list.
ticketPrices = []
for line in lines:
    cols = line.split(" ")
    ticketID = cols[0]
    price = float(cols[1])
    ticketPrices.append(price)

#Count lines, compute total, avg, min and max.
ticketlines = len(lines)    
total = sum(ticketPrices)
average = total / ticketlines
minimum = min(ticketPrices)
maximum = max(ticketPrices)

#open the output file for writing
file = open('C:/Users/Dell/Desktop/output.txt', 'w')
o = """
***************************************
            TICKET REPORT
***************************************

There are """ + str(ticketlines) + """ tickets in the database.

Maximum Ticket price is $""" + str(maximum) + """.
Minimum Ticket price is $""" + str(minimum) + """.
Average Ticket price is $""" + str(average) + """.

Thank you for using our ticket system!

***************************************
"""
file.write(o)
file.close()