#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID.');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error making request:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data:', response.statusCode);
    return;
  }

  // Parse the response body as JSON
  const movieData = JSON.parse(body);

  // Extract the list of character URLs from the movie data
  const characterUrls = movieData.characters;

  // Loop through each character URL and make a request to get the character name
  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error('Failed to fetch character data:', charResponse.statusCode);
        return;
      }

      // Parse the character data and print the character name
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
