olutsaatavuus
=============

An experimental web app that shows the current availability per store and history data for beers that are available at Alko's stores in Helsinki.

## Tech stack ##
* Python scripts for fetching and updating availability data
* MongoDB for storing the availability data
* Node.js for the webapp
* Jade for templates and CSS

## Running ##
First, configure your MongoDB settings to config.js and the python scripts. Then run fetch_availability.py to store the initial data for the products. After that, you can run update_availability.py daily to update the history data for the products.

The webapp requires some node.js packages that can be installed using 
	
	npm install
	
The webapp can be run using
	
	node app.js
	
By default, the application runs on port 3000, so you can try it out at
	
	http://localhost:3000
	
Live version of the webapp can be found at http://olutsaatavuus.herokuapp.com
