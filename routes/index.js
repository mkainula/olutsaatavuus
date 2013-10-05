
/*
 * GET home page.
 */


 exports.index = function(req, res){
 	var mongojs = require('mongojs');
 	var config = require('../config.js');

 	var db = mongojs(config.mongoDbUrl);
 	var coll = db.collection(config.mongoDbCollection);
 	coll.find(function(err, data){
 		data.sort(function(a,b){
 			if(a.name == b.name) return 0;
 			if(a.name < b.name) return -1;
 			if(a.name > b.name) return 1;

 		});
 		res.render('index', { availability: data });
 	});
 	
 
 	};
 	
