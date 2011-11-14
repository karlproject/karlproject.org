
(function($){

    $(document).ready(function() {

        $('#statusbox').multistatusbox({
        });

        $('#button1').click(function() {
            $('#statusbox').multistatusbox('append',
                'A message'
            );
        });

        $('#button2').click(function() {
            $('#statusbox').multistatusbox('append',
                'A <span style="color: blue">blue</span> message'
            );
        });

        $('#button3').click(function() {
            $('#statusbox').multistatusbox('append',
                'A <span style="color: green;">green</span> message'
            );
        });

        $('#button4').click(function() {
            $('#statusbox').multistatusbox('clear');
        });

    });

})(jQuery);

