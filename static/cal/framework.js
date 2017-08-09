DATA = [];
CONTROLLERS = [];
function addText($elt, txt) {
    $elt.append('<p>' + txt + '<\/p>');
}
function DayController(date) {
    this.date = date;
    this.chunks = DATA[this.date];
    this.$cell = $('#c-'+this.date);
}
DayController.prototype.render = function() {
    for (var j=0; j<this.chunks.length; j++) {
        var chunk = this.chunks[j];
        addText(this.$cell, chunk.user);
        addText(this.$cell, chunk.availability);
        addText(this.$cell, chunk.text);
    }
};
