
/*
 * GET home page.
 */


 exports.store = function(req, res){
 	var mongojs = require('mongojs');
 	var config = require('../config.js');
 	var d3 = require('d3');

 	var db = mongojs(config.mongoDbUrl);
 	var coll = db.collection(config.mongoDbCollection);
 	
 	coll.find({"availability.store":req.params["name"]}, function(err, data){
 		 data.sort(function(a,b){
 			if(a.name == b.name) return 0;
 			if(a.name < b.name) return -1;
 			if(a.name > b.name) return 1;

 		});
 		res.render('store', { availability: data, storeName: req.params["name"], d3: d3 });
 	});
 	
 
 	};
 	
  exports.history = function(req, res){
 	var mongojs = require('mongojs');
 	var config = require('../config.js');
 	var d3 = require('d3');

 	var db = mongojs(config.mongoDbUrl);
 	var coll = db.collection(config.mongoDbCollection);
 	
 	coll.find({"availability.store":req.params["name"], "name":req.params["productname"]}, function(err, data){
 		 data.sort(function(a,b){
 			if(a.name == b.name) return 0;
 			if(a.name < b.name) return -1;
 			if(a.name > b.name) return 1;

 		});
 		res.render('storehistory', { availability: data, storeName: req.params["name"], productName: req.params["productname"], d3: d3 });
 	});
 	
 
 	};
