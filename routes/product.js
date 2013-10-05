
/*
 * GET home page.
 */


 exports.product = function(req, res){
 	var mongojs = require('mongojs');
 	var config = require('../config.js');

 	var db = mongojs(config.mongoDbUrl);
 	var coll = db.collection(config.mongoDbCollection);
 	coll.find({"name":req.params["name"]}, function(err, data){
 		res.render('product', { availability: data, productName: req.params["name"] });
 	});
 	
 
 	};
 	
