
/*
 * GET home page.
 */


 exports.store = function(req, res){
 	var mongojs = require('mongojs');
 	var config = require('../config.js');

 	var db = mongojs(config.mongoDbUrl);
 	var coll = db.collection(config.mongoDbCollection);
 	coll.find({"availability.store":req.params["name"]}, function(err, data){
 		 data.sort(function(a,b){
 			if(a.name == b.name) return 0;
 			if(a.name < b.name) return -1;
 			if(a.name > b.name) return 1;

 		});
 		res.render('store', { availability: data, storeName: req.params["name"] });
 	});
 	
 
 	};
 	
