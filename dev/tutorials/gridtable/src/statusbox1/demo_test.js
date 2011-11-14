
(function($){

var sc = function() {
    return $($('#statusbox .ui-multistatusbox-item')
        .map(function() {
            return $(this).text();
        }));
};

$(document).ready(function() {

    test("Widget attachment with no options", function() {

        $('#statusbox').multistatusbox({});

        same(sc(), $([
            "A message that came with the page"
        ]))

        same(sc(), $([
            "A message that came with the page"
            ]), 'Statusbox content does not match');

    });


    test("Append messages", function() {

        $('#statusbox').multistatusbox({});

        $('#statusbox').multistatusbox('append', 'Message1');
        $('#statusbox').multistatusbox('append', 'Message2');
        $('#statusbox').multistatusbox('append', 'Message3');

        same(sc(), $([
            'A message that came with the page',
            'Message1X',
            'Message2X',
            'Message3X'
            ]), 'Statusbox content does not match');

        ok($('#statusbox .ui-multistatusbox-item .ui-multistatusbox-closebutton').length == 3,
            'Has close button');

    });

    test("Clear all messages", function() {

        $('#statusbox').multistatusbox({});

        $('#statusbox').multistatusbox('append', 'Message1');
        $('#statusbox').multistatusbox('append', 'Message2');
        $('#statusbox').multistatusbox('append', 'Message3');

        same(sc(), $([
            'A message that came with the page',
            'Message1X',
            'Message2X',
            'Message3X',
            ]), 'Statusbox content does not match');

        $('#statusbox').multistatusbox('clear');

        same(sc(), $([
            ]), 'Statusbox content does not match');

    });

    test("Close button works", function() {

        $('#statusbox').multistatusbox({});

        $('#statusbox').multistatusbox('append', 'Message1');
        $('#statusbox').multistatusbox('append', 'Message2');
        $('#statusbox').multistatusbox('append', 'Message3');

        same(sc(), $([
            'A message that came with the page',
            'Message1X',
            'Message2X',
            'Message3X'
            ]), 'Statusbox content does not match');

        $('#statusbox').children().eq(2)
            .find('.ui-multistatusbox-closebutton')
                .click();

        same(sc(), $([
            'A message that came with the page',
            'Message1X',
            'Message3X'
            ]), 'Statusbox content does not match');

        $('#statusbox').children().eq(2)
            .find('.ui-multistatusbox-closebutton')
                .click();

        same(sc(), $([
            'A message that came with the page',
            'Message1X'
            ]), 'Statusbox content does not match');

        $('#statusbox').children().eq(1)
            .find('.ui-multistatusbox-closebutton')
                .click();

        same(sc(), $([
            'A message that came with the page',
            ]), 'Statusbox content does not match');

    });

    test("Widget attachment with hasCloseButton options", function() {

        $('#statusbox').multistatusbox({
            hasCloseButton: false
        });

        $('#statusbox').multistatusbox('append', 'Message1');

        same(sc(), $([
            'A message that came with the page',
            "Message1"
            ]), 'Statusbox content does not match');

        ok($('#statusbox .ui-multistatusbox-item .ui-multistatusbox-closebutton').length == 0,
            'No close button');

    });

    test("Widget attachment with cls options", function() {

        $('#statusbox').multistatusbox({
            clsContainer: 'marker-a',
            clsItem: 'marker-b',
        });

        $('#statusbox').multistatusbox('append', 'Message1');

        same(sc(), $([
            'A message that came with the page',
            "Message1X"
            ]), 'Statusbox content does not match');

        ok($('#statusbox.marker-a').length == 1,
            'Cls applied on container');

        ok($('#statusbox .ui-multistatusbox-item.marker-b').length == 1,
            'Cls applied on item');
    });

});

})(jQuery);

