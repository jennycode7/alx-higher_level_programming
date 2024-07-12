#!/usr/bin/node
// a function that increments and calls a function.
// Prototype: function (number, theFunction)

exports.addMeMaybe = function (number, theFunction) {
  const result = number + 1;
  theFunction(result);
};
