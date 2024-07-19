#simple code on python syntax
def sum_of_numbers(numbers):
    #initialize the sum variable 
    total =0
    #iterate through the list of numbers
    for number in numbers:
        #Add each number to the total
        total +=number
    #return the total sum
    return total
#Example usage
numbers=[1,2,3,4,5]
print(sum_of_numbers(numbers))