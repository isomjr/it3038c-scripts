const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');
const formidable = require('formidable');

http.createServer((req, res) => {
	if (req.url === "/"){
		fs.readFile("./index.html", "UTF-8", (err, body) => {
			res.writeHead(200, {"Content-Type": "text/html"});
			res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
			res.write('<input type="file" name="upfile"><br>');
			res.write('<input type="submit">');
			res.write('</form>');
			res.write('<script></script>');
			res.end();
		})}}).listen(3000)

console.log("Server listening on port 3000")
