/* Implement a word search. Given a 2D array of letters and a word to find, 
   return the 2D array with the found word’s letters replaced with an asterisk (*). 

Example: 

let grid = [['a','a','q','t'],
            ['x','c','w','e'],
            ['r','l','e','p']]

$ findWord(grid, 'ace')
$ [['*','a','q','t'],
   ['x','*','w','e'],
   ['r','l','*','p']] 
   
  */

function replaceLetter(letter: String, line: Array<String>):Array<String> {
  return line.map(l => l === letter ? '*' : l)
}

function findWord(grid: Array<Array<String>>, word: String): Array<Array<String>> {
  return grid.map((line, index) => replaceLetter(word[index], line))
}


var results = findWord([['a','a','q','t'],['x','c','w','e'],['r','l','e','p']], 'ace')
