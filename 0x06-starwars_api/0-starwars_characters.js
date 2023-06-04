#!/usr/bin/node
const r = require('request');
r('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const info = JSON.parse(body);
  for (let i = 0; i < info.characters.length; i++) {
    const req = require('request');
    req(info.characters[i], function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }
      const chars = JSON.parse(body);
      console.log(chars.name);
    });
  }
});
