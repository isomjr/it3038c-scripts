const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');
const readline = require('readline');

http.createServer((req, res) => {
	if (req.url === "/"){
		logdata = fs.readFileSync('/var/log/firewalld')
		html=`
		<!DOCTYPE html>
		<html>
		  <head>
			<title>Node JS Response</title>
		  </head>
		  <body>
			<p>/var/log/firewalld Log Contents</p>
			<p>${logdata}</p>
		  </body>
		</html>`
		res.writeHead(200, {"Content-Type": "text/html"});
		res.end(html);
	} else {
		res.writeHead(404, {"Content-Type": "text/plain"});
		res.end(`404 File Not found at ${req.url}`)
	}
}).listen(3000)

console.log("Server listening on port 3000")

