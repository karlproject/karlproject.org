
$(document).ready(function() {

    $('#grid').karlgrid({


    });
    
    // Add columns (XXX actually, set columns)
    $('#grid').data('karlgrid')._addColumns([
        {id: "mimetype", label: "Type", width: 64},
        {id: "title", label: "Title", width: 500 - (64 + 128)},
        {id: "modified_date", label: "Last Modified", width: 128}
    ]);

    // either: $('#grid').data('karlgrid').addRows([
    // ... or: $('#grid').karlgrid('addRows', [
    $('#grid').data('karlgrid').addRows([
        ['file', 'Grotty', '2009-06-11'],
        ['file', 'Able', '2009-06-11'],
        ['file', 'Zeppelin', '2009-06-11'],
        ['file', 'Hiawatha', '2009-06-11'],
        ['file', 'Bubbly', '2009-06-11'],
        ['file', 'Yellow', '2009-06-11'],
        ['file', 'Maroon', '2009-06-11'],
        ['file', 'Paris', '2009-06-11'],
        ['file', 'Berlin', '2009-06-11'],
        ['file', 'Brussels', '2009-06-11'],
        ['file', 'London', '2009-06-11'],
        ['file', 'Atlanta', '2009-06-11'],
        ['file', 'Richmond', '2009-06-11'],
        ['file', 'Tallahassee', '2009-06-11'],
        ['file', 'Miami', '2009-06-11'],
        ['file', 'Tuscaloosa', '2009-06-11'],
        ['file', 'Baton Rouge', '2009-06-11'],
        ['file', 'Little Rock', '2009-06-11'],
        ['file', 'Lexington', '2009-06-11'],
        ['file', 'Knoxville', '2009-06-11'],
        ['file', 'Auburn', '2009-06-11'],
        ['file', 'Nashville', '2009-06-11'],
        ['file', 'Columbus', '2009-06-11'],
        ['file', 'Charleston', '2009-06-11'],
        ['file', 'Starkeville', '2009-06-11'],
        ['file', 'Gainesville', '2009-06-11']
    ]);


});
