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

function replaceFirstOccurrence(letter: String, line: Array<String>): Array<String> {
  let index = line.indexOf(letter);
  if (index > -1) {
    return line.map((l, i) => i === index ? '*' : l)
  }
  return line
}

function findWord(grid: Array<Array<String>>, word: String): Array<Array<String>> {
  return grid.map((line, index) => replaceFirstOccurrence(word[index], line))
}


// Test
let grid = [['a', 'a', 'q', 't'],
  ['x', 'c', 'w', 'e'],
  ['r', 'l', 'e', 'p']]

let word = 'ace'

let target = [['*', 'a', 'q', 't'],
  ['x', '*', 'w', 'e'],
  ['r', 'l', '*', 'p']]

let actual = findWord(grid, word)

let truth = actual.every((line, i) => line.every((letter, j) => letter === target[i][j]))
console.assert(truth, 'The arrays were not equal')
