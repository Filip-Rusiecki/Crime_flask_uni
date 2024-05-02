

document.getElementById('year_slider').oninput = function () {
    document.getElementById('year').textContent = this.value;
    $.post('/data', { year: this.value }, function (html) {
        $('#map').html(html);
    });
};