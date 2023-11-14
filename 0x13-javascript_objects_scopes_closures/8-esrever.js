#!/usr/bin/node
exports.esrever = function (list) {
  let temp, i, j;
  for (i = 0; i < list.length; i++) {
    for (j = i + 1; j < list.length; j++) {
      if (i < j) {
        temp = list[i];
        list[i] = list[j];
        list[j] = temp;
      }
    }
  }
  return list;
};
