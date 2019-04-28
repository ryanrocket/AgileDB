// AgileDB NodeJS Framework
// By Ryan Wans
// Specifically for RYANWANS.com , expansion in near future

var sys = require('util');
var fs = require('fs');
var exec = require('child_process').exec;
var child;
var queOut;
const queryOutput = 'no output';

// || DEBUG || //
function puts(error, stdout, stderr) { var output = stdout; }
// || DEBUG || //
function saver(input) { let queOut = input; }
// || DEBUG || //

module.exports = {
    create: function(db, type, name) {
        db = String(db);
        type = String(type);
        name = String(name);
        if(type === "dict") {
            exec("python3 /home/ubuntu/agiledb/src/cli.py dbSet " + db + " add dict " + name, puts);
        } else if(type === "list") {
            exec("python3 /home/ubuntu/agiledb/src/cli.py dbSet " + db + " add list " + name, puts);
        } else {
            console.log("[ agile ] ERR >> func: create >> local: input >> parm: type >> log: 'invalid data type';");
        }
    },
    add: function(db, key, val) {
        db = String(db);
        key = String(key);
        val = String(val);
        exec("python3 /home/ubuntu/agiledb/src/cli.py dbSet " + db + " add rel " + key + " " + val, puts);
    },
    tag: function(db, tag) {
        db = String(db);
        tag = String(tag);
        exec("python3 /home/ubuntu/agiledb/src/cli.py dbSet " + db + " add tag " + tag, puts);
    },
    updateList: function(db, list, val) {
        db = String(db);
        list = String(list);
        val = String(val);
        exec("python3 /home/ubuntu/agiledb/src/cli.py dbSet " + db + " update list " + list + " " + val, puts);
    },
    updateDict: function(db, dict, key, val) {
        db = String(db);
        dict = String(dict);
        key = String(key);
        val = String(val);
        exec("python3 /home/ubuntu/agiledb/src/cli.py dbSet " + db + " update dict " + dict + " " + key + " " + val, puts);
    },
    display: function(db) {
        db = String(db);
        exec("python3 /home/ubuntu/agiledb/src/cli.py dbSet " + db + " display", puts);
    },
    select: function(db) {
        db = String(db);
        let rawdata = fs.readFileSync('/home/ubuntu/agile_data/stored_local/' + db + '.json');
        let formdata = JSON.parse(rawdata);
        return formdata;
    },
    varOut: queOut
};

function slc (db, type, key) {
	type = String(type);
	key = String(key);
	exec('python3 /home/ubuntu/agiledb/src/cli.py dbSet ' + db + " select " + type + " " + key, function(error, stdout, stderr){saver(stdout);});
	setTimeout(function(){ console.log(queOut) }, 3000);
}
