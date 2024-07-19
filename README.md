"# DemoBlazeAutomation"

About
Automated  E-commerce Application (https://www.demoblaze.com/) using Selenium,Pytest 
implemented page Object mechanism , pytest data driven fixtures in framework design 

Setup Instruction 
pip install -r requirements.txt 

To run the test cases from root folder
py.test --html="report.html"

report.html 
shows a comprehensive test report 

![image](https://github.com/user-attachments/assets/b8b898c9-63b8-4b2b-bce8-11506ac14378)


Functional issues found :- 
1)Empty Cart Purchasing allowed whereas it should not

2) None of the forms be it Signup,Login,Purchase have any sort of data validation 
For example :-
Signup ,login forms username fields allow numbers whereas it should not 
purchase form fields allows just any datatype wheras if its country it should not allow numbers 
this applies to all form fields across

4) Without login i am allowed to add items to cart and purchse 


