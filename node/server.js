const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {
	if (req.url === "/"){
		fs.readFile("./Public/index.html", "UTF-8", (err, body) => {
			res.writeHead(200, {"Content-Type": "text/html"});
			res.end(body);
			});
	} else if(req.url.match("/sysinfo")) {
		myHostName=os.hostname();
		totalmem=os.totalmem() / 1000000;
		freemem=os.freemem() / 1000000;
		cpus=os.cpus();
		uptime=os.uptime();		
		uptimeDays=Math.trunc(uptime / 86400);
		uptimeHours=Math.trunc((uptime - (uptimeDays * 86400)) / 3600);
		uptimeMinutes=Math.trunc((uptime - ((uptimeDays * 86400) + (uptimeHours * 3600))) / 60);
		uptimeSeconds=Math.trunc((uptime - ((uptimeDays * 86400) + (uptimeHours * 3600) + (uptimeMinutes * 60))));
		html=`
		<!DOCTYPE html>
		<html>
		  <head>
			<title>Node JS Response</title>
		  </head>
		  <body>
			<p>Hostname: ${myHostName}</p>
			<p>IP: ${ip.address()}</p>
			<p>Server Uptime: ${uptimeDays}:${uptimeHours}:${uptimeMinutes}:${uptimeSeconds}</p>
			<p>Total Memory: ${totalmem} MB</p>
			<p>Free Memory: ${freemem} MB</p>
			<p>Number of CPUs: ${cpus.length}</p>
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

