# javaScriptReadFile
JavaScript to read local text file
# Without Jquery
 document.getElementById('file').onchange = function(){

  var file = this.files[0];

  var reader = new FileReader();
  reader.onload = function(progressEvent){
    // Entire file
    console.log(this.result);

    // By lines
    var lines = this.result.split('\n');
    for(var line = 0; line < lines.length; line++){
      console.log(lines[line]);
    }
  };
  reader.readAsText(file);
};
# Using ES6 the javascript becomes a little cleaner
handleFiles(input) {

    const file = input.target.files[0];
    const reader = new FileReader();

    reader.onload = (event) => {
        const file = event.target.result;
        const allLines = file.split(/\r\n|\n/);
        // Reading line by line
        allLines.map((line) => {
            console.log(line);
        });
    };

    reader.onerror = (evt) => {
        alert(evt.target.error.name);
    };

    reader.readAsText(file);
}
