PROGRAMING CHALLENGES

001 - Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.
______________________________________________________________

002 - Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples:

to_camel_case("the-stealth-warrior") #returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") #returns "TheStealthWarrior"
______________________________________________________________

003 - Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples:

pig_it('Pig latin is cool') # igPay atinlay siay oolcay

pig_it('Hello world !')     # elloHay orldway !
______________________________________________________________

004 - Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: 

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
