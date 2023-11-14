#!/usr/bin/node

exports.esrever = function (list) {
  let idx = list.length - 1;
  let i = 0;
  const revList = [];
  while (idx >= 0) {
    revList[i] = list[idx];
    i++;
    idx--;
  }
  return revList;
};
