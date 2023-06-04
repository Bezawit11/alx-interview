#!/usr/bin/node
const r = require('request');
r('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const info = JSON.parse(body);
  const chars = info.characters;
  if (chars && chars.length > 0) {
      const limit = chars.length;
      PrintChar(0, chars[0], chars, limit);
    }
});

function PrintChar (idx, url, characters, limit) {
  if (idx === limit) {
    return;
  }
  r(url, function (error, response, body) {
    if (!error) {
      const ub = JSON.parse(body);
      console.log(ub.name);
      idx++;
      PrintChar(idx, characters[idx], characters, limit);
    } else {
      console.error('error:', error);
    }
  });
}
