/**
 * A script to read the content of a file
 */


const fs = require("fs");
const file_name = process.argv[1];

fs.readFile(file_name, 'utf-8', (err, data) => {
	if (err) {
		console.error(err);
		return;
	}
	console.log(data);
})
