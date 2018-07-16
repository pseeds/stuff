sample_0.py - Various simple checks

sample_get_most_common.py - Get most common strings - 10 max
document.txt

sample_richter_joules_tnt.py

sample_empcontemp.py - Sample Staffinig Model class and Employee, Temporary and Contractor class
                       built from Staffing Model class. 
Description below:
Employee
Constructor:
accepts First Name, Last Name, Pay Rate, Yearly Vacation (num days)
Public Methods:
* get_name - returns the employee’s name in the format “Last Name, First Name"
* get_pay_rate - returns hourly pay rate
* get_yearly_vacation - returns the amount of yearly vacation for the employee
Contractor
Constructor:
accepts First Name, Last Name, Pay Rate, Agency Name (Note: By policy, all contractors have 0 days of vacation)
Public Methods:
* get_name - returns the contractor's name in the format “Last Name, First Name [ C ]"
* get_pay_rate - returns hourly pay rate
* get_yearly_vacation - returns the amount of yearly vacation for the contractor
* get_agency - returns the name of the contracting agency that represents the contractor
Temporary
Constructor:
accepts First Name, Last Name, Pay Rate, Agency Name (Note: By policy, all temporaries have 0 days of vacation)
Public Methods:
* get_name - returns the contractor's name in the format “Last Name, First Name [ T ]"
* get_pay_rate - returns hourly pay rate
* get_yearly_vacation - returns the amount of yearly vacation for the temporary
* get_agency - returns the name of the temp agency that represents the temporary

sample_is_pangram.py - Determine if hard-coded strings are pangrams

sample_find_pairs.py - Find consecutive # pairs

sample_return_unique.py - Return unique occurences of chars in hard-coded strings as a string 

sample_fizz_buzz.py - Use modulo operator with 3 and 5 as divisor. Print "Fizz" for value % 3, "Buzz" for value % 5 and "FizzBuzz" if 3 & 5 divide evenly into value.
