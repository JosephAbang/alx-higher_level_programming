#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let found = 0;
  while (list[i]) {
    if (list[i] === searchElement) {
      found++;
      i++;
    } else {
      i++;
    }
  }
  return found;
};
