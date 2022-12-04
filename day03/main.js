fs = require('fs');

// Returns priority of the item/character
const priority = char => {
  const codePoint = char.codePointAt(0);
  // lowercase
  if (codePoint >= 97 && codePoint <= 122) {
    return codePoint - 'a'.codePointAt(0) + 1;
  }
  // UPPERCASE
  else {
    return codePoint - 'A'.codePointAt(0) + 27;
  }
};

const findWrongItem = rucksackString => {
  const itemCount = rucksackString.length;
  const compartment1 = rucksackString.substring(0, itemCount / 2);
  const compartment2 = rucksackString.substring(itemCount / 2);
  for (const item of compartment1) {
    if (compartment2.includes(item)) {
      return item;
    }
  }
};

const findBadge = (rucksack1, rucksack2, rucksack3) => {
  for (const item of rucksack1) {
    if (rucksack2.includes(item) && rucksack3.includes(item)) {
      return item;
    }
  }
};

file = fs.readFile('./input.txt', 'utf8', (error, data) => {
  if (error) {
    return console.log(error);
  }
  const rucksackList = data.split('\n');

  let prioritySum = 0;
  for (const rucksackString of rucksackList) {
    // Skip empty lines
    if (rucksackString.length === 0) {
      continue;
    }
    const wrongItem = findWrongItem(rucksackString);
    prioritySum += priority(wrongItem);
  }

  console.log('Answer Part 1 = ' + prioritySum);

  prioritySum = 0;

  // For each group of 3 rucksacks
  for (i = 0; i + 2 < rucksackList.length; i += 3) {
    const badge = findBadge(rucksackList[i], rucksackList[i + 1], rucksackList[i + 2]);
    prioritySum += priority(badge);
  }
  console.log('Answer Part 2 = ' + prioritySum);
});
