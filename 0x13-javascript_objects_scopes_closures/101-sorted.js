#!/usr/bin/node
const { dict } = require('./101-data');

// Function to compute dictionary of user ids by occurrence
function computeUserIdsByOccurrence(occurrences) {
  const userIdsByOccurrence = {};

  for (const userId in occurrences) {
    const occurrence = occurrences[userId];

    if (!userIdsByOccurrence[occurrence]) {
      userIdsByOccurrence[occurrence] = [];
    }

    userIdsByOccurrence[occurrence].push(userId);
  }

  return userIdsByOccurrence;
}

// Compute user ids by occurrence
const userIdsByOccurrence = computeUserIdsByOccurrence(dict);

// Print the new dictionary
console.log(userIdsByOccurrence);
