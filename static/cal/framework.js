DATA = [];
CONTROLLERS = [];
function DayController(date) {
    this.date = date;
    this.chunks = DATA[this.date];
    this.$cell = $('#c-'+this.date);
}
DayController.prototype.render = function() {
    for (var j=0; j<this.chunks.length; j++) {
        var chunk = this.chunks[j];
        this.$cell.append(chunk.user);
        this.$cell.append(chunk.text);
    }
};
